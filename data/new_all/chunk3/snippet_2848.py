# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60923917/apache-arrow-with-tensorflow-type-error-arrow-type-mismatch-expected-dtype-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import partial
    _l_(523373)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(523375)

except ImportError:
    pass
try:
    import pyarrow.csv
    _l_(523377)

except ImportError:
    pass
try:
    import pyarrow as pa
    _l_(523379)

except ImportError:
    pass
try:
    from sklearn.preprocessing import Normalizer
    _l_(523381)

except ImportError:
    pass
try:
    import tensorflow_io.arrow as arrow_io
    _l_(523383)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(523385)

except ImportError:
    pass

"""run arrow_mnist local"""

# total columns num of mnist
COLUMNS_LEN = 785
_l_(523386)
# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '5'

# set gpu config
gpus = _c_(523391, _a_(523390, _a_(523389, _a_(523388, _n_(523387, "tf", lambda: tf), "config"), "experimental"), "list_physical_devices"), device_type='GPU')
_l_(523392)
for gpu in _n_(523393, "gpus", lambda: gpus):
    _l_(523401)

    _c_(523399, _a_(523397, _a_(523396, _a_(523395, _n_(523394, "tf", lambda: tf), "config"), "experimental"), "set_memory_growth"), _n_(523398, "gpu", lambda: gpu), True)
    _l_(523400)

# from tensorflow demo
def model_fit(ds):
    _l_(523453)

    model = _c_(523430, _a_(523404, _a_(523403, _n_(523402, "tf", lambda: tf), "keras"), "Sequential"), [
        _c_(523409, _a_(523408, _a_(523407, _a_(523406, _n_(523405, "tf", lambda: tf), "keras"), "layers"), "Conv2D"), 32, 1, activation='relu', input_shape=(28, 28, 1)),
        _c_(523414, _a_(523413, _a_(523412, _a_(523411, _n_(523410, "tf", lambda: tf), "keras"), "layers"), "MaxPooling2D")),
        _c_(523419, _a_(523418, _a_(523417, _a_(523416, _n_(523415, "tf", lambda: tf), "keras"), "layers"), "Flatten")),
        _c_(523424, _a_(523423, _a_(523422, _a_(523421, _n_(523420, "tf", lambda: tf), "keras"), "layers"), "Dense"), 64, activation='relu'),
        _c_(523429, _a_(523428, _a_(523427, _a_(523426, _n_(523425, "tf", lambda: tf), "keras"), "layers"), "Dense"), 10)
    ])
    _l_(523431)

    _c_(523444, _a_(523433, _n_(523432, "model", lambda: model), "compile"), loss=_c_(523438, _a_(523437, _a_(523436, _a_(523435, _n_(523434, "tf", lambda: tf), "keras"), "losses"), "SparseCategoricalCrossentropy"), from_logits=True),
                  optimizer=_c_(523443, _a_(523442, _a_(523441, _a_(523440, _n_(523439, "tf", lambda: tf), "keras"), "optimizers"), "Adam")),
                  metrics=['accuracy'])
    _l_(523445)

    _c_(523449, _a_(523447, _n_(523446, "model", lambda: model), "fit"), _n_(523448, "ds", lambda: ds), epochs=10)
    _l_(523450)
    aux = _n_(523451, "model", lambda: model)
    _l_(523452)
    return aux


def read_and_process(filename):
    _l_(523531)

    """Read the given CSV file and yield processed Arrow batches."""

    # Read a CSV file into an Arrow Table
    opts = _c_(523456, _a_(523455, _a_(523454, pyarrow, "csv"), "ReadOptions"), use_threads=True, autogenerate_column_names=True)
    _l_(523457)
    table = _c_(523462, _a_(523459, _a_(523458, pyarrow, "csv"), "read_csv"), _n_(523460, "filename", lambda: filename), _n_(523461, "opts", lambda: opts))
    _l_(523463)
    # Fit the feature transform
    df = _c_(523466, _a_(523465, _n_(523464, "table", lambda: table), "to_pandas"))
    _l_(523467)

    # normalizer the value except 'target'
    # for preprocess
    mylist = []
    _l_(523468)
    for i in _c_(523471, _n_(523469, "range", lambda: range), _n_(523470, "COLUMNS_LEN", lambda: COLUMNS_LEN) - 1):
        _l_(523481)

        tmp1 = 'f' + _c_(523474, _n_(523472, "str", lambda: str), _n_(523473, "i", lambda: i)+1)
        _l_(523475)
        _c_(523479, _a_(523477, _n_(523476, "mylist", lambda: mylist), "append"), _n_(523478, "tmp1", lambda: tmp1))
        _l_(523480)

    scaler = _c_(523487, _a_(523484, _c_(523483, _n_(523482, "Normalizer", lambda: Normalizer)), "fit"), _n_(523485, "df", lambda: df)[_n_(523486, "mylist", lambda: mylist)])
    _l_(523488)
    # Iterate over batches in the pyarrow.Table and apply processing
    for batch in _c_(523491, _a_(523490, _n_(523489, "table", lambda: table), "to_batches")):
        _l_(523530)

        df = _c_(523494, _a_(523493, _n_(523492, "batch", lambda: batch), "to_pandas"))
        _l_(523495)

        # Process the batch and apply feature transform
        X_scaled = _c_(523500, _a_(523497, _n_(523496, "scaler", lambda: scaler), "transform"), _n_(523498, "df", lambda: df)[_n_(523499, "mylist", lambda: mylist)])
        _l_(523501)

        my_dict = {'f0': _n_(523502, "df", lambda: df)['f0']}
        _l_(523503)
        for i in _c_(523506, _n_(523504, "range", lambda: range), _n_(523505, "COLUMNS_LEN", lambda: COLUMNS_LEN) - 1):
            _l_(523516)

            tmp2 = 'f' + _c_(523509, _n_(523507, "str", lambda: str), _n_(523508, "i", lambda: i)+1)
            _l_(523510)
            _n_(523511, "my_dict", lambda: my_dict)[_n_(523512, "tmp2", lambda: tmp2)] = _n_(523513, "X_scaled", lambda: X_scaled)[:, _n_(523514, "i", lambda: i)]
            _l_(523515)

        # use my_dict will be successful
        # df_scaled = pd.DataFrame(my_dict)
        df_scaled = _c_(523520, _a_(523518, _n_(523517, "pd", lambda: pd), "DataFrame"), _n_(523519, "df", lambda: df))
        _l_(523521)

        batch_scaled = _c_(523526, _a_(523524, _a_(523523, _n_(523522, "pa", lambda: pa), "RecordBatch"), "from_pandas"), _n_(523525, "df_scaled", lambda: df_scaled), preserve_index=False)
        _l_(523527)

        yield _n_(523528, "batch_scaled", lambda: batch_scaled)
        _l_(523529)


