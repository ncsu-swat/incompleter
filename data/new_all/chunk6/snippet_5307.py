# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70269982/typeerror-init-got-an-unexpected-keyword-argument-iid-while-running-gri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import TimeSeriesSplit
    _l_(349115)

except ImportError:
    pass
try:
    from sklearn.model_selection import KFold
    _l_(349117)

except ImportError:
    pass
try:
    import numpy as np
    _l_(349119)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(349121)

except ImportError:
    pass
try:
    from matplotlib.patches import Patch
    _l_(349123)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(349125)

except ImportError:
    pass
try:
    import sklearn
    _l_(349127)

except ImportError:
    pass
try:
    from sklearn.linear_model import ElasticNet
    _l_(349129)

except ImportError:
    pass
try:
    from sklearn.multioutput import MultiOutputRegressor
    _l_(349131)

except ImportError:
    pass
try:
    from sklearn.model_selection import cross_val_score
    _l_(349133)

except ImportError:
    pass
try:
    from sklearn.model_selection import GridSearchCV
    _l_(349135)

except ImportError:
    pass

_c_(349139, _a_(349138, _a_(349137, _n_(349136, "np", lambda: np), "random"), "seed"), 1338)
_l_(349140)
cmap_data = _a_(349143, _a_(349142, _n_(349141, "plt", lambda: plt), "cm"), "Paired")
_l_(349144)
cmap_cv = _a_(349147, _a_(349146, _n_(349145, "plt", lambda: plt), "cm"), "coolwarm")
_l_(349148)
n_splits = 5
_l_(349149)
try:
    import pandas as pd
    _l_(349151)

except ImportError:
    pass
try:
    import warnings
    _l_(349153)

except ImportError:
    pass
_c_(349156, _a_(349155, _n_(349154, "warnings", lambda: warnings), "filterwarnings"), 'ignore')
_l_(349157)


df = _c_(349161, _a_(349159, _n_(349158, "pd", lambda: pd), "read_csv"), './Gemini_ETHUSD_d.csv', skiprows=1, parse_dates=True, index_col='Date',dtype=_n_(349160, "str", lambda: str))
_l_(349162)
df = _c_(349167, _a_(349166, _c_(349165, _a_(349164, _n_(349163, "df", lambda: df), "sort_index")), "drop"), 'Symbol', axis=1)
_l_(349168)
_c_(349171, _a_(349170, _n_(349169, "df", lambda: df), "head"))
_l_(349172)

