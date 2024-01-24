# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49332694/attributeerror-grammatrix-object-has-no-attribute-gradinput
# Define an nn Module to compute content loss in-place
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ContentLoss(_n_(660321, "object", lambda: object)):
    _l_(660405)


    def __init__(self, strength):
        _l_(660337)

        _c_(660326, _a_(660325, _n_(660322, "super", lambda: super)(_n_(660323, "ContentLoss", lambda: ContentLoss), _n_(660324, "self", lambda: self)), "__init__"))
        _l_(660327)
        _n_(660328, "self", lambda: self).strength = _n_(660329, "strength", lambda: strength)
        _l_(660330)
        _n_(660331, "self", lambda: self).target = 0
        _l_(660332)
        _n_(660333, "self", lambda: self).loss = 0
        _l_(660334)
        _n_(660335, "self", lambda: self).mode = None
        _l_(660336)

    def forward(self, input):
        _l_(660369)

        _c_(660339, _n_(660338, "print", lambda: print), "ContentLoss - Forward")
        _l_(660340)
        if _a_(660342, _n_(660341, "self", lambda: self), "mode") == 'loss':
            _l_(660362)

            _c_(660344, _n_(660343, "print", lambda: print), "ContentLoss - Forward - Loss")
            _l_(660345)
            _n_(660346, "self", lambda: self).loss = (_n_(660347, "input", lambda: input) * _a_(660349, _n_(660348, "self", lambda: self), "target")) * _a_(660351, _n_(660350, "self", lambda: self), "strength") #Forward
            _l_(660352) #Forward
        elif _a_(660354, _n_(660353, "self", lambda: self), "mode") == 'capture':
            _l_(660361)

            _c_(660356, _n_(660355, "print", lambda: print), "ContentLoss - Forward - Capture")
            _l_(660357)
            _n_(660358, "self", lambda: self).target = _n_(660359, "input", lambda: input)
            _l_(660360)
        _n_(660363, "self", lambda: self).output = _n_(660364, "input", lambda: input) 
        _l_(660365) 
        aux = _a_(660367, _n_(660366, "self", lambda: self), "output")
        _l_(660368)
        return aux

    def backward(self, input, gradOutput):
        _l_(660404)

        _c_(660371, _n_(660370, "print", lambda: print), "ContentLoss - Backward") 
        _l_(660372) 
        if _a_(660374, _n_(660373, "self", lambda: self), "mode") == 'loss':
            _l_(660400)

            _c_(660376, _n_(660375, "print", lambda: print), "ContentLoss - Backward - Loss")
            _l_(660377)
            _n_(660378, "self", lambda: self).gradInput = _n_(660379, "input", lambda: input) * _a_(660381, _n_(660380, "self", lambda: self), "target") # Backward
            _l_(660382) # Backward
            _n_(660383, "self", lambda: self).gradInput = _a_(660385, _n_(660384, "self", lambda: self), "gradInput") * _a_(660387, _n_(660386, "self", lambda: self), "strength")
            _l_(660388)
            _n_(660389, "self", lambda: self).gradInput = _a_(660391, _n_(660390, "self", lambda: self), "gradInput") + _n_(660392, "gradOutput", lambda: gradOutput)
            _l_(660393)
        else:
          _c_(660395, _n_(660394, "print", lambda: print), "ContentLoss - Backward - Capture")
          _l_(660396)
          _n_(660397, "self", lambda: self).target = _n_(660398, "gradOutput", lambda: gradOutput)
          _l_(660399)
        aux = _a_(660402, _n_(660401, "self", lambda: self), "gradInput")
        _l_(660403)
        return aux


class GramMatrix(_n_(660406, "object", lambda: object)):
    _l_(660431)

    def __init__(self):
        _l_(660413)

        _c_(660411, _a_(660410, _n_(660407, "super", lambda: super)(_n_(660408, "GramMatrix", lambda: GramMatrix), _n_(660409, "self", lambda: self)), "__init__"))
        _l_(660412)

    def forward(self, input):
        _l_(660420)

        _n_(660414, "self", lambda: self).output = _n_(660415, "input", lambda: input)
        _l_(660416)
        aux = _a_(660418, _n_(660417, "self", lambda: self), "output")
        _l_(660419)
        return aux

    def backward(self, input, gradOutput):
        _l_(660430)

        _n_(660421, "self", lambda: self).gradInput = _a_(660423, _n_(660422, "self", lambda: self), "gradInput") + _n_(660424, "gradOutput", lambda: gradOutput) + _n_(660425, "input", lambda: input)
        _l_(660426)
        aux = _a_(660428, _n_(660427, "self", lambda: self), "gradInput")
        _l_(660429)
        return aux

