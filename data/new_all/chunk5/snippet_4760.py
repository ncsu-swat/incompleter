# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49332694/attributeerror-grammatrix-object-has-no-attribute-gradinput
# Define an nn Module to compute content loss in-place
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ContentLoss(_n_(661721, "object", lambda: object)):
    _l_(661805)


    def __init__(self, strength):
        _l_(661737)

        _c_(661726, _a_(661725, _n_(661722, "super", lambda: super)(_n_(661723, "ContentLoss", lambda: ContentLoss), _n_(661724, "self", lambda: self)), "__init__"))
        _l_(661727)
        _n_(661728, "self", lambda: self).strength = _n_(661729, "strength", lambda: strength)
        _l_(661730)
        _n_(661731, "self", lambda: self).target = 0
        _l_(661732)
        _n_(661733, "self", lambda: self).loss = 0
        _l_(661734)
        _n_(661735, "self", lambda: self).mode = None
        _l_(661736)

    def forward(self, input):
        _l_(661769)

        _c_(661739, _n_(661738, "print", lambda: print), "ContentLoss - Forward")
        _l_(661740)
        if _a_(661742, _n_(661741, "self", lambda: self), "mode") == 'loss':
            _l_(661762)

            _c_(661744, _n_(661743, "print", lambda: print), "ContentLoss - Forward - Loss")
            _l_(661745)
            _n_(661746, "self", lambda: self).loss = (_n_(661747, "input", lambda: input) * _a_(661749, _n_(661748, "self", lambda: self), "target")) * _a_(661751, _n_(661750, "self", lambda: self), "strength") #Forward
            _l_(661752) #Forward
        elif _a_(661754, _n_(661753, "self", lambda: self), "mode") == 'capture':
            _l_(661761)

            _c_(661756, _n_(661755, "print", lambda: print), "ContentLoss - Forward - Capture")
            _l_(661757)
            _n_(661758, "self", lambda: self).target = _n_(661759, "input", lambda: input)
            _l_(661760)
        _n_(661763, "self", lambda: self).output = _n_(661764, "input", lambda: input) 
        _l_(661765) 
        aux = _a_(661767, _n_(661766, "self", lambda: self), "output")
        _l_(661768)
        return aux

    def backward(self, input, gradOutput):
        _l_(661804)

        _c_(661771, _n_(661770, "print", lambda: print), "ContentLoss - Backward") 
        _l_(661772) 
        if _a_(661774, _n_(661773, "self", lambda: self), "mode") == 'loss':
            _l_(661800)

            _c_(661776, _n_(661775, "print", lambda: print), "ContentLoss - Backward - Loss")
            _l_(661777)
            _n_(661778, "self", lambda: self).gradInput = _n_(661779, "input", lambda: input) * _a_(661781, _n_(661780, "self", lambda: self), "target") # Backward
            _l_(661782) # Backward
            _n_(661783, "self", lambda: self).gradInput = _a_(661785, _n_(661784, "self", lambda: self), "gradInput") * _a_(661787, _n_(661786, "self", lambda: self), "strength")
            _l_(661788)
            _n_(661789, "self", lambda: self).gradInput = _a_(661791, _n_(661790, "self", lambda: self), "gradInput") + _n_(661792, "gradOutput", lambda: gradOutput)
            _l_(661793)
        else:
          _c_(661795, _n_(661794, "print", lambda: print), "ContentLoss - Backward - Capture")
          _l_(661796)
          _n_(661797, "self", lambda: self).target = _n_(661798, "gradOutput", lambda: gradOutput)
          _l_(661799)
        aux = _a_(661802, _n_(661801, "self", lambda: self), "gradInput")
        _l_(661803)
        return aux


class GramMatrix(_n_(661806, "object", lambda: object)):
    _l_(661831)

    def __init__(self):
        _l_(661813)

        _c_(661811, _a_(661810, _n_(661807, "super", lambda: super)(_n_(661808, "GramMatrix", lambda: GramMatrix), _n_(661809, "self", lambda: self)), "__init__"))
        _l_(661812)

    def forward(self, input):
        _l_(661820)

        _n_(661814, "self", lambda: self).output = _n_(661815, "input", lambda: input)
        _l_(661816)
        aux = _a_(661818, _n_(661817, "self", lambda: self), "output")
        _l_(661819)
        return aux

    def backward(self, input, gradOutput):
        _l_(661830)

        _n_(661821, "self", lambda: self).gradInput = _a_(661823, _n_(661822, "self", lambda: self), "gradInput") + _n_(661824, "gradOutput", lambda: gradOutput) + _n_(661825, "input", lambda: input)
        _l_(661826)
        aux = _a_(661828, _n_(661827, "self", lambda: self), "gradInput")
        _l_(661829)
        return aux

