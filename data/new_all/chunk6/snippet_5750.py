# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55667502/attributeerror-int-object-has-no-attribute-squeeze
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    _l_(337453)

    _c_(337423, _n_(337421, "output_file", lambda: output_file), _n_(337422, "file_name", lambda: file_name))
    _l_(337424)
    p = _c_(337427, _n_(337425, "figure", lambda: figure), title=_n_(337426, "title", lambda: title), x_axis_label='year', y_axis_label='%')
    _l_(337428)
    _c_(337437, _a_(337430, _n_(337429, "p", lambda: p), "line"), _c_(337433, _a_(337432, _n_(337431, "x", lambda: x), "squeeze")), _c_(337436, _a_(337435, _n_(337434, "gdp_change", lambda: gdp_change), "squeeze")), color="firebrick", line_width=4, legend="% GDP change")
    _l_(337438)
    _c_(337447, _a_(337440, _n_(337439, "p", lambda: p), "line"), _c_(337443, _a_(337442, _n_(337441, "x", lambda: x), "squeeze")), _c_(337446, _a_(337445, _n_(337444, "unemployment", lambda: unemployment), "squeeze")), line_width=4, legend="% unemployed")
    _l_(337448)
    _c_(337451, _n_(337449, "show", lambda: show), _n_(337450, "p", lambda: p))
    _l_(337452)


_c_(337457, _n_(337454, "make_dashboard", lambda: make_dashboard), x=1948, gdp_change=10, unemployment=3.75, title=_n_(337455, "title", lambda: title), file_name=_n_(337456, "file_name", lambda: file_name))
_l_(337458)