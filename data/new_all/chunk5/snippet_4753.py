# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49332694/attributeerror-grammatrix-object-has-no-attribute-gradinput
# Define an nn Module to compute content loss in-place
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ContentLoss(_n_(695809, "object", lambda: object)):
    _l_(695893)


    def __init__(self, strength):
        _l_(695825)

        _c_(695814, _a_(695813, _n_(695810, "super", lambda: super)(_n_(695811, "ContentLoss", lambda: ContentLoss), _n_(695812, "self", lambda: self)), "__init__"))
        _l_(695815)
        _n_(695816, "self", lambda: self).strength = _n_(695817, "strength", lambda: strength)
        _l_(695818)
        _n_(695819, "self", lambda: self).target = 0
        _l_(695820)
        _n_(695821, "self", lambda: self).loss = 0
        _l_(695822)
        _n_(695823, "self", lambda: self).mode = None
        _l_(695824)

    def forward(self, input):
        _l_(695857)

        _c_(695827, _n_(695826, "print", lambda: print), "ContentLoss - Forward")
        _l_(695828)
        if _a_(695830, _n_(695829, "self", lambda: self), "mode") == 'loss':
            _l_(695850)

            _c_(695832, _n_(695831, "print", lambda: print), "ContentLoss - Forward - Loss")
            _l_(695833)
            _n_(695834, "self", lambda: self).loss = (_n_(695835, "input", lambda: input) * _a_(695837, _n_(695836, "self", lambda: self), "target")) * _a_(695839, _n_(695838, "self", lambda: self), "strength") #Forward
            _l_(695840) #Forward
        elif _a_(695842, _n_(695841, "self", lambda: self), "mode") == 'capture':
            _l_(695849)

            _c_(695844, _n_(695843, "print", lambda: print), "ContentLoss - Forward - Capture")
            _l_(695845)
            _n_(695846, "self", lambda: self).target = _n_(695847, "input", lambda: input)
            _l_(695848)
        _n_(695851, "self", lambda: self).output = _n_(695852, "input", lambda: input) 
        _l_(695853) 
        aux = _a_(695855, _n_(695854, "self", lambda: self), "output")
        _l_(695856)
        return aux

    def backward(self, input, gradOutput):
        _l_(695892)

        _c_(695859, _n_(695858, "print", lambda: print), "ContentLoss - Backward") 
        _l_(695860) 
        if _a_(695862, _n_(695861, "self", lambda: self), "mode") == 'loss':
            _l_(695888)

            _c_(695864, _n_(695863, "print", lambda: print), "ContentLoss - Backward - Loss")
            _l_(695865)
            _n_(695866, "self", lambda: self).gradInput = _n_(695867, "input", lambda: input) * _a_(695869, _n_(695868, "self", lambda: self), "target") # Backward
            _l_(695870) # Backward
            _n_(695871, "self", lambda: self).gradInput = _a_(695873, _n_(695872, "self", lambda: self), "gradInput") * _a_(695875, _n_(695874, "self", lambda: self), "strength")
            _l_(695876)
            _n_(695877, "self", lambda: self).gradInput = _a_(695879, _n_(695878, "self", lambda: self), "gradInput") + _n_(695880, "gradOutput", lambda: gradOutput)
            _l_(695881)
        else:
          _c_(695883, _n_(695882, "print", lambda: print), "ContentLoss - Backward - Capture")
          _l_(695884)
          _n_(695885, "self", lambda: self).target = _n_(695886, "gradOutput", lambda: gradOutput)
          _l_(695887)
        aux = _a_(695890, _n_(695889, "self", lambda: self), "gradInput")
        _l_(695891)
        return aux


class GramMatrix(_n_(695894, "object", lambda: object)):
    _l_(695919)

    def __init__(self):
        _l_(695901)

        _c_(695899, _a_(695898, _n_(695895, "super", lambda: super)(_n_(695896, "GramMatrix", lambda: GramMatrix), _n_(695897, "self", lambda: self)), "__init__"))
        _l_(695900)

    def forward(self, input):
        _l_(695908)

        _n_(695902, "self", lambda: self).output = _n_(695903, "input", lambda: input)
        _l_(695904)
        aux = _a_(695906, _n_(695905, "self", lambda: self), "output")
        _l_(695907)
        return aux

    def backward(self, input, gradOutput):
        _l_(695918)

        _n_(695909, "self", lambda: self).gradInput = _a_(695911, _n_(695910, "self", lambda: self), "gradInput") + _n_(695912, "gradOutput", lambda: gradOutput) + _n_(695913, "input", lambda: input)
        _l_(695914)
        aux = _a_(695916, _n_(695915, "self", lambda: self), "gradInput")
        _l_(695917)
        return aux

