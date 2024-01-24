# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59474790/getting-nonetype-attribute-error-in-python3
# Generating data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
training_data = [
    ["Green", 3, "Mango"],
    ["Yellow", 3, "Mango"],
    ["Red", 1, "Grape"],
    ["Red", 1, "Grape"],
    ["Yellow", 3, "Lemon"],
]
_l_(706451)


# Column Labels
header = ["color", "diameter", "label"]
_l_(706452)

def unique_vals(rows, col):
    _l_(706459)

    """Find unique values for a column in dataset."""
    aux = _c_(706457, _n_(706453, "set", lambda: set), [_n_(706454, "row", lambda: row)[_n_(706455, "col", lambda: col)] for row in _n_(706456, "rows", lambda: rows)])
    _l_(706458)
    return aux

def class_counts(rows):
    _l_(706476)

    """Counts # of each typre of eg. in datset."""
    counts = {}
    _l_(706460)
    for row in _n_(706461, "rows", lambda: rows):
        _l_(706473)

        label = _n_(706462, "row", lambda: row)[-1]
        _l_(706463)
        if _n_(706464, "label", lambda: label) not in _n_(706465, "counts", lambda: counts):
            _l_(706469)

            _n_(706466, "counts", lambda: counts)[_n_(706467, "label", lambda: label)] = 0
            _l_(706468)
        _n_(706470, "counts", lambda: counts)[_n_(706471, "label", lambda: label)] += 1
        _l_(706472)
    aux = _n_(706474, "counts", lambda: counts)
    _l_(706475)
    return aux

def is_numeric(value):
    _l_(706486)

    """Check if a value is numeric"""
    aux = _c_(706480, _n_(706477, "isinstance", lambda: isinstance), _n_(706478, "value", lambda: value), _n_(706479, "int", lambda: int)) or _c_(706484, _n_(706481, "isinstance", lambda: isinstance), _n_(706482, "value", lambda: value), _n_(706483, "float", lambda: float))
    _l_(706485)
    return aux


# Spliting dataset based on questions
class Question:
    _l_(706528)


    def __init__(self, column, value):
        _l_(706493)

        _n_(706487, "self", lambda: self).column = _n_(706488, "column", lambda: column)
        _l_(706489)
        _n_(706490, "self", lambda: self).value = _n_(706491, "value", lambda: value)
        _l_(706492)

    def match(self, example):
        _l_(706510)

        # compare feature values
        val = _n_(706494, "example", lambda: example)[_a_(706496, _n_(706495, "self", lambda: self), "column")]
        _l_(706497)
        if _c_(706500, _n_(706498, "is_numeric", lambda: is_numeric), _n_(706499, "val", lambda: val)):
            _l_(706509)

            aux = _n_(706501, "val", lambda: val) >= _a_(706503, _n_(706502, "self", lambda: self), "value")
            _l_(706504)
            return aux
        else:
            aux = _n_(706505, "val", lambda: val) == _a_(706507, _n_(706506, "self", lambda: self), "value")
            _l_(706508)
            return aux


    def __repr__(self):
        _l_(706527)

        condition = "=="
        _l_(706511)
        if _c_(706515, _n_(706512, "is_numeric", lambda: is_numeric), _a_(706514, _n_(706513, "self", lambda: self), "value")):
            _l_(706517)

            condition = ">="
            _l_(706516)
        aux = "Is %s %s %s?" % (
            _n_(706518, "header", lambda: header)[_a_(706520, _n_(706519, "self", lambda: self), "column")], _n_(706521, "condition", lambda: condition), _c_(706525, _n_(706522, "str", lambda: str), _a_(706524, _n_(706523, "self", lambda: self), "value")))
        _l_(706526)
        return aux


def partition(rows, question):
    _l_(706550)

    true_rows, false_rows = [], []
    _l_(706529)
    for row in _n_(706530, "rows", lambda: rows):
        _l_(706546)

        if _c_(706534, _a_(706532, _n_(706531, "question", lambda: question), "match"), _n_(706533, "row", lambda: row)):
            _l_(706545)

            _c_(706538, _a_(706536, _n_(706535, "true_rows", lambda: true_rows), "append"), _n_(706537, "row", lambda: row))
            _l_(706539)
        else:
            _c_(706543, _a_(706541, _n_(706540, "false_rows", lambda: false_rows), "append"), _n_(706542, "row", lambda: row))
            _l_(706544)
    aux = _n_(706547, "true_rows", lambda: true_rows), _n_(706548, "false_rows", lambda: false_rows)
    _l_(706549)
    return aux

# Entropy    
def gini(rows):
    _l_(706570)


    counts = _c_(706553, _n_(706551, "class_counts", lambda: class_counts), _n_(706552, "rows", lambda: rows))
    _l_(706554)
    impurity = 1
    _l_(706555)
    for lbl in _n_(706556, "counts", lambda: counts):
        _l_(706567)

        prob_if_lbl = _n_(706557, "counts", lambda: counts)[_n_(706558, "lbl", lambda: lbl)]/_c_(706563, _n_(706559, "float", lambda: float), _c_(706562, _n_(706560, "len", lambda: len), _n_(706561, "rows", lambda: rows)))
        _l_(706564)
        impurity -= _n_(706565, "prob_if_lbl", lambda: prob_if_lbl)**2
        _l_(706566)
    aux = _n_(706568, "impurity", lambda: impurity)
    _l_(706569)
    return aux

