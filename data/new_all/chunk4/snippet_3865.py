# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66365065/typeerror-unhashable-type-bunch-appears-after-selecting-value-from-ipywidget
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ipywidgets as widgets
    _l_(645219)

except ImportError:
    pass
try:
    from IPython.display import display
    _l_(645221)

except ImportError:
    pass
try:
    from branca.colormap import linear
    _l_(645223)

except ImportError:
    pass

dropdownMenu = _c_(645226, _a_(645225, _n_(645224, "widgets", lambda: widgets), "Dropdown"), options=['mean','median'],value='mean',description='Column:')
_l_(645227)
widgetOutput = _c_(645230, _a_(645229, _n_(645228, "widgets", lambda: widgets), "Output"))
_l_(645231)

def colEvent(col):
    _l_(645287)

    _c_(645234, _a_(645233, _n_(645232, "widgetOutput", lambda: widgetOutput), "clear_output"))
    _l_(645235)
    colorDic = {}
    _l_(645236)
    namesList = ['A', 'B', 'C', 'D', 'E']
    _l_(645237)
    with _n_(645238, "widgetOutput", lambda: widgetOutput):
        _l_(645286)

        colormap = _c_(645256, _a_(645241, _a_(645240, _n_(645239, "linear", lambda: linear), "YlGn_09"), "scale"), _c_(645248, _n_(645242, "min", lambda: min), (_n_(645243, "nest", lambda: nest)[_n_(645244, "col", lambda: col)] for nest in _c_(645247, _a_(645246, _n_(645245, "testDict", lambda: testDict), "values")))),
            _c_(645255, _n_(645249, "max", lambda: max), (_n_(645250, "nest", lambda: nest)[_n_(645251, "col", lambda: col)] for nest in _c_(645254, _a_(645253, _n_(645252, "testDict", lambda: testDict), "values")))))
        _l_(645257)
        for name in _n_(645258, "namesList", lambda: namesList):
            _l_(645285)

            if _c_(645262, _a_(645260, _n_(645259, "testDict", lambda: testDict), "get"), _n_(645261, "name", lambda: name)):
                _l_(645284)

                _n_(645263, "colorDic", lambda: colorDic)[_n_(645264, "name", lambda: name)] = {}
                _l_(645265)
                _n_(645266, "colorDic", lambda: colorDic)[_n_(645267, "name", lambda: name)]=_c_(645276, _n_(645268, "colormap", lambda: colormap), _c_(645275, _a_(645273, _c_(645272, _a_(645270, _n_(645269, "testDict", lambda: testDict), "get"), _n_(645271, "name", lambda: name)), "get"), _n_(645274, "col", lambda: col)))
                _l_(645277)
            else:
                _n_(645278, "colorDic", lambda: colorDic)[_n_(645279, "name", lambda: name)] = {}
                _l_(645280)
                _n_(645281, "colorDic", lambda: colorDic)[_n_(645282, "name", lambda: name)] = '#ffffffff'
                _l_(645283)

_c_(645291, _a_(645289, _n_(645288, "dropdownMenu", lambda: dropdownMenu), "observe"), _n_(645290, "colEvent", lambda: colEvent), names='value')
_l_(645292)
_c_(645295, _n_(645293, "display", lambda: display), _n_(645294, "dropdownMenu", lambda: dropdownMenu))
_l_(645296)
_c_(645299, _n_(645297, "display", lambda: display), _n_(645298, "widgetOutput", lambda: widgetOutput))
_l_(645300)