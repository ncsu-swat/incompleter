# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70269982/typeerror-init-got-an-unexpected-keyword-argument-iid-while-running-gri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import TimeSeriesSplit
    _l_(336188)

except ImportError:
    pass
try:
    from sklearn.model_selection import KFold
    _l_(336190)

except ImportError:
    pass
try:
    import numpy as np
    _l_(336192)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(336194)

except ImportError:
    pass
try:
    from matplotlib.patches import Patch
    _l_(336196)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(336198)

except ImportError:
    pass
try:
    import sklearn
    _l_(336200)

except ImportError:
    pass
try:
    from sklearn.linear_model import ElasticNet
    _l_(336202)

except ImportError:
    pass
try:
    from sklearn.multioutput import MultiOutputRegressor
    _l_(336204)

except ImportError:
    pass
try:
    from sklearn.model_selection import cross_val_score
    _l_(336206)

except ImportError:
    pass
try:
    from sklearn.model_selection import GridSearchCV
    _l_(336208)

except ImportError:
    pass

_c_(336212, _a_(336211, _a_(336210, _n_(336209, "np", lambda: np), "random"), "seed"), 1338)
_l_(336213)
cmap_data = _a_(336216, _a_(336215, _n_(336214, "plt", lambda: plt), "cm"), "Paired")
_l_(336217)
cmap_cv = _a_(336220, _a_(336219, _n_(336218, "plt", lambda: plt), "cm"), "coolwarm")
_l_(336221)
n_splits = 5
_l_(336222)
try:
    import pandas as pd
    _l_(336224)

except ImportError:
    pass
try:
    import warnings
    _l_(336226)

except ImportError:
    pass
_c_(336229, _a_(336228, _n_(336227, "warnings", lambda: warnings), "filterwarnings"), 'ignore')
_l_(336230)


df = _c_(336234, _a_(336232, _n_(336231, "pd", lambda: pd), "read_csv"), './Gemini_ETHUSD_d.csv', skiprows=1, parse_dates=True, index_col='Date',dtype=_n_(336233, "str", lambda: str))
_l_(336235)
df = _c_(336240, _a_(336239, _c_(336238, _a_(336237, _n_(336236, "df", lambda: df), "sort_index")), "drop"), 'Symbol', axis=1)
_l_(336241)
_c_(336244, _a_(336243, _n_(336242, "df", lambda: df), "head"))
_l_(336245)

