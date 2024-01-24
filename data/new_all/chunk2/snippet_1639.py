# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67712782/using-pypubsub-wxpython-to-transfer-data-between-windows-getting-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pubsub import pub
    _l_(450318)

except ImportError:
    pass
try:
    import wx
    _l_(450320)

except ImportError:
    pass

class MainFrame (_a_(450322, _n_(450321, "wx", lambda: wx), "Frame")):
    _l_(450337)

    def __init__(self, parent, title):
        _l_(450336)

        _c_(450329, _a_(450326, _n_(450323, "super", lambda: super)(_n_(450324, "MainFrame", lambda: MainFrame), _n_(450325, "self", lambda: self)), "__init__"), _n_(450327, "parent", lambda: parent), title = _n_(450328, "title", lambda: title), size = (200,200))
        _l_(450330)
        _n_(450331, "self", lambda: self).panel = _c_(450334, _n_(450332, "MainPanel", lambda: MainPanel), _n_(450333, "self", lambda: self))
        _l_(450335)

class CoordFrame (_a_(450339, _n_(450338, "wx", lambda: wx), "Frame")):
    _l_(450354)

    def __init__(self, parent, title):
        _l_(450353)

        _c_(450346, _a_(450343, _n_(450340, "super", lambda: super)(_n_(450341, "CoordFrame", lambda: CoordFrame), _n_(450342, "self", lambda: self)), "__init__"), _n_(450344, "parent", lambda: parent), title = _n_(450345, "title", lambda: title), size = (200,200))
        _l_(450347)
        _n_(450348, "self", lambda: self).panel = _c_(450351, _n_(450349, "CoordPanel", lambda: CoordPanel), _n_(450350, "self", lambda: self))
        _l_(450352)


class MainPanel(_a_(450356, _n_(450355, "wx", lambda: wx), "Panel")):
    _l_(450429)

    def __init__(self, parent):
        _l_(450410)

        _c_(450362, _a_(450360, _n_(450357, "super", lambda: super)(_n_(450358, "MainPanel", lambda: MainPanel), _n_(450359, "self", lambda: self)), "__init__"), _n_(450361, "parent", lambda: parent))
        _l_(450363)
        vsizer = _c_(450368, _a_(450365, _n_(450364, "wx", lambda: wx), "BoxSizer"), _a_(450367, _n_(450366, "wx", lambda: wx), "VERTICAL"))
        _l_(450369)
    
        _n_(450370, "self", lambda: self).tbxNewMap = _c_(450380, _a_(450372, _n_(450371, "wx", lambda: wx), "TextCtrl"), _n_(450373, "self", lambda: self), id=1001, pos=(20,20), size = (50,20) ,style = _a_(450375, _n_(450374, "wx", lambda: wx), "TE_CENTER")|_a_(450377, _n_(450376, "wx", lambda: wx), "TE_NOHIDESEL")|_a_(450379, _n_(450378, "wx", lambda: wx), "TE_PROCESS_ENTER"))
        _l_(450381)
        _c_(450386, _a_(450383, _n_(450382, "vsizer", lambda: vsizer), "Add"), _a_(450385, _n_(450384, "self", lambda: self), "tbxNewMap"))
        _l_(450387)

        _n_(450388, "self", lambda: self).btnEnterNewMap = _c_(450392, _a_(450390, _n_(450389, "wx", lambda: wx), "Button"), _n_(450391, "self", lambda: self), id=1002, label = "New Data", pos = (20,80), size = (80,40))
        _l_(450393)
        _c_(450400, _a_(450395, _n_(450394, "vsizer", lambda: vsizer), "Add"), _a_(450397, _n_(450396, "self", lambda: self), "btnEnterNewMap"),0,_a_(450399, _n_(450398, "wx", lambda: wx), "EXPAND"))
        _l_(450401)
        _c_(450408, _a_(450403, _n_(450402, "self", lambda: self), "Bind"), _a_(450405, _n_(450404, "wx", lambda: wx), "EVT_BUTTON"), _a_(450407, _n_(450406, "self", lambda: self), "onButtonNewMap"), id=1002)
        _l_(450409)

    def onButtonNewMap(self,event):
        _l_(450428)

        temp = _c_(450414, _a_(450413, _a_(450412, _n_(450411, "self", lambda: self), "tbxNewMap"), "GetValue"))
        _l_(450415)
        _c_(450419, _a_(450417, _n_(450416, "pub", lambda: pub), "sendMessage"), "coord_listener", _n_(450418, "temp", lambda: temp))
        _l_(450420)
        coordframe = _c_(450422, _n_(450421, "CoordFrame", lambda: CoordFrame), None,"Entry")
        _l_(450423)
        _c_(450426, _a_(450425, _n_(450424, "coordframe", lambda: coordframe), "Show"))
        _l_(450427)

