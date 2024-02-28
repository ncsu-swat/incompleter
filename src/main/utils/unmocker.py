import ast
import astunparse
from main.utils.snippet import Snippet
# Infers the type of a class based on several deductions
class TypeInferrer(ast.NodeVisitor):
    def __init__(self):
        self.unroll_dict = {}
        self.current_class = None
        self.class_methods = {}
        self.class_attributes = {}
        self.class_container_init = {}

    def visit_ClassDef(self, node):
        self.current_class = node.name
        # self.unroll_dict[node.name] = {'deductions': [], 'type': 'unknown'}
        base_classes = [base.id for base in node.bases if isinstance(base, ast.Name)] 
        self.unroll_dict[node.name] = {
            'deductions': [],
            'type': 'unknown',
            'base_classes': base_classes
        }
        self.class_methods[node.name] = []
        self.class_attributes[node.name] = {}
        self.generic_visit(node)
        self.infer_class_type(node.name)
        self.current_class = None

    def visit_FunctionDef(self, node):
        if self.current_class:
            self.class_methods[self.current_class].append(node.name)
        self.generic_visit(node)

    def visit_Assign(self, node):
        if self.current_class and isinstance(node.targets[0], ast.Attribute) and \
           isinstance(node.targets[0].value, ast.Name) and \
           node.targets[0].value.id == 'self' and node.targets[0].attr == 'container':
            self.class_container_init[self.current_class] = node.value
            
    def is_primitive(self, class_name):
        deductions = self.unroll_dict[class_name]['deductions']
        base_classes = self.unroll_dict[class_name].get('base_classes', [])

        # Check for direct inheritance from primitive types
        if 'int' in base_classes:
            deductions.append(f'{class_name} subclasses int')
            self.unroll_dict[class_name]['type'] = 'int'
        elif 'str' in base_classes:
            deductions.append(f'{class_name} subclasses str')
            self.unroll_dict[class_name]['type'] = 'str'

    def mock_container_keys(self, class_name):
        container_node = self.class_container_init.get(class_name, None)
        if container_node and isinstance(container_node, ast.Dict):
            # Extract keys from the dictionary assignment
            keys = [ast.literal_eval(key) for key in container_node.keys]
            return keys
        return None 

    def is_collection(self, class_name):
        essential_methods = ['__init__', '__iter__', '__len__', '__getitem__', '__setitem__']
        methods = self.class_methods[class_name]
        deductions = self.unroll_dict[class_name]['deductions']

        # Check if essential methods are implemented
        if not all(method in methods for method in essential_methods):
            return

        # Retrieve the keys from the 'container' attribute, if it exists
        container_keys = self.mock_container_keys(class_name)

        # Check if any unique methods are implemented
        if any(method in methods for method in ['append', 'extend', 'insert', 'remove', 'index', 'count', 'sort', 'reverse']):
            deductions.append('implements list-specific methods')
            self.unroll_dict[class_name]['type'] = 'list'
        elif any(method in methods for method in ['get', 'items', 'keys', 'popitem', 'setdefault', 'update', 'values']):
            deductions.append('implements dict-specific methods')
            self.unroll_dict[class_name]['type'] = 'dict'
        elif any(method in methods for method in ['add', 'discard', 'union', 'intersection', 'difference', 'symmetric_difference', 
                                                'intersection_update', 'difference_update', 'symmetric_difference_update']):
            deductions.append('implements set-specific methods')
            self.unroll_dict[class_name]['type'] = 'set'

        # Parse through container keys to determine type if no unique methods are implemented
        elif container_keys:
            if all(isinstance(key, int) for key in container_keys) and \
                    sorted(container_keys) == list(range(min(container_keys), max(container_keys)+1)):
                deductions.append('key structure suggests list-like behavior')
                self.unroll_dict[class_name]['type'] = 'list'
            else:
                deductions.append('key structure suggests dict-like behavior')
                self.unroll_dict[class_name]['type'] = 'dict'
        else:
            deductions.append('defaulting to dict due to general format and absence of unique collection methods')
            self.unroll_dict[class_name]['type'] = 'dict'


    def infer_class_type(self, class_name):
        self.is_primitive(class_name)
        if self.unroll_dict[class_name]['type'] == 'unknown':
            self.is_collection(class_name)
        if self.unroll_dict[class_name]['type'] == 'unknown':
            self.unroll_dict[class_name]['deductions'].append('no specific type patterns recognized')
            self.unroll_dict[class_name]['type'] = 'object'