def plot_cv_indices(cv, X, y, ax, n_splits, lw=10):
    _l_(349256)

    """Create a sample plot for indices of a cross-validation object."""

    # Generate the training/testing visualizations for each CV split
    for ii, (tr, tt) in _c_(349179, _n_(349173, "enumerate", lambda: enumerate), _c_(349178, _a_(349175, _n_(349174, "cv", lambda: cv), "split"), X=_n_(349176, "X", lambda: X), y=_n_(349177, "y", lambda: y), groups=None)):
        _l_(349211)

        # Fill in indices with the training/test groups
        indices = _c_(349187, _a_(349181, _n_(349180, "np", lambda: np), "array"), [_a_(349183, _n_(349182, "np", lambda: np), "nan")] * _c_(349186, _n_(349184, "len", lambda: len), _n_(349185, "X", lambda: X)))
        _l_(349188)
        _n_(349189, "indices", lambda: indices)[_n_(349190, "tt", lambda: tt)] = 1
        _l_(349191)
        _n_(349192, "indices", lambda: indices)[_n_(349193, "tr", lambda: tr)] = 0
        _l_(349194)

        # Visualize the results
        _c_(349209, _a_(349196, _n_(349195, "ax", lambda: ax), "scatter"), _c_(349201, _n_(349197, "range", lambda: range), _c_(349200, _n_(349198, "len", lambda: len), _n_(349199, "indices", lambda: indices))), [_n_(349202, "ii", lambda: ii) + .5] * _c_(349205, _n_(349203, "len", lambda: len), _n_(349204, "indices", lambda: indices)),
                   c=_n_(349206, "indices", lambda: indices), marker='_', lw=_n_(349207, "lw", lambda: lw), cmap=_n_(349208, "cmap_cv", lambda: cmap_cv),
                   vmin=-.2, vmax=1.2)
        _l_(349210)
    # Plot the data classes and groups at the end
    _c_(349226, _a_(349213, _n_(349212, "ax", lambda: ax), "scatter"), _c_(349218, _n_(349214, "range", lambda: range), _c_(349217, _n_(349215, "len", lambda: len), _n_(349216, "X", lambda: X))), [_n_(349219, "ii", lambda: ii) + 1.5] * _c_(349222, _n_(349220, "len", lambda: len), _n_(349221, "X", lambda: X)),
               c=_n_(349223, "y", lambda: y), marker='_', lw=_n_(349224, "lw", lambda: lw), cmap=_n_(349225, "cmap_data", lambda: cmap_data))
    _l_(349227)

    # Formatting
    yticklabels = _c_(349232, _n_(349228, "list", lambda: list), _c_(349231, _n_(349229, "range", lambda: range), _n_(349230, "n_splits", lambda: n_splits))) + ['class']
    _l_(349233)
    _c_(349242, _a_(349235, _n_(349234, "ax", lambda: ax), "set"), yticks=_c_(349239, _a_(349237, _n_(349236, "np", lambda: np), "arange"), _n_(349238, "n_splits", lambda: n_splits)+2) + .5, yticklabels=_n_(349240, "yticklabels", lambda: yticklabels),
           xlabel='Sample index', ylabel="CV iteration",
           ylim=[_n_(349241, "n_splits", lambda: n_splits)+1.2, -.1], xlim=[0, 100])
    _l_(349243)
    _c_(349252, _a_(349245, _n_(349244, "ax", lambda: ax), "set_title"), _c_(349251, _a_(349246, '{}', "format"), _a_(349250, _c_(349249, _n_(349247, "type", lambda: type), _n_(349248, "cv", lambda: cv)), "__name__")), fontsize=15)
    _l_(349253)
    aux = _n_(349254, "ax", lambda: ax)
    _l_(349255)
    return aux

class BlockingTimeSeriesSplit():
    _l_(349305)

    def __init__(self, n_splits):
        _l_(349260)

        _n_(349257, "self", lambda: self).n_splits = _n_(349258, "n_splits", lambda: n_splits)
        _l_(349259)
    
    def get_n_splits(self, X, y, groups):
        _l_(349264)

        aux = _a_(349262, _n_(349261, "self", lambda: self), "n_splits")
        _l_(349263)
        return aux
    
    def split(self, X, y=None, groups=None):
        _l_(349304)

        n_samples = _c_(349267, _n_(349265, "len", lambda: len), _n_(349266, "X", lambda: X))
        _l_(349268)
        k_fold_size = _n_(349269, "n_samples", lambda: n_samples) // _a_(349271, _n_(349270, "self", lambda: self), "n_splits")
        _l_(349272)
        indices = _c_(349276, _a_(349274, _n_(349273, "np", lambda: np), "arange"), _n_(349275, "n_samples", lambda: n_samples))
        _l_(349277)

        margin = 0
        _l_(349278)
        for i in _c_(349282, _n_(349279, "range", lambda: range), _a_(349281, _n_(349280, "self", lambda: self), "n_splits")):
            _l_(349303)

            start = _n_(349283, "i", lambda: i) * _n_(349284, "k_fold_size", lambda: k_fold_size)
            _l_(349285)
            stop = _n_(349286, "start", lambda: start) + _n_(349287, "k_fold_size", lambda: k_fold_size)
            _l_(349288)
            mid = _c_(349292, _n_(349289, "int", lambda: int), 0.5 * (_n_(349290, "stop", lambda: stop) - _n_(349291, "start", lambda: start))) + _n_(349293, "start", lambda: start)
            _l_(349294)
            yield _n_(349295, "indices", lambda: indices)[_n_(349296, "start", lambda: start): _n_(349297, "mid", lambda: mid)], _n_(349298, "indices", lambda: indices)[_n_(349299, "mid", lambda: mid) + _n_(349300, "margin", lambda: margin): _n_(349301, "stop", lambda: stop)]
            _l_(349302)
