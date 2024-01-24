# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67342655/multiclass-text-classification-typeerror-input-must-be-a-sparsetensor
# Split the data into training and test sets
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import train_test_split
    _l_(541638)

except ImportError:
    pass
X_train, X_validation, y_train, y_validation = _c_(541642, _n_(541639, "train_test_split", lambda: train_test_split), _n_(541640, "X", lambda: X), _n_(541641, "y", lambda: y), test_size=0.2, random_state=42)
_l_(541643)

# encode class values as integers
encoder = _c_(541645, _n_(541644, "LabelEncoder", lambda: LabelEncoder))
_l_(541646)
_c_(541650, _a_(541648, _n_(541647, "encoder", lambda: encoder), "fit"), _n_(541649, "y_train", lambda: y_train))
_l_(541651)
encoded_y_train = _c_(541655, _a_(541653, _n_(541652, "encoder", lambda: encoder), "transform"), _n_(541654, "y_train", lambda: y_train))
_l_(541656)
# convert integers to dummy variables (i.e. one hot encoded)
y_train= _c_(541660, _a_(541658, _n_(541657, "np_utils", lambda: np_utils), "to_categorical"), _n_(541659, "encoded_y_train", lambda: encoded_y_train))
_l_(541661)

# encode class values as integers
encoder = _c_(541663, _n_(541662, "LabelEncoder", lambda: LabelEncoder))
_l_(541664)
_c_(541668, _a_(541666, _n_(541665, "encoder", lambda: encoder), "fit"), _n_(541667, "y_validation", lambda: y_validation))
_l_(541669)
encoded_y_validation = _c_(541673, _a_(541671, _n_(541670, "encoder", lambda: encoder), "transform"), _n_(541672, "y_validation", lambda: y_validation))
_l_(541674)
# convert integers to dummy variables (i.e. one hot encoded)
y_validation= _c_(541678, _a_(541676, _n_(541675, "np_utils", lambda: np_utils), "to_categorical"), _n_(541677, "encoded_y_validation", lambda: encoded_y_validation))
_l_(541679)
try:
    from sklearn.feature_extraction.text import CountVectorizer
    _l_(541681)

except ImportError:
    pass

cv1 = _c_(541683, _n_(541682, "CountVectorizer", lambda: CountVectorizer), analyzer='char',ngram_range=(2, 2))
_l_(541684)

X_train_cv1 = _c_(541688, _a_(541686, _n_(541685, "cv1", lambda: cv1), "fit_transform"), _n_(541687, "X_train", lambda: X_train))
_l_(541689)
X_validation_cv1  = _c_(541693, _a_(541691, _n_(541690, "cv1", lambda: cv1), "transform"), _n_(541692, "X_validation", lambda: X_validation))
_l_(541694)

input_dim = _a_(541696, _n_(541695, "X_train_cv1", lambda: X_train_cv1), "shape")[1]  # Number of features
_l_(541697)  # Number of features
model = _c_(541699, _n_(541698, "Sequential", lambda: Sequential))
_l_(541700)
_c_(541707, _a_(541702, _n_(541701, "model", lambda: model), "add"), _c_(541706, _a_(541704, _n_(541703, "layers", lambda: layers), "Dense"), 10, input_dim=_n_(541705, "input_dim", lambda: input_dim), activation='relu'))
_l_(541708)
_c_(541714, _a_(541710, _n_(541709, "model", lambda: model), "add"), _c_(541713, _a_(541712, _n_(541711, "layers", lambda: layers), "Dense"), 3, activation='softmax'))
_l_(541715)

_c_(541718, _a_(541717, _n_(541716, "model", lambda: model), "compile"), loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
_l_(541719)
_c_(541722, _a_(541721, _n_(541720, "model", lambda: model), "summary"))
_l_(541723)

X_train_cv1 = _c_(541728, _a_(541726, _a_(541725, _n_(541724, "tf", lambda: tf), "sparse"), "reorder"), _n_(541727, "X_train_cv1", lambda: X_train_cv1))
_l_(541729)
y_train = _c_(541734, _a_(541732, _a_(541731, _n_(541730, "tf", lambda: tf), "sparse"), "reorder"), _n_(541733, "y_train", lambda: y_train))
_l_(541735)
X_validation_cv1 = _c_(541740, _a_(541738, _a_(541737, _n_(541736, "tf", lambda: tf), "sparse"), "reorder"), _n_(541739, "X_validation_cv1", lambda: X_validation_cv1))
_l_(541741)
y_validation = _c_(541746, _a_(541744, _a_(541743, _n_(541742, "tf", lambda: tf), "sparse"), "reorder"), _n_(541745, "y_validation", lambda: y_validation))
_l_(541747)

history = _c_(541754, _a_(541749, _n_(541748, "model", lambda: model), "fit"), _n_(541750, "X_train_cv1", lambda: X_train_cv1), _n_(541751, "y_train", lambda: y_train),epochs=100,verbose=True,validation_data=(_n_(541752, "X_validation_cv1", lambda: X_validation_cv1), _n_(541753, "y_validation", lambda: y_validation)),batch_size=10)
_l_(541755)