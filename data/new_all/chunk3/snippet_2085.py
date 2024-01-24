# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65145362/python-typeerror-item-1-in-argtypes-passes-a-union-by-value-which-is-unsupp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import wx.lib.activex
    _l_(570346)

except ImportError:
    pass
try:
    import csv
    _l_(570348)

except ImportError:
    pass
try:
    import comtypes.client
    _l_(570350)

except ImportError:
    pass

class EventSink(_n_(570351, "object", lambda: object)):
    _l_(570368)


    def __init__(self, frame):
        _l_(570357)

        _n_(570352, "self", lambda: self).counter = 0
        _l_(570353)
        _n_(570354, "self", lambda: self).frame = _n_(570355, "frame", lambda: frame)
        _l_(570356)

    def DataReady(self):
        _l_(570367)

        _n_(570358, "self", lambda: self).counter +=1
        _l_(570359)
        _a_(570361, _n_(570360, "self", lambda: self), "frame").Title= _c_(570365, _a_(570362, "DataReady fired {0} times", "format"), _a_(570364, _n_(570363, "self", lambda: self), "counter"))
        _l_(570366)


class MyApp( _a_(570370, _n_(570369, "wx", lambda: wx), "App") ):
    _l_(570721)


    def OnClick(self,e):
        _l_(570452)

        rb_selection = _c_(570374, _a_(570373, _a_(570372, _n_(570371, "self", lambda: self), "rb"), "GetStringSelection"))
        _l_(570375)
        if _n_(570376, "rb_selection", lambda: rb_selection) == "WinCam":
            _l_(570433)

            data = _c_(570381, _a_(570380, _a_(570379, _a_(570378, _n_(570377, "self", lambda: self), "gd"), "ctrl"), "GetWinCamDataAsVariant"))
            _l_(570382)
            data = [[_n_(570383, "x", lambda: x)] for x in _n_(570384, "data", lambda: data)]
            _l_(570385)
        else:
            p_selection = _c_(570389, _a_(570388, _a_(570387, _n_(570386, "self", lambda: self), "cb"), "GetStringSelection"))
            _l_(570390)
            if _n_(570391, "p_selection", lambda: p_selection) == "Profile_X":
                _l_(570432)

                data = _c_(570396, _a_(570395, _a_(570394, _a_(570393, _n_(570392, "self", lambda: self), "px"), "ctrl"), "GetProfileDataAsVariant"))
                _l_(570397)
                data = [[_n_(570398, "x", lambda: x)] for x in _n_(570399, "data", lambda: data)]#csv.writerows accepts a list of rows where each row is a list, a list of lists
                _l_(570400)#csv.writerows accepts a list of rows where each row is a list, a list of lists
            elif _n_(570401, "p_selection", lambda: p_selection) == "Profile_Y":
                _l_(570431)

                data = _c_(570406, _a_(570405, _a_(570404, _a_(570403, _n_(570402, "self", lambda: self), "py"), "ctrl"), "GetProfileDataAsVariant"))
                _l_(570407)
                data = [[_n_(570408, "x", lambda: x)] for x in _n_(570409, "data", lambda: data)]
                _l_(570410)
            else:
                datax = _c_(570415, _a_(570414, _a_(570413, _a_(570412, _n_(570411, "self", lambda: self), "px"), "ctrl"), "GetProfileDataAsVariant"))
                _l_(570416)
                datay = _c_(570421, _a_(570420, _a_(570419, _a_(570418, _n_(570417, "self", lambda: self), "py"), "ctrl"), "GetProfileDataAsVariant"))
                _l_(570422)
                data = [_c_(570425, _n_(570423, "list", lambda: list), _n_(570424, "row", lambda: row)) for row in _c_(570429, _n_(570426, "zip", lambda: zip), _n_(570427, "datax", lambda: datax),_n_(570428, "datay", lambda: datay))]#Makes a list of lists; X1 with Y1 in a list, X2 with Y2 in a list etc...
                _l_(570430)#Makes a list of lists; X1 with Y1 in a list, X2 with Y2 in a list etc...
        filename = _a_(570436, _a_(570435, _n_(570434, "self", lambda: self), "ti"), "Value")
        _l_(570437)
        with _c_(570440, _n_(570438, "open", lambda: open), _n_(570439, "filename", lambda: filename), 'wb') as fp:
            _l_(570451)

            w = _c_(570444, _a_(570442, _n_(570441, "csv", lambda: csv), "writer"), _n_(570443, "fp", lambda: fp), delimiter=',')
            _l_(570445)
            _c_(570449, _a_(570447, _n_(570446, "w", lambda: w), "writerows"), _n_(570448, "data", lambda: data))
            _l_(570450)

    def __init__( self, redirect=False, filename=None ):
        _l_(570720)

        _c_(570459, _a_(570455, _a_(570454, _n_(570453, "wx", lambda: wx), "App"), "__init__"), _n_(570456, "self", lambda: self), _n_(570457, "redirect", lambda: redirect), _n_(570458, "filename", lambda: filename) )
        _l_(570460)
        _n_(570461, "self", lambda: self).frame = _c_(570466, _a_(570463, _n_(570462, "wx", lambda: wx), "Frame"), parent=None, id=_a_(570465, _n_(570464, "wx", lambda: wx), "ID_ANY"),size=(1000,760), title='Python Interface to DataRay')
        _l_(570467)
        #Panel
        p = _c_(570474, _a_(570469, _n_(570468, "wx", lambda: wx), "Panel"), _a_(570471, _n_(570470, "self", lambda: self), "frame"), _a_(570473, _n_(570472, "wx", lambda: wx), "ID_ANY"))
        _l_(570475)
        #Get Data
        _n_(570476, "self", lambda: self).gd = _c_(570481, _a_(570479, _a_(570478, _a_(570477, wx, "lib"), "activex"), "ActiveXCtrl"), _n_(570480, "p", lambda: p), 'DATARAYOCX.GetDataCtrl.1')
        _l_(570482)
        #The methods of the object are available through the ctrl property of the item
        _c_(570487, _a_(570486, _a_(570485, _a_(570484, _n_(570483, "self", lambda: self), "gd"), "ctrl"), "StartDriver"))
        _l_(570488)
        _n_(570489, "self", lambda: self).counter = 0
        _l_(570490)
        sink = _c_(570494, _n_(570491, "EventSink", lambda: EventSink), _a_(570493, _n_(570492, "self", lambda: self), "frame"))
        _l_(570495)
        _n_(570496, "self", lambda: self).sink = _c_(570503, _a_(570498, _a_(570497, comtypes, "client"), "GetEvents"), _a_(570501, _a_(570500, _n_(570499, "self", lambda: self), "gd"), "ctrl"), _n_(570502, "sink", lambda: sink))
        _l_(570504)
        #Button Panel
        bp = _c_(570511, _a_(570506, _n_(570505, "wx", lambda: wx), "Panel"), parent=_a_(570508, _n_(570507, "self", lambda: self), "frame"), id=_a_(570510, _n_(570509, "wx", lambda: wx), "ID_ANY"), size=(215, 250))
        _l_(570512)
        b1 = _c_(570517, _a_(570515, _a_(570514, _a_(570513, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(570516, "bp", lambda: bp),size=(200,50), pos=(1, 0),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(570518)
        _a_(570520, _n_(570519, "b1", lambda: b1), "ctrl").ButtonID =297 #Id's for some ActiveX controls must be set
        _l_(570521) #Id's for some ActiveX controls must be set
        b2 = _c_(570526, _a_(570524, _a_(570523, _a_(570522, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(570525, "bp", lambda: bp),size=(100,25), pos=(5, 55),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(570527)
        _a_(570529, _n_(570528, "b2", lambda: b2), "ctrl").ButtonID =171
        _l_(570530)
        b3 = _c_(570535, _a_(570533, _a_(570532, _a_(570531, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(570534, "bp", lambda: bp),size=(100,25), pos=(110,55),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(570536)
        _a_(570538, _n_(570537, "b3", lambda: b3), "ctrl").ButtonID =172
        _l_(570539)
        b4 = _c_(570544, _a_(570542, _a_(570541, _a_(570540, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(570543, "bp", lambda: bp),size=(100,25), pos=(5, 85),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(570545)
        _a_(570547, _n_(570546, "b4", lambda: b4), "ctrl").ButtonID =177
        _l_(570548)
        b4 = _c_(570553, _a_(570551, _a_(570550, _a_(570549, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(570552, "bp", lambda: bp),size=(100,25), pos=(110, 85),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(570554)
        _a_(570556, _n_(570555, "b4", lambda: b4), "ctrl").ButtonID =179
        _l_(570557)
        #Custom controls
        t = _c_(570561, _a_(570559, _n_(570558, "wx", lambda: wx), "StaticText"), _n_(570560, "bp", lambda: bp), label="File:", pos=(5, 115))
        _l_(570562)
        _n_(570563, "self", lambda: self).ti = _c_(570567, _a_(570565, _n_(570564, "wx", lambda: wx), "TextCtrl"), _n_(570566, "bp", lambda: bp), value="C:\\Users\\Public\\Documents\\output.csv", pos=(30, 115), size=(170, -1))
        _l_(570568)
        _n_(570569, "self", lambda: self).rb = _c_(570573, _a_(570571, _n_(570570, "wx", lambda: wx), "RadioBox"), _n_(570572, "bp", lambda: bp), label="Data:", pos=(5, 140), choices=["Profile", "WinCam"])
        _l_(570574)
        _n_(570575, "self", lambda: self).cb = _c_(570579, _a_(570577, _n_(570576, "wx", lambda: wx), "ComboBox"), _n_(570578, "bp", lambda: bp), pos=(5,200), choices=[ "Profile_X", "Profile_Y", "Both"])
        _l_(570580)
        _c_(570584, _a_(570583, _a_(570582, _n_(570581, "self", lambda: self), "cb"), "SetSelection"), 0)
        _l_(570585)
        myb = _c_(570589, _a_(570587, _n_(570586, "wx", lambda: wx), "Button"), _n_(570588, "bp", lambda: bp), label="Write", pos=(5,225))
        _l_(570590)
        _c_(570597, _a_(570592, _n_(570591, "myb", lambda: myb), "Bind"), _a_(570594, _n_(570593, "wx", lambda: wx), "EVT_BUTTON"), _a_(570596, _n_(570595, "self", lambda: self), "OnClick"))
        _l_(570598)
        #Pictures
        pic = _c_(570604, _a_(570601, _a_(570600, _a_(570599, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(570603, _n_(570602, "self", lambda: self), "frame"),size=(250,250),axID='DATARAYOCX.CCDimageCtrl.1')
        _l_(570605)
        tpic = _c_(570611, _a_(570608, _a_(570607, _a_(570606, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(570610, _n_(570609, "self", lambda: self), "frame"),size=(250,250), axID='DATARAYOCX.ThreeDviewCtrl.1')
        _l_(570612)
        palette = _c_(570618, _a_(570615, _a_(570614, _a_(570613, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(570617, _n_(570616, "self", lambda: self), "frame"),size=(10,250), axID='DATARAYOCX.PaletteBarCtrl.1')
        _l_(570619)
        #Profiles
        _n_(570620, "self", lambda: self).px = _c_(570626, _a_(570623, _a_(570622, _a_(570621, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(570625, _n_(570624, "self", lambda: self), "frame"),size=(300,200),axID='DATARAYOCX.ProfilesCtrl.1')
        _l_(570627)
        _a_(570630, _a_(570629, _n_(570628, "self", lambda: self), "px"), "ctrl").ProfileID=22
        _l_(570631)
        _n_(570632, "self", lambda: self).py = _c_(570638, _a_(570635, _a_(570634, _a_(570633, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(570637, _n_(570636, "self", lambda: self), "frame"),size=(300,200),axID='DATARAYOCX.ProfilesCtrl.1')
        _l_(570639)
        _a_(570642, _a_(570641, _n_(570640, "self", lambda: self), "py"), "ctrl").ProfileID = 23
        _l_(570643)
        #Formatting 
        row1 = _c_(570648, _a_(570645, _n_(570644, "wx", lambda: wx), "BoxSizer"), _a_(570647, _n_(570646, "wx", lambda: wx), "HORIZONTAL"))
        _l_(570649)
        _c_(570655, _a_(570651, _n_(570650, "row1", lambda: row1), "Add"), window=_n_(570652, "bp", lambda: bp),flag=_a_(570654, _n_(570653, "wx", lambda: wx), "RIGHT"), border=10)
        _l_(570656)
        _c_(570660, _a_(570658, _n_(570657, "row1", lambda: row1), "Add"), _n_(570659, "pic", lambda: pic))
        _l_(570661)
        _c_(570667, _a_(570663, _n_(570662, "row1", lambda: row1), "Add"), window=_n_(570664, "tpic", lambda: tpic), flag=_a_(570666, _n_(570665, "wx", lambda: wx), "LEFT"), border=10)
        _l_(570668)
        row2 = _c_(570673, _a_(570670, _n_(570669, "wx", lambda: wx), "BoxSizer"), _a_(570672, _n_(570671, "wx", lambda: wx), "HORIZONTAL"))
        _l_(570674)
        _c_(570681, _a_(570676, _n_(570675, "row2", lambda: row2), "Add"), _a_(570678, _n_(570677, "self", lambda: self), "px"), 0, _a_(570680, _n_(570679, "wx", lambda: wx), "RIGHT"), 100)# Arguments: item, proportion, flags, border
        _l_(570682)# Arguments: item, proportion, flags, border
        _c_(570687, _a_(570684, _n_(570683, "row2", lambda: row2), "Add"), _a_(570686, _n_(570685, "self", lambda: self), "py"))
        _l_(570688)
        col1 = _c_(570693, _a_(570690, _n_(570689, "wx", lambda: wx), "BoxSizer"), _a_(570692, _n_(570691, "wx", lambda: wx), "VERTICAL"))
        _l_(570694)
        _c_(570700, _a_(570696, _n_(570695, "col1", lambda: col1), "Add"), sizer=_n_(570697, "row1", lambda: row1), flag=_a_(570699, _n_(570698, "wx", lambda: wx), "BOTTOM"), border=10)
        _l_(570701)
        _c_(570707, _a_(570703, _n_(570702, "col1", lambda: col1), "Add"), sizer=_n_(570704, "row2", lambda: row2), flag=_a_(570706, _n_(570705, "wx", lambda: wx), "ALIGN_CENTER_HORIZONTAL"))
        _l_(570708)
        _c_(570713, _a_(570711, _a_(570710, _n_(570709, "self", lambda: self), "frame"), "SetSizer"), _n_(570712, "col1", lambda: col1))
        _l_(570714)
        _c_(570718, _a_(570717, _a_(570716, _n_(570715, "self", lambda: self), "frame"), "Show"))
        _l_(570719)

if _n_(570722, "__name__", lambda: __name__) == "__main__":
    _l_(570730)

    app = _c_(570724, _n_(570723, "MyApp", lambda: MyApp))
    _l_(570725)
    _c_(570728, _a_(570727, _n_(570726, "app", lambda: app), "MainLoop"))
    _l_(570729)