class CoordPanel(_a_(450431, _n_(450430, "wx", lambda: wx), "Panel")):
    _l_(450484)

    def __init__(self, parent):
        _l_(450469)

        _c_(450437, _a_(450435, _n_(450432, "super", lambda: super)(_n_(450433, "CoordPanel", lambda: CoordPanel), _n_(450434, "self", lambda: self)), "__init__"), _n_(450436, "parent", lambda: parent))
        _l_(450438)
        vsizer = _c_(450443, _a_(450440, _n_(450439, "wx", lambda: wx), "BoxSizer"), _a_(450442, _n_(450441, "wx", lambda: wx), "VERTICAL"))
        _l_(450444)
        _c_(450449, _a_(450446, _n_(450445, "pub", lambda: pub), "subscribe"), _a_(450448, _n_(450447, "self", lambda: self), "coord_listener"), "coord_listener")
        _l_(450450)

        _n_(450451, "self", lambda: self).tbxNewMapNumber = _c_(450461, _a_(450453, _n_(450452, "wx", lambda: wx), "TextCtrl"), _n_(450454, "self", lambda: self), id=1000, pos=(20,20), size = (50,20), style = _a_(450456, _n_(450455, "wx", lambda: wx), "TE_CENTER")|_a_(450458, _n_(450457, "wx", lambda: wx), "TE_NOHIDESEL")|_a_(450460, _n_(450459, "wx", lambda: wx), "TE_PROCESS_ENTER"))
        _l_(450462)
        _c_(450467, _a_(450464, _n_(450463, "vsizer", lambda: vsizer), "Add"), _a_(450466, _n_(450465, "self", lambda: self), "tbxNewMapNumber"))
        _l_(450468)
    def coord_listener(self, message):
        _l_(450483)

        newmapnum = _n_(450470, "message", lambda: message)
        _l_(450471)
        _c_(450476, _a_(450474, _a_(450473, _n_(450472, "self", lambda: self), "tbxNewMapNumber"), "SetValue"), _n_(450475, "newmapnum", lambda: newmapnum))
        _l_(450477)
        _c_(450481, _a_(450480, _a_(450479, _n_(450478, "self", lambda: self), "tbxNewMapNumber"), "Refresh"))
        _l_(450482)


class GMDash(_a_(450486, _n_(450485, "wx", lambda: wx), "App")):
    _l_(450498)

    def OnInit(self):
        _l_(450497)

        _n_(450487, "self", lambda: self).mainframe = _c_(450489, _n_(450488, "MainFrame", lambda: MainFrame), parent = None, title = "Dashboard")
        _l_(450490)
        _c_(450494, _a_(450493, _a_(450492, _n_(450491, "self", lambda: self), "mainframe"), "Show"))
        _l_(450495)
        aux = True
        _l_(450496)
        return aux

app = _c_(450500, _n_(450499, "GMDash", lambda: GMDash))
_l_(450501)
_c_(450504, _a_(450503, _n_(450502, "app", lambda: app), "MainLoop"))
_l_(450505)