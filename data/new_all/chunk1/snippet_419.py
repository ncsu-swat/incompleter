# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55884002/how-to-fix-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
labels = []
_l_(418298)
label_np = _c_(418302, _a_(418300, _n_(418299, "np", lambda: np), "array"), _n_(418301, "labels", lambda: labels))
_l_(418303)

with _c_(418306, _n_(418304, "open", lambda: open), _n_(418305, "path", lambda: path), encoding='utf-8') as in_file:
    _l_(418320)

    data = _c_(418310, _a_(418308, _n_(418307, "csv", lambda: csv), "reader"), _n_(418309, "in_file", lambda: in_file))
    _l_(418311)
    for line in _n_(418312, "data", lambda: data):
        _l_(418319)

        label_ = _c_(418317, _a_(418314, _n_(418313, "np", lambda: np), "append"), _n_(418315, "label_np", lambda: label_np), _n_(418316, "line", lambda: line))
        _l_(418318)

model = _c_(418322, _n_(418321, "SVC", lambda: SVC), kernel='linear')
_l_(418323)
total_svm = []
_l_(418324)
total_mat_svm = _c_(418327, _a_(418326, _n_(418325, "np", lambda: np), "zeros"), (2,2))
_l_(418328)

kf = _c_(418330, _n_(418329, "StratifiedKFold", lambda: StratifiedKFold), n_splits=3)
_l_(418331)
_c_(418336, _a_(418333, _n_(418332, "kf", lambda: kf), "get_n_splits"), _n_(418334, "result_preprocess", lambda: result_preprocess), _n_(418335, "label_", lambda: label_))
_l_(418337)

for train_index, test_index in _c_(418342, _a_(418339, _n_(418338, "kf", lambda: kf), "split"), _n_(418340, "result_preprocess", lambda: result_preprocess), _n_(418341, "label_", lambda: label_)):
    _l_(418353)

    # print('Train : ', test_index, 'Test : ', test_index)
    x_train, x_test = _n_(418343, "result_preprocess", lambda: result_preprocess)[_n_(418344, "train_index", lambda: train_index)], _n_(418345, "result_preprocess", lambda: result_preprocess)[_n_(418346, "test_index", lambda: test_index)]
    _l_(418347)
    y_train, y_test = _n_(418348, "label_", lambda: label_)[_n_(418349, "train_index", lambda: train_index)], _n_(418350, "label_", lambda: label_)[_n_(418351, "test_index", lambda: test_index)]
    _l_(418352)

vectorizer = _c_(418355, _n_(418354, "TfidfVectorizer", lambda: TfidfVectorizer), min_df=5,
                             max_df=0.8,
                             sublinear_tf=True,
                             use_idf=True)
_l_(418356)
train_vector = _c_(418360, _a_(418358, _n_(418357, "vectorizer", lambda: vectorizer), "fit_transform"), _n_(418359, "x_train", lambda: x_train))
_l_(418361)
test_vector = _c_(418365, _a_(418363, _n_(418362, "vectorizer", lambda: vectorizer), "transform"), _n_(418364, "x_test", lambda: x_test))
_l_(418366)

_c_(418371, _a_(418368, _n_(418367, "model", lambda: model), "fit"), _n_(418369, "x_train", lambda: x_train), _n_(418370, "y_train", lambda: y_train))
_l_(418372)
hasil_svm = _c_(418376, _a_(418374, _n_(418373, "model", lambda: model), "predict"), _n_(418375, "x_test", lambda: x_test))
_l_(418377)

total_mat_svm = _n_(418378, "total_mat_svm", lambda: total_mat_svm) + _c_(418382, _n_(418379, "confusion_matrix", lambda: confusion_matrix), _n_(418380, "y_test", lambda: y_test), _n_(418381, "hasil_svm", lambda: hasil_svm))
_l_(418383)
total_svm = _n_(418384, "total_mat_svm", lambda: total_mat_svm) + _c_(418388, _n_(418385, "sum", lambda: sum), _n_(418386, "y_test", lambda: y_test)==_n_(418387, "hasil_svm", lambda: hasil_svm))
_l_(418389)

_c_(418392, _n_(418390, "print", lambda: print), _n_(418391, "total_mat_svm", lambda: total_mat_svm))
_l_(418393)