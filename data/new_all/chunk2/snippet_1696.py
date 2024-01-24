# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62588981/typeerror-invalid-shape-10000-28-28-for-image-data-in-tensor-flow-fashion
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(436584)

except ImportError:
    pass
try:
    import numpy as np
    _l_(436586)

except ImportError:
    pass
try:
    from tensorflow import keras
    _l_(436588)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(436590)

except ImportError:
    pass

fashion_mnist = _a_(436593, _a_(436592, _n_(436591, "keras", lambda: keras), "datasets"), "fashion_mnist")
_l_(436594)
(train_images, train_labels), (test_images, test_labels) = _c_(436597, _a_(436596, _n_(436595, "fashion_mnist", lambda: fashion_mnist), "load_data"))
_l_(436598)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 
'Sneaker', 'Bag', 'Ankle boot']
_l_(436599)

_c_(436602, _a_(436601, _n_(436600, "plt", lambda: plt), "figure"))
_l_(436603)
_c_(436607, _a_(436605, _n_(436604, "plt", lambda: plt), "imshow"), _n_(436606, "train_images", lambda: train_images)[0])
_l_(436608)
_c_(436611, _a_(436610, _n_(436609, "plt", lambda: plt), "colorbar"))
_l_(436612)
_n_(436613, "plt", lambda: plt).grid = False
_l_(436614)

train_images = _n_(436615, "train_images", lambda: train_images)/255
_l_(436616)
test_images = _n_(436617, "test_images", lambda: test_images)/255
_l_(436618)

_c_(436621, _a_(436620, _n_(436619, "plt", lambda: plt), "figure"), figsize=(10,10))
_l_(436622)
for i in _c_(436624, _n_(436623, "range", lambda: range), 25):
    _l_(436656)

    _c_(436628, _a_(436626, _n_(436625, "plt", lambda: plt), "subplot"), 5,5,_n_(436627, "i", lambda: i)+1)
    _l_(436629)
    _c_(436632, _a_(436631, _n_(436630, "plt", lambda: plt), "xticks"), [])
    _l_(436633)
    _c_(436636, _a_(436635, _n_(436634, "plt", lambda: plt), "yticks"), [])
    _l_(436637)
    _n_(436638, "plt", lambda: plt).grid=False
    _l_(436639)
    _c_(436647, _a_(436641, _n_(436640, "plt", lambda: plt), "imshow"), _n_(436642, "train_images", lambda: train_images)[_n_(436643, "i", lambda: i)], cmap=_a_(436646, _a_(436645, _n_(436644, "plt", lambda: plt), "cm"), "binary"))
    _l_(436648)
    _c_(436654, _a_(436650, _n_(436649, "plt", lambda: plt), "xlabel"), _n_(436651, "class_names", lambda: class_names)[_n_(436652, "train_labels", lambda: train_labels)[_n_(436653, "i", lambda: i)]])
    _l_(436655)

model = _c_(436671, _a_(436658, _n_(436657, "keras", lambda: keras), "Sequential"), [_c_(436662, _a_(436661, _a_(436660, _n_(436659, "keras", lambda: keras), "layers"), "Flatten"), input_shape=(28,28)),_c_(436666, _a_(436665, _a_(436664, _n_(436663, "keras", lambda: keras), "layers"), "Dense"), 128, 
activation ='relu'),_c_(436670, _a_(436669, _a_(436668, _n_(436667, "keras", lambda: keras), "layers"), "Dense"), 10)])
_l_(436672)



_c_(436680, _a_(436674, _n_(436673, "model", lambda: model), "compile"), optimizer='adam',loss=_c_(436679, _a_(436678, _a_(436677, _a_(436676, _n_(436675, "tf", lambda: tf), "keras"), "losses"), "SparseCategoricalCrossentropy"), from_logits=True),metrics=['accuracy'])
_l_(436681)

_c_(436686, _a_(436683, _n_(436682, "model", lambda: model), "fit"), _n_(436684, "train_images", lambda: train_images), _n_(436685, "train_labels", lambda: train_labels), epochs=50)
_l_(436687)

test_loss, test_acc = _c_(436692, _a_(436689, _n_(436688, "model", lambda: model), "evaluate"), _n_(436690, "test_images", lambda: test_images), _n_(436691, "test_labels", lambda: test_labels), verbose=2)
_l_(436693)
_c_(436696, _n_(436694, "print", lambda: print), 'Test Accuracy:', _n_(436695, "test_acc", lambda: test_acc))
_l_(436697)

probability_model = _c_(436707, _a_(436700, _a_(436699, _n_(436698, "tf", lambda: tf), "keras"), "Sequential"), [_n_(436701, "model", lambda: model), _c_(436706, _a_(436705, _a_(436704, _a_(436703, _n_(436702, "tf", lambda: tf), "keras"), "layers"), "Softmax"))])
_l_(436708)
predictions = _c_(436712, _a_(436710, _n_(436709, "probability_model", lambda: probability_model), "predict"), _n_(436711, "test_images", lambda: test_images))
_l_(436713)

