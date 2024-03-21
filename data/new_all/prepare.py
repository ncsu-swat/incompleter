import ast
import os
import re
from subprocess import Popen, PIPE
import copy
import json
import sys
from subprocess import TimeoutExpired

input_file_path = 'input.txt'
problem_solutions_dir = "./ProblemSolutionsPython"

if not os.path.exists(input_file_path):
    print("Warning: 'input.txt' does not exist in the current directory.")
    exit(1)

def has_imports(code):
    return "import " in code or "from " in code

def run_script_with_input(script_path, input_file_path, timeout=None):
    with open(input_file_path, 'rb') as input_file:
        proc = Popen(['python3', script_path], stdout=PIPE, stderr=PIPE, stdin=input_file)
        try:
            out, err = proc.communicate(timeout=timeout)
        except TimeoutExpired:
            proc.kill() 
            out, err = proc.communicate()  
            raise TimeoutExpired(proc.args, timeout) 
    return out.decode('utf-8'), err.decode('utf-8')


def parse_output(output):
    pattern = r"\[FROM INNER-WORLD\]\nVAR=(\w+)@(\d+)\nTYPE=(\w+)"
    matches = re.findall(pattern, output)
    
    # Using a set for loops that print the same var many times
    formatted_matches = set() 
    for var, line_no, var_type in matches:
        formatted_matches.add((var, var_type, line_no))

    return list(formatted_matches)


class PrintRemover(ast.NodeTransformer):
    def __init__(self):
        pass

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            return None
        return node

class Visitor(ast.NodeTransformer):
    def __init__(self):
        self.tmp_var_counter = 0
        self.assignments = []

    def visit_Assign(self, node):
        self.assignments.append((node, node.lineno if hasattr(node, 'lineno') else None))
        return node

    def visit_Body(self, node):
        if 'body' in dir(node):
            idx = 0
            lim = len(node.body)
            while idx < lim:
                if isinstance(node.body[idx], ast.Assign):
                    line_no = getattr(node.body[idx], 'lineno', '0')
                    node.body.insert(idx, ast.parse(f'tmp_var{self.tmp_var_counter} = ' + ast.unparse(ast.fix_missing_locations(node.body[idx].value))))
                    node.body.insert(idx+1, ast.parse('print("[FROM INNER-WORLD]")'))

                    ident = ''
                    if isinstance(node.body[idx+2].targets[0], ast.Name):
                        ident = node.body[idx+2].targets[0].id
                    elif isinstance(node.body[idx+2].targets[0], ast.Attribute):
                        ident = node.body[idx+2].targets[0].attr

                    # node.body.insert(idx+2, ast.parse(f'print("VAR={ident}")'))
                    node.body.insert(idx+2, ast.parse(f'print("VAR={ident}@{line_no}")'))
                    node.body.insert(idx+3, ast.parse(f'print("TYPE="+type(tmp_var{self.tmp_var_counter}).__name__)'))

                    node.body[idx+4].value = ast.Name(id=f'tmp_var{self.tmp_var_counter}', ctx=ast.Load())
                    idx += 4
                    lim += 4
                    self.tmp_var_counter += 1
                else:
                    self.visit_Body(node.body[idx])
                idx += 1
        return node

class AssignmentRemover(ast.NodeTransformer):
    def __init__(self, var_to_remove, line_no_to_remove):
        self.var_to_remove = var_to_remove
        self.line_no_to_remove = int(line_no_to_remove) 

    def visit_Assign(self, node):
        if hasattr(node.targets[0], 'id') and node.targets[0].id == self.var_to_remove:
            if getattr(node, 'lineno', 0) == self.line_no_to_remove:
                return None  # Remove the assignment
        elif hasattr(node.targets[0], 'attr') and node.targets[0].attr == self.var_to_remove:
            if getattr(node, 'lineno', 0) == self.line_no_to_remove:
                return None  # Remove the attribute assignment
        return node



def process_files(directory, input_file_path, specific_file=None):
    assignment_removed_dir = 'assignment_removed'
    os.makedirs(assignment_removed_dir, exist_ok=True)
    json_data = []
    files_to_process = [specific_file] if specific_file else os.listdir(directory)

    for filename in files_to_process:
        if filename.endswith('.py'):
            snippet_path = os.path.join(directory, filename)
            with open(snippet_path, 'r') as snippet_file:
                snippet = snippet_file.read()

            contains_imports = has_imports(snippet)
            tree = ast.parse(snippet)
            visitor = Visitor()
            modified_tree = visitor.visit_Body(tree)
            modified_code = ast.unparse(ast.fix_missing_locations(modified_tree))
            print(modified_code)

            with open('tmp.py', 'w') as tmp_file:
                tmp_file.write(modified_code)

            try:
                output, _ = run_script_with_input('tmp.py', input_file_path, timeout=30)
            except TimeoutExpired:
                print(f"Execution of {filename} exceeded 30 seconds and was skipped.")
                continue  

            vars_and_types = parse_output(output)
            print(vars_and_types)
            if len(vars_and_types) > 50:
                print(f"Error: More than 50 assignments in {filename}. Something might be wrong.")
                sys.exit(1)

            original_tree = ast.parse(snippet)
            for idx, (var, var_type, line_no) in enumerate(vars_and_types):
                remover = AssignmentRemover(var, line_no)
                modified_tree = remover.visit(copy.deepcopy(original_tree))
                modified_code = ast.unparse(ast.fix_missing_locations(modified_tree))

                modified_script_name = f'{filename[:-3]}_{idx}.py'
                modified_script_path = os.path.join(assignment_removed_dir, modified_script_name)
                with open(modified_script_path, 'w') as modified_file:
                    modified_file.write(modified_code)

                json_data.append({
                    "snippet_name": modified_script_name,
                    "variable": var,
                    "type": var_type,
                    "line_no": line_no,
                    "contains_imports": contains_imports
                })

    json_file_path = os.path.join(assignment_removed_dir, 'assignments_info.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Processing complete.")

if __name__ == "__main__":
    specific_file = sys.argv[1] if len(sys.argv) > 1 else None
    process_files(problem_solutions_dir, input_file_path, specific_file=specific_file)