def make_local_dataset(filename):
    _l_(523617)

    """Make a TensorFlow Arrow Dataset that reads from a local CSV file."""

    # Read the local file and get a record batch iterator
    batch_iter = _c_(523534, _n_(523532, "read_and_process", lambda: read_and_process), _n_(523533, "filename", lambda: filename))
    _l_(523535)

    # make output_types
    my_types_list = [_a_(523537, _n_(523536, "tf", lambda: tf), "int64")]
    _l_(523538)
    for i in _c_(523541, _n_(523539, "range", lambda: range), _n_(523540, "COLUMNS_LEN", lambda: COLUMNS_LEN) - 1):
        _l_(523548)

        _c_(523546, _a_(523543, _n_(523542, "my_types_list", lambda: my_types_list), "append"), _a_(523545, _n_(523544, "tf", lambda: tf), "float64"))
        _l_(523547)
    my_types_tuple = _c_(523551, _n_(523549, "tuple", lambda: tuple), _n_(523550, "my_types_list", lambda: my_types_list))
    _l_(523552)

    # make output_shapes
    my_shapes_list = []
    _l_(523553)
    for i in _c_(523556, _n_(523554, "range", lambda: range), _n_(523555, "COLUMNS_LEN", lambda: COLUMNS_LEN)):
        _l_(523564)

        _c_(523562, _a_(523558, _n_(523557, "my_shapes_list", lambda: my_shapes_list), "append"), _c_(523561, _a_(523560, _n_(523559, "tf", lambda: tf), "TensorShape"), []))
        _l_(523563)
    my_shapes_tuple = _c_(523567, _n_(523565, "tuple", lambda: tuple), _n_(523566, "my_shapes_list", lambda: my_shapes_list))
    _l_(523568)

    # Create the Arrow Dataset as a stream from local iterator of record batches
    ds = _c_(523579, _a_(523571, _a_(523570, _n_(523569, "arrow_io", lambda: arrow_io), "ArrowStreamDataset"), "from_record_batches"), _n_(523572, "batch_iter", lambda: batch_iter),
        batch_size=500,
        batch_mode='keep_remainder',
        output_types=_n_(523573, "my_types_tuple", lambda: my_types_tuple),
        output_shapes=_n_(523574, "my_shapes_tuple", lambda: my_shapes_tuple),
        record_batch_iter_factory=_c_(523578, _n_(523575, "partial", lambda: partial), _n_(523576, "read_and_process", lambda: read_and_process), _n_(523577, "filename", lambda: filename)))
    _l_(523580)

    def my_map_func(*args):
        _l_(523609)

        data_list = []
        _l_(523581)
        # split the label and data
        flag = 1
        _l_(523582)
        for i in _n_(523583, "args", lambda: args):
            _l_(523595)

            if _n_(523584, "flag", lambda: flag) == 1:
                _l_(523594)

                data_label = _n_(523585, "i", lambda: i)
                _l_(523586)
                flag = _n_(523587, "flag", lambda: flag) + 1
                _l_(523588)
            else:
                _c_(523592, _a_(523590, _n_(523589, "data_list", lambda: data_list), "append"), _n_(523591, "i", lambda: i))
                _l_(523593)

        data_tensor = _c_(523599, _a_(523597, _n_(523596, "tf", lambda: tf), "stack"), _n_(523598, "data_list", lambda: data_list), axis=1)
        _l_(523600)

        # reshape data to (28, 28 , 1)
        data_tensor_reshape = _c_(523604, _a_(523602, _n_(523601, "tf", lambda: tf), "reshape"), _n_(523603, "data_tensor", lambda: data_tensor), (-1, 28, 28, 1))
        _l_(523605)
        aux = (_n_(523606, "data_tensor_reshape", lambda: data_tensor_reshape), _n_(523607, "data_label", lambda: data_label))
        _l_(523608)

        # return with label
        return aux

    ds = _c_(523613, _a_(523611, _n_(523610, "ds", lambda: ds), "map"), _n_(523612, "my_map_func", lambda: my_map_func))
    _l_(523614)
    aux = _n_(523615, "ds", lambda: ds)
    _l_(523616)
    return aux


if _n_(523618, "__name__", lambda: __name__) == '__main__':
    _l_(523629)


    ds = _c_(523620, _n_(523619, "make_local_dataset", lambda: make_local_dataset), '/home/maqy/data/mnist_test.csv')
    _l_(523621)

    _c_(523623, _n_(523622, "print", lambda: print), "hello")
    _l_(523624)
    model = _c_(523627, _n_(523625, "model_fit", lambda: model_fit), _n_(523626, "ds", lambda: ds))
    _l_(523628)