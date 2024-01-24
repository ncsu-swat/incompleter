# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57102028/plotly-attributeerror-figure-object-has-no-attribute-update-layout
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from _plotly_future_ import v4_subplots
    _l_(410837)

except ImportError:
    pass
try:
    from plotly.subplots import make_subplots
    _l_(410839)

except ImportError:
    pass
try:
    import plotly.graph_objs as go
    _l_(410841)

except ImportError:
    pass
try:
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
    _l_(410843)

except ImportError:
    pass
try:
    import plotly.plotly as py
    _l_(410845)

except ImportError:
    pass

fig1 = _c_(410847, _n_(410846, "make_subplots", lambda: make_subplots), rows=2, cols=2,
    specs=[[{"type": "pie"}, {"type": "pie"}],
           [{"type": "table"}, {"type": "table"}]],
)
_l_(410848)

_c_(410856, _a_(410850, _n_(410849, "fig1", lambda: fig1), "add_trace"), _c_(410855, _a_(410852, _n_(410851, "go", lambda: go), "Pie"), labels=_n_(410853, "pie_alarms_total", lambda: pie_alarms_total)['alarm_type'],
        values=_n_(410854, "pie_alarms_total", lambda: pie_alarms_total)['alarm_timestamp'],
        name="Total Alarms",
        title="test"
    ),
    row=1, col=1

)
_l_(410857)

_c_(410865, _a_(410859, _n_(410858, "fig1", lambda: fig1), "add_trace"), _c_(410864, _a_(410861, _n_(410860, "go", lambda: go), "Pie"), labels=_n_(410862, "pie_alarms_notbd", lambda: pie_alarms_notbd)['alarm_type'],
        values=_n_(410863, "pie_alarms_notbd", lambda: pie_alarms_notbd)['alarm_timestamp'],
        name="No TBDs"
    ),
    row=1, col=2
)
_l_(410866)

_c_(410878, _a_(410868, _n_(410867, "fig1", lambda: fig1), "add_trace"), _c_(410877, _a_(410870, _n_(410869, "go", lambda: go), "Table"), header=_c_(410873, _n_(410871, "dict", lambda: dict), values=_n_(410872, "pie_alarms_total", lambda: pie_alarms_total)['alarm_type'],
            line_color='darkslategray',
            fill_color='lightskyblue'
        ),
        cells=_c_(410876, _n_(410874, "dict", lambda: dict), values=_n_(410875, "pie_alarms_total", lambda: pie_alarms_total)['alarm_timestamp'],
            line_color='darkslategray',
            fill_color='lightcyan'
        )
    ),
    row=2, col=1
)
_l_(410879)

_c_(410891, _a_(410881, _n_(410880, "fig1", lambda: fig1), "add_trace"), _c_(410890, _a_(410883, _n_(410882, "go", lambda: go), "Table"), header=_c_(410886, _n_(410884, "dict", lambda: dict), values=_n_(410885, "pie_alarms_notbd", lambda: pie_alarms_notbd)['alarm_type'],
            line_color='darkslategray',
            fill_color='lightskyblue'
        ),
        cells=_c_(410889, _n_(410887, "dict", lambda: dict), values=_n_(410888, "pie_alarms_notbd", lambda: pie_alarms_notbd)['alarm_timestamp'],
            line_color='darkslategray',
            fill_color='lightcyan'
        )
    ),
    row=2, col=2
)
_l_(410892)

_c_(410895, _a_(410894, _n_(410893, "fig1", lambda: fig1), "update_layout"), title_text="Test")
_l_(410896)

_c_(410899, _n_(410897, "plot", lambda: plot), _n_(410898, "fig1", lambda: fig1), filename="test.html")
_l_(410900)