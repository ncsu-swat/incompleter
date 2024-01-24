# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37220843/attributeerror-str-object-has-no-attribute-day-error-when-trying-to-put-day
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = {'days': [],
        'times': []}
_l_(368517)

with _c_(368520, _n_(368518, "open", lambda: open), _n_(368519, "open_file", lambda: open_file)) as in_f:
    _l_(368560)

    reader = _c_(368523, _n_(368521, "DictReader", lambda: DictReader), _n_(368522, "in_f", lambda: in_f))
    _l_(368524)
    for line in _n_(368525, "reader", lambda: reader):
        _l_(368559)

        _c_(368530, _a_(368527, _n_(368526, "data", lambda: data)['day'], "append"), _a_(368529, _n_(368528, "line", lambda: line)['time_received_isoformat'], "day"))
        _l_(368531)
        _c_(368538, _a_(368533, _n_(368532, "data", lambda: data)['time'], "append"), _a_(368535, _n_(368534, "line", lambda: line)['time_received_isoformat'], "hour") * 60 + _a_(368537, _n_(368536, "line", lambda: line)['time_received_isoformat'], "minute"))
        _l_(368539)
        data = _c_(368542, _n_(368540, "DataFrame", lambda: DataFrame), _n_(368541, "data", lambda: data))
        _l_(368543)
        plot = _c_(368547, _a_(368545, _n_(368544, "seaborn", lambda: seaborn), "stripplot"), data=_n_(368546, "data", lambda: data), x='day', y='time')
        _l_(368548)
        _c_(368553, _a_(368552, _c_(368551, _a_(368550, _n_(368549, "plot", lambda: plot), "get_figure")), "savefig"), '/home/jacob/Projects/CIS2302/CW2/ddd_cw2/temporal_graphs/' + 'days_stripplot' + '.png')
        _l_(368554)
        _c_(368557, _a_(368556, _n_(368555, "pyplot", lambda: pyplot), "close"))
        _l_(368558)