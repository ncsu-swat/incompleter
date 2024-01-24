# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64988130/error-typeerror-item-1-in-argtypes-passes-a-union-by-value-which-is-unsuppo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import wx
    _l_(528563)

except ImportError:
    pass
try:
    import wx.lib.activex
    _l_(528565)

except ImportError:
    pass
try:
    import csv
    _l_(528567)

except ImportError:
    pass
try:
    import comtypes.client
    _l_(528569)

except ImportError:
    pass

class EventSink(_n_(528570, "object", lambda: object)):
    _l_(528587)


    def __init__(self, frame):
        _l_(528576)

        _n_(528571, "self", lambda: self).counter = 0
        _l_(528572)
        _n_(528573, "self", lambda: self).frame = _n_(528574, "frame", lambda: frame)
        _l_(528575)

    def DataReady(self):
        _l_(528586)

        _n_(528577, "self", lambda: self).counter +=1
        _l_(528578)
        _a_(528580, _n_(528579, "self", lambda: self), "frame").Title= _c_(528584, _a_(528581, "DataReady fired {0} times", "format"), _a_(528583, _n_(528582, "self", lambda: self), "counter"))
        _l_(528585)

class MyApp( _a_(528589, _n_(528588, "wx", lambda: wx), "App") ):
    _l_(528971)


    def __init__( self, redirect=False, filename=None ):
        _l_(528606)

        _c_(528596, _a_(528592, _a_(528591, _n_(528590, "wx", lambda: wx), "App"), "__init__"), _n_(528593, "self", lambda: self), _n_(528594, "redirect", lambda: redirect), _n_(528595, "filename", lambda: filename) )
        _l_(528597)
        _c_(528600, _a_(528599, _n_(528598, "self", lambda: self), "initUI"))
        _l_(528601)
        _c_(528604, _a_(528603, _n_(528602, "self", lambda: self), "bindUI"))
        _l_(528605)

    def bindUI(self):
        _l_(528625)

        _c_(528614, _a_(528609, _a_(528608, _n_(528607, "self", lambda: self), "myb1"), "Bind"), _a_(528611, _n_(528610, "wx", lambda: wx), "EVT_BUTTON"), _a_(528613, _n_(528612, "self", lambda: self), "myb1click"))
        _l_(528615)
        _c_(528623, _a_(528618, _a_(528617, _n_(528616, "self", lambda: self), "myb2"), "Bind"), _a_(528620, _n_(528619, "wx", lambda: wx), "EVT_BUTTON"), _a_(528622, _n_(528621, "self", lambda: self), "myb2click"))
        _l_(528624)

    def initUI(self):
        _l_(528885)

        _n_(528626, "self", lambda: self).frame = _c_(528631, _a_(528628, _n_(528627, "wx", lambda: wx), "Frame"), parent=None, id=_a_(528630, _n_(528629, "wx", lambda: wx), "ID_ANY"),size=(760,500), title='Python Interface to DataRay')
        _l_(528632)
        #Panel
        p = _c_(528639, _a_(528634, _n_(528633, "wx", lambda: wx), "Panel"), _a_(528636, _n_(528635, "self", lambda: self), "frame"), _a_(528638, _n_(528637, "wx", lambda: wx), "ID_ANY"))
        _l_(528640)
        #Get Data
        _n_(528641, "self", lambda: self).gd = _c_(528646, _a_(528644, _a_(528643, _a_(528642, wx, "lib"), "activex"), "ActiveXCtrl"), _n_(528645, "p", lambda: p), 'DATARAYOCX.GetDataCtrl.1')
        _l_(528647)
        _c_(528652, _a_(528651, _a_(528650, _a_(528649, _n_(528648, "self", lambda: self), "gd"), "ctrl"), "StartDriver"))#The methods of the object are available through the ctrl property of the item
        _l_(528653)#The methods of the object are available through the ctrl property of the item
        sink = _c_(528657, _n_(528654, "EventSink", lambda: EventSink), _a_(528656, _n_(528655, "self", lambda: self), "frame"))
        _l_(528658)
        _n_(528659, "self", lambda: self).sink = _c_(528666, _a_(528661, _a_(528660, comtypes, "client"), "GetEvents"), _a_(528664, _a_(528663, _n_(528662, "self", lambda: self), "gd"), "ctrl"), _n_(528665, "sink", lambda: sink))
        _l_(528667)
        #Button Panel
        bp = _c_(528674, _a_(528669, _n_(528668, "wx", lambda: wx), "Panel"), parent=_a_(528671, _n_(528670, "self", lambda: self), "frame"), id=_a_(528673, _n_(528672, "wx", lambda: wx), "ID_ANY"), size=(215, 250))
        _l_(528675)
        b1 = _c_(528680, _a_(528678, _a_(528677, _a_(528676, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(528679, "bp", lambda: bp),size=(200,50), pos=(7, 0),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(528681)
        _a_(528683, _n_(528682, "b1", lambda: b1), "ctrl").ButtonID =297 #Id's for some ActiveX controls must be set
        _l_(528684) #Id's for some ActiveX controls must be set
        b2 = _c_(528689, _a_(528687, _a_(528686, _a_(528685, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(528688, "bp", lambda: bp),size=(100,25), pos=(5, 55),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(528690)
        _a_(528692, _n_(528691, "b2", lambda: b2), "ctrl").ButtonID =86
        _l_(528693)
        b3 = _c_(528698, _a_(528696, _a_(528695, _a_(528694, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(528697, "bp", lambda: bp),size=(100,25), pos=(110,55),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(528699)
        _a_(528701, _n_(528700, "b3", lambda: b3), "ctrl").ButtonID =87
        _l_(528702)
        b4 = _c_(528707, _a_(528705, _a_(528704, _a_(528703, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(528706, "bp", lambda: bp),size=(100,25), pos=(5, 85),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(528708)
        _a_(528710, _n_(528709, "b4", lambda: b4), "ctrl").ButtonID =96
        _l_(528711)
        b4 = _c_(528716, _a_(528714, _a_(528713, _a_(528712, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_n_(528715, "bp", lambda: bp),size=(100,25), pos=(110, 85),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(528717)
        _a_(528719, _n_(528718, "b4", lambda: b4), "ctrl").ButtonID =9
        _l_(528720)
        
        #Custom controls
        t = _c_(528724, _a_(528722, _n_(528721, "wx", lambda: wx), "StaticText"), _n_(528723, "bp", lambda: bp), label="File:", pos=(5, 115))
        _l_(528725)
        _n_(528726, "self", lambda: self).ti = _c_(528730, _a_(528728, _n_(528727, "wx", lambda: wx), "TextCtrl"), _n_(528729, "bp", lambda: bp), value="C:\\Users\\Public\\Documents\\output.csv", pos=(30, 115), size=(170, -1))
        _l_(528731)
        _n_(528732, "self", lambda: self).rb = _c_(528736, _a_(528734, _n_(528733, "wx", lambda: wx), "RadioBox"), _n_(528735, "bp", lambda: bp), label="Data:", pos=(5, 140), choices=["Profile"])
        _l_(528737)
        _n_(528738, "self", lambda: self).cb = _c_(528742, _a_(528740, _n_(528739, "wx", lambda: wx), "ComboBox"), _n_(528741, "bp", lambda: bp), pos=(5,200), choices=[ "Profile_X", "Profile_Y", "Both"])
        _l_(528743)
        _c_(528747, _a_(528746, _a_(528745, _n_(528744, "self", lambda: self), "cb"), "SetSelection"), 0)
        _l_(528748)
        _n_(528749, "self", lambda: self).myb1 = _c_(528753, _a_(528751, _n_(528750, "wx", lambda: wx), "Button"), _n_(528752, "bp", lambda: bp), label="Write", pos=(5,225))
        _l_(528754)
        _n_(528755, "self", lambda: self).myb2 = _c_(528759, _a_(528757, _n_(528756, "wx", lambda: wx), "Button"), _n_(528758, "bp", lambda: bp), label="Switch", pos=(110,225))
        _l_(528760)
        #Pictures
        wanderer = _c_(528766, _a_(528763, _a_(528762, _a_(528761, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(528765, _n_(528764, "self", lambda: self), "frame"),size=(250,250),axID='DATARAYOCX.ButtonCtrl.1')
        _l_(528767)
        _a_(528769, _n_(528768, "wanderer", lambda: wanderer), "ctrl").ButtonID = 197
        _l_(528770)
        tpic = _c_(528776, _a_(528773, _a_(528772, _a_(528771, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(528775, _n_(528774, "self", lambda: self), "frame"),size=(250,250), axID='DATARAYOCX.TwoDCtrl.1')
        _l_(528777)
        palette = _c_(528783, _a_(528780, _a_(528779, _a_(528778, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(528782, _n_(528781, "self", lambda: self), "frame"),size=(10,250), axID='DATARAYOCX.PaletteBarCtrl.1')
        _l_(528784)
        #Profiles
        _n_(528785, "self", lambda: self).px = _c_(528791, _a_(528788, _a_(528787, _a_(528786, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(528790, _n_(528789, "self", lambda: self), "frame"),size=(300,200),axID='DATARAYOCX.ProfilesCtrl.1')
        _l_(528792)
        _a_(528795, _a_(528794, _n_(528793, "self", lambda: self), "px"), "ctrl").ProfileID=4
        _l_(528796)
        _n_(528797, "self", lambda: self).py = _c_(528803, _a_(528800, _a_(528799, _a_(528798, wx, "lib"), "activex"), "ActiveXCtrl"), parent=_a_(528802, _n_(528801, "self", lambda: self), "frame"),size=(300,200),axID='DATARAYOCX.ProfilesCtrl.1')
        _l_(528804)
        _a_(528807, _a_(528806, _n_(528805, "self", lambda: self), "py"), "ctrl").ProfileID =5
        _l_(528808)

        #Formatting 
        row1 = _c_(528813, _a_(528810, _n_(528809, "wx", lambda: wx), "BoxSizer"), _a_(528812, _n_(528811, "wx", lambda: wx), "HORIZONTAL"))
        _l_(528814)
        _c_(528820, _a_(528816, _n_(528815, "row1", lambda: row1), "Add"), item=_n_(528817, "bp", lambda: bp),flag=_a_(528819, _n_(528818, "wx", lambda: wx), "RIGHT"), border=10)
        _l_(528821)
        _c_(528825, _a_(528823, _n_(528822, "row1", lambda: row1), "Add"), _n_(528824, "wanderer", lambda: wanderer))
        _l_(528826)
        _c_(528832, _a_(528828, _n_(528827, "row1", lambda: row1), "Add"), item=_n_(528829, "tpic", lambda: tpic), flag=_a_(528831, _n_(528830, "wx", lambda: wx), "LEFT"), border=10)
        _l_(528833)
        
        row2 = _c_(528838, _a_(528835, _n_(528834, "wx", lambda: wx), "BoxSizer"), _a_(528837, _n_(528836, "wx", lambda: wx), "HORIZONTAL"))
        _l_(528839)
        _c_(528846, _a_(528841, _n_(528840, "row2", lambda: row2), "Add"), _a_(528843, _n_(528842, "self", lambda: self), "px"), 0, _a_(528845, _n_(528844, "wx", lambda: wx), "RIGHT"), 100)# Arguments: item, proportion, flags, border
        _l_(528847)# Arguments: item, proportion, flags, border
        _c_(528852, _a_(528849, _n_(528848, "row2", lambda: row2), "Add"), _a_(528851, _n_(528850, "self", lambda: self), "py"))
        _l_(528853)

        col1 = _c_(528858, _a_(528855, _n_(528854, "wx", lambda: wx), "BoxSizer"), _a_(528857, _n_(528856, "wx", lambda: wx), "VERTICAL"))
        _l_(528859)
        _c_(528865, _a_(528861, _n_(528860, "col1", lambda: col1), "Add"), item=_n_(528862, "row1", lambda: row1), flag=_a_(528864, _n_(528863, "wx", lambda: wx), "BOTTOM"), border=10)
        _l_(528866)
        _c_(528872, _a_(528868, _n_(528867, "col1", lambda: col1), "Add"), item=_n_(528869, "row2", lambda: row2), flag=_a_(528871, _n_(528870, "wx", lambda: wx), "ALIGN_CENTER_HORIZONTAL"))
        _l_(528873)
        _c_(528878, _a_(528876, _a_(528875, _n_(528874, "self", lambda: self), "frame"), "SetSizer"), _n_(528877, "col1", lambda: col1))
        _l_(528879)
        _c_(528883, _a_(528882, _a_(528881, _n_(528880, "self", lambda: self), "frame"), "Show"))
        _l_(528884)

    def myb1click(self,e):
        _l_(528956)

        rb_selection = _c_(528889, _a_(528888, _a_(528887, _n_(528886, "self", lambda: self), "rb"), "GetStringSelection"))
        _l_(528890)
        p_selection = _c_(528894, _a_(528893, _a_(528892, _n_(528891, "self", lambda: self), "cb"), "GetStringSelection"))
        _l_(528895)
        if _n_(528896, "p_selection", lambda: p_selection) == "Profile_X":
            _l_(528937)

            data = _c_(528901, _a_(528900, _a_(528899, _a_(528898, _n_(528897, "self", lambda: self), "px"), "ctrl"), "GetProfileDataAsVariant"))
            _l_(528902)
            data = [[_n_(528903, "x", lambda: x)] for x in _n_(528904, "data", lambda: data)]#csv.writerows accepts a list of rows where each row is a list, a list of lists
            _l_(528905)#csv.writerows accepts a list of rows where each row is a list, a list of lists
        elif _n_(528906, "p_selection", lambda: p_selection) == "Profile_Y":
            _l_(528936)

            data = _c_(528911, _a_(528910, _a_(528909, _a_(528908, _n_(528907, "self", lambda: self), "py"), "ctrl"), "GetProfileDataAsVariant"))
            _l_(528912)
            data = [[_n_(528913, "x", lambda: x)] for x in _n_(528914, "data", lambda: data)]
            _l_(528915)
        else:
            datax = _c_(528920, _a_(528919, _a_(528918, _a_(528917, _n_(528916, "self", lambda: self), "px"), "ctrl"), "GetProfileDataAsVariant"))
            _l_(528921)
            datay = _c_(528926, _a_(528925, _a_(528924, _a_(528923, _n_(528922, "self", lambda: self), "py"), "ctrl"), "GetProfileDataAsVariant"))
            _l_(528927)
            data = [_c_(528930, _n_(528928, "list", lambda: list), _n_(528929, "a", lambda: a)) for a in _c_(528934, _n_(528931, "zip", lambda: zip), _n_(528932, "datax", lambda: datax),_n_(528933, "datay", lambda: datay))]#Makes a list of lists; X1 with Y1 in a list, X2 with Y2 in a list etc...
            _l_(528935)#Makes a list of lists; X1 with Y1 in a list, X2 with Y2 in a list etc...
        filename = _a_(528940, _a_(528939, _n_(528938, "self", lambda: self), "ti"), "Value")
        _l_(528941)
        with _c_(528944, _n_(528942, "open", lambda: open), _n_(528943, "filename", lambda: filename), 'wb') as fp:
            _l_(528955)

            w = _c_(528948, _a_(528946, _n_(528945, "csv", lambda: csv), "writer"), _n_(528947, "fp", lambda: fp), delimiter=',')
            _l_(528949)
            _c_(528953, _a_(528951, _n_(528950, "w", lambda: w), "writerows"), _n_(528952, "data", lambda: data))
            _l_(528954)

    def myb2click(self,e):
        _l_(528970)

        if _a_(528960, _a_(528959, _a_(528958, _n_(528957, "self", lambda: self), "gd"), "ctrl"), "AlternateDetector") == 0:
            _l_(528969)

            _a_(528963, _a_(528962, _n_(528961, "self", lambda: self), "gd"), "ctrl").AlternateDetector = 1
            _l_(528964)
        else:
            _a_(528967, _a_(528966, _n_(528965, "self", lambda: self), "gd"), "ctrl").AlternateDetector = 0
            _l_(528968)

if _n_(528972, "__name__", lambda: __name__) == "__main__":
    _l_(528980)

    app = _c_(528974, _n_(528973, "MyApp", lambda: MyApp))
    _l_(528975)
    _c_(528978, _a_(528977, _n_(528976, "app", lambda: app), "MainLoop"))
    _l_(528979)