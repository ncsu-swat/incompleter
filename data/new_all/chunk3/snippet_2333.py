# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50236372/typeerror-expected-binary-or-unicode-string-got-0-0
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(530074)

except ImportError:
    pass
try:
    import tarfile
    _l_(530076)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(530078)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(530080)

except ImportError:
    pass
try:
    import numpy as np
    _l_(530082)

except ImportError:
    pass
try:
    from six.moves import urllib
    _l_(530084)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(530086)

except ImportError:
    pass
try:
    from sklearn.preprocessing import LabelBinarizer
    _l_(530088)

except ImportError:
    pass
try:
    from sklearn.preprocessing import StandardScaler
    _l_(530090)

except ImportError:
    pass
try:
    from sklearn.preprocessing import Imputer
    _l_(530092)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(530094)

except ImportError:
    pass
try:
    from sklearn.utils import shuffle
    _l_(530096)

except ImportError:
    pass

HOME_PATH = _c_(530099, _a_(530098, _n_(530097, "os", lambda: os), "getcwd"))
_l_(530100)

""" load the csv file with the lending data and convert to tensors """


def convert_duration(s):
    _l_(530127)

    try:
        _l_(530126)

        if _c_(530104, _a_(530102, _n_(530101, "pd", lambda: pd), "isnull"), _n_(530103, "s", lambda: s)):
            _l_(530118)

            aux = _n_(530105, "s", lambda: s)
            _l_(530106)
            return aux
        elif _n_(530107, "s", lambda: s)[0] == '<':
            _l_(530117)

            aux = 0.0
            _l_(530108)
            return aux
        elif _n_(530109, "s", lambda: s)[:2] == '10':
            _l_(530116)

            aux = 10.0
            _l_(530110)
            return aux
        else:
            aux = _c_(530114, _a_(530112, _n_(530111, "np", lambda: np), "float"), _n_(530113, "s", lambda: s)[0])
            _l_(530115)
            return aux
    except _n_(530119, "TypeError", lambda: TypeError):
        _l_(530125)

        aux = _c_(530123, _a_(530121, _n_(530120, "np", lambda: np), "float64"), _n_(530122, "s", lambda: s))
        _l_(530124)
        return aux