def plot_cv_indices(cv, X, y, ax, n_splits, lw=10):
    _l_(336329)

    """Create a sample plot for indices of a cross-validation object."""

    # Generate the training/testing visualizations for each CV split
    for ii, (tr, tt) in _c_(336252, _n_(336246, "enumerate", lambda: enumerate), _c_(336251, _a_(336248, _n_(336247, "cv", lambda: cv), "split"), X=_n_(336249, "X", lambda: X), y=_n_(336250, "y", lambda: y), groups=None)):
        _l_(336284)

        # Fill in indices with the training/test groups
        indices = _c_(336260, _a_(336254, _n_(336253, "np", lambda: np), "array"), [_a_(336256, _n_(336255, "np", lambda: np), "nan")] * _c_(336259, _n_(336257, "len", lambda: len), _n_(336258, "X", lambda: X)))
        _l_(336261)
        _n_(336262, "indices", lambda: indices)[_n_(336263, "tt", lambda: tt)] = 1
        _l_(336264)
        _n_(336265, "indices", lambda: indices)[_n_(336266, "tr", lambda: tr)] = 0
        _l_(336267)

        # Visualize the results
        _c_(336282, _a_(336269, _n_(336268, "ax", lambda: ax), "scatter"), _c_(336274, _n_(336270, "range", lambda: range), _c_(336273, _n_(336271, "len", lambda: len), _n_(336272, "indices", lambda: indices))), [_n_(336275, "ii", lambda: ii) + .5] * _c_(336278, _n_(336276, "len", lambda: len), _n_(336277, "indices", lambda: indices)),
                   c=_n_(336279, "indices", lambda: indices), marker='_', lw=_n_(336280, "lw", lambda: lw), cmap=_n_(336281, "cmap_cv", lambda: cmap_cv),
                   vmin=-.2, vmax=1.2)
        _l_(336283)
    # Plot the data classes and groups at the end
    _c_(336299, _a_(336286, _n_(336285, "ax", lambda: ax), "scatter"), _c_(336291, _n_(336287, "range", lambda: range), _c_(336290, _n_(336288, "len", lambda: len), _n_(336289, "X", lambda: X))), [_n_(336292, "ii", lambda: ii) + 1.5] * _c_(336295, _n_(336293, "len", lambda: len), _n_(336294, "X", lambda: X)),
               c=_n_(336296, "y", lambda: y), marker='_', lw=_n_(336297, "lw", lambda: lw), cmap=_n_(336298, "cmap_data", lambda: cmap_data))
    _l_(336300)

    # Formatting
    yticklabels = _c_(336305, _n_(336301, "list", lambda: list), _c_(336304, _n_(336302, "range", lambda: range), _n_(336303, "n_splits", lambda: n_splits))) + ['class']
    _l_(336306)
    _c_(336315, _a_(336308, _n_(336307, "ax", lambda: ax), "set"), yticks=_c_(336312, _a_(336310, _n_(336309, "np", lambda: np), "arange"), _n_(336311, "n_splits", lambda: n_splits)+2) + .5, yticklabels=_n_(336313, "yticklabels", lambda: yticklabels),
           xlabel='Sample index', ylabel="CV iteration",
           ylim=[_n_(336314, "n_splits", lambda: n_splits)+1.2, -.1], xlim=[0, 100])
    _l_(336316)
    _c_(336325, _a_(336318, _n_(336317, "ax", lambda: ax), "set_title"), _c_(336324, _a_(336319, '{}', "format"), _a_(336323, _c_(336322, _n_(336320, "type", lambda: type), _n_(336321, "cv", lambda: cv)), "__name__")), fontsize=15)
    _l_(336326)
    aux = _n_(336327, "ax", lambda: ax)
    _l_(336328)
    return aux

class BlockingTimeSeriesSplit():
    _l_(336378)

    def __init__(self, n_splits):
        _l_(336333)

        _n_(336330, "self", lambda: self).n_splits = _n_(336331, "n_splits", lambda: n_splits)
        _l_(336332)
    
    def get_n_splits(self, X, y, groups):
        _l_(336337)

        aux = _a_(336335, _n_(336334, "self", lambda: self), "n_splits")
        _l_(336336)
        return aux
    
    def split(self, X, y=None, groups=None):
        _l_(336377)

        n_samples = _c_(336340, _n_(336338, "len", lambda: len), _n_(336339, "X", lambda: X))
        _l_(336341)
        k_fold_size = _n_(336342, "n_samples", lambda: n_samples) // _a_(336344, _n_(336343, "self", lambda: self), "n_splits")
        _l_(336345)
        indices = _c_(336349, _a_(336347, _n_(336346, "np", lambda: np), "arange"), _n_(336348, "n_samples", lambda: n_samples))
        _l_(336350)

        margin = 0
        _l_(336351)
        for i in _c_(336355, _n_(336352, "range", lambda: range), _a_(336354, _n_(336353, "self", lambda: self), "n_splits")):
            _l_(336376)

            start = _n_(336356, "i", lambda: i) * _n_(336357, "k_fold_size", lambda: k_fold_size)
            _l_(336358)
            stop = _n_(336359, "start", lambda: start) + _n_(336360, "k_fold_size", lambda: k_fold_size)
            _l_(336361)
            mid = _c_(336365, _n_(336362, "int", lambda: int), 0.5 * (_n_(336363, "stop", lambda: stop) - _n_(336364, "start", lambda: start))) + _n_(336366, "start", lambda: start)
            _l_(336367)
            yield _n_(336368, "indices", lambda: indices)[_n_(336369, "start", lambda: start): _n_(336370, "mid", lambda: mid)], _n_(336371, "indices", lambda: indices)[_n_(336372, "mid", lambda: mid) + _n_(336373, "margin", lambda: margin): _n_(336374, "stop", lambda: stop)]
            _l_(336375)
