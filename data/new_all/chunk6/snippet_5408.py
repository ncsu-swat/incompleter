# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37220843/attributeerror-str-object-has-no-attribute-day-error-when-trying-to-put-day
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = {'days': [],
        'times': []}
_l_(350334)

with _c_(350337, _n_(350335, "open", lambda: open), _n_(350336, "open_file", lambda: open_file)) as in_f:
    _l_(350377)

    reader = _c_(350340, _n_(350338, "DictReader", lambda: DictReader), _n_(350339, "in_f", lambda: in_f))
    _l_(350341)
    for line in _n_(350342, "reader", lambda: reader):
        _l_(350376)

        _c_(350347, _a_(350344, _n_(350343, "data", lambda: data)['day'], "append"), _a_(350346, _n_(350345, "line", lambda: line)['time_received_isoformat'], "day"))
        _l_(350348)
        _c_(350355, _a_(350350, _n_(350349, "data", lambda: data)['time'], "append"), _a_(350352, _n_(350351, "line", lambda: line)['time_received_isoformat'], "hour") * 60 + _a_(350354, _n_(350353, "line", lambda: line)['time_received_isoformat'], "minute"))
        _l_(350356)
        data = _c_(350359, _n_(350357, "DataFrame", lambda: DataFrame), _n_(350358, "data", lambda: data))
        _l_(350360)
        plot = _c_(350364, _a_(350362, _n_(350361, "seaborn", lambda: seaborn), "stripplot"), data=_n_(350363, "data", lambda: data), x='day', y='time')
        _l_(350365)
        _c_(350370, _a_(350369, _c_(350368, _a_(350367, _n_(350366, "plot", lambda: plot), "get_figure")), "savefig"), '/home/jacob/Projects/CIS2302/CW2/ddd_cw2/temporal_graphs/' + 'days_stripplot' + '.png')
        _l_(350371)
        _c_(350374, _a_(350373, _n_(350372, "pyplot", lambda: pyplot), "close"))
        _l_(350375)