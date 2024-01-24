# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70269982/typeerror-init-got-an-unexpected-keyword-argument-iid-while-running-gri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import TimeSeriesSplit
    _l_(360784)

except ImportError:
    pass
try:
    from sklearn.model_selection import KFold
    _l_(360786)

except ImportError:
    pass
try:
    import numpy as np
    _l_(360788)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(360790)

except ImportError:
    pass
try:
    from matplotlib.patches import Patch
    _l_(360792)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(360794)

except ImportError:
    pass
try:
    import sklearn
    _l_(360796)

except ImportError:
    pass
try:
    from sklearn.linear_model import ElasticNet
    _l_(360798)

except ImportError:
    pass
try:
    from sklearn.multioutput import MultiOutputRegressor
    _l_(360800)

except ImportError:
    pass
try:
    from sklearn.model_selection import cross_val_score
    _l_(360802)

except ImportError:
    pass
try:
    from sklearn.model_selection import GridSearchCV
    _l_(360804)

except ImportError:
    pass

_c_(360808, _a_(360807, _a_(360806, _n_(360805, "np", lambda: np), "random"), "seed"), 1338)
_l_(360809)
cmap_data = _a_(360812, _a_(360811, _n_(360810, "plt", lambda: plt), "cm"), "Paired")
_l_(360813)
cmap_cv = _a_(360816, _a_(360815, _n_(360814, "plt", lambda: plt), "cm"), "coolwarm")
_l_(360817)
n_splits = 5
_l_(360818)
try:
    import pandas as pd
    _l_(360820)

except ImportError:
    pass
try:
    import warnings
    _l_(360822)

except ImportError:
    pass
_c_(360825, _a_(360824, _n_(360823, "warnings", lambda: warnings), "filterwarnings"), 'ignore')
_l_(360826)


df = _c_(360830, _a_(360828, _n_(360827, "pd", lambda: pd), "read_csv"), './Gemini_ETHUSD_d.csv', skiprows=1, parse_dates=True, index_col='Date',dtype=_n_(360829, "str", lambda: str))
_l_(360831)
df = _c_(360836, _a_(360835, _c_(360834, _a_(360833, _n_(360832, "df", lambda: df), "sort_index")), "drop"), 'Symbol', axis=1)
_l_(360837)
_c_(360840, _a_(360839, _n_(360838, "df", lambda: df), "head"))
_l_(360841)