STEPS = 9
_l_(336379)
for i in _c_(336383, _a_(336381, _n_(336380, "np", lambda: np), "arange"), 1, _n_(336382, "STEPS", lambda: STEPS)):
    _l_(336395)

    col_name = _c_(336386, _a_(336384, '{}d_Fwd_Close', "format"), _n_(336385, "i", lambda: i))
    _l_(336387)
    _n_(336388, "df", lambda: df)[_n_(336389, "col_name", lambda: col_name)] = _c_(336393, _a_(336391, _n_(336390, "df", lambda: df)['Close'], "shift"), -_n_(336392, "i", lambda: i))
    _l_(336394)
df = _c_(336398, _a_(336397, _n_(336396, "df", lambda: df), "dropna"))
_l_(336399)

Features = 6
_l_(336400)

X = _a_(336402, _n_(336401, "df", lambda: df), "iloc")[:, :_n_(336403, "Features", lambda: Features)]
_l_(336404)
y = _a_(336406, _n_(336405, "df", lambda: df), "iloc")[:, _n_(336407, "Features", lambda: Features):]
_l_(336408)

split = _c_(336413, _n_(336409, "int", lambda: int), _c_(336412, _n_(336410, "len", lambda: len), _n_(336411, "df", lambda: df)) * 0.7)
_l_(336414)

X_train = _n_(336415, "X", lambda: X)[:_n_(336416, "split", lambda: split)]
_l_(336417)
y_train = _n_(336418, "y", lambda: y)[:_n_(336419, "split", lambda: split)]
_l_(336420)

X_test = _n_(336421, "X", lambda: X)[_n_(336422, "split", lambda: split):]
_l_(336423)
y_test = _n_(336424, "y", lambda: y)[_n_(336425, "split", lambda: split):]
_l_(336426)
_c_(336429, _a_(336428, _n_(336427, "X", lambda: X), "head"))
_l_(336430)


