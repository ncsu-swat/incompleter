# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54998967/attributeerror-list-object-has-no-attribute-feature
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def tree_to_code(tree, feature_names):
    _l_(691022)

    tree_ = _a_(690897, _n_(690896, "tree", lambda: tree), "estimators_")
    _l_(690898)
    #print(tree_)
    feature_name = [
        _n_(690899, "feature_names", lambda: feature_names)[_n_(690900, "i", lambda: i)] if _n_(690901, "i", lambda: i) != _a_(690903, _n_(690902, "_tree", lambda: _tree), "TREE_UNDEFINED") else "undefined!"
        for i in _a_(690905, _n_(690904, "tree_", lambda: tree_), "feature")
    ]
    _l_(690906)
    _c_(690913, _n_(690907, "print", lambda: print), _c_(690912, _a_(690908, "def tree({}):", "format"), _c_(690911, _a_(690909, ", ", "join"), _n_(690910, "feature_names", lambda: feature_names))))
    _l_(690914)
    symptoms_present = []
    _l_(690915)
    def recurse(node, depth):
        _l_(691018)

        indent = "  " * _n_(690916, "depth", lambda: depth)
        _l_(690917)
        if _a_(690919, _n_(690918, "tree_", lambda: tree_), "feature")[_n_(690920, "node", lambda: node)] != _a_(690922, _n_(690921, "_tree", lambda: _tree), "TREE_UNDEFINED"):
            _l_(691017)

            name = _n_(690923, "feature_name", lambda: feature_name)[_n_(690924, "node", lambda: node)]
            _l_(690925)
            threshold = _a_(690927, _n_(690926, "tree_", lambda: tree_), "threshold")[_n_(690928, "node", lambda: node)]
            _l_(690929)
            _c_(690932, _n_(690930, "print", lambda: print), _n_(690931, "name", lambda: name) + " ?")
            _l_(690933)
            ans = _c_(690935, _n_(690934, "input", lambda: input))
            _l_(690936)
            ans = _c_(690939, _a_(690938, _n_(690937, "ans", lambda: ans), "lower"))
            _l_(690940)
            if _n_(690941, "ans", lambda: ans) == 'yes':
                _l_(690944)

                val = 1
                _l_(690942)
            else:
                val = 0
                _l_(690943)
            if  _n_(690945, "val", lambda: val) <= _n_(690946, "threshold", lambda: threshold):
                _l_(690966)

                _c_(690952, _n_(690947, "recurse", lambda: recurse), _a_(690949, _n_(690948, "tree_", lambda: tree_), "children_left")[_n_(690950, "node", lambda: node)], _n_(690951, "depth", lambda: depth) + 1)
                _l_(690953)
            else:
                _c_(690957, _a_(690955, _n_(690954, "symptoms_present", lambda: symptoms_present), "append"), _n_(690956, "name", lambda: name))
                _l_(690958)
                _c_(690964, _n_(690959, "recurse", lambda: recurse), _a_(690961, _n_(690960, "tree_", lambda: tree_), "children_right")[_n_(690962, "node", lambda: node)], _n_(690963, "depth", lambda: depth) + 1)
                _l_(690965)
        else:
            present_disease = _c_(690971, _n_(690967, "print_disease", lambda: print_disease), _a_(690969, _n_(690968, "tree_", lambda: tree_), "value")[_n_(690970, "node", lambda: node)])
            _l_(690972)
            _c_(690975, _n_(690973, "print", lambda: print), "You may have " +  _n_(690974, "present_disease", lambda: present_disease) )
            _l_(690976)
            red_cols = _a_(690978, _n_(690977, "reduced_data", lambda: reduced_data), "columns") 
            _l_(690979) 
            symptoms_given = _n_(690980, "red_cols", lambda: red_cols)[_c_(690986, _a_(690985, _a_(690984, _a_(690982, _n_(690981, "reduced_data", lambda: reduced_data), "loc")[_n_(690983, "present_disease", lambda: present_disease)], "values")[0], "nonzero"))]
            _l_(690987)
            _c_(690994, _n_(690988, "print", lambda: print), "symptoms present  " + _c_(690993, _n_(690989, "str", lambda: str), _c_(690992, _n_(690990, "list", lambda: list), _n_(690991, "symptoms_present", lambda: symptoms_present))))
            _l_(690995)
            _c_(691002, _n_(690996, "print", lambda: print), "symptoms given "  +  _c_(691001, _n_(690997, "str", lambda: str), _c_(691000, _n_(690998, "list", lambda: list), _n_(690999, "symptoms_given", lambda: symptoms_given))) )  
            _l_(691003)  
            confidence_level = (1.0*_c_(691006, _n_(691004, "len", lambda: len), _n_(691005, "symptoms_present", lambda: symptoms_present)))/_c_(691009, _n_(691007, "len", lambda: len), _n_(691008, "symptoms_given", lambda: symptoms_given))
            _l_(691010)
            _c_(691015, _n_(691011, "print", lambda: print), "confidence level is " + _c_(691014, _n_(691012, "str", lambda: str), _n_(691013, "confidence_level", lambda: confidence_level)))
            _l_(691016)

    _c_(691020, _n_(691019, "recurse", lambda: recurse), 0, 1)
    _l_(691021)

_c_(691026, _n_(691023, "tree_to_code", lambda: tree_to_code), _n_(691024, "clf", lambda: clf),_n_(691025, "cols", lambda: cols))
_l_(691027)