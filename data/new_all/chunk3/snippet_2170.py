# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59990889/i-keep-getting-typeerror-template-takes-no-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
selectedVersion = _c_(533556, _a_(533555, _n_(533554, "tk", lambda: tk), "StringVar"))
_l_(533557)
_c_(533561, _a_(533559, _n_(533558, "selectedVersion", lambda: selectedVersion), "set"), _n_(533560, "templateVersion", lambda: templateVersion)[0])
_l_(533562)
#Template Menu
templateMenu = _c_(533567, _n_(533563, "OptionMenu", lambda: OptionMenu), _n_(533564, "frameTemp", lambda: frameTemp), _n_(533565, "selectedVersion", lambda: selectedVersion), *_n_(533566, "templateVersion", lambda: templateVersion))
_l_(533568)
_c_(533571, _a_(533570, _n_(533569, "templateMenu", lambda: templateMenu), "pack"))
_l_(533572)

selectBtn = _c_(533577, _a_(533574, _n_(533573, "tk", lambda: tk), "Button"), _n_(533575, "frameTemp", lambda: frameTemp), text = "Select", command = _n_(533576, "selectVersion", lambda: selectVersion))
_l_(533578)
_c_(533581, _a_(533580, _n_(533579, "selectBtn", lambda: selectBtn), "pack"))
_l_(533582)

version = _c_(533585, _a_(533584, _n_(533583, "tk", lambda: tk), "StringVar"))
_l_(533586)

#label

tempLbl = _c_(533590, _n_(533587, "Label", lambda: Label), _n_(533588, "frameTemp", lambda: frameTemp), textvariable = _n_(533589, "version", lambda: version))
_l_(533591)
_c_(533594, _a_(533593, _n_(533592, "tempLbl", lambda: tempLbl), "pack"))
_l_(533595)

_c_(533598, _a_(533597, _n_(533596, "win", lambda: win), "mainloop"))
_l_(533599)