# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73727265/attributeerror-wsgirequest-object-has-no-attribute-is-ajax-in-django-4-hi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(605540)

except ImportError:
    pass
try:
    from django.shortcuts import render
    _l_(605542)

except ImportError:
    pass
try:
    from highcharts.views import HighChartsBarView
    _l_(605544)

except ImportError:
    pass


class BarView(_n_(605545, "HighChartsBarView", lambda: HighChartsBarView)):
    _l_(605580)

    title = 'Example Bar Chart'
    _l_(605546)
    subtitle = 'my subtitle'
    _l_(605547)
    categories = ['Orange', 'Bananas', 'Apples']
    _l_(605548)
    chart_type = ''
    _l_(605549)
    chart = {'zoomType': 'xy'}
    _l_(605550)
    tooltip = {'shared': 'true'}
    _l_(605551)
    legend = {'layout': 'horizontal', 'align': 'left',
              'floating': 'true', 'verticalAlign': 'top',
              'y': -10, 'borderColor': '#e3e3e3'}
    _l_(605552)

    @_n_(605553, "property", lambda: property)
    def series(self):
        _l_(605579)

        result = []
        _l_(605554)
        for name in ('Joe', 'Jack', 'William', 'Averell'):
            _l_(605556)

            data = []
            _l_(605555)

        for x in _c_(605562, _n_(605557, "range", lambda: range), _c_(605561, _n_(605558, "len", lambda: len), _a_(605560, _n_(605559, "self", lambda: self), "categories"))):
            _l_(605570)

            _c_(605568, _a_(605564, _n_(605563, "data", lambda: data), "append"), _c_(605567, _a_(605566, _n_(605565, "random", lambda: random), "randint"), 0, 10))
            _l_(605569)
        _c_(605575, _a_(605572, _n_(605571, "result", lambda: result), "append"), {'name': _n_(605573, "name", lambda: name), "data": _n_(605574, "data", lambda: data)})
        _l_(605576)
        aux = _n_(605577, "result", lambda: result)
        _l_(605578)
        return aux