def info_gain(left, right, current_uncertainity):
    _l_(706593)

    p = _c_(706575, _n_(706571, "float", lambda: float), _c_(706574, _n_(706572, "len", lambda: len), _n_(706573, "left", lambda: left)))/_c_(706578, _n_(706576, "len", lambda: len), _n_(706577, "left", lambda: left)) + _c_(706581, _n_(706579, "len", lambda: len), _n_(706580, "right", lambda: right))
    _l_(706582)
    aux = _n_(706583, "current_uncertainity", lambda: current_uncertainity) - _n_(706584, "p", lambda: p) * _c_(706587, _n_(706585, "gini", lambda: gini), _n_(706586, "left", lambda: left)) - (1-_n_(706588, "p", lambda: p)) * _c_(706591, _n_(706589, "gini", lambda: gini), _n_(706590, "right", lambda: right))
    _l_(706592)
    return aux


def find_best_split(rows):
    _l_(706649)

    best_gain = 0
    _l_(706594)
    best_question = None
    _l_(706595)
    current_uncertainity = _c_(706598, _n_(706596, "gini", lambda: gini), _n_(706597, "rows", lambda: rows))
    _l_(706599)
    n_features = _c_(706602, _n_(706600, "len", lambda: len), _n_(706601, "rows", lambda: rows)[0]) - 1
    _l_(706603)

    for col in _c_(706606, _n_(706604, "range", lambda: range), _n_(706605, "n_features", lambda: n_features)):
        _l_(706645)

        values = _c_(706611, _n_(706607, "set", lambda: set), [_n_(706608, "row", lambda: row)[_n_(706609, "col", lambda: col)] for row in _n_(706610, "rows", lambda: rows)])
        _l_(706612)

        for val in _n_(706613, "values", lambda: values):
            _l_(706644)

            question = _c_(706617, _n_(706614, "Question", lambda: Question), _n_(706615, "col", lambda: col), _n_(706616, "val", lambda: val))
            _l_(706618)
            true_rows, false_rows = _c_(706622, _n_(706619, "partition", lambda: partition), _n_(706620, "rows", lambda: rows), _n_(706621, "question", lambda: question))
            _l_(706623)

            if _c_(706626, _n_(706624, "len", lambda: len), _n_(706625, "true_rows", lambda: true_rows)) == 0 or _c_(706629, _n_(706627, "len", lambda: len), _n_(706628, "false_rows", lambda: false_rows)) == 0:
                _l_(706631)

                continue
                _l_(706630)

            gain = _c_(706636, _n_(706632, "info_gain", lambda: info_gain), _n_(706633, "true_rows", lambda: true_rows), _n_(706634, "false_rows", lambda: false_rows), _n_(706635, "current_uncertainity", lambda: current_uncertainity))
            _l_(706637)

            if _n_(706638, "gain", lambda: gain) >= _n_(706639, "best_gain", lambda: best_gain):
                _l_(706643)

                best_gain, best_question = _n_(706640, "gain", lambda: gain), _n_(706641, "question", lambda: question)
                _l_(706642)
    aux = _n_(706646, "best_gain", lambda: best_gain), _n_(706647, "best_question", lambda: best_question)
    _l_(706648)
    return aux


# Defining tree

class leaf:
    _l_(706656)


    def __init__(self, rows):
        _l_(706655)

        _n_(706650, "self", lambda: self).predicitons = _c_(706653, _n_(706651, "class_counts", lambda: class_counts), _n_(706652, "rows", lambda: rows))
        _l_(706654)

class Decision_Node:
    _l_(706667)


    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        _l_(706666)

        _n_(706657, "self", lambda: self).question = _n_(706658, "question", lambda: question)
        _l_(706659)
        _n_(706660, "self", lambda: self).true_branch = _n_(706661, "true_branch", lambda: true_branch)
        _l_(706662)
        _n_(706663, "self", lambda: self).false_branch = _n_(706664, "false_branch", lambda: false_branch)
        _l_(706665)

def build_tree(rows):
    _l_(706691)

    gain, question = _c_(706670, _n_(706668, "find_best_split", lambda: find_best_split), _n_(706669, "rows", lambda: rows))
    _l_(706671)

    if _n_(706672, "gain", lambda: gain) == 0:
        _l_(706677)

        aux = _c_(706675, _n_(706673, "leaf", lambda: leaf), _n_(706674, "rows", lambda: rows))
        _l_(706676)
        return aux

    true_rows, false_rows = _c_(706681, _n_(706678, "partition", lambda: partition), _n_(706679, "rows", lambda: rows), _n_(706680, "question", lambda: question))
    _l_(706682)
    true_branch = _c_(706685, _n_(706683, "build_tree", lambda: build_tree), _n_(706684, "true_rows", lambda: true_rows))
    _l_(706686)
    false_branch = _c_(706689, _n_(706687, "build_tree", lambda: build_tree), _n_(706688, "false_rows", lambda: false_rows))
    _l_(706690)

