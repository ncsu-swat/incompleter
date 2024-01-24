# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65352993/typeerror-callback-got-an-unexpected-keyword-argument-prevent-initial-call
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import dash
    _l_(578020)

except ImportError:
    pass
try:
    from dash.dependencies import Input, Output
    _l_(578022)

except ImportError:
    pass
try:
    import dash_html_components as html
    _l_(578024)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(578026)

except ImportError:
    pass
try:
    import time
    _l_(578028)

except ImportError:
    pass

app = _c_(578031, _a_(578030, _n_(578029, "dash", lambda: dash), "Dash"))
_l_(578032)

_n_(578033, "app", lambda: app).layout = _c_(578051, _a_(578035, _n_(578034, "html", lambda: html), "Div"), [
        _c_(578038, _a_(578037, _n_(578036, "html", lambda: html), "Button"), "execute callbacks", id="button_2"),
        _c_(578041, _a_(578040, _n_(578039, "html", lambda: html), "Div"), children="callback not executed", id="first_output_2"),
        _c_(578044, _a_(578043, _n_(578042, "html", lambda: html), "Div"), children="callback not executed", id="second_output_2"),
        _c_(578047, _a_(578046, _n_(578045, "html", lambda: html), "Div"), children="callback not executed", id="third_output_2"),
        _c_(578050, _a_(578049, _n_(578048, "html", lambda: html), "Div"), children="callback not executed", id="fourth_output_2"),
    ]
)
_l_(578052)


@_c_(578061, _a_(578054, _n_(578053, "app", lambda: app), "callback"), _c_(578056, _n_(578055, "Output", lambda: Output), "first_output_2", "children"),
    _c_(578058, _n_(578057, "Output", lambda: Output), "second_output_2", "children"),
    _c_(578060, _n_(578059, "Input", lambda: Input), "button_2", "n_clicks"), prevent_initial_call=True)
def first_callback(n):
    _l_(578073)

    now = _c_(578064, _a_(578063, _n_(578062, "datetime", lambda: datetime), "now"))
    _l_(578065)
    current_time = _c_(578068, _a_(578067, _n_(578066, "now", lambda: now), "strftime"), "%H:%M:%S")
    _l_(578069)
    aux = ["in the first callback it is " + _n_(578070, "current_time", lambda: current_time), "in the first callback it is " + _n_(578071, "current_time", lambda: current_time)]
    _l_(578072)
    return aux


@_c_(578080, _a_(578075, _n_(578074, "app", lambda: app), "callback"), _c_(578077, _n_(578076, "Output", lambda: Output), "third_output_2", "children"), _c_(578079, _n_(578078, "Input", lambda: Input), "second_output_2", "children"), prevent_initial_call=True)
def second_callback(n):
    _l_(578095)

    _c_(578083, _a_(578082, _n_(578081, "time", lambda: time), "sleep"), 2)
    _l_(578084)
    now = _c_(578087, _a_(578086, _n_(578085, "datetime", lambda: datetime), "now"))
    _l_(578088)
    current_time = _c_(578091, _a_(578090, _n_(578089, "now", lambda: now), "strftime"), "%H:%M:%S")
    _l_(578092)
    aux = "in the second callback it is " + _n_(578093, "current_time", lambda: current_time)
    _l_(578094)
    return aux


@_c_(578104, _a_(578097, _n_(578096, "app", lambda: app), "callback"), _c_(578099, _n_(578098, "Output", lambda: Output), "fourth_output_2", "children"),
    _c_(578101, _n_(578100, "Input", lambda: Input), "first_output_2", "children"),
    _c_(578103, _n_(578102, "Input", lambda: Input), "third_output_2", "children"), prevent_initial_call=True)
def third_output(n, m):
    _l_(578119)

    _c_(578107, _a_(578106, _n_(578105, "time", lambda: time), "sleep"), 2)
    _l_(578108)
    now = _c_(578111, _a_(578110, _n_(578109, "datetime", lambda: datetime), "now"))
    _l_(578112)
    current_time = _c_(578115, _a_(578114, _n_(578113, "now", lambda: now), "strftime"), "%H:%M:%S")
    _l_(578116)
    aux = "in the third callback it is " + _n_(578117, "current_time", lambda: current_time)
    _l_(578118)
    return aux


if _n_(578120, "__name__", lambda: __name__) == '__main__':
    _l_(578125)

    _c_(578123, _a_(578122, _n_(578121, "app", lambda: app), "run_server"), debug=True)
    _l_(578124)