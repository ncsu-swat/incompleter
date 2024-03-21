import ast
import os
import re
from subprocess import Popen, PIPE
import copy
import json

input_file_path = 'input.txt'
if not os.path.exists(input_file_path):
    print("Warning: 'input.txt' does not exist in the current directory.")
    exit(1)

def has_imports(code):
    return "import " in code or "from " in code

def run_script_with_input(script_path, input_file_path):
    with open(input_file_path, 'rb') as input_file:
        proc = Popen(['python3', script_path], stdout=PIPE, stderr=PIPE, stdin=input_file)
        out, err = proc.communicate()
    return out.decode('utf-8'), err.decode('utf-8')

def parse_output(output):
    pattern = r"\[FROM INNER-WORLD\]\nVAR=(\w+)\nTYPE=(\w+)"
    return re.findall(pattern, output)

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

    def visit_Body(self, node):
        if 'body' in dir(node):
            idx = 0
            lim = len(node.body)
            while idx < lim:
                if isinstance(node.body[idx], ast.Assign):
                    node.body.insert(idx, ast.parse(f'tmp_var{self.tmp_var_counter} = ' + ast.unparse(ast.fix_missing_locations(node.body[idx].value))))
                    node.body.insert(idx+1, ast.parse('print("[FROM INNER-WORLD]")'))

                    ident = ''
                    if isinstance(node.body[idx+2].targets[0], ast.Name):
                        ident = node.body[idx+2].targets[0].id
                    elif isinstance(node.body[idx+2].targets[0], ast.Attribute):
                        ident = node.body[idx+2].targets[0].attr

                    node.body.insert(idx+2, ast.parse(f'print("VAR={ident}")'))
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
    def __init__(self, var_to_remove):
        self.var_to_remove = var_to_remove

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name) and node.targets[0].id == self.var_to_remove:
            return None 
        elif isinstance(node.targets[0], ast.Attribute) and node.targets[0].attr == self.var_to_remove:
            return None 
        return node 

def process_files(directory, input_file_path):
    assignment_removed_dir = 'assignment_removed'
    os.makedirs(assignment_removed_dir, exist_ok=True)
    json_data = []

    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            snippet_path = os.path.join(directory, filename)
            with open(snippet_path, 'r') as snippet_file:
                snippet = snippet_file.read()

            # Check if the snippet contains import statements
            contains_imports = has_imports(snippet)

            # Parse the AST and modify it as before
            tree = ast.parse(snippet)
            visitor = Visitor()
            modified_tree = visitor.visit_Body(tree)
            modified_code = ast.unparse(ast.fix_missing_locations(modified_tree))

            with open('tmp.py', 'w') as tmp_file:
                tmp_file.write(modified_code)

            # Run modified script and capture output
            output, _ = run_script_with_input('tmp.py', input_file_path)
            vars_and_types = parse_output(output)

            original_tree = ast.parse(snippet)

            # Process each variable and type captured from the output
            for idx, (var, var_type) in enumerate(vars_and_types):
                remover = AssignmentRemover(var)
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
                    "contains_imports": contains_imports
                })

    # Save the collected data into a JSON file
    json_file_path = os.path.join(assignment_removed_dir, 'assignments_info.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Processing complete. Metadata saved.")

# Usage
problem_solutions_dir = './ProblemSolutionsPython'
process_files(problem_solutions_dir, input_file_path)

