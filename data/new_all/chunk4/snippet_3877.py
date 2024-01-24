# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66087209/dictionary-typeerror-list-indices-must-be-integers-or-slices-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(590657)

except ImportError:
    pass

textures = {"on_start.png":"(pygame image)","print.png":"(pygame image)"}
_l_(590658)

class block(_a_(590661, _a_(590660, _n_(590659, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(590691)

    def __init__(self,initx,inity,initp,initty,initte,initid):
        _l_(590690)

        _c_(590664, _a_(590663, _n_(590662, "super", lambda: super)(), "__init__"))
        _l_(590665)
        _n_(590666, "self", lambda: self).xpos = _n_(590667, "initx", lambda: initx)
        _l_(590668)
        _n_(590669, "self", lambda: self).ypos = _n_(590670, "inity", lambda: inity)
        _l_(590671)
        _n_(590672, "self", lambda: self).parent = _n_(590673, "initp", lambda: initp)
        _l_(590674)
        _n_(590675, "self", lambda: self).blockType = _n_(590676, "initty", lambda: initty)
        _l_(590677)
        _n_(590678, "self", lambda: self).texture = _n_(590679, "textures", lambda: textures)[_n_(590680, "initte", lambda: initte)]
        _l_(590681)
        _n_(590682, "self", lambda: self).blockID = _n_(590683, "initid", lambda: initid)
        _l_(590684)
        _c_(590688, _a_(590686, _n_(590685, "block_loop", lambda: block_loop), "add"), _n_(590687, "self", lambda: self))
        _l_(590689)

def load():
    _l_(590721)

    global block_loop, block_store, blockNumber
    _l_(590692)
    block_store = []
    _l_(590693)
    block_loop = _c_(590697, _a_(590696, _a_(590695, _n_(590694, "pygame", lambda: pygame), "sprite"), "Group"))
    _l_(590698)
    pend1 = {"next":2,"0":{"type":"on_start","x":50,"y":50,"parent":-1},"1":{"type":"print","x":0,"y":0,"parent":0}}
    _l_(590699)
    blockNumber = _n_(590700, "pend1", lambda: pend1)["next"]
    _l_(590701)
    del pend1["next"]
    _l_(590702)
    for item in _n_(590703, "pend1", lambda: pend1):
        _l_(590720)

        #print(pend1[item]["x"],pend1[item]["y"],pend1[item]["parent"],pend1[item]["type"],pend1[item]["type"] + ".png",item)
        _n_(590704, "block_store", lambda: block_store)[_n_(590705, "item", lambda: item)] = _c_(590718, _n_(590706, "block", lambda: block), _n_(590707, "pend1", lambda: pend1)[_n_(590708, "item", lambda: item)]["x"],_n_(590709, "pend1", lambda: pend1)[_n_(590710, "item", lambda: item)]["y"],_n_(590711, "pend1", lambda: pend1)[_n_(590712, "item", lambda: item)]["parent"],_n_(590713, "pend1", lambda: pend1)[_n_(590714, "item", lambda: item)]["type"],_n_(590715, "pend1", lambda: pend1)[_n_(590716, "item", lambda: item)]["type"] + ".png",_n_(590717, "item", lambda: item))
        _l_(590719)

_c_(590723, _n_(590722, "load", lambda: load))
_l_(590724)