class StyleLoss(_n_(660432, "object", lambda: object)):
    _l_(660548)


    def __init__(self, strength):
        _l_(660456)

        _c_(660437, _a_(660436, _n_(660433, "super", lambda: super)(_n_(660434, "StyleLoss", lambda: StyleLoss), _n_(660435, "self", lambda: self)), "__init__"))
        _l_(660438)
        _n_(660439, "self", lambda: self).strength = _n_(660440, "strength", lambda: strength)
        _l_(660441)
        _n_(660442, "self", lambda: self).target = 0
        _l_(660443)
        _n_(660444, "self", lambda: self).mode = None
        _l_(660445)
        _n_(660446, "self", lambda: self).loss = 0
        _l_(660447)
        _n_(660448, "self", lambda: self).gram = _c_(660450, _n_(660449, "GramMatrix", lambda: GramMatrix))
        _l_(660451)
        _n_(660452, "self", lambda: self).blend_weight = None
        _l_(660453)
        _n_(660454, "self", lambda: self).G = None
        _l_(660455)

    def forward(self, input):
        _l_(660508)

        _c_(660458, _n_(660457, "print", lambda: print), "StyleLoss - Forward")
        _l_(660459)
        _n_(660460, "self", lambda: self).G = _c_(660465, _a_(660463, _a_(660462, _n_(660461, "self", lambda: self), "gram"), "forward"), _n_(660464, "input", lambda: input))
        _l_(660466)
        if _a_(660468, _n_(660467, "self", lambda: self), "mode") == 'capture':
            _l_(660501)

            _c_(660470, _n_(660469, "print", lambda: print), "StyleLoss - Forward - Capture")
            _l_(660471)
            if _a_(660473, _n_(660472, "self", lambda: self), "blend_weight") == None:
                _l_(660486)

                _n_(660474, "self", lambda: self).target = _a_(660476, _n_(660475, "self", lambda: self), "G")
                _l_(660477)
            else:
              _n_(660478, "self", lambda: self).target = _a_(660480, _n_(660479, "self", lambda: self), "target") + (_a_(660482, _n_(660481, "self", lambda: self), "blend_weight") * _a_(660484, _n_(660483, "self", lambda: self), "G"))
              _l_(660485)
        elif _a_(660488, _n_(660487, "self", lambda: self), "mode") == 'loss':
            _l_(660500)

            _c_(660490, _n_(660489, "print", lambda: print), "StyleLoss - Forward - Loss")
            _l_(660491)
            _n_(660492, "self", lambda: self).loss = _a_(660494, _n_(660493, "self", lambda: self), "strength") * (_a_(660496, _n_(660495, "self", lambda: self), "G") * _a_(660498, _n_(660497, "self", lambda: self), "target")) #Forward
            _l_(660499) #Forward
        _n_(660502, "self", lambda: self).output = _n_(660503, "input", lambda: input)
        _l_(660504)
        aux = _a_(660506, _n_(660505, "self", lambda: self), "output")
        _l_(660507)
        return aux

    def backward(self, input, gradOutput):
        _l_(660547)

        _c_(660510, _n_(660509, "print", lambda: print), "StyleLoss - Backward")
        _l_(660511)
        if _a_(660513, _n_(660512, "self", lambda: self), "mode") == 'loss':
            _l_(660543)

            dG = _c_(660521, _a_(660516, _a_(660515, _n_(660514, "self", lambda: self), "gram"), "backward"), _a_(660518, _n_(660517, "self", lambda: self), "G"), _a_(660520, _n_(660519, "self", lambda: self), "target"))
            _l_(660522)
            _n_(660523, "self", lambda: self).gradInput = _n_(660524, "input", lambda: input) * _n_(660525, "dG", lambda: dG)
            _l_(660526)
            _n_(660527, "self", lambda: self).gradInput = _a_(660529, _n_(660528, "self", lambda: self), "gradInput") * _a_(660531, _n_(660530, "self", lambda: self), "strength")
            _l_(660532)
            _n_(660533, "self", lambda: self).gradInput = _a_(660535, _n_(660534, "self", lambda: self), "gradOutput")
            _l_(660536)
        else: 
          _c_(660538, _n_(660537, "print", lambda: print), "StyleLoss - Backward - Capture")
          _l_(660539)
          _n_(660540, "self", lambda: self).gradInput = _n_(660541, "gradOutput", lambda: gradOutput)
          _l_(660542)
        aux = _a_(660545, _n_(660544, "self", lambda: self), "gradInput")
        _l_(660546)
        return aux



input_value = 1
_l_(660549)
gradOut_value = 0
_l_(660550)
weight = 5
_l_(660551)
CL = _c_(660554, _n_(660552, "ContentLoss", lambda: ContentLoss), _n_(660553, "weight", lambda: weight))
_l_(660555)
SL = _c_(660558, _n_(660556, "StyleLoss", lambda: StyleLoss), _n_(660557, "weight", lambda: weight))
_l_(660559)

_n_(660560, "CL", lambda: CL).mode = 'capture'
_l_(660561)
_c_(660565, _a_(660563, _n_(660562, "CL", lambda: CL), "forward"), _n_(660564, "input_value", lambda: input_value))
_l_(660566)

_n_(660567, "CL", lambda: CL).mode = None
_l_(660568)
_n_(660569, "SL", lambda: SL).mode = 'capture'
_l_(660570)
_c_(660574, _a_(660572, _n_(660571, "SL", lambda: SL), "forward"), _n_(660573, "input_value", lambda: input_value))
_l_(660575)

_n_(660576, "CL", lambda: CL).mode = 'loss'
_l_(660577)
_n_(660578, "SL", lambda: SL).mode = 'loss'
_l_(660579)

_c_(660583, _a_(660581, _n_(660580, "CL", lambda: CL), "forward"), _n_(660582, "input_value", lambda: input_value))
_l_(660584)
_c_(660588, _a_(660586, _n_(660585, "SL", lambda: SL), "forward"), _n_(660587, "input_value", lambda: input_value))
_l_(660589)

_c_(660594, _a_(660591, _n_(660590, "CL", lambda: CL), "backward"), _n_(660592, "input_value", lambda: input_value), _n_(660593, "gradOut_value", lambda: gradOut_value))
_l_(660595)
_c_(660600, _a_(660597, _n_(660596, "SL", lambda: SL), "backward"), _n_(660598, "input_value", lambda: input_value), _n_(660599, "gradOut_value", lambda: gradOut_value))
_l_(660601)