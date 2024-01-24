# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77469949/model-fit-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tensorflow import keras
    _l_(443300)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(443302)

except ImportError:
    pass
try:
    from keras.utils import to_categorical
    _l_(443304)

except ImportError:
    pass

label_map = {_n_(443305, "label", lambda: label):_n_(443306, "num", lambda: num) for num, label in _c_(443309, _n_(443307, "enumerate", lambda: enumerate), _n_(443308, "signs", lambda: signs))}
_l_(443310)
_n_(443311, "label_map", lambda: label_map)
_l_(443312)

sequences, labels = [], []
_l_(443313)
for sign in _n_(443314, "signs", lambda: signs):
    _l_(443356)

    for sequence in _c_(443317, _n_(443315, "range", lambda: range), _n_(443316, "no_sequences", lambda: no_sequences)):
        _l_(443355)

        window = []
        _l_(443318)
        for frame_no in _c_(443321, _n_(443319, "range", lambda: range), _n_(443320, "sequence_length", lambda: sequence_length)):
            _l_(443343)

            res = _c_(443336, _a_(443323, _n_(443322, "np", lambda: np), "load"), _c_(443335, _a_(443326, _a_(443325, _n_(443324, "os", lambda: os), "path"), "join"), _n_(443327, "Data_Path", lambda: Data_Path), _n_(443328, "sign", lambda: sign), _c_(443331, _n_(443329, "str", lambda: str), _n_(443330, "sequence", lambda: sequence)),_c_(443334, _a_(443332, "{}.npy", "format"), _n_(443333, "frame_no", lambda: frame_no))))
            _l_(443337)
            _c_(443341, _a_(443339, _n_(443338, "window", lambda: window), "append"), _n_(443340, "res", lambda: res))
            _l_(443342)
        _c_(443347, _a_(443345, _n_(443344, "sequences", lambda: sequences), "append"), _n_(443346, "window", lambda: window))
        _l_(443348)
        _c_(443353, _a_(443350, _n_(443349, "labels", lambda: labels), "append"), _n_(443351, "label_map", lambda: label_map)[_n_(443352, "sign", lambda: sign)])
        _l_(443354)

X = _c_(443360, _a_(443358, _n_(443357, "np", lambda: np), "array"), _n_(443359, "sequences", lambda: sequences))
_l_(443361)
_a_(443363, _n_(443362, "X", lambda: X), "shape")
_l_(443364)

y = _c_(443370, _a_(443368, _c_(443367, _n_(443365, "to_categorical", lambda: to_categorical), _n_(443366, "labels", lambda: labels)), "astype"), _n_(443369, "int", lambda: int))
_l_(443371)

X_train, X_test, y_train, y_test = _c_(443375, _n_(443372, "train_test_split", lambda: train_test_split), _n_(443373, "X", lambda: X), _n_(443374, "y", lambda: y), test_size=0.05)
_l_(443376)
try:
    from keras.models import Sequential
    _l_(443378)

except ImportError:
    pass
try:
    from keras.layers import LSTM, Dense
    _l_(443380)

except ImportError:
    pass
try:
    from keras.callbacks import TensorBoard
    _l_(443382)

except ImportError:
    pass

log_dir = _c_(443386, _a_(443385, _a_(443384, _n_(443383, "os", lambda: os), "path"), "join"), 'Logs')
_l_(443387)
tb_callback = _c_(443390, _n_(443388, "TensorBoard", lambda: TensorBoard), log_dir = _n_(443389, "log_dir", lambda: log_dir))
_l_(443391)


model = _c_(443393, _n_(443392, "Sequential", lambda: Sequential))
_l_(443394)
_c_(443399, _a_(443396, _n_(443395, "model", lambda: model), "add"), _c_(443398, _n_(443397, "LSTM", lambda: LSTM), 64, return_sequences=True, activation="relu", input_shape=(30,1662)))
_l_(443400)
_c_(443405, _a_(443402, _n_(443401, "model", lambda: model), "add"), _c_(443404, _n_(443403, "LSTM", lambda: LSTM), 128, return_sequences=True, activation="relu"))
_l_(443406)
_c_(443411, _a_(443408, _n_(443407, "model", lambda: model), "add"), _c_(443410, _n_(443409, "LSTM", lambda: LSTM), 64, return_sequences=False, activation="relu"))
_l_(443412)
_c_(443417, _a_(443414, _n_(443413, "model", lambda: model), "add"), _c_(443416, _n_(443415, "Dense", lambda: Dense), 64, activation="relu"))
_l_(443418)
_c_(443423, _a_(443420, _n_(443419, "model", lambda: model), "add"), _c_(443422, _n_(443421, "Dense", lambda: Dense), 32, activation="relu"))
_l_(443424)
_c_(443431, _a_(443426, _n_(443425, "model", lambda: model), "add"), _c_(443430, _n_(443427, "Dense", lambda: Dense), _a_(443429, _n_(443428, "signs", lambda: signs), "shape")[0], activation='softmax'))
_l_(443432)

_c_(443435, _a_(443434, _n_(443433, "model", lambda: model), "compile"), optimizer='Adam', loss="categorical_crossentropy", metrics=['categorical accuracy'])
_l_(443436)

_c_(443442, _a_(443438, _n_(443437, "model", lambda: model), "fit"), _n_(443439, "X_train", lambda: X_train), _n_(443440, "y_train", lambda: y_train), epochs=2000, callbacks=[_n_(443441, "tb_callback", lambda: tb_callback)])
_l_(443443)