# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65049767/correlation-analysis-using-seaborn-typeerror-float-object-cannot-be-interpr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import seaborn as sb
    _l_(447934)

except ImportError:
    pass
corr = _c_(447937, _a_(447936, _n_(447935, "V", lambda: V), "corr"))
_l_(447938)
ax = _c_(447945, _a_(447940, _n_(447939, "sb", lambda: sb), "heatmap"), _n_(447941, "corr", lambda: corr), 
    vmin=-1, vmax=1, center=0,
    cmap=_c_(447944, _a_(447943, _n_(447942, "sb", lambda: sb), "diverging_palette"), 20, 220, n=200),
    square=True
)
_l_(447946)
_c_(447952, _a_(447948, _n_(447947, "ax", lambda: ax), "set_xticklabels"), _c_(447951, _a_(447950, _n_(447949, "ax", lambda: ax), "get_xticklabels")),
    rotation=45,
    horizontalalignment='right'
);
_l_(447953)