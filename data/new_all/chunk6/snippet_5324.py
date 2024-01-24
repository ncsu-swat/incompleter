# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66995341/typeerror-cannot-unpack-non-iterable-int-object-when-i-tried-to-attend-the-le
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
D = _c_(364205, _n_(364202, "calculate_distances", lambda: calculate_distances), _n_(364203, "x", lambda: x),_n_(364204, "y", lambda: y))
_l_(364206)

fig = _c_(364209, _a_(364208, _n_(364207, "plt", lambda: plt), "figure"), figsize=(6,6));
_l_(364210)
total_distance = 0
_l_(364211)
for i in _c_(364214, _n_(364212, "range", lambda: range), _n_(364213, "n_city", lambda: n_city)-1):
    _l_(364255)

    _c_(364219, _a_(364216, _n_(364215, "plt", lambda: plt), "scatter"), _n_(364217, "x", lambda: x),_n_(364218, "y", lambda: y),marker="s",c="k");
    _l_(364220)
    _c_(364233, _a_(364222, _n_(364221, "plt", lambda: plt), "plot"), [_n_(364223, "x", lambda: x)[_n_(364224, "i", lambda: i)],_n_(364225, "x", lambda: x)[_n_(364226, "i", lambda: i)+1]], [_n_(364227, "y", lambda: y)[_n_(364228, "i", lambda: i)],_n_(364229, "y", lambda: y)[_n_(364230, "i", lambda: i)+1]],
             alpha=(_n_(364231, "i", lambda: i)+1)/_n_(364232, "n_city", lambda: (n_city)),lw=2,color="k");
    _l_(364234)
    total_distance += _n_(364235, "D", lambda: D)[_n_(364236, "i", lambda: i),_n_(364237, "i", lambda: i)+1]
    _l_(364238)
    _c_(364242, _a_(364240, _n_(364239, "plt", lambda: plt), "title"), "Distance traveled = %0.3f" %_n_(364241, "total_distance", lambda: total_distance))
    _l_(364243)
    _c_(364246, _a_(364245, _n_(364244, "time", lambda: time), "sleep"), 1.0)  
    _l_(364247)  
    _c_(364249, _n_(364248, "clear_output", lambda: clear_output), wait = True)
    _l_(364250)
    _c_(364253, _n_(364251, "display", lambda: display), _n_(364252, "fig", lambda: fig)) # Reset display
    _l_(364254) # Reset display