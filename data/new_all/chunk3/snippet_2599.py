# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70044473/typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index-in-tens
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
_l_(574391)
class_names = _c_(574395, _a_(574393, _n_(574392, "np", lambda: np), "array"), _n_(574394, "class_names", lambda: class_names))
_l_(574396)

train_images = _n_(574397, "train_images", lambda: train_images) / 255.0
_l_(574398)
test_images = _n_(574399, "test_images", lambda: test_images) / 255.0
_l_(574400)

_c_(574403, _a_(574402, _n_(574401, "plt", lambda: plt), "figure"), figsize=(10, 10))
_l_(574404)
for i in _c_(574406, _n_(574405, "range", lambda: range), 25):
    _l_(574436)

    _c_(574410, _a_(574408, _n_(574407, "plt", lambda: plt), "subplot"), 5, 5 ,_n_(574409, "i", lambda: i)+1)
    _l_(574411)
    _c_(574419, _a_(574413, _n_(574412, "plt", lambda: plt), "imshow"), _n_(574414, "train_images", lambda: train_images)[_n_(574415, "i", lambda: i)], cmap=_a_(574418, _a_(574417, _n_(574416, "plt", lambda: plt), "cm"), "binary"))
    _l_(574420)
    _c_(574423, _a_(574422, _n_(574421, "plt", lambda: plt), "xticks"), [])
    _l_(574424)
    _c_(574427, _a_(574426, _n_(574425, "plt", lambda: plt), "yticks"), [])
    _l_(574428)
    _c_(574434, _a_(574430, _n_(574429, "plt", lambda: plt), "xlabel"), _n_(574431, "class_names", lambda: class_names)[_n_(574432, "train_labels", lambda: train_labels)[_n_(574433, "i", lambda: i)]])
    _l_(574435)
_c_(574439, _a_(574438, _n_(574437, "plt", lambda: plt), "show"))
_l_(574440)

cnn = _c_(574479, _a_(574443, _a_(574442, _n_(574441, "tf", lambda: tf), "keras"), "Sequential"), [
    _c_(574448, _a_(574447, _a_(574446, _a_(574445, _n_(574444, "tf", lambda: tf), "keras"), "layers"), "Conv2D"), filters=34, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)),
    _c_(574453, _a_(574452, _a_(574451, _a_(574450, _n_(574449, "tf", lambda: tf), "keras"), "layers"), "MaxPooling2D"), (2,2)),
    _c_(574458, _a_(574457, _a_(574456, _a_(574455, _n_(574454, "tf", lambda: tf), "keras"), "layers"), "Conv2D"), filters=64, kernel_size=(3, 3), activation='relu'),
    _c_(574463, _a_(574462, _a_(574461, _a_(574460, _n_(574459, "tf", lambda: tf), "keras"), "layers"), "MaxPooling2D"), (2,2)),

    _c_(574468, _a_(574467, _a_(574466, _a_(574465, _n_(574464, "tf", lambda: tf), "keras"), "layers"), "Flatten")),
    _c_(574473, _a_(574472, _a_(574471, _a_(574470, _n_(574469, "tf", lambda: tf), "keras"), "layers"), "Dense"), 64, activation='relu'),
    _c_(574478, _a_(574477, _a_(574476, _a_(574475, _n_(574474, "tf", lambda: tf), "keras"), "layers"), "Dense"), 10, activation='softmax')
])
_l_(574480)

_c_(574488, _a_(574482, _n_(574481, "cnn", lambda: cnn), "compile"), optimizer='adam', loss=_c_(574487, _a_(574486, _a_(574485, _a_(574484, _n_(574483, "tf", lambda: tf), "keras"), "losses"), "SparseCategoricalCrossentropy")), metrics=['accuracy'])
_l_(574489)

_c_(574494, _a_(574491, _n_(574490, "cnn", lambda: cnn), "fit"), _n_(574492, "train_images", lambda: train_images), _n_(574493, "train_labels", lambda: train_labels), epochs=10)
_l_(574495)

def plot_image(i, predictions_array, true_label, img):
    _l_(574546)

    true_label, img = _n_(574496, "true_label", lambda: true_label)[_n_(574497, "i", lambda: i)], _n_(574498, "img", lambda: img)[_n_(574499, "i", lambda: i)]
    _l_(574500)
    _c_(574503, _a_(574502, _n_(574501, "plt", lambda: plt), "grid"), False)
    _l_(574504)
    _c_(574507, _a_(574506, _n_(574505, "plt", lambda: plt), "xticks"), [])
    _l_(574508)
    _c_(574511, _a_(574510, _n_(574509, "plt", lambda: plt), "yticks"), [])
    _l_(574512)

    _c_(574519, _a_(574514, _n_(574513, "plt", lambda: plt), "imshow"), _n_(574515, "img", lambda: img), cmap=_a_(574518, _a_(574517, _n_(574516, "plt", lambda: plt), "cm"), "binary"))
    _l_(574520)

    predicted_label = _c_(574524, _a_(574522, _n_(574521, "np", lambda: np), "argmax"), _n_(574523, "predictions_array", lambda: predictions_array))
    _l_(574525)
    if _n_(574526, "predicted_label", lambda: predicted_label) == _n_(574527, "true_label", lambda: true_label):
        _l_(574530)

        color = 'blue'
        _l_(574528)
    else:
        color = 'red'
        _l_(574529)

    _c_(574544, _a_(574532, _n_(574531, "plt", lambda: plt), "xlabel"), _c_(574542, _a_(574533, "{} {:2.0f}% ({})", "format"), _n_(574534, "class_names", lambda: class_names)[_n_(574535, "predicted_label", lambda: predicted_label)],
                            100*_c_(574539, _a_(574537, _n_(574536, "np", lambda: np), "max"), _n_(574538, "predictions_array", lambda: predictions_array)),
                            _n_(574540, "class_names", lambda: class_names)[_n_(574541, "true_label", lambda: true_label)]),
                            color=_n_(574543, "color", lambda: color))
    _l_(574545)