def plot_cv_indices(cv, X, y, ax, n_splits, lw=10):
    _l_(360925)

    """Create a sample plot for indices of a cross-validation object."""

    # Generate the training/testing visualizations for each CV split
    for ii, (tr, tt) in _c_(360848, _n_(360842, "enumerate", lambda: enumerate), _c_(360847, _a_(360844, _n_(360843, "cv", lambda: cv), "split"), X=_n_(360845, "X", lambda: X), y=_n_(360846, "y", lambda: y), groups=None)):
        _l_(360880)

        # Fill in indices with the training/test groups
        indices = _c_(360856, _a_(360850, _n_(360849, "np", lambda: np), "array"), [_a_(360852, _n_(360851, "np", lambda: np), "nan")] * _c_(360855, _n_(360853, "len", lambda: len), _n_(360854, "X", lambda: X)))
        _l_(360857)
        _n_(360858, "indices", lambda: indices)[_n_(360859, "tt", lambda: tt)] = 1
        _l_(360860)
        _n_(360861, "indices", lambda: indices)[_n_(360862, "tr", lambda: tr)] = 0
        _l_(360863)

        # Visualize the results
        _c_(360878, _a_(360865, _n_(360864, "ax", lambda: ax), "scatter"), _c_(360870, _n_(360866, "range", lambda: range), _c_(360869, _n_(360867, "len", lambda: len), _n_(360868, "indices", lambda: indices))), [_n_(360871, "ii", lambda: ii) + .5] * _c_(360874, _n_(360872, "len", lambda: len), _n_(360873, "indices", lambda: indices)),
                   c=_n_(360875, "indices", lambda: indices), marker='_', lw=_n_(360876, "lw", lambda: lw), cmap=_n_(360877, "cmap_cv", lambda: cmap_cv),
                   vmin=-.2, vmax=1.2)
        _l_(360879)
    # Plot the data classes and groups at the end
    _c_(360895, _a_(360882, _n_(360881, "ax", lambda: ax), "scatter"), _c_(360887, _n_(360883, "range", lambda: range), _c_(360886, _n_(360884, "len", lambda: len), _n_(360885, "X", lambda: X))), [_n_(360888, "ii", lambda: ii) + 1.5] * _c_(360891, _n_(360889, "len", lambda: len), _n_(360890, "X", lambda: X)),
               c=_n_(360892, "y", lambda: y), marker='_', lw=_n_(360893, "lw", lambda: lw), cmap=_n_(360894, "cmap_data", lambda: cmap_data))
    _l_(360896)

    # Formatting
    yticklabels = _c_(360901, _n_(360897, "list", lambda: list), _c_(360900, _n_(360898, "range", lambda: range), _n_(360899, "n_splits", lambda: n_splits))) + ['class']
    _l_(360902)
    _c_(360911, _a_(360904, _n_(360903, "ax", lambda: ax), "set"), yticks=_c_(360908, _a_(360906, _n_(360905, "np", lambda: np), "arange"), _n_(360907, "n_splits", lambda: n_splits)+2) + .5, yticklabels=_n_(360909, "yticklabels", lambda: yticklabels),
           xlabel='Sample index', ylabel="CV iteration",
           ylim=[_n_(360910, "n_splits", lambda: n_splits)+1.2, -.1], xlim=[0, 100])
    _l_(360912)
    _c_(360921, _a_(360914, _n_(360913, "ax", lambda: ax), "set_title"), _c_(360920, _a_(360915, '{}', "format"), _a_(360919, _c_(360918, _n_(360916, "type", lambda: type), _n_(360917, "cv", lambda: cv)), "__name__")), fontsize=15)
    _l_(360922)
    aux = _n_(360923, "ax", lambda: ax)
    _l_(360924)
    return aux

class BlockingTimeSeriesSplit():
    _l_(360974)

    def __init__(self, n_splits):
        _l_(360929)

        _n_(360926, "self", lambda: self).n_splits = _n_(360927, "n_splits", lambda: n_splits)
        _l_(360928)
    
    def get_n_splits(self, X, y, groups):
        _l_(360933)

        aux = _a_(360931, _n_(360930, "self", lambda: self), "n_splits")
        _l_(360932)
        return aux
    
    def split(self, X, y=None, groups=None):
        _l_(360973)

        n_samples = _c_(360936, _n_(360934, "len", lambda: len), _n_(360935, "X", lambda: X))
        _l_(360937)
        k_fold_size = _n_(360938, "n_samples", lambda: n_samples) // _a_(360940, _n_(360939, "self", lambda: self), "n_splits")
        _l_(360941)
        indices = _c_(360945, _a_(360943, _n_(360942, "np", lambda: np), "arange"), _n_(360944, "n_samples", lambda: n_samples))
        _l_(360946)

        margin = 0
        _l_(360947)
        for i in _c_(360951, _n_(360948, "range", lambda: range), _a_(360950, _n_(360949, "self", lambda: self), "n_splits")):
            _l_(360972)

            start = _n_(360952, "i", lambda: i) * _n_(360953, "k_fold_size", lambda: k_fold_size)
            _l_(360954)
            stop = _n_(360955, "start", lambda: start) + _n_(360956, "k_fold_size", lambda: k_fold_size)
            _l_(360957)
            mid = _c_(360961, _n_(360958, "int", lambda: int), 0.5 * (_n_(360959, "stop", lambda: stop) - _n_(360960, "start", lambda: start))) + _n_(360962, "start", lambda: start)
            _l_(360963)
            yield _n_(360964, "indices", lambda: indices)[_n_(360965, "start", lambda: start): _n_(360966, "mid", lambda: mid)], _n_(360967, "indices", lambda: indices)[_n_(360968, "mid", lambda: mid) + _n_(360969, "margin", lambda: margin): _n_(360970, "stop", lambda: stop)]
            _l_(360971)
