# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62208703/in-wxgrid-with-two-sizers-when-i-try-to-add-event-receive-this-error-typeerro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import wx
    _l_(650694)

except ImportError:
    pass
try:
    import wx.grid
    _l_(650696)

except ImportError:
    pass
try:
    from wx.lib.scrolledpanel import ScrolledPanel
    _l_(650698)

except ImportError:
    pass


class TestPanel(_n_(650699, "ScrolledPanel", lambda: ScrolledPanel)):
    _l_(650858)

    def __init__(self, parent):
        _l_(650826)

        _c_(650706, _a_(650701, _n_(650700, "ScrolledPanel", lambda: ScrolledPanel), "__init__"), _n_(650702, "self", lambda: self), _n_(650703, "parent", lambda: parent), _a_(650705, _n_(650704, "wx", lambda: wx), "ID_ANY"), size=(640, 480))
        _l_(650707)
        _n_(650708, "self", lambda: self).sizer = _c_(650713, _a_(650710, _n_(650709, "wx", lambda: wx), "BoxSizer"), _a_(650712, _n_(650711, "wx", lambda: wx), "VERTICAL"))
        _l_(650714)
        _c_(650725, _a_(650717, _a_(650716, _n_(650715, "self", lambda: self), "sizer"), "Add"), _c_(650720, _a_(650719, _n_(650718, "self", lambda: self), "_create_table")), 1, _a_(650722, _n_(650721, "wx", lambda: wx), "EXPAND") | _a_(650724, _n_(650723, "wx", lambda: wx), "ALL"), 5)
        _l_(650726)

        vbox1 = _c_(650729, _a_(650728, _n_(650727, "wx", lambda: wx), "FlexGridSizer"), rows = 1 , cols = 3 , hgap = 5 , vgap = 5 ) #rows = 3 , cols = 1
        _l_(650730) #rows = 3 , cols = 1
        _n_(650731, "self", lambda: self).b1 = _c_(650735, _a_(650733, _n_(650732, "wx", lambda: wx), "Button"), _n_(650734, "self", lambda: self), -1, "Button 1")
        _l_(650736)
        _n_(650737, "self", lambda: self).b2 = _c_(650741, _a_(650739, _n_(650738, "wx", lambda: wx), "Button"), _n_(650740, "self", lambda: self), -1, "Button 2")
        _l_(650742)
        _n_(650743, "self", lambda: self).b3 = _c_(650747, _a_(650745, _n_(650744, "wx", lambda: wx), "Button"), _n_(650746, "self", lambda: self), -1, "Button 3")
        _l_(650748)

        button_sizer = _c_(650753, _a_(650750, _n_(650749, "wx", lambda: wx), "BoxSizer"), _a_(650752, _n_(650751, "wx", lambda: wx), "VERTICAL")) # HORIZONTAL
        _l_(650754) # HORIZONTAL
        _c_(650759, _a_(650756, _n_(650755, "button_sizer", lambda: button_sizer), "Add"), _a_(650758, _n_(650757, "self", lambda: self), "b1"))
        _l_(650760)
        _c_(650765, _a_(650762, _n_(650761, "button_sizer", lambda: button_sizer), "Add"), _a_(650764, _n_(650763, "self", lambda: self), "b2"))
        _l_(650766)
        _c_(650771, _a_(650768, _n_(650767, "button_sizer", lambda: button_sizer), "Add"), _a_(650770, _n_(650769, "self", lambda: self), "b3"))
        _l_(650772)
        _c_(650776, _a_(650774, _n_(650773, "vbox1", lambda: vbox1), "Add"), _n_(650775, "button_sizer", lambda: button_sizer) )
        _l_(650777)

        _c_(650782, _a_(650779, _n_(650778, "vbox1", lambda: vbox1), "Add"), _a_(650781, _n_(650780, "self", lambda: self), "sizer") )
        _l_(650783)

        midPan1 = _c_(650787, _a_(650785, _n_(650784, "wx", lambda: wx), "Panel"), _n_(650786, "self", lambda: self) )
        _l_(650788)
        _c_(650791, _a_(650790, _n_(650789, "midPan1", lambda: midPan1), "SetBackgroundColour"), '#ededed' )
        _l_(650792)

        _c_(650802, _a_(650794, _n_(650793, "vbox1", lambda: vbox1), "Add"), _n_(650795, "midPan1", lambda: midPan1) , _a_(650797, _n_(650796, "wx", lambda: wx), "ID_ANY") , _a_(650799, _n_(650798, "wx", lambda: wx), "EXPAND") | _a_(650801, _n_(650800, "wx", lambda: wx), "ALL") , 20 )
        _l_(650803)

        _c_(650807, _a_(650805, _n_(650804, "self", lambda: self), "SetSizer"), _n_(650806, "vbox1", lambda: vbox1) )
        _l_(650808)


        _c_(650811, _a_(650810, _n_(650809, "self", lambda: self), "SetupScrolling"))
        _l_(650812)
        _c_(650815, _a_(650814, _n_(650813, "self", lambda: self), "SetAutoLayout"), 1)
        _l_(650816)

        _c_(650824, _a_(650819, _a_(650818, _n_(650817, "self", lambda: self), "b1"), "Bind"), _a_(650821, _n_(650820, "wx", lambda: wx), "EVT_BUTTON") , _a_(650823, _n_(650822, "self", lambda: self), "be1") )
        _l_(650825)

    def be1 (self) :
        _l_(650830)

        _c_(650828, _n_(650827, "print", lambda: print), "7654321" )
        _l_(650829)


    def _create_table(self):
        _l_(650857)

        _table = _c_(650834, _a_(650832, _a_(650831, wx, "grid"), "Grid"), _n_(650833, "self", lambda: self), -1)
        _l_(650835)
        _c_(650838, _a_(650837, _n_(650836, "_table", lambda: _table), "CreateGrid"), 0, 10)
        _l_(650839)
        for i in _c_(650841, _n_(650840, "range", lambda: range), 30):
            _l_(650854)

            _c_(650844, _a_(650843, _n_(650842, "_table", lambda: _table), "AppendRows"))
            _l_(650845)
            _c_(650852, _a_(650847, _n_(650846, "_table", lambda: _table), "SetCellValue"), _n_(650848, "i", lambda: i), 0, _c_(650851, _n_(650849, "str", lambda: str), _n_(650850, "i", lambda: i)))
            _l_(650853)
        aux = _n_(650855, "_table", lambda: _table)
        _l_(650856)
        return aux

