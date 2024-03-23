#Source: https://stackoverflow.com/questions/37587459/python-ast-assign-node-attribute-error
source = r'C:\path\to\file\test.py'
with tokenize.open(source) as f:
    readFile = f.read()

class Py2Neko(ast.NodeVisitor):
    def generic_visit(self, node):
        #print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Assign(self, node):
        try:
            print("Assign :", node.value.id, node.lineno, node.col_offset)
        except AttributeError:
            print('Attribute Error:', node.lineno, node.col_offset)
        ast.NodeVisitor.generic_visit(self, node)

node = ast.parse(file_contents)
v = Py2Neko()
v.visit(node)