STEPS = 9
_l_(360975)
for i in _c_(360979, _a_(360977, _n_(360976, "np", lambda: np), "arange"), 1, _n_(360978, "STEPS", lambda: STEPS)):
    _l_(360991)

    col_name = _c_(360982, _a_(360980, '{}d_Fwd_Close', "format"), _n_(360981, "i", lambda: i))
    _l_(360983)
    _n_(360984, "df", lambda: df)[_n_(360985, "col_name", lambda: col_name)] = _c_(360989, _a_(360987, _n_(360986, "df", lambda: df)['Close'], "shift"), -_n_(360988, "i", lambda: i))
    _l_(360990)
df = _c_(360994, _a_(360993, _n_(360992, "df", lambda: df), "dropna"))
_l_(360995)

Features = 6
_l_(360996)

X = _a_(360998, _n_(360997, "df", lambda: df), "iloc")[:, :_n_(360999, "Features", lambda: Features)]
_l_(361000)
y = _a_(361002, _n_(361001, "df", lambda: df), "iloc")[:, _n_(361003, "Features", lambda: Features):]
_l_(361004)

split = _c_(361009, _n_(361005, "int", lambda: int), _c_(361008, _n_(361006, "len", lambda: len), _n_(361007, "df", lambda: df)) * 0.7)
_l_(361010)

X_train = _n_(361011, "X", lambda: X)[:_n_(361012, "split", lambda: split)]
_l_(361013)
y_train = _n_(361014, "y", lambda: y)[:_n_(361015, "split", lambda: split)]
_l_(361016)

X_test = _n_(361017, "X", lambda: X)[_n_(361018, "split", lambda: split):]
_l_(361019)
y_test = _n_(361020, "y", lambda: y)[_n_(361021, "split", lambda: split):]
_l_(361022)
_c_(361025, _a_(361024, _n_(361023, "X", lambda: X), "head"))
_l_(361026)


