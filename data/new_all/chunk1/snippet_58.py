# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48719937/getting-typeerror-reduction-operation-argmax-not-allowed-for-this-dtype-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ExploratoryDataAnalysis as eda
    _l_(405902)

except ImportError:
    pass
try:
    import Preprocessing as processor
    _l_(405904)

except ImportError:
    pass
try:
    import Classification as classify
    _l_(405906)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(405908)

except ImportError:
    pass


data_path = '/Users/username/college/year-4/fyp-credit-card-fraud/data/'
_l_(405909)

if _n_(405910, "__name__", lambda: __name__) == '__main__':
    _l_(405932)

    df = _c_(405914, _a_(405912, _n_(405911, "pd", lambda: pd), "read_csv"), _n_(405913, "data_path", lambda: data_path) + 'creditcard.csv')
    _l_(405915)
    # eda.init(df)
    # eda.check_null_values()
    # eda.view_data()
    # eda.check_target_classes()
    df = _c_(405919, _a_(405917, _n_(405916, "processor", lambda: processor), "noramlize"), _n_(405918, "df", lambda: df))
    _l_(405920)

    X_training, X_testing, y_training, y_testing, X_training_undersampled, X_testing_undersampled, \
    y_training_undersampled, y_testing_undersampled = _c_(405924, _a_(405922, _n_(405921, "processor", lambda: processor), "resample"), _n_(405923, "df", lambda: df))
    _l_(405925)

    best_c_param = _c_(405930, _a_(405927, _n_(405926, "classify", lambda: classify), "print_kfold_scores"), _n_(405928, "X_training_undersampled", lambda: X_training_undersampled), _n_(405929, "y_training_undersampled", lambda: y_training_undersampled))
    _l_(405931)