class StyleLoss(_n_(661832, "object", lambda: object)):
    _l_(661948)


    def __init__(self, strength):
        _l_(661856)

        _c_(661837, _a_(661836, _n_(661833, "super", lambda: super)(_n_(661834, "StyleLoss", lambda: StyleLoss), _n_(661835, "self", lambda: self)), "__init__"))
        _l_(661838)
        _n_(661839, "self", lambda: self).strength = _n_(661840, "strength", lambda: strength)
        _l_(661841)
        _n_(661842, "self", lambda: self).target = 0
        _l_(661843)
        _n_(661844, "self", lambda: self).mode = None
        _l_(661845)
        _n_(661846, "self", lambda: self).loss = 0
        _l_(661847)
        _n_(661848, "self", lambda: self).gram = _c_(661850, _n_(661849, "GramMatrix", lambda: GramMatrix))
        _l_(661851)
        _n_(661852, "self", lambda: self).blend_weight = None
        _l_(661853)
        _n_(661854, "self", lambda: self).G = None
        _l_(661855)

    def forward(self, input):
        _l_(661908)

        _c_(661858, _n_(661857, "print", lambda: print), "StyleLoss - Forward")
        _l_(661859)
        _n_(661860, "self", lambda: self).G = _c_(661865, _a_(661863, _a_(661862, _n_(661861, "self", lambda: self), "gram"), "forward"), _n_(661864, "input", lambda: input))
        _l_(661866)
        if _a_(661868, _n_(661867, "self", lambda: self), "mode") == 'capture':
            _l_(661901)

            _c_(661870, _n_(661869, "print", lambda: print), "StyleLoss - Forward - Capture")
            _l_(661871)
            if _a_(661873, _n_(661872, "self", lambda: self), "blend_weight") == None:
                _l_(661886)

                _n_(661874, "self", lambda: self).target = _a_(661876, _n_(661875, "self", lambda: self), "G")
                _l_(661877)
            else:
              _n_(661878, "self", lambda: self).target = _a_(661880, _n_(661879, "self", lambda: self), "target") + (_a_(661882, _n_(661881, "self", lambda: self), "blend_weight") * _a_(661884, _n_(661883, "self", lambda: self), "G"))
              _l_(661885)
        elif _a_(661888, _n_(661887, "self", lambda: self), "mode") == 'loss':
            _l_(661900)

            _c_(661890, _n_(661889, "print", lambda: print), "StyleLoss - Forward - Loss")
            _l_(661891)
            _n_(661892, "self", lambda: self).loss = _a_(661894, _n_(661893, "self", lambda: self), "strength") * (_a_(661896, _n_(661895, "self", lambda: self), "G") * _a_(661898, _n_(661897, "self", lambda: self), "target")) #Forward
            _l_(661899) #Forward
        _n_(661902, "self", lambda: self).output = _n_(661903, "input", lambda: input)
        _l_(661904)
        aux = _a_(661906, _n_(661905, "self", lambda: self), "output")
        _l_(661907)
        return aux

    def backward(self, input, gradOutput):
        _l_(661947)

        _c_(661910, _n_(661909, "print", lambda: print), "StyleLoss - Backward")
        _l_(661911)
        if _a_(661913, _n_(661912, "self", lambda: self), "mode") == 'loss':
            _l_(661943)

            dG = _c_(661921, _a_(661916, _a_(661915, _n_(661914, "self", lambda: self), "gram"), "backward"), _a_(661918, _n_(661917, "self", lambda: self), "G"), _a_(661920, _n_(661919, "self", lambda: self), "target"))
            _l_(661922)
            _n_(661923, "self", lambda: self).gradInput = _n_(661924, "input", lambda: input) * _n_(661925, "dG", lambda: dG)
            _l_(661926)
            _n_(661927, "self", lambda: self).gradInput = _a_(661929, _n_(661928, "self", lambda: self), "gradInput") * _a_(661931, _n_(661930, "self", lambda: self), "strength")
            _l_(661932)
            _n_(661933, "self", lambda: self).gradInput = _a_(661935, _n_(661934, "self", lambda: self), "gradOutput")
            _l_(661936)
        else: 
          _c_(661938, _n_(661937, "print", lambda: print), "StyleLoss - Backward - Capture")
          _l_(661939)
          _n_(661940, "self", lambda: self).gradInput = _n_(661941, "gradOutput", lambda: gradOutput)
          _l_(661942)
        aux = _a_(661945, _n_(661944, "self", lambda: self), "gradInput")
        _l_(661946)
        return aux



input_value = 1
_l_(661949)
gradOut_value = 0
_l_(661950)
weight = 5
_l_(661951)
CL = _c_(661954, _n_(661952, "ContentLoss", lambda: ContentLoss), _n_(661953, "weight", lambda: weight))
_l_(661955)
SL = _c_(661958, _n_(661956, "StyleLoss", lambda: StyleLoss), _n_(661957, "weight", lambda: weight))
_l_(661959)

_n_(661960, "CL", lambda: CL).mode = 'capture'
_l_(661961)
_c_(661965, _a_(661963, _n_(661962, "CL", lambda: CL), "forward"), _n_(661964, "input_value", lambda: input_value))
_l_(661966)

_n_(661967, "CL", lambda: CL).mode = None
_l_(661968)
_n_(661969, "SL", lambda: SL).mode = 'capture'
_l_(661970)
_c_(661974, _a_(661972, _n_(661971, "SL", lambda: SL), "forward"), _n_(661973, "input_value", lambda: input_value))
_l_(661975)

_n_(661976, "CL", lambda: CL).mode = 'loss'
_l_(661977)
_n_(661978, "SL", lambda: SL).mode = 'loss'
_l_(661979)

_c_(661983, _a_(661981, _n_(661980, "CL", lambda: CL), "forward"), _n_(661982, "input_value", lambda: input_value))
_l_(661984)
_c_(661988, _a_(661986, _n_(661985, "SL", lambda: SL), "forward"), _n_(661987, "input_value", lambda: input_value))
_l_(661989)

_c_(661994, _a_(661991, _n_(661990, "CL", lambda: CL), "backward"), _n_(661992, "input_value", lambda: input_value), _n_(661993, "gradOut_value", lambda: gradOut_value))
_l_(661995)
_c_(662000, _a_(661997, _n_(661996, "SL", lambda: SL), "backward"), _n_(661998, "input_value", lambda: input_value), _n_(661999, "gradOut_value", lambda: gradOut_value))
_l_(662001)