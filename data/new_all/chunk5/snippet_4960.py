# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37587459/python-ast-assign-node-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
source = r'C:\path\to\file\test.py'
_l_(684416)
with _c_(684420, _a_(684418, _n_(684417, "tokenize", lambda: tokenize), "open"), _n_(684419, "source", lambda: source)) as f:
    _l_(684425)

    readFile = _c_(684423, _a_(684422, _n_(684421, "f", lambda: f), "read"))
    _l_(684424)

class Py2Neko(_a_(684427, _n_(684426, "ast", lambda: ast), "NodeVisitor")):
    _l_(684464)

    def generic_visit(self, node):
        _l_(684435)

        #print(type(node).__name__)
        _c_(684433, _a_(684430, _a_(684429, _n_(684428, "ast", lambda: ast), "NodeVisitor"), "generic_visit"), _n_(684431, "self", lambda: self), _n_(684432, "node", lambda: node))
        _l_(684434)

    def visit_Assign(self, node):
        _l_(684463)

        try:
            _l_(684455)

            _c_(684444, _n_(684436, "print", lambda: print), "Assign :", _a_(684439, _a_(684438, _n_(684437, "node", lambda: node), "value"), "id"), _a_(684441, _n_(684440, "node", lambda: node), "lineno"), _a_(684443, _n_(684442, "node", lambda: node), "col_offset"))
            _l_(684445)
        except _n_(684446, "AttributeError", lambda: AttributeError):
            _l_(684454)

            _c_(684452, _n_(684447, "print", lambda: print), 'Attribute Error:', _a_(684449, _n_(684448, "node", lambda: node), "lineno"), _a_(684451, _n_(684450, "node", lambda: node), "col_offset"))
            _l_(684453)
        _c_(684461, _a_(684458, _a_(684457, _n_(684456, "ast", lambda: ast), "NodeVisitor"), "generic_visit"), _n_(684459, "self", lambda: self), _n_(684460, "node", lambda: node))
        _l_(684462)

node = _c_(684468, _a_(684466, _n_(684465, "ast", lambda: ast), "parse"), _n_(684467, "file_contents", lambda: file_contents))
_l_(684469)
v = _c_(684471, _n_(684470, "Py2Neko", lambda: Py2Neko))
_l_(684472)
_c_(684476, _a_(684474, _n_(684473, "v", lambda: v), "visit"), _n_(684475, "node", lambda: node))
_l_(684477)