# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47249491/how-to-fix-attributeerror-module-testing2-has-no-attribute-printpackage
#testing2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import testing1
    _l_(669086)

except ImportError:
    pass
menuList = _c_(669090, _a_(669088, _n_(669087, "testing1", lambda: testing1), "calculateMenuPrice"), _n_(669089, "choice", lambda: choice))
_l_(669091)
def printPackage(menuList):
    _l_(669106)

    for x in _n_(669092, "menuList", lambda: menuList):
        _l_(669105)

        if _n_(669093, "menuList", lambda: menuList) == '1':
            _l_(669104)

            aux = ('''
----------
Menu List
----------
1. Jelly Fish Yee Sang with Pear
2. Dried Seafood with Fish Soup 
3. Steamed Sea Water Grouper

''')        
            _l_(669094)        
            return aux        
        elif _n_(669095, "menuList", lambda: menuList) == '2':
            _l_(669103)

            aux = ('''
----------
Menu List
----------
1. Jelly Fish Yee Sang with Pear
2. Shark Fin Soup with Crab Meat
3. Steamed River Patin Fish
''')
            _l_(669096)
            return aux
        elif _n_(669097, "menuList", lambda: menuList) == '3':
            _l_(669102)

            aux = ('''
----------
Menu List
----------
1. Salmon Fish Yee Sang with Pear
2. Steamed Classic Abalone Soup
3. Steamed Bamboo Fish

''')
            _l_(669098)
            return aux

        elif _n_(669099, "menuList", lambda: menuList) == '4':
            _l_(669101)

            aux = ('''
----------
Menu List
----------
1. Abalone Yee Sang with Pear
2. Mini Classic Steam Soup
3. Steamed Local Pomfret Fish

''')
            _l_(669100)
            return aux