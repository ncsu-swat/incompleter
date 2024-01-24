# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49204913/tensorflow-use-tf-data-textlinedataset-return-attributeerror-list-object-ha
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(445787)

except ImportError:
    pass
feature_names = ['length_1',
             'width_1',
             'length_2',
             'width_2']
_l_(445788)
FILE_TRAIN = 'iris_training.csv'
_l_(445789)
FILE_TEST = 'iris_test.csv'
_l_(445790)
def my_input_fn(file_path, perform_shuffle=False, repeat_count=1):
    _l_(445849)

    def decode_csv(line):
        _l_(445811)

        parsed_line = _c_(445794, _a_(445792, _n_(445791, "tf", lambda: tf), "decode_csv"), _n_(445793, "line", lambda: line), [[0.], [0.], [0.], [0.], [0]])
        _l_(445795)
        label = _n_(445796, "parsed_line", lambda: parsed_line)[-1:]  # Last element is the label
        _l_(445797)  # Last element is the label
        del parsed_line[-1]  # Delete last element
        _l_(445798)  # Delete last element
        features = _n_(445799, "parsed_line", lambda: parsed_line)
        _l_(445800)
        d = _c_(445806, _n_(445801, "dict", lambda: dict), _c_(445805, _n_(445802, "zip", lambda: zip), _n_(445803, "feature_names", lambda: feature_names), _n_(445804, "features", lambda: features)))
        _l_(445807)
        aux = _n_(445808, "d", lambda: d), _n_(445809, "label", lambda: label)
        _l_(445810)
        return aux

    dataset = _c_(445821, _a_(445819, _c_(445818, _a_(445817, _c_(445816, _a_(445814, _a_(445813, _n_(445812, "tf", lambda: tf), "data"), "TextLineDataset"), _n_(445815, "file_path", lambda: file_path)), "skip"), 1), "map"), _n_(445820, "decode_csv", lambda: decode_csv))  # Transform each elem by applying decode_csv fn
    _l_(445822)  # Transform each elem by applying decode_csv fn
    if _n_(445823, "perform_shuffle", lambda: perform_shuffle):
        _l_(445828)

        # Randomizes input using a window of 256 elements (read into memory)
        dataset = _c_(445826, _a_(445825, _n_(445824, "dataset", lambda: dataset), "shuffle"), buffer_size=256)
        _l_(445827)
    dataset = _c_(445832, _a_(445830, _n_(445829, "dataset", lambda: dataset), "repeat"), _n_(445831, "repeat_count", lambda: repeat_count))  # Repeats dataset this # times
    _l_(445833)  # Repeats dataset this # times
    dataset = _c_(445836, _a_(445835, _n_(445834, "dataset", lambda: dataset), "batch"), 32)  # Batch size to use
    _l_(445837)  # Batch size to use
    iterator = _c_(445840, _a_(445839, _n_(445838, "dataset", lambda: dataset), "make_one_shot_iterator"))
    _l_(445841)
    batch_features, batch_labels = _c_(445844, _a_(445843, _n_(445842, "iterator", lambda: iterator), "get_next"))
    _l_(445845)
    aux = _n_(445846, "batch_features", lambda: batch_features), _n_(445847, "batch_labels", lambda: batch_labels)
    _l_(445848)
    return aux
next_batch = _c_(445852, _n_(445850, "my_input_fn", lambda: my_input_fn), _n_(445851, "FILE_TRAIN", lambda: FILE_TRAIN), True)  # Will return 32 random elements
_l_(445853)  # Will return 32 random elements
feature_columns = [_c_(445858, _a_(445856, _a_(445855, _n_(445854, "tf", lambda: tf), "feature_column"), "numeric_column"), _n_(445857, "k", lambda: k)) for k in _n_(445859, "feature_names", lambda: feature_names)]
_l_(445860)
classifier = _c_(445865, _a_(445863, _a_(445862, _n_(445861, "tf", lambda: tf), "estimator"), "DNNClassifier"), feature_columns=_n_(445864, "feature_columns", lambda: feature_columns),  # The input features to our model
    hidden_units=[10, 10],  # Two layers, each with 10 neurons
    n_classes=3,
    model_dir='iris_model')  # Path to where checkpoints etc are stored
_l_(445866)  # Path to where checkpoints etc are stored
_c_(445872, _a_(445868, _n_(445867, "classifier", lambda: classifier), "train"), input_fn=lambda: _c_(445871, _n_(445869, "my_input_fn", lambda: my_input_fn), _n_(445870, "FILE_TRAIN", lambda: FILE_TRAIN), True, 8))
_l_(445873)
evaluate_result = _c_(445879, _a_(445875, _n_(445874, "classifier", lambda: classifier), "evaluate"), input_fn=lambda: _c_(445878, _n_(445876, "my_input_fn", lambda: my_input_fn), _n_(445877, "FILE_TEST", lambda: FILE_TEST), False, 4))
_l_(445880)
_c_(445882, _n_(445881, "print", lambda: print), "Evaluation results")
_l_(445883)

for key in _n_(445884, "evaluate_result", lambda: evaluate_result):
    _l_(445893)

    _c_(445891, _n_(445885, "print", lambda: print), _c_(445890, _a_(445886, "   {}, was: {}", "format"), _n_(445887, "key", lambda: key), _n_(445888, "evaluate_result", lambda: evaluate_result)[_n_(445889, "key", lambda: key)]))
    _l_(445892)