STEPS = 9
_l_(349306)
for i in _c_(349310, _a_(349308, _n_(349307, "np", lambda: np), "arange"), 1, _n_(349309, "STEPS", lambda: STEPS)):
    _l_(349322)

    col_name = _c_(349313, _a_(349311, '{}d_Fwd_Close', "format"), _n_(349312, "i", lambda: i))
    _l_(349314)
    _n_(349315, "df", lambda: df)[_n_(349316, "col_name", lambda: col_name)] = _c_(349320, _a_(349318, _n_(349317, "df", lambda: df)['Close'], "shift"), -_n_(349319, "i", lambda: i))
    _l_(349321)
df = _c_(349325, _a_(349324, _n_(349323, "df", lambda: df), "dropna"))
_l_(349326)

Features = 6
_l_(349327)

X = _a_(349329, _n_(349328, "df", lambda: df), "iloc")[:, :_n_(349330, "Features", lambda: Features)]
_l_(349331)
y = _a_(349333, _n_(349332, "df", lambda: df), "iloc")[:, _n_(349334, "Features", lambda: Features):]
_l_(349335)

split = _c_(349340, _n_(349336, "int", lambda: int), _c_(349339, _n_(349337, "len", lambda: len), _n_(349338, "df", lambda: df)) * 0.7)
_l_(349341)

X_train = _n_(349342, "X", lambda: X)[:_n_(349343, "split", lambda: split)]
_l_(349344)
y_train = _n_(349345, "y", lambda: y)[:_n_(349346, "split", lambda: split)]
_l_(349347)

X_test = _n_(349348, "X", lambda: X)[_n_(349349, "split", lambda: split):]
_l_(349350)
y_test = _n_(349351, "y", lambda: y)[_n_(349352, "split", lambda: split):]
_l_(349353)
_c_(349356, _a_(349355, _n_(349354, "X", lambda: X), "head"))
_l_(349357)


def build_model(_alpha, _l1_ratio):
    _l_(349367)

    estimator = _c_(349361, _n_(349358, "ElasticNet", lambda: ElasticNet), alpha=_n_(349359, "_alpha", lambda: _alpha),
        l1_ratio=_n_(349360, "_l1_ratio", lambda: _l1_ratio),
        fit_intercept=True,
        normalize=False,
        precompute=False,
        max_iter=16,
        copy_X=True,
        tol=0.1,
        warm_start=False,
        positive=False,
        random_state=None,
        selection='random'
    )
    _l_(349362)
    aux = _c_(349365, _n_(349363, "MultiOutputRegressor", lambda: MultiOutputRegressor), _n_(349364, "estimator", lambda: estimator), n_jobs=4)
    _l_(349366)

    return aux
_c_(349372, _a_(349371, _a_(349370, _a_(349369, _n_(349368, "sklearn", lambda: sklearn), "metrics"), "SCORERS"), "keys"))
_l_(349373)


model = _c_(349375, _n_(349374, "build_model", lambda: build_model), _alpha=1.0, _l1_ratio=0.3)
_l_(349376)
tscv = _c_(349378, _n_(349377, "TimeSeriesSplit", lambda: TimeSeriesSplit), n_splits=5)
_l_(349379)
rmse = _c_(349388, _a_(349381, _n_(349380, "np", lambda: np), "sqrt"), -_c_(349387, _n_(349382, "cross_val_score", lambda: cross_val_score), _n_(349383, "model", lambda: model), _n_(349384, "X_train", lambda: X_train), _n_(349385, "y_train", lambda: y_train), cv=_n_(349386, "tscv", lambda: tscv), scoring='neg_mean_squared_error'))
_l_(349389)
R2 = _c_(349395, _n_(349390, "cross_val_score", lambda: cross_val_score), _n_(349391, "model", lambda: model), _n_(349392, "X_train", lambda: X_train), _n_(349393, "y_train", lambda: y_train), cv=_n_(349394, "tscv", lambda: tscv), scoring='r2')
_l_(349396)

