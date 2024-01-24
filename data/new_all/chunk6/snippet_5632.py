# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57302078/constant-name-errors-in-ipython
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(366723, "df", lambda: df)["date"] = _c_(366728, _a_(366725, _n_(366724, "pd", lambda: pd), "to_datetime"), _a_(366727, _n_(366726, "df", lambda: df), "index"))
_l_(366729)

mids = (_a_(366731, _n_(366730, "df", lambda: df), "Open") + _a_(366733, _n_(366732, "df", lambda: df), "Close"))/2
_l_(366734)
spans = _c_(366740, _n_(366735, "abs", lambda: abs), _a_(366737, _n_(366736, "df", lambda: df), "Close")-_a_(366739, _n_(366738, "df", lambda: df), "Open"))
_l_(366741)

inc = _a_(366743, _n_(366742, "df", lambda: df), "Close") > _a_(366745, _n_(366744, "df", lambda: df), "Open")
_l_(366746)
dec = _a_(366748, _n_(366747, "df", lambda: df), "Open") > _a_(366750, _n_(366749, "df", lambda: df), "Close")
_l_(366751)
w = 12*60*60*1000 # half day in ms
_l_(366752) # half day in ms

_c_(366754, _n_(366753, "output_notebook", lambda: output_notebook))
_l_(366755)

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
_l_(366756)

p = _c_(366759, _n_(366757, "figure", lambda: figure), x_axis_type="datetime", tools=_n_(366758, "TOOLS", lambda: TOOLS), plot_width=1000,      toolbar_location="left",y_axis_label = "Price",
      x_axis_label = "Date")
_l_(366760)

_c_(366771, _a_(366762, _n_(366761, "p", lambda: p), "segment"), _a_(366764, _n_(366763, "df", lambda: df), "date"), _a_(366766, _n_(366765, "df", lambda: df), "High"), _a_(366768, _n_(366767, "df", lambda: df), "date"), _a_(366770, _n_(366769, "df", lambda: df), "Low"), color="black")
_l_(366772)
_c_(366783, _a_(366774, _n_(366773, "p", lambda: p), "rect"), _a_(366776, _n_(366775, "df", lambda: df), "date")[_n_(366777, "inc", lambda: inc)], _n_(366778, "mids", lambda: mids)[_n_(366779, "inc", lambda: inc)], _n_(366780, "w", lambda: w), _n_(366781, "spans", lambda: spans)[_n_(366782, "inc", lambda: inc)], fill_color='green', line_color="green")
_l_(366784)
_c_(366795, _a_(366786, _n_(366785, "p", lambda: p), "rect"), _a_(366788, _n_(366787, "df", lambda: df), "date")[_n_(366789, "dec", lambda: dec)], _n_(366790, "mids", lambda: mids)[_n_(366791, "dec", lambda: dec)], _n_(366792, "w", lambda: w), _n_(366793, "spans", lambda: spans)[_n_(366794, "dec", lambda: dec)], fill_color='red', line_color="red")
_l_(366796)
_c_(366802, _a_(366798, _n_(366797, "p", lambda: p), "line"), _a_(366800, _n_(366799, "df", lambda: df), "date"),_n_(366801, "state_means", lambda: state_means),line_width=1,line_color = 'blue',legend="Kalman filter")
_l_(366803)

_n_(366804, "p", lambda: p).title = "Implementation of Kalman Filter Estimation - TCS EOD chart"
_l_(366805)
_a_(366807, _n_(366806, "p", lambda: p), "xaxis").major_label_orientation = _n_(366808, "pi", lambda: pi)/4
_l_(366809)
_a_(366811, _n_(366810, "p", lambda: p), "grid").grid_line_alpha=0.3
_l_(366812)