def build_model(_alpha, _l1_ratio):
    _l_(361036)

    estimator = _c_(361030, _n_(361027, "ElasticNet", lambda: ElasticNet), alpha=_n_(361028, "_alpha", lambda: _alpha),
        l1_ratio=_n_(361029, "_l1_ratio", lambda: _l1_ratio),
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
    _l_(361031)
    aux = _c_(361034, _n_(361032, "MultiOutputRegressor", lambda: MultiOutputRegressor), _n_(361033, "estimator", lambda: estimator), n_jobs=4)
    _l_(361035)

    return aux
_c_(361041, _a_(361040, _a_(361039, _a_(361038, _n_(361037, "sklearn", lambda: sklearn), "metrics"), "SCORERS"), "keys"))
_l_(361042)


model = _c_(361044, _n_(361043, "build_model", lambda: build_model), _alpha=1.0, _l1_ratio=0.3)
_l_(361045)
tscv = _c_(361047, _n_(361046, "TimeSeriesSplit", lambda: TimeSeriesSplit), n_splits=5)
_l_(361048)
rmse = _c_(361057, _a_(361050, _n_(361049, "np", lambda: np), "sqrt"), -_c_(361056, _n_(361051, "cross_val_score", lambda: cross_val_score), _n_(361052, "model", lambda: model), _n_(361053, "X_train", lambda: X_train), _n_(361054, "y_train", lambda: y_train), cv=_n_(361055, "tscv", lambda: tscv), scoring='neg_mean_squared_error'))
_l_(361058)
R2 = _c_(361064, _n_(361059, "cross_val_score", lambda: cross_val_score), _n_(361060, "model", lambda: model), _n_(361061, "X_train", lambda: X_train), _n_(361062, "y_train", lambda: y_train), cv=_n_(361063, "tscv", lambda: tscv), scoring='r2')
_l_(361065)

_c_(361073, _n_(361066, "print", lambda: print), f"RMSE: {_c_(361069, _a_(361068, _n_(361067, 'rmse', lambda: rmse), 'mean'))} (+/- {_c_(361072, _a_(361071, _n_(361070, 'rmse', lambda: rmse), 'std'))}")
_l_(361074)
_c_(361082, _n_(361075, "print", lambda: print), f"\nR2: {_c_(361078, _a_(361077, _n_(361076, 'R2', lambda: R2), 'mean'))} (+/- {_c_(361081, _a_(361080, _n_(361079, 'R2', lambda: R2), 'std'))}")
_l_(361083)

# Blocking time series splitter

btscv = _c_(361085, _n_(361084, "BlockingTimeSeriesSplit", lambda: BlockingTimeSeriesSplit), n_splits=5)
_l_(361086)
rmse = _c_(361095, _a_(361088, _n_(361087, "np", lambda: np), "sqrt"), -_c_(361094, _n_(361089, "cross_val_score", lambda: cross_val_score), _n_(361090, "model", lambda: model), _n_(361091, "X_train", lambda: X_train), _n_(361092, "y_train", lambda: y_train), cv=_n_(361093, "btscv", lambda: btscv), scoring='neg_mean_squared_error'))
_l_(361096)
R2 = _c_(361102, _n_(361097, "cross_val_score", lambda: cross_val_score), _n_(361098, "model", lambda: model), _n_(361099, "X_train", lambda: X_train), _n_(361100, "y_train", lambda: y_train), cv=_n_(361101, "btscv", lambda: btscv), scoring='r2')
_l_(361103)

_c_(361111, _n_(361104, "print", lambda: print), f"RMSE: {_c_(361107, _a_(361106, _n_(361105, 'rmse', lambda: rmse), 'mean'))} (+/- {_c_(361110, _a_(361109, _n_(361108, 'rmse', lambda: rmse), 'std'))}")
_l_(361112)
_c_(361120, _n_(361113, "print", lambda: print), f"\nR2: {_c_(361116, _a_(361115, _n_(361114, 'R2', lambda: R2), 'mean'))} (+/- {_c_(361119, _a_(361118, _n_(361117, 'R2', lambda: R2), 'std'))}")
_l_(361121)


def plot_grid_search(cv_results, grid_param_1, grid_param_2, name_param_1, name_param_2, best_params):
    _l_(361197)

    
    # Get Test Scores Mean and std for each grid search
    scores_mean = _n_(361122, "cv_results", lambda: cv_results)['mean_test_score']
    _l_(361123)
    scores_mean = _c_(361135, _a_(361128, _c_(361127, _a_(361125, _n_(361124, "np", lambda: np), "array"), _n_(361126, "scores_mean", lambda: scores_mean)), "reshape"), _c_(361131, _n_(361129, "len", lambda: len), _n_(361130, "grid_param_2", lambda: grid_param_2)),_c_(361134, _n_(361132, "len", lambda: len), _n_(361133, "grid_param_1", lambda: grid_param_1)))
    _l_(361136)

    scores_sd = _n_(361137, "cv_results", lambda: cv_results)['std_test_score']
    _l_(361138)
    scores_sd = _c_(361150, _a_(361143, _c_(361142, _a_(361140, _n_(361139, "np", lambda: np), "array"), _n_(361141, "scores_sd", lambda: scores_sd)), "reshape"), _c_(361146, _n_(361144, "len", lambda: len), _n_(361145, "grid_param_2", lambda: grid_param_2)),_c_(361149, _n_(361147, "len", lambda: len), _n_(361148, "grid_param_1", lambda: grid_param_1)))
    _l_(361151)

    # Plot Grid search scores
    _, ax = _c_(361154, _a_(361153, _n_(361152, "plt", lambda: plt), "subplots"), 1,1)
    _l_(361155)

    # Param1 is the X-axis, Param 2 is represented as a different curve (color line)
    for idx, val in _c_(361158, _n_(361156, "enumerate", lambda: enumerate), _n_(361157, "grid_param_2", lambda: grid_param_2)):
        _l_(361170)

        _c_(361168, _a_(361160, _n_(361159, "ax", lambda: ax), "plot"), _n_(361161, "grid_param_1", lambda: grid_param_1), _n_(361162, "scores_mean", lambda: scores_mean)[_n_(361163, "idx", lambda: idx),:], '-o', label= _n_(361164, "name_param_2", lambda: name_param_2) + ': ' + _c_(361167, _n_(361165, "str", lambda: str), _n_(361166, "val", lambda: val)))
        _l_(361169)

    _c_(361174, _a_(361172, _n_(361171, "ax", lambda: ax), "set_title"), f"Grid Search Best Params: {_n_(361173, 'best_params', lambda: best_params)}", fontsize=12, fontweight='medium')
    _l_(361175)
    _c_(361179, _a_(361177, _n_(361176, "ax", lambda: ax), "set_xlabel"), _n_(361178, "name_param_1", lambda: name_param_1), fontsize=12)
    _l_(361180)
    _c_(361183, _a_(361182, _n_(361181, "ax", lambda: ax), "set_ylabel"), 'CV Average Score', fontsize=12)
    _l_(361184)
    _c_(361187, _a_(361186, _n_(361185, "ax", lambda: ax), "legend"), loc="best", fontsize=15)
    _l_(361188)
    _c_(361191, _a_(361190, _n_(361189, "ax", lambda: ax), "grid"), 'on')
    _l_(361192)
    _c_(361195, _a_(361194, _n_(361193, "ax", lambda: ax), "legend"), bbox_to_anchor=(1.02, 1.02))
    _l_(361196)
# Time series splitter

_c_(361202, _a_(361201, _c_(361200, _a_(361199, _n_(361198, "model", lambda: model), "get_params")), "keys"))
_l_(361203)

params = {
    'estimator__alpha':(0.1, 0.3, 0.5, 0.7, 0.9),
    'estimator__l1_ratio':(0.1, 0.3, 0.5, 0.7, 0.9)
}
_l_(361204)

scores = []
_l_(361205)
for i in _c_(361207, _n_(361206, "range", lambda: range), 30):
    _l_(361236)

    model = _c_(361209, _n_(361208, "build_model", lambda: build_model), _alpha=1.0, _l1_ratio=0.3)
    _l_(361210)

    finder = _c_(361215, _n_(361211, "GridSearchCV", lambda: GridSearchCV), estimator=_n_(361212, "model", lambda: model),
        param_grid=_n_(361213, "params", lambda: params),
        scoring='r2',
        n_jobs=4,
        iid=False,
        refit=True,
        cv=_n_(361214, "tscv", lambda: tscv),  # change this to the splitter subject to test
        verbose=1,
        pre_dispatch=8,
        error_score=-999,
        return_train_score=True
        )
    _l_(361216)

    _c_(361221, _a_(361218, _n_(361217, "finder", lambda: finder), "fit"), _n_(361219, "X_train", lambda: X_train), _n_(361220, "y_train", lambda: y_train))
    _l_(361222)

    best_params = _a_(361224, _n_(361223, "finder", lambda: finder), "best_params_")
    _l_(361225)
    best_score = _c_(361229, _n_(361226, "round", lambda: round), _a_(361228, _n_(361227, "finder", lambda: finder), "best_score_"),4)
    _l_(361230)
    _c_(361234, _a_(361232, _n_(361231, "scores", lambda: scores), "append"), _n_(361233, "best_score", lambda: best_score))
    _l_(361235)