_c_(349404, _n_(349397, "print", lambda: print), f"RMSE: {_c_(349400, _a_(349399, _n_(349398, 'rmse', lambda: rmse), 'mean'))} (+/- {_c_(349403, _a_(349402, _n_(349401, 'rmse', lambda: rmse), 'std'))}")
_l_(349405)
_c_(349413, _n_(349406, "print", lambda: print), f"\nR2: {_c_(349409, _a_(349408, _n_(349407, 'R2', lambda: R2), 'mean'))} (+/- {_c_(349412, _a_(349411, _n_(349410, 'R2', lambda: R2), 'std'))}")
_l_(349414)

# Blocking time series splitter

btscv = _c_(349416, _n_(349415, "BlockingTimeSeriesSplit", lambda: BlockingTimeSeriesSplit), n_splits=5)
_l_(349417)
rmse = _c_(349426, _a_(349419, _n_(349418, "np", lambda: np), "sqrt"), -_c_(349425, _n_(349420, "cross_val_score", lambda: cross_val_score), _n_(349421, "model", lambda: model), _n_(349422, "X_train", lambda: X_train), _n_(349423, "y_train", lambda: y_train), cv=_n_(349424, "btscv", lambda: btscv), scoring='neg_mean_squared_error'))
_l_(349427)
R2 = _c_(349433, _n_(349428, "cross_val_score", lambda: cross_val_score), _n_(349429, "model", lambda: model), _n_(349430, "X_train", lambda: X_train), _n_(349431, "y_train", lambda: y_train), cv=_n_(349432, "btscv", lambda: btscv), scoring='r2')
_l_(349434)

_c_(349442, _n_(349435, "print", lambda: print), f"RMSE: {_c_(349438, _a_(349437, _n_(349436, 'rmse', lambda: rmse), 'mean'))} (+/- {_c_(349441, _a_(349440, _n_(349439, 'rmse', lambda: rmse), 'std'))}")
_l_(349443)
_c_(349451, _n_(349444, "print", lambda: print), f"\nR2: {_c_(349447, _a_(349446, _n_(349445, 'R2', lambda: R2), 'mean'))} (+/- {_c_(349450, _a_(349449, _n_(349448, 'R2', lambda: R2), 'std'))}")
_l_(349452)


