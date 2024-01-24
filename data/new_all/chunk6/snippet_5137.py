# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31354629/python-list-loop-error-typeerror-list-indices-must-be-integers-not-str
#Inventory and the Loot value
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
inv = {'gold coin': 42, 'rope': 1}
_l_(359414)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
_l_(359415)

#Function to loop through the items in the list
def displayInventory(inventory):
    _l_(359439)

    _c_(359417, _n_(359416, "print", lambda: print), 'Inventory:')
    _l_(359418)
    item_total = 0
    _l_(359419)
    for j, k in _c_(359422, _a_(359421, _n_(359420, "inventory", lambda: inventory), "items")):
        _l_(359432)

        _c_(359428, _n_(359423, "print", lambda: print), _c_(359426, _n_(359424, "str", lambda: str), _n_(359425, "k", lambda: k)) + ' ' + _n_(359427, "j", lambda: j))
        _l_(359429)
        item_total += _n_(359430, "k", lambda: k)
        _l_(359431)
    _c_(359437, _n_(359433, "print", lambda: print), 'Total number of items: %s' % _c_(359436, _n_(359434, "str", lambda: str), _n_(359435, "item_total", lambda: item_total)))
    _l_(359438)

#Where the problem occur
def addToInventory(inventory, addedItems):
    _l_(359458)

    for i in _n_(359440, "addedItems", lambda: addedItems):
        _l_(359457)

        if _n_(359441, "addedItems", lambda: addedItems)[_n_(359442, "i", lambda: i)] in _c_(359445, _a_(359444, _n_(359443, "inventory", lambda: inventory), "keys")):
            _l_(359456)

            #Edit: I see an error here now, but I will fix it after I get the loop working
            _n_(359446, "inventory", lambda: inventory)[_n_(359447, "addedItems", lambda: addedItems)[_n_(359448, "i", lambda: i)]] + 1
            _l_(359449)
        else:
            _c_(359454, _a_(359451, _n_(359450, "inventory", lambda: inventory), "setdefault"), _n_(359452, "addedItems", lambda: addedItems)[_n_(359453, "i", lambda: i)], 1)
            _l_(359455)

inv = _c_(359462, _n_(359459, "addToInventory", lambda: addToInventory), _n_(359460, "inv", lambda: inv), _n_(359461, "dragonLoot", lambda: dragonLoot))
_l_(359463)
_c_(359466, _n_(359464, "displayInventory", lambda: displayInventory), _n_(359465, "inv", lambda: inv))
_l_(359467)