_n_(436714, "predictions", lambda: predictions)[0]
_l_(436715)

_c_(436719, _a_(436717, _n_(436716, "np", lambda: np), "argmax"), _n_(436718, "predictions", lambda: predictions)[0])
_l_(436720)

def plot_image(i, predictions_array, true_label, img):
    _l_(436769)

    predictions_array, true_labels, image=_n_(436721, "predictions_array", lambda: predictions_array), _n_(436722, "true_label", lambda: true_label)[_n_(436723, "i", lambda: i)], _n_(436724, "img", lambda: img)[_n_(436725, "i", lambda: i)]
    _l_(436726)
    _n_(436727, "plt", lambda: plt).grid=False
    _l_(436728)
    _c_(436731, _a_(436730, _n_(436729, "plt", lambda: plt), "xticks"), [])
    _l_(436732)
    _c_(436735, _a_(436734, _n_(436733, "plt", lambda: plt), "yticks"), [])
    _l_(436736)

    _c_(436743, _a_(436738, _n_(436737, "plt", lambda: plt), "imshow"), _n_(436739, "img", lambda: img), cmap=_a_(436742, _a_(436741, _n_(436740, "plt", lambda: plt), "cm"), "binary"))
    _l_(436744)
    predicted_label = _c_(436748, _a_(436746, _n_(436745, "np", lambda: np), "argmax"), _n_(436747, "predictions_array", lambda: predictions_array))
    _l_(436749)

    if _n_(436750, "predicted_label", lambda: predicted_label) == _n_(436751, "true_label", lambda: true_label):
        _l_(436754)

        color = 'blue'
        _l_(436752)
    else:
        color = 'red'
        _l_(436753)
    
    _c_(436767, _a_(436756, _n_(436755, "plt", lambda: plt), "xlabel"), _c_(436765, _a_(436757, '{}{:2.0f}%({})', "format"), _n_(436758, "class_names", lambda: class_names)[_n_(436759, "predicted_label", lambda: predicted_label)], 100*_a_(436761, _n_(436760, "np", lambda: np), "max")[_n_(436762, "predictions_array", lambda: predictions_array)], _n_(436763, "class_names", lambda: class_names)[_n_(436764, "true_label", lambda: true_label)]),color=_n_(436766, "color", lambda: color))
    _l_(436768)

def plot_value_array(i, predictions_array, true_label):
    _l_(436808)

    predictions_array, true_label = _n_(436770, "predictions_array", lambda: predictions_array), _n_(436771, "true_label", lambda: true_label)[_n_(436772, "i", lambda: i)]
    _l_(436773)
    _n_(436774, "plt", lambda: plt).grid=False
    _l_(436775)
    _c_(436780, _a_(436777, _n_(436776, "plt", lambda: plt), "xticks"), _c_(436779, _n_(436778, "range", lambda: range), 10))
    _l_(436781)
    _c_(436784, _a_(436783, _n_(436782, "plt", lambda: plt), "yticks"), [])
    _l_(436785)
    thisplot = _c_(436791, _a_(436787, _n_(436786, "plt", lambda: plt), "bar"), _c_(436789, _n_(436788, "range", lambda: range), 10), _n_(436790, "predictions_array", lambda: predictions_array), color='#777777')
    _l_(436792)
    predicted_label = _c_(436796, _a_(436794, _n_(436793, "np", lambda: np), "argmax"), _n_(436795, "predictions_array", lambda: predictions_array))
    _l_(436797)

    _c_(436801, _a_(436800, _n_(436798, "thisplot", lambda: thisplot)[_n_(436799, "predicted_label", lambda: predicted_label)], "set_color"), 'red')
    _l_(436802)
    _c_(436806, _a_(436805, _n_(436803, "thisplot", lambda: thisplot)[_n_(436804, "true_label", lambda: true_label)], "set_color"), 'blue')
    _l_(436807)

i = 0
_l_(436809)
_c_(436812, _a_(436811, _n_(436810, "plt", lambda: plt), "figure"), figsize=(6,3))
_l_(436813)
_c_(436816, _a_(436815, _n_(436814, "plt", lambda: plt), "subplot"), 1,2,1)
_l_(436817)
_c_(436824, _n_(436818, "plot_image", lambda: plot_image), _n_(436819, "i", lambda: i), _n_(436820, "predictions", lambda: predictions)[_n_(436821, "i", lambda: i)], _n_(436822, "test_labels", lambda: test_labels), _n_(436823, "test_images", lambda: test_images))
_l_(436825)
_c_(436828, _a_(436827, _n_(436826, "plt", lambda: plt), "subplot"), 1,2,2)
_l_(436829)
_c_(436835, _n_(436830, "plot_value_array", lambda: plot_value_array), _n_(436831, "i", lambda: i), _n_(436832, "predictions", lambda: predictions)[_n_(436833, "i", lambda: i)],  _n_(436834, "test_labels", lambda: test_labels))
_l_(436836)