def plot_value_array(i, predictions_array, true_label):
    _l_(574590)

    true_label = _n_(574547, "true_label", lambda: true_label)[_n_(574548, "i", lambda: i)]
    _l_(574549)
    _c_(574552, _a_(574551, _n_(574550, "plt", lambda: plt), "grid"), False)
    _l_(574553)
    _c_(574558, _a_(574555, _n_(574554, "plt", lambda: plt), "xticks"), _c_(574557, _n_(574556, "range", lambda: range), 10))
    _l_(574559)
    _c_(574562, _a_(574561, _n_(574560, "plt", lambda: plt), "yticks"), [])
    _l_(574563)
    thisplot = _c_(574569, _a_(574565, _n_(574564, "plt", lambda: plt), "bar"), _c_(574567, _n_(574566, "range", lambda: range), 10), _n_(574568, "predictions_array", lambda: predictions_array), color="#777777")
    _l_(574570)
    _c_(574573, _a_(574572, _n_(574571, "plt", lambda: plt), "ylim"), [0, 1])
    _l_(574574)
    predicted_label = _c_(574578, _a_(574576, _n_(574575, "np", lambda: np), "argmax"), _n_(574577, "predictions_array", lambda: predictions_array))
    _l_(574579)

    _c_(574583, _a_(574582, _n_(574580, "thisplot", lambda: thisplot)[_n_(574581, "predicted_label", lambda: predicted_label)], "set_color"), 'red')
    _l_(574584)
    _c_(574588, _a_(574587, _n_(574585, "thisplot", lambda: thisplot)[_n_(574586, "true_label", lambda: true_label)], "set_color"), 'blue')
    _l_(574589)

probability_model = _c_(574600, _a_(574593, _a_(574592, _n_(574591, "tf", lambda: tf), "keras"), "Sequential"), [_n_(574594, "cnn", lambda: cnn), _c_(574599, _a_(574598, _a_(574597, _a_(574596, _n_(574595, "tf", lambda: tf), "keras"), "layers"), "Softmax"))])
_l_(574601)

predictions = _c_(574605, _a_(574603, _n_(574602, "probability_model", lambda: probability_model), "predict"), _n_(574604, "test_images", lambda: test_images))
_l_(574606)

num_rows = 5
_l_(574607)
num_cols = 3
_l_(574608)
num_images = _n_(574609, "num_rows", lambda: num_rows)*_n_(574610, "num_cols", lambda: num_cols)
_l_(574611)
_c_(574616, _a_(574613, _n_(574612, "plt", lambda: plt), "figure"), figsize=(2*2*_n_(574614, "num_cols", lambda: num_cols), 2*_n_(574615, "num_rows", lambda: num_rows)))
_l_(574617)
for i in _c_(574620, _n_(574618, "range", lambda: range), _n_(574619, "num_images", lambda: num_images)):
    _l_(574650)

    _c_(574626, _a_(574622, _n_(574621, "plt", lambda: plt), "subplot"), _n_(574623, "num_rows", lambda: num_rows), 2*_n_(574624, "num_cols", lambda: num_cols), 2*_n_(574625, "i", lambda: i)+1)
    _l_(574627)
    _c_(574634, _n_(574628, "plot_image", lambda: plot_image), _n_(574629, "i", lambda: i), _n_(574630, "predictions", lambda: predictions)[_n_(574631, "i", lambda: i)], _n_(574632, "test_labels", lambda: test_labels), _n_(574633, "test_images", lambda: test_images))
    _l_(574635)
    _c_(574641, _a_(574637, _n_(574636, "plt", lambda: plt), "subplot"), _n_(574638, "num_rows", lambda: num_rows), 2*_n_(574639, "num_cols", lambda: num_cols), 2*_n_(574640, "i", lambda: i)+2)
    _l_(574642)
    _c_(574648, _n_(574643, "plot_value_array", lambda: plot_value_array), _n_(574644, "i", lambda: i), _n_(574645, "predictions", lambda: predictions)[_n_(574646, "i", lambda: i)], _n_(574647, "test_labels", lambda: test_labels))
    _l_(574649)
_c_(574653, _a_(574652, _n_(574651, "plt", lambda: plt), "tight_layout"))
_l_(574654)
_c_(574657, _a_(574656, _n_(574655, "plt", lambda: plt), "show"))
_l_(574658)