def build_model(_alpha, _l1_ratio):
    _l_(336440)

    estimator = _c_(336434, _n_(336431, "ElasticNet", lambda: ElasticNet), alpha=_n_(336432, "_alpha", lambda: _alpha),
        l1_ratio=_n_(336433, "_l1_ratio", lambda: _l1_ratio),
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
    _l_(336435)
    aux = _c_(336438, _n_(336436, "MultiOutputRegressor", lambda: MultiOutputRegressor), _n_(336437, "estimator", lambda: estimator), n_jobs=4)
    _l_(336439)

    return aux
_c_(336445, _a_(336444, _a_(336443, _a_(336442, _n_(336441, "sklearn", lambda: sklearn), "metrics"), "SCORERS"), "keys"))
_l_(336446)


model = _c_(336448, _n_(336447, "build_model", lambda: build_model), _alpha=1.0, _l1_ratio=0.3)
_l_(336449)
tscv = _c_(336451, _n_(336450, "TimeSeriesSplit", lambda: TimeSeriesSplit), n_splits=5)
_l_(336452)
rmse = _c_(336461, _a_(336454, _n_(336453, "np", lambda: np), "sqrt"), -_c_(336460, _n_(336455, "cross_val_score", lambda: cross_val_score), _n_(336456, "model", lambda: model), _n_(336457, "X_train", lambda: X_train), _n_(336458, "y_train", lambda: y_train), cv=_n_(336459, "tscv", lambda: tscv), scoring='neg_mean_squared_error'))
_l_(336462)
R2 = _c_(336468, _n_(336463, "cross_val_score", lambda: cross_val_score), _n_(336464, "model", lambda: model), _n_(336465, "X_train", lambda: X_train), _n_(336466, "y_train", lambda: y_train), cv=_n_(336467, "tscv", lambda: tscv), scoring='r2')
_l_(336469)

_c_(336477, _n_(336470, "print", lambda: print), f"RMSE: {_c_(336473, _a_(336472, _n_(336471, 'rmse', lambda: rmse), 'mean'))} (+/- {_c_(336476, _a_(336475, _n_(336474, 'rmse', lambda: rmse), 'std'))}")
_l_(336478)
_c_(336486, _n_(336479, "print", lambda: print), f"\nR2: {_c_(336482, _a_(336481, _n_(336480, 'R2', lambda: R2), 'mean'))} (+/- {_c_(336485, _a_(336484, _n_(336483, 'R2', lambda: R2), 'std'))}")
_l_(336487)

# Blocking time series splitter

btscv = _c_(336489, _n_(336488, "BlockingTimeSeriesSplit", lambda: BlockingTimeSeriesSplit), n_splits=5)
_l_(336490)
rmse = _c_(336499, _a_(336492, _n_(336491, "np", lambda: np), "sqrt"), -_c_(336498, _n_(336493, "cross_val_score", lambda: cross_val_score), _n_(336494, "model", lambda: model), _n_(336495, "X_train", lambda: X_train), _n_(336496, "y_train", lambda: y_train), cv=_n_(336497, "btscv", lambda: btscv), scoring='neg_mean_squared_error'))
_l_(336500)
R2 = _c_(336506, _n_(336501, "cross_val_score", lambda: cross_val_score), _n_(336502, "model", lambda: model), _n_(336503, "X_train", lambda: X_train), _n_(336504, "y_train", lambda: y_train), cv=_n_(336505, "btscv", lambda: btscv), scoring='r2')
_l_(336507)

_c_(336515, _n_(336508, "print", lambda: print), f"RMSE: {_c_(336511, _a_(336510, _n_(336509, 'rmse', lambda: rmse), 'mean'))} (+/- {_c_(336514, _a_(336513, _n_(336512, 'rmse', lambda: rmse), 'std'))}")
_l_(336516)
_c_(336524, _n_(336517, "print", lambda: print), f"\nR2: {_c_(336520, _a_(336519, _n_(336518, 'R2', lambda: R2), 'mean'))} (+/- {_c_(336523, _a_(336522, _n_(336521, 'R2', lambda: R2), 'std'))}")
_l_(336525)


def plot_grid_search(cv_results, grid_param_1, grid_param_2, name_param_1, name_param_2, best_params):
    _l_(336601)

    
    # Get Test Scores Mean and std for each grid search
    scores_mean = _n_(336526, "cv_results", lambda: cv_results)['mean_test_score']
    _l_(336527)
    scores_mean = _c_(336539, _a_(336532, _c_(336531, _a_(336529, _n_(336528, "np", lambda: np), "array"), _n_(336530, "scores_mean", lambda: scores_mean)), "reshape"), _c_(336535, _n_(336533, "len", lambda: len), _n_(336534, "grid_param_2", lambda: grid_param_2)),_c_(336538, _n_(336536, "len", lambda: len), _n_(336537, "grid_param_1", lambda: grid_param_1)))
    _l_(336540)

    scores_sd = _n_(336541, "cv_results", lambda: cv_results)['std_test_score']
    _l_(336542)
    scores_sd = _c_(336554, _a_(336547, _c_(336546, _a_(336544, _n_(336543, "np", lambda: np), "array"), _n_(336545, "scores_sd", lambda: scores_sd)), "reshape"), _c_(336550, _n_(336548, "len", lambda: len), _n_(336549, "grid_param_2", lambda: grid_param_2)),_c_(336553, _n_(336551, "len", lambda: len), _n_(336552, "grid_param_1", lambda: grid_param_1)))
    _l_(336555)

    # Plot Grid search scores
    _, ax = _c_(336558, _a_(336557, _n_(336556, "plt", lambda: plt), "subplots"), 1,1)
    _l_(336559)

    # Param1 is the X-axis, Param 2 is represented as a different curve (color line)
    for idx, val in _c_(336562, _n_(336560, "enumerate", lambda: enumerate), _n_(336561, "grid_param_2", lambda: grid_param_2)):
        _l_(336574)

        _c_(336572, _a_(336564, _n_(336563, "ax", lambda: ax), "plot"), _n_(336565, "grid_param_1", lambda: grid_param_1), _n_(336566, "scores_mean", lambda: scores_mean)[_n_(336567, "idx", lambda: idx),:], '-o', label= _n_(336568, "name_param_2", lambda: name_param_2) + ': ' + _c_(336571, _n_(336569, "str", lambda: str), _n_(336570, "val", lambda: val)))
        _l_(336573)

    _c_(336578, _a_(336576, _n_(336575, "ax", lambda: ax), "set_title"), f"Grid Search Best Params: {_n_(336577, 'best_params', lambda: best_params)}", fontsize=12, fontweight='medium')
    _l_(336579)
    _c_(336583, _a_(336581, _n_(336580, "ax", lambda: ax), "set_xlabel"), _n_(336582, "name_param_1", lambda: name_param_1), fontsize=12)
    _l_(336584)
    _c_(336587, _a_(336586, _n_(336585, "ax", lambda: ax), "set_ylabel"), 'CV Average Score', fontsize=12)
    _l_(336588)
    _c_(336591, _a_(336590, _n_(336589, "ax", lambda: ax), "legend"), loc="best", fontsize=15)
    _l_(336592)
    _c_(336595, _a_(336594, _n_(336593, "ax", lambda: ax), "grid"), 'on')
    _l_(336596)
    _c_(336599, _a_(336598, _n_(336597, "ax", lambda: ax), "legend"), bbox_to_anchor=(1.02, 1.02))
    _l_(336600)
# Time series splitter

_c_(336606, _a_(336605, _c_(336604, _a_(336603, _n_(336602, "model", lambda: model), "get_params")), "keys"))
_l_(336607)

params = {
    'estimator__alpha':(0.1, 0.3, 0.5, 0.7, 0.9),
    'estimator__l1_ratio':(0.1, 0.3, 0.5, 0.7, 0.9)
}
_l_(336608)

scores = []
_l_(336609)
for i in _c_(336611, _n_(336610, "range", lambda: range), 30):
    _l_(336640)

    model = _c_(336613, _n_(336612, "build_model", lambda: build_model), _alpha=1.0, _l1_ratio=0.3)
    _l_(336614)

    finder = _c_(336619, _n_(336615, "GridSearchCV", lambda: GridSearchCV), estimator=_n_(336616, "model", lambda: model),
        param_grid=_n_(336617, "params", lambda: params),
        scoring='r2',
        n_jobs=4,
        iid=False,
        refit=True,
        cv=_n_(336618, "tscv", lambda: tscv),  # change this to the splitter subject to test
        verbose=1,
        pre_dispatch=8,
        error_score=-999,
        return_train_score=True
        )
    _l_(336620)

    _c_(336625, _a_(336622, _n_(336621, "finder", lambda: finder), "fit"), _n_(336623, "X_train", lambda: X_train), _n_(336624, "y_train", lambda: y_train))
    _l_(336626)

    best_params = _a_(336628, _n_(336627, "finder", lambda: finder), "best_params_")
    _l_(336629)
    best_score = _c_(336633, _n_(336630, "round", lambda: round), _a_(336632, _n_(336631, "finder", lambda: finder), "best_score_"),4)
    _l_(336634)
    _c_(336638, _a_(336636, _n_(336635, "scores", lambda: scores), "append"), _n_(336637, "best_score", lambda: best_score))
    _l_(336639)