def plot_grid_search(cv_results, grid_param_1, grid_param_2, name_param_1, name_param_2, best_params):
    _l_(349528)

    
    # Get Test Scores Mean and std for each grid search
    scores_mean = _n_(349453, "cv_results", lambda: cv_results)['mean_test_score']
    _l_(349454)
    scores_mean = _c_(349466, _a_(349459, _c_(349458, _a_(349456, _n_(349455, "np", lambda: np), "array"), _n_(349457, "scores_mean", lambda: scores_mean)), "reshape"), _c_(349462, _n_(349460, "len", lambda: len), _n_(349461, "grid_param_2", lambda: grid_param_2)),_c_(349465, _n_(349463, "len", lambda: len), _n_(349464, "grid_param_1", lambda: grid_param_1)))
    _l_(349467)

    scores_sd = _n_(349468, "cv_results", lambda: cv_results)['std_test_score']
    _l_(349469)
    scores_sd = _c_(349481, _a_(349474, _c_(349473, _a_(349471, _n_(349470, "np", lambda: np), "array"), _n_(349472, "scores_sd", lambda: scores_sd)), "reshape"), _c_(349477, _n_(349475, "len", lambda: len), _n_(349476, "grid_param_2", lambda: grid_param_2)),_c_(349480, _n_(349478, "len", lambda: len), _n_(349479, "grid_param_1", lambda: grid_param_1)))
    _l_(349482)

    # Plot Grid search scores
    _, ax = _c_(349485, _a_(349484, _n_(349483, "plt", lambda: plt), "subplots"), 1,1)
    _l_(349486)

    # Param1 is the X-axis, Param 2 is represented as a different curve (color line)
    for idx, val in _c_(349489, _n_(349487, "enumerate", lambda: enumerate), _n_(349488, "grid_param_2", lambda: grid_param_2)):
        _l_(349501)

        _c_(349499, _a_(349491, _n_(349490, "ax", lambda: ax), "plot"), _n_(349492, "grid_param_1", lambda: grid_param_1), _n_(349493, "scores_mean", lambda: scores_mean)[_n_(349494, "idx", lambda: idx),:], '-o', label= _n_(349495, "name_param_2", lambda: name_param_2) + ': ' + _c_(349498, _n_(349496, "str", lambda: str), _n_(349497, "val", lambda: val)))
        _l_(349500)

    _c_(349505, _a_(349503, _n_(349502, "ax", lambda: ax), "set_title"), f"Grid Search Best Params: {_n_(349504, 'best_params', lambda: best_params)}", fontsize=12, fontweight='medium')
    _l_(349506)
    _c_(349510, _a_(349508, _n_(349507, "ax", lambda: ax), "set_xlabel"), _n_(349509, "name_param_1", lambda: name_param_1), fontsize=12)
    _l_(349511)
    _c_(349514, _a_(349513, _n_(349512, "ax", lambda: ax), "set_ylabel"), 'CV Average Score', fontsize=12)
    _l_(349515)
    _c_(349518, _a_(349517, _n_(349516, "ax", lambda: ax), "legend"), loc="best", fontsize=15)
    _l_(349519)
    _c_(349522, _a_(349521, _n_(349520, "ax", lambda: ax), "grid"), 'on')
    _l_(349523)
    _c_(349526, _a_(349525, _n_(349524, "ax", lambda: ax), "legend"), bbox_to_anchor=(1.02, 1.02))
    _l_(349527)
# Time series splitter

_c_(349533, _a_(349532, _c_(349531, _a_(349530, _n_(349529, "model", lambda: model), "get_params")), "keys"))
_l_(349534)

params = {
    'estimator__alpha':(0.1, 0.3, 0.5, 0.7, 0.9),
    'estimator__l1_ratio':(0.1, 0.3, 0.5, 0.7, 0.9)
}
_l_(349535)

scores = []
_l_(349536)
for i in _c_(349538, _n_(349537, "range", lambda: range), 30):
    _l_(349567)

    model = _c_(349540, _n_(349539, "build_model", lambda: build_model), _alpha=1.0, _l1_ratio=0.3)
    _l_(349541)

    finder = _c_(349546, _n_(349542, "GridSearchCV", lambda: GridSearchCV), estimator=_n_(349543, "model", lambda: model),
        param_grid=_n_(349544, "params", lambda: params),
        scoring='r2',
        n_jobs=4,
        iid=False,
        refit=True,
        cv=_n_(349545, "tscv", lambda: tscv),  # change this to the splitter subject to test
        verbose=1,
        pre_dispatch=8,
        error_score=-999,
        return_train_score=True
        )
    _l_(349547)

    _c_(349552, _a_(349549, _n_(349548, "finder", lambda: finder), "fit"), _n_(349550, "X_train", lambda: X_train), _n_(349551, "y_train", lambda: y_train))
    _l_(349553)

    best_params = _a_(349555, _n_(349554, "finder", lambda: finder), "best_params_")
    _l_(349556)
    best_score = _c_(349560, _n_(349557, "round", lambda: round), _a_(349559, _n_(349558, "finder", lambda: finder), "best_score_"),4)
    _l_(349561)
    _c_(349565, _a_(349563, _n_(349562, "scores", lambda: scores), "append"), _n_(349564, "best_score", lambda: best_score))
    _l_(349566)