def analyze_code_to_unroll_dict(code):
    tree = ast.parse(code)
    inferrer = TypeInferrer()
    inferrer.visit(tree)
    return inferrer.unroll_dict, inferrer.class_container_init

def extract_initialization_expression(node, type_str):
    if isinstance(node, ast.Dict):
        if type_str == 'dict':
            keys = [astunparse.unparse(k).strip() for k in node.keys]
            values = [astunparse.unparse(v).strip() for v in node.values]
            items = [f"{k}: {v}" for k, v in zip(keys, values)]
            return "{" + ", ".join(items) + "}"
        elif type_str in ['list', 'set']:
            values = [astunparse.unparse(v).strip() for v in node.values]
            if type_str == 'list':
                return "[" + ", ".join(values) + "]"
            else:  # set
                return "{" + ", ".join(values) + "}"
    # Empty structures to be safe
    if type_str == 'dict':
        return "{}"
    elif type_str == 'list':
        return "[]"
    elif type_str == 'set':
        return "set()"

class InstantiationTracker(ast.NodeVisitor):
    def __init__(self):
        self.instantiated_classes = set()

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.instantiated_classes.add(node.func.id)
        self.generic_visit(node)

def apply_replacements_and_remove_classes(code_snippet, unroll_dict, class_container_init):
    replaced_classes = set()

    for class_name, info in unroll_dict.items():
        if info['type'] in ['list', 'dict', 'set']:
            # Container types
            replacement = extract_initialization_expression(class_container_init.get(class_name, ast.Dict()), info['type'] )
        elif info['type'] == 'int':
            # Set Integers to 0
            replacement = '0'
        elif info['type'] == 'str':
            # Set strings to an empty string
            replacement = '""'
        else:
            # If no specific type was recognized, skip replacement
            continue
        
        # Perform the replacement in the code snippet
        code_snippet = code_snippet.replace(f"{class_name}()", replacement)
        replaced_classes.add(class_name)

    # Removes classes that were identified as a type like str
    tree = ast.parse(code_snippet)
    for node in ast.walk(tree):
        if isinstance(node, ast.Module):
            node.body = [n for n in node.body if not (isinstance(n, ast.ClassDef) and n.name in replaced_classes)]

    # Removes classes that are leftover object classes
    tracker = InstantiationTracker()
    tracker.visit(tree)

    new_body = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            # Keep the class def only if it's instantiated
            if node.name not in tracker.instantiated_classes:
                continue 
        new_body.append(node)
    tree.body = new_body
    
    return astunparse.unparse(tree)

def unmock_code_snippet(snippet_obj):
    """
    Analyzes the given code snippet, applies type deductions to replace class instantiations,
    and removes unused class definitions.

    Args:
        snippet_obj (Snippet): The Snippet object to analyze and update.

    Returns:
        str: The updated code snippet.
    """

    code_snippet = snippet_obj.get_latest()
    unroll_dict, class_container_init = analyze_code_to_unroll_dict(code_snippet)
    updated_code_snippet = apply_replacements_and_remove_classes(code_snippet, unroll_dict, class_container_init)
    for var, info in unroll_dict.items():
        print(f"{var}: {info}")
    return updated_code_snippet

# To run directly for testing
if __name__ == "__main__":
    code_snippet = """ 
    """
    unroll_dict, class_container_init = analyze_code_to_unroll_dict(code_snippet)
    updated_code_snippet = apply_replacements_and_remove_classes(code_snippet, unroll_dict, class_container_init)
    for var, info in unroll_dict.items():
        print(f"{var}: {info}")
    print(updated_code_snippet)