def load_data(file_name):
    _l_(530239)

    csv_path = _c_(530133, _a_(530130, _a_(530129, _n_(530128, "os", lambda: os), "path"), "join"), _n_(530131, "HOME_PATH", lambda: HOME_PATH), _n_(530132, "file_name", lambda: file_name))
    _l_(530134)
    csv_data =  _c_(530144, _a_(530136, _n_(530135, "pd", lambda: pd), "read_csv"), _n_(530137, "csv_path", lambda: csv_path), encoding = "ISO-8859-1", dtype={'desc': _a_(530139, _n_(530138, "np", lambda: np), "str"), 'verification_status_joint': _a_(530141, _n_(530140, "np", lambda: np), "str"), 'loan_status': _a_(530143, _n_(530142, "np", lambda: np), "str")},low_memory=False, na_values=[])
    _l_(530145)
    loans = _a_(530147, _n_(530146, "csv_data", lambda: csv_data), "loc")[_c_(530150, _a_(530149, _n_(530148, "csv_data", lambda: csv_data)['loan_status'], "isin"), ['Fully Paid', 'Charged Off'])]  # Sort out only fully Paid (Paid) and Charged Off (Default)
    _l_(530151)  # Sort out only fully Paid (Paid) and Charged Off (Default)
    _n_(530152, "loans", lambda: loans)['loan_status'] = _c_(530159, _a_(530154, _n_(530153, "loans", lambda: loans)['loan_status'], "apply"), lambda s: _c_(530158, _a_(530156, _n_(530155, "np", lambda: np), "int"), _n_(530157, "s", lambda: s) == 'Fully Paid')) # Convert to boolean integer
    _l_(530160) # Convert to boolean integer
    # Drop Columns with one distinct data field
    for col in _a_(530162, _n_(530161, "loans", lambda: loans), "columns"):
        _l_(530169)

        if _c_(530166, _a_(530165, _n_(530163, "loans", lambda: loans)[_n_(530164, "col", lambda: col)], "nunique")) == 1:
            _l_(530168)

            del loans[col]
            _l_(530167)
    for col in _a_(530171, _n_(530170, "loans", lambda: loans), "columns"):
        _l_(530184)

        if (_c_(530177, _a_(530176, _c_(530175, _a_(530174, _n_(530172, "loans", lambda: loans)[_n_(530173, "col", lambda: col)], "notnull")), "sum")) / _c_(530181, _n_(530178, "len", lambda: len), _a_(530180, _n_(530179, "loans", lambda: loans), "index"))) < 0.1 :
            _l_(530183)

            del loans[col]
            _l_(530182)

    # Remove all irrelevant columns & hifg prediction columns based on pure descetion
    _c_(530187, _a_(530186, _n_(530185, "loans", lambda: loans), "drop"), labels=['id', 'member_id', 'grade', 'sub_grade', 'last_credit_pull_d', 'emp_title', 'url', 'desc', 'title', 'issue_d', 'earliest_cr_line', 'last_pymnt_d','addr_state'], axis=1, inplace=True)
    _l_(530188)

    # Process the text based variables
    # Term
    _n_(530189, "loans", lambda: loans)['term'] = _c_(530196, _a_(530191, _n_(530190, "loans", lambda: loans)['term'], "apply"), lambda s:_c_(530195, _a_(530193, _n_(530192, "np", lambda: np), "float"), _n_(530194, "s", lambda: s)[1:3]))
    _l_(530197)

    _n_(530198, "loans", lambda: loans)['emp_length'] = _c_(530204, _a_(530200, _n_(530199, "loans", lambda: loans)['emp_length'], "apply"), lambda s: _c_(530203, _n_(530201, "convert_duration", lambda: convert_duration), _n_(530202, "s", lambda: s)))
    _l_(530205)

    #change zip code to just the first 3 significant digits
    _n_(530206, "loans", lambda: loans)['zip_code'] = _c_(530213, _a_(530208, _n_(530207, "loans", lambda: loans)['zip_code'], "apply"), lambda s:_c_(530212, _a_(530210, _n_(530209, "np", lambda: np), "float"), _n_(530211, "s", lambda: s)[:3]))
    _l_(530214)
    _c_(530217, _a_(530216, _n_(530215, "loans", lambda: loans), "fillna"), '',inplace=True)
    _l_(530218)
    loan_data = _c_(530221, _n_(530219, "shuffle", lambda: shuffle), _n_(530220, "loans", lambda: loans))
    _l_(530222)
    X = _c_(530225, _a_(530224, _n_(530223, "loan_data", lambda: loan_data), "drop"), labels=['loan_status'], axis=1)
    _l_(530226)
    Y = _n_(530227, "loan_data", lambda: loan_data)['loan_status']
    _l_(530228)
    ## consider processing tensorflow feature columns here and return as one response and standardise at one
    X_train, X_test, Y_train, Y_test = _c_(530232, _n_(530229, "train_test_split", lambda: train_test_split), _n_(530230, "X", lambda: X), _n_(530231, "Y", lambda: Y), test_size=0.2, random_state=42)
    _l_(530233)
    aux = (_n_(530234, "X_train", lambda: X_train), _n_(530235, "Y_train", lambda: Y_train)), (_n_(530236, "X_test", lambda: X_test), _n_(530237, "Y_test", lambda: Y_test))
    _l_(530238)
    # scaler = StandardScaler()
    # X_train = scaler.fit_transform(X_train)
    # X_test = scaler.fit_transform(X_test)
    return aux



def my_input_fn(features, labels, batch_size , shuffle=True):
    _l_(530265)

    # consider changing categorical columns and all
    dataset = _c_(530248, _a_(530243, _a_(530242, _a_(530241, _n_(530240, "tf", lambda: tf), "data"), "Dataset"), "from_tensor_slices"), (_c_(530246, _n_(530244, "dict", lambda: dict), _n_(530245, "features", lambda: features)), _n_(530247, "labels", lambda: labels)))
    _l_(530249)
    dataset = _c_(530257, _a_(530255, _c_(530254, _a_(530253, _c_(530252, _a_(530251, _n_(530250, "dataset", lambda: dataset), "shuffle"), buffer_size=100000), "repeat"), count=None), "batch"), _n_(530256, "batch_size", lambda: batch_size))
    _l_(530258)
    aux = _c_(530263, _a_(530262, _c_(530261, _a_(530260, _n_(530259, "dataset", lambda: dataset), "make_one_shot_iterator")), "get_next"))
    _l_(530264)
    return aux