class StyleLoss(_n_(695920, "object", lambda: object)):
    _l_(696036)


    def __init__(self, strength):
        _l_(695944)

        _c_(695925, _a_(695924, _n_(695921, "super", lambda: super)(_n_(695922, "StyleLoss", lambda: StyleLoss), _n_(695923, "self", lambda: self)), "__init__"))
        _l_(695926)
        _n_(695927, "self", lambda: self).strength = _n_(695928, "strength", lambda: strength)
        _l_(695929)
        _n_(695930, "self", lambda: self).target = 0
        _l_(695931)
        _n_(695932, "self", lambda: self).mode = None
        _l_(695933)
        _n_(695934, "self", lambda: self).loss = 0
        _l_(695935)
        _n_(695936, "self", lambda: self).gram = _c_(695938, _n_(695937, "GramMatrix", lambda: GramMatrix))
        _l_(695939)
        _n_(695940, "self", lambda: self).blend_weight = None
        _l_(695941)
        _n_(695942, "self", lambda: self).G = None
        _l_(695943)

    def forward(self, input):
        _l_(695996)

        _c_(695946, _n_(695945, "print", lambda: print), "StyleLoss - Forward")
        _l_(695947)
        _n_(695948, "self", lambda: self).G = _c_(695953, _a_(695951, _a_(695950, _n_(695949, "self", lambda: self), "gram"), "forward"), _n_(695952, "input", lambda: input))
        _l_(695954)
        if _a_(695956, _n_(695955, "self", lambda: self), "mode") == 'capture':
            _l_(695989)

            _c_(695958, _n_(695957, "print", lambda: print), "StyleLoss - Forward - Capture")
            _l_(695959)
            if _a_(695961, _n_(695960, "self", lambda: self), "blend_weight") == None:
                _l_(695974)

                _n_(695962, "self", lambda: self).target = _a_(695964, _n_(695963, "self", lambda: self), "G")
                _l_(695965)
            else:
              _n_(695966, "self", lambda: self).target = _a_(695968, _n_(695967, "self", lambda: self), "target") + (_a_(695970, _n_(695969, "self", lambda: self), "blend_weight") * _a_(695972, _n_(695971, "self", lambda: self), "G"))
              _l_(695973)
        elif _a_(695976, _n_(695975, "self", lambda: self), "mode") == 'loss':
            _l_(695988)

            _c_(695978, _n_(695977, "print", lambda: print), "StyleLoss - Forward - Loss")
            _l_(695979)
            _n_(695980, "self", lambda: self).loss = _a_(695982, _n_(695981, "self", lambda: self), "strength") * (_a_(695984, _n_(695983, "self", lambda: self), "G") * _a_(695986, _n_(695985, "self", lambda: self), "target")) #Forward
            _l_(695987) #Forward
        _n_(695990, "self", lambda: self).output = _n_(695991, "input", lambda: input)
        _l_(695992)
        aux = _a_(695994, _n_(695993, "self", lambda: self), "output")
        _l_(695995)
        return aux

    def backward(self, input, gradOutput):
        _l_(696035)

        _c_(695998, _n_(695997, "print", lambda: print), "StyleLoss - Backward")
        _l_(695999)
        if _a_(696001, _n_(696000, "self", lambda: self), "mode") == 'loss':
            _l_(696031)

            dG = _c_(696009, _a_(696004, _a_(696003, _n_(696002, "self", lambda: self), "gram"), "backward"), _a_(696006, _n_(696005, "self", lambda: self), "G"), _a_(696008, _n_(696007, "self", lambda: self), "target"))
            _l_(696010)
            _n_(696011, "self", lambda: self).gradInput = _n_(696012, "input", lambda: input) * _n_(696013, "dG", lambda: dG)
            _l_(696014)
            _n_(696015, "self", lambda: self).gradInput = _a_(696017, _n_(696016, "self", lambda: self), "gradInput") * _a_(696019, _n_(696018, "self", lambda: self), "strength")
            _l_(696020)
            _n_(696021, "self", lambda: self).gradInput = _a_(696023, _n_(696022, "self", lambda: self), "gradOutput")
            _l_(696024)
        else: 
          _c_(696026, _n_(696025, "print", lambda: print), "StyleLoss - Backward - Capture")
          _l_(696027)
          _n_(696028, "self", lambda: self).gradInput = _n_(696029, "gradOutput", lambda: gradOutput)
          _l_(696030)
        aux = _a_(696033, _n_(696032, "self", lambda: self), "gradInput")
        _l_(696034)
        return aux



input_value = 1
_l_(696037)
gradOut_value = 0
_l_(696038)
weight = 5
_l_(696039)
CL = _c_(696042, _n_(696040, "ContentLoss", lambda: ContentLoss), _n_(696041, "weight", lambda: weight))
_l_(696043)
SL = _c_(696046, _n_(696044, "StyleLoss", lambda: StyleLoss), _n_(696045, "weight", lambda: weight))
_l_(696047)

_n_(696048, "CL", lambda: CL).mode = 'capture'
_l_(696049)
_c_(696053, _a_(696051, _n_(696050, "CL", lambda: CL), "forward"), _n_(696052, "input_value", lambda: input_value))
_l_(696054)

_n_(696055, "CL", lambda: CL).mode = None
_l_(696056)
_n_(696057, "SL", lambda: SL).mode = 'capture'
_l_(696058)
_c_(696062, _a_(696060, _n_(696059, "SL", lambda: SL), "forward"), _n_(696061, "input_value", lambda: input_value))
_l_(696063)

_n_(696064, "CL", lambda: CL).mode = 'loss'
_l_(696065)
_n_(696066, "SL", lambda: SL).mode = 'loss'
_l_(696067)

_c_(696071, _a_(696069, _n_(696068, "CL", lambda: CL), "forward"), _n_(696070, "input_value", lambda: input_value))
_l_(696072)
_c_(696076, _a_(696074, _n_(696073, "SL", lambda: SL), "forward"), _n_(696075, "input_value", lambda: input_value))
_l_(696077)

_c_(696082, _a_(696079, _n_(696078, "CL", lambda: CL), "backward"), _n_(696080, "input_value", lambda: input_value), _n_(696081, "gradOut_value", lambda: gradOut_value))
_l_(696083)
_c_(696088, _a_(696085, _n_(696084, "SL", lambda: SL), "backward"), _n_(696086, "input_value", lambda: input_value), _n_(696087, "gradOut_value", lambda: gradOut_value))
_l_(696089)