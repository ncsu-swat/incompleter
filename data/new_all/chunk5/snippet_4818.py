# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47249491/how-to-fix-attributeerror-module-testing2-has-no-attribute-printpackage
#testing2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import testing1
    _l_(649651)

except ImportError:
    pass
menuList = _c_(649655, _a_(649653, _n_(649652, "testing1", lambda: testing1), "calculateMenuPrice"), _n_(649654, "choice", lambda: choice))
_l_(649656)
def printPackage(menuList):
    _l_(649671)

    for x in _n_(649657, "menuList", lambda: menuList):
        _l_(649670)

        if _n_(649658, "menuList", lambda: menuList) == '1':
            _l_(649669)

            aux = ('''
----------
Menu List
----------
1. Jelly Fish Yee Sang with Pear
2. Dried Seafood with Fish Soup 
3. Steamed Sea Water Grouper

''')        
            _l_(649659)        
            return aux        
        elif _n_(649660, "menuList", lambda: menuList) == '2':
            _l_(649668)

            aux = ('''
----------
Menu List
----------
1. Jelly Fish Yee Sang with Pear
2. Shark Fin Soup with Crab Meat
3. Steamed River Patin Fish
''')
            _l_(649661)
            return aux
        elif _n_(649662, "menuList", lambda: menuList) == '3':
            _l_(649667)

            aux = ('''
----------
Menu List
----------
1. Salmon Fish Yee Sang with Pear
2. Steamed Classic Abalone Soup
3. Steamed Bamboo Fish

''')
            _l_(649663)
            return aux

        elif _n_(649664, "menuList", lambda: menuList) == '4':
            _l_(649666)

            aux = ('''
----------
Menu List
----------
1. Abalone Yee Sang with Pear
2. Mini Classic Steam Soup
3. Steamed Local Pomfret Fish

''')
            _l_(649665)
            return aux