def my_eval_fn(features, labels, batch_size , shuffle=True):
    _l_(530285)

    # consider changing categorical columns and all
    dataset = _c_(530272, _a_(530269, _a_(530268, _a_(530267, _n_(530266, "tf", lambda: tf), "data"), "Dataset"), "from_tensor_slices"), (_n_(530270, "features", lambda: features),_n_(530271, "labels", lambda: labels)))
    _l_(530273)
    dataset = _c_(530277, _a_(530275, _n_(530274, "dataset", lambda: dataset), "batch"), _n_(530276, "batch_size", lambda: batch_size))
    _l_(530278)
    aux = _c_(530283, _a_(530282, _c_(530281, _a_(530280, _n_(530279, "dataset", lambda: dataset), "make_one_shot_iterator")), "get_next"))
    _l_(530284)
    return aux



#Start on calls to make data available

(X_train, Y_train), (X_test, Y_test) = _c_(530287, _n_(530286, "load_data", lambda: load_data), "loan_data.csv")
_l_(530288)
_c_(530293, _n_(530289, "print", lambda: print), _c_(530292, _n_(530290, "dict", lambda: dict), _n_(530291, "X_train", lambda: X_train)))
_l_(530294)

my_feature_columns = []
_l_(530295)
numerical_columns = ['loan_amnt',
 'funded_amnt',
 'funded_amnt_inv',
 'int_rate',
 'installment',
 'annual_inc',
 'dti',
 'delinq_2yrs',
 'inq_last_6mths',
 'mths_since_last_delinq',
 'mths_since_last_record',
 'open_acc',
 'pub_rec',
 'revol_bal',
 'revol_util',
 'total_acc',
 'total_pymnt',
 'total_pymnt_inv',
 'total_rec_prncp',
 'total_rec_int',
 'total_rec_late_fee',
 'recoveries',
 'collection_recovery_fee',
 'last_pymnt_amnt',
 'collections_12_mths_ex_med',
 'mths_since_last_major_derog',
 'acc_now_delinq',
 'tot_coll_amt',
 'tot_cur_bal',
 'total_rev_hi_lim']
_l_(530296)

categorical_columns = ['home_ownership',
 'verification_status',
 'pymnt_plan',
 'purpose',
 'initial_list_status',
 'application_type']
_l_(530297)

for key in _n_(530298, "numerical_columns", lambda: numerical_columns):
    _l_(530308)

    _c_(530306, _a_(530300, _n_(530299, "my_feature_columns", lambda: my_feature_columns), "append"), _c_(530305, _a_(530303, _a_(530302, _n_(530301, "tf", lambda: tf), "feature_column"), "numeric_column"), key=_n_(530304, "key", lambda: key)))
    _l_(530307)

for key in _n_(530309, "categorical_columns", lambda: categorical_columns):
    _l_(530319)

    _c_(530317, _a_(530311, _n_(530310, "my_feature_columns", lambda: my_feature_columns), "append"), _c_(530316, _a_(530314, _a_(530313, _n_(530312, "tf", lambda: tf), "feature_column"), "categorical_column_with_hash_bucket"), key=_n_(530315, "key", lambda: key), hash_bucket_size = 10))
    _l_(530318)

classifier = _c_(530324, _a_(530322, _a_(530321, _n_(530320, "tf", lambda: tf), "estimator"), "LinearClassifier"), feature_columns=_n_(530323, "my_feature_columns", lambda: my_feature_columns)
        )
_l_(530325)

_c_(530332, _a_(530327, _n_(530326, "classifier", lambda: classifier), "train"), input_fn=lambda:_c_(530331, _n_(530328, "my_input_fn", lambda: my_input_fn), _n_(530329, "X_train", lambda: X_train), _n_(530330, "Y_train", lambda: Y_train), 100),
        steps=100
        )
_l_(530333)

eval_result = _c_(530340, _a_(530335, _n_(530334, "classifier", lambda: classifier), "evaluate"), input_fn=lambda:_c_(530339, _n_(530336, "my_eval_fn", lambda: my_eval_fn), _n_(530337, "X_test", lambda: X_test), _n_(530338, "Y_test", lambda: Y_test), 100)
    )
_l_(530341)

_c_(530346, _n_(530342, "print", lambda: print), _c_(530345, _a_(530343, '\nTest set accuracy: {accuracy:0.3f}\n', "format"), **_n_(530344, "eval_result", lambda: eval_result)))
_l_(530347)