class TestFrame(_a_(650860, _n_(650859, "wx", lambda: wx), "Frame")):
    _l_(650897)

    def __init__(self):
        _l_(650896)

        _c_(650867, _a_(650863, _a_(650862, _n_(650861, "wx", lambda: wx), "Frame"), "__init__"), _n_(650864, "self", lambda: self), None, _a_(650866, _n_(650865, "wx", lambda: wx), "ID_ANY"),
                title="Scroll table", size=(640, 480))
        _l_(650868)
        _n_(650869, "self", lambda: self).fSizer = _c_(650874, _a_(650871, _n_(650870, "wx", lambda: wx), "BoxSizer"), _a_(650873, _n_(650872, "wx", lambda: wx), "VERTICAL"))
        _l_(650875)
        _c_(650884, _a_(650878, _a_(650877, _n_(650876, "self", lambda: self), "fSizer"), "Add"), _c_(650881, _n_(650879, "TestPanel", lambda: TestPanel), _n_(650880, "self", lambda: self)), 1, _a_(650883, _n_(650882, "wx", lambda: wx), "EXPAND"))
        _l_(650885)
        _c_(650890, _a_(650887, _n_(650886, "self", lambda: self), "SetSizer"), _a_(650889, _n_(650888, "self", lambda: self), "fSizer"))
        _l_(650891)
        _c_(650894, _a_(650893, _n_(650892, "self", lambda: self), "Show"))
        _l_(650895)

if _n_(650898, "__name__", lambda: __name__) == "__main__":
    _l_(650910)

    app = _c_(650901, _a_(650900, _n_(650899, "wx", lambda: wx), "App"), False)
    _l_(650902)
    frame = _c_(650904, _n_(650903, "TestFrame", lambda: TestFrame))
    _l_(650905)
    _c_(650908, _a_(650907, _n_(650906, "app", lambda: app), "MainLoop"))
    _l_(650909)