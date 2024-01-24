# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72751187/attributeerror-function-object-has-no-attribute-issubtree-for-recursive-fun
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(584042)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> _n_(583993, "bool", lambda: bool):
        _l_(584041)


        def is_the_same(s, t):
            _l_(584019)


            if not _n_(583994, "s", lambda: s) and not _n_(583995, "t", lambda: t):
                _l_(584018)

                aux = True
                _l_(583996)
                # both s and t are empty
                return aux

            elif _n_(583997, "s", lambda: s) and _n_(583998, "t", lambda: t):
                _l_(584017)

                aux = _a_(584000, _n_(583999, "s", lambda: s), "val") == _a_(584002, _n_(584001, "t", lambda: t), "val") and _c_(584008, _n_(584003, "is_the_same", lambda: is_the_same), _a_(584005, _n_(584004, "s", lambda: s), "left"), _a_(584007, _n_(584006, "t", lambda: t), "left")) and _c_(584014, _n_(584009, "is_the_same", lambda: is_the_same), _a_(584011, _n_(584010, "s", lambda: s), "right"), _a_(584013, _n_(584012, "t", lambda: t), "right"))
                _l_(584015)
                # both s and t are non-empty
                # keep checking in DFS
                return aux

            else:
                aux = False
                _l_(584016)
                # one is empty, the other is non-empty
                return aux
        aux = _c_(584023, _n_(584020, "bool", lambda: bool), _n_(584021, "s", lambda: s) and _n_(584022, "t", lambda: t)) and (_c_(584027, _n_(584024, "is_the_same", lambda: is_the_same), _n_(584025, "s", lambda: s), _n_(584026, "t", lambda: t)) or _c_(584033, _a_(584029, _n_(584028, "self", lambda: self), "isSubtree"), _a_(584031, _n_(584030, "s", lambda: s), "left"), _n_(584032, "t", lambda: t)) or _c_(584039, _a_(584035, _n_(584034, "self", lambda: self), "isSubtree"), _a_(584037, _n_(584036, "s", lambda: s), "right"), _n_(584038, "t", lambda: t)))
        _l_(584040)

        # -----------------------------------------------------------
        return aux

t3 = _c_(584044, _n_(584043, "TreeNode", lambda: TreeNode), 3)
_l_(584045)
_n_(584046, "t3", lambda: t3).left = _c_(584048, _n_(584047, "TreeNode", lambda: TreeNode), 4)
_l_(584049)
_n_(584050, "t3", lambda: t3).right = _c_(584052, _n_(584051, "TreeNode", lambda: TreeNode), 5)
_l_(584053)
_a_(584055, _n_(584054, "t3", lambda: t3), "left").left = _c_(584057, _n_(584056, "TreeNode", lambda: TreeNode), 1)
_l_(584058)
_a_(584060, _n_(584059, "t3", lambda: t3), "left").right = _c_(584062, _n_(584061, "TreeNode", lambda: TreeNode), 2)
_l_(584063)

t4 = _c_(584065, _n_(584064, "TreeNode", lambda: TreeNode), 4)
_l_(584066)
_n_(584067, "t4", lambda: t4).left = _c_(584069, _n_(584068, "TreeNode", lambda: TreeNode), 1)
_l_(584070)
_n_(584071, "t4", lambda: t4).right = _c_(584073, _n_(584072, "TreeNode", lambda: TreeNode), 2)
_l_(584074)

a = _c_(584080, _a_(584076, _n_(584075, "Solution", lambda: Solution), "isSubtree"), _n_(584077, "self", lambda: self), _n_(584078, "t3", lambda: t3),_n_(584079, "t4", lambda: t4))
_l_(584081)
_c_(584084, _n_(584082, "print", lambda: print), _n_(584083, "a", lambda: a))
_l_(584085)