def print_tree(node, spacing=""):
    _l_(706732)

    if _c_(706695, _n_(706692, "isinstance", lambda: isinstance), _n_(706693, "node", lambda: node), _n_(706694, "leaf", lambda: leaf)):
        _l_(706703)

        _c_(706700, _n_(706696, "print", lambda: print), _n_(706697, "spacing", lambda: spacing) + "Predict", _a_(706699, _n_(706698, "node", lambda: node), "predicitons"))
        _l_(706701)
        aux = ""
        _l_(706702)
        return aux

    _c_(706710, _n_(706704, "print", lambda: print), _n_(706705, "spacing", lambda: spacing) + _c_(706709, _n_(706706, "str", lambda: str), _a_(706708, _n_(706707, "node", lambda: node), "question")))
    _l_(706711)

    _c_(706714, _n_(706712, "print", lambda: print), _n_(706713, "spacing", lambda: spacing) + "--> True")
    _l_(706715)
    _c_(706720, _n_(706716, "print_tree", lambda: print_tree), _a_(706718, _n_(706717, "node", lambda: node), "true_branch"), _n_(706719, "spacing", lambda: spacing) + " ")
    _l_(706721)
    _c_(706724, _n_(706722, "print", lambda: print), _n_(706723, "spacing", lambda: spacing) + "--> False")
    _l_(706725)
    _c_(706730, _n_(706726, "print_tree", lambda: print_tree), _a_(706728, _n_(706727, "node", lambda: node), "false_branch"), _n_(706729, "spacing", lambda: spacing) + " ")  
    _l_(706731)  


def classify(row,node):
    _l_(706759)


    if _c_(706736, _n_(706733, "isinstance", lambda: isinstance), _n_(706734, "node", lambda: node),_n_(706735, "leaf", lambda: leaf)):
        _l_(706740)

        aux = _a_(706738, _n_(706737, "node", lambda: node), "predicitons")
        _l_(706739)
        return aux

    if _c_(706745, _a_(706743, _a_(706742, _n_(706741, "node", lambda: node), "question"), "match"), _n_(706744, "row", lambda: row)):
        _l_(706758)

        aux = _c_(706750, _n_(706746, "classify", lambda: classify), _n_(706747, "row", lambda: row), _a_(706749, _n_(706748, "node", lambda: node), "true_branch"))
        _l_(706751)
        return aux
    else:
          aux = _c_(706756, _n_(706752, "classify", lambda: classify), _n_(706753, "row", lambda: row), _a_(706755, _n_(706754, "node", lambda: node), "false_branch"))
          _l_(706757)
          return aux

def print_leaf(counts):
    _l_(706783)

    total = _c_(706764, _n_(706760, "sum", lambda: sum), _c_(706763, _a_(706762, _n_(706761, "counts", lambda: counts), "values"))) * 1.0
    _l_(706765)
    probs = {}
    _l_(706766)
    for lbl in _c_(706769, _a_(706768, _n_(706767, "counts", lambda: counts), "keys")):
        _l_(706780)

        _n_(706770, "probs", lambda: probs)[_n_(706771, "lbl", lambda: lbl)] = _c_(706778, _n_(706772, "str", lambda: str), _c_(706777, _n_(706773, "int", lambda: int), _n_(706774, "counts", lambda: counts)[_n_(706775, "lbl", lambda: lbl)] / _n_(706776, "total", lambda: total) * 100)) + "%"
        _l_(706779)
    aux = _n_(706781, "probs", lambda: probs)
    _l_(706782)
    return aux


if _n_(706784, "__name__", lambda: __name__) == "__main__":
    _l_(706806)


    my_tree = _c_(706787, _n_(706785, "build_tree", lambda: build_tree), _n_(706786, "training_data", lambda: training_data))
    _l_(706788)

    _c_(706791, _n_(706789, "print_tree", lambda: print_tree), _n_(706790, "my_tree", lambda: my_tree))
    _l_(706792)

    testing_data = [
    ["Green", 3, "Mango"],
    ["Yellow", 4, "Mango"],
    ["Red", 2, "Grape"],
    ["Red", 1, "Grape"],
    ["Yellow", 3, "Lemon"],
]
    _l_(706793)

    for row in _n_(706794, "testing_data", lambda: testing_data):
        _l_(706805)

        _c_(706803, _n_(706795, "print", lambda: print), "Actual: %s. Predicted: %s" %
             (_n_(706796, "row", lambda: row)[-1], _c_(706802, _n_(706797, "print_leaf", lambda: print_leaf), _c_(706801, _n_(706798, "classify", lambda: classify), _n_(706799, "row", lambda: row), _n_(706800, "my_tree", lambda: my_tree)))))
        _l_(706804)