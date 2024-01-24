# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71079469/attributeerror-nonetype-object-has-no-attribute-name-neural-style-transfe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    _l_(582424)

except ImportError:
    pass

target_image_path = 'test/Stil/portrait.jpg'
_l_(582425)
style_ref_image_path = 'test/Stil/style_reference.jpg'
_l_(582426)

width, height = _a_(582430, _c_(582429, _n_(582427, "load_img", lambda: load_img), _n_(582428, "target_image_path", lambda: target_image_path)), "size")
_l_(582431)
img_height = 400
_l_(582432)
img_width = _c_(582437, _n_(582433, "int", lambda: int), _n_(582434, "width", lambda: width) * _n_(582435, "img_height", lambda: img_height) / _n_(582436, "height", lambda: height))
_l_(582438)
try:
    import numpy as np
    _l_(582440)

except ImportError:
    pass
try:
    from tensorflow.keras.applications import vgg19
    _l_(582442)

except ImportError:
    pass

def preprocess_image(image_path):
    _l_(582465)

    img = _c_(582447, _n_(582443, "load_img", lambda: load_img), _n_(582444, "image_path", lambda: image_path), target_size = (_n_(582445, "img_height", lambda: img_height), _n_(582446, "img_width", lambda: img_width)))
    _l_(582448)
    img = _c_(582451, _n_(582449, "img_to_array", lambda: img_to_array), _n_(582450, "img", lambda: img))
    _l_(582452)
    img = _c_(582456, _a_(582454, _n_(582453, "np", lambda: np), "expand_dims"), _n_(582455, "img", lambda: img), axis=0)
    _l_(582457)
    img = _c_(582461, _a_(582459, _n_(582458, "vgg19", lambda: vgg19), "preprocess_input"), _n_(582460, "img", lambda: img))
    _l_(582462)
    aux = _n_(582463, "img", lambda: img)
    _l_(582464)
    return aux
def deprocess_image(x):
    _l_(582483)

    _n_(582466, "x", lambda: x)[:, :, 0] += 103.939
    _l_(582467)
    _n_(582468, "x", lambda: x)[:, :, 1] += 116.779
    _l_(582469)
    _n_(582470, "x", lambda: x)[:, :, 2] += 123.68
    _l_(582471)
    x = _n_(582472, "x", lambda: x)[:, :, ::-1]
    _l_(582473)
    x = _c_(582479, _a_(582478, _c_(582477, _a_(582475, _n_(582474, "np", lambda: np), "clip"), _n_(582476, "x", lambda: x), 0, 255), "astype"), 'uint8')
    _l_(582480)
    aux = _n_(582481, "x", lambda: x)
    _l_(582482)
    return aux
try:
    import tensorflow as tf
    _l_(582485)

except ImportError:
    pass
try:
    import tensorflow.compat.v1 as tfv1
    _l_(582487)

except ImportError:
    pass
_c_(582490, _a_(582489, _n_(582488, "tfv1", lambda: tfv1), "disable_eager_execution")) 
_l_(582491) 
try:
    from tensorflow.keras import backend as K
    _l_(582493)

except ImportError:
    pass

target_image = _c_(582499, _a_(582495, _n_(582494, "K", lambda: K), "constant"), _c_(582498, _n_(582496, "preprocess_image", lambda: preprocess_image), _n_(582497, "target_image_path", lambda: target_image_path)))
_l_(582500)
style_ref_image = _c_(582506, _a_(582502, _n_(582501, "K", lambda: K), "constant"), _c_(582505, _n_(582503, "preprocess_image", lambda: preprocess_image), _n_(582504, "style_ref_image_path", lambda: style_ref_image_path)))
_l_(582507)
combination_image = _c_(582512, _a_(582509, _n_(582508, "K", lambda: K), "placeholder"), (1, _n_(582510, "img_height", lambda: img_height), _n_(582511, "img_width", lambda: img_width), 3))
_l_(582513)

input_tensor = _c_(582519, _a_(582515, _n_(582514, "K", lambda: K), "concatenate"), [_n_(582516, "target_image", lambda: target_image), _n_(582517, "style_ref_image", lambda: style_ref_image), _n_(582518, "combination_image", lambda: combination_image)], axis=0)
_l_(582520)
model = _c_(582524, _a_(582522, _n_(582521, "vgg19", lambda: vgg19), "VGG19"), input_tensor=_n_(582523, "input_tensor", lambda: input_tensor), weights='imagenet', include_top=False)
_l_(582525)

def content_loss(base, combination):
    _l_(582535)

    aux = _c_(582533, _a_(582527, _n_(582526, "K", lambda: K), "sum"), _c_(582532, _a_(582529, _n_(582528, "K", lambda: K), "square"), _n_(582530, "combination", lambda: combination) - _n_(582531, "base", lambda: base)))
    _l_(582534)
    return aux

def gram_matrix(x):
    _l_(582555)

    features = _c_(582542, _a_(582537, _n_(582536, "K", lambda: K), "batch_flatten"), _c_(582541, _a_(582539, _n_(582538, "K", lambda: K), "permute_dimensions"), _n_(582540, "x", lambda: x), (2, 0, 1)))
    _l_(582543)
    gram = _c_(582551, _a_(582545, _n_(582544, "K", lambda: K), "dot"), _n_(582546, "features", lambda: features), _c_(582550, _a_(582548, _n_(582547, "K", lambda: K), "transpose"), _n_(582549, "features", lambda: features)))
    _l_(582552)
    aux = _n_(582553, "gram", lambda: gram)
    _l_(582554)
    return aux
def style_loss(style, combination):
    _l_(582579)

    S = _c_(582558, _n_(582556, "gram_matrix", lambda: gram_matrix), _n_(582557, "style", lambda: style))
    _l_(582559)
    C = _c_(582562, _n_(582560, "gram_matrix", lambda: gram_matrix), _n_(582561, "combination", lambda: combination))
    _l_(582563)
    channels = 3
    _l_(582564)
    size = _n_(582565, "img_height", lambda: img_height) * _n_(582566, "img_width", lambda: img_width)
    _l_(582567)
    aux = _c_(582575, _a_(582569, _n_(582568, "K", lambda: K), "sum"), _c_(582574, _a_(582571, _n_(582570, "K", lambda: K), "square"), _n_(582572, "S", lambda: S) - _n_(582573, "C", lambda: C))) / (4. * (_n_(582576, "channels", lambda: channels) ** 2) * (_n_(582577, "size", lambda: size) ** 2))
    _l_(582578)
    return aux
def total_variation_loss(x):
    _l_(582607)

    a = _c_(582587, _a_(582581, _n_(582580, "K", lambda: K), "square"), _n_(582582, "x", lambda: x)[:, :_n_(582583, "img_height", lambda: img_height) - 1, :_n_(582584, "img_width", lambda: img_width) - 1, :] - _n_(582585, "x", lambda: x)[:, 1:, :_n_(582586, "img_width", lambda: img_width) - 1, :])
    _l_(582588)
    b = _c_(582596, _a_(582590, _n_(582589, "K", lambda: K), "square"), _n_(582591, "x", lambda: x)[:,:_n_(582592, "img_height", lambda: img_height) - 1, :_n_(582593, "img_width", lambda: img_width) - 1, :] - _n_(582594, "x", lambda: x)[:, :_n_(582595, "img_height", lambda: img_height) - 1,  1:, :])
    _l_(582597)
    aux = _c_(582605, _a_(582599, _n_(582598, "K", lambda: K), "sum"), _c_(582604, _a_(582601, _n_(582600, "K", lambda: K), "pow"), _n_(582602, "a", lambda: a) + _n_(582603, "b", lambda: b), 1.25))
    _l_(582606)
    return aux
outputs_dict = _c_(582615, _n_(582608, "dict", lambda: dict), [(_a_(582610, _n_(582609, "layer", lambda: layer), "name"), _a_(582612, _n_(582611, "layer", lambda: layer), "output")) for layer in _a_(582614, _n_(582613, "model", lambda: model), "layers")])
_l_(582616)
content_layer = 'block5_conv2'
_l_(582617)
style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']
_l_(582618)

total_variation_weight = 1e-4
_l_(582619)
style_weight = 1.
_l_(582620)
content_weight = 0.025
_l_(582621)

loss = _c_(582624, _a_(582623, _n_(582622, "tf", lambda: tf), "Variable"), 0.)
_l_(582625)
layer_features = _n_(582626, "outputs_dict", lambda: outputs_dict)[_n_(582627, "content_layer", lambda: content_layer)]
_l_(582628)
target_image_features = _n_(582629, "layer_features", lambda: layer_features)[0, :, :, :]
_l_(582630)
combination_features = _n_(582631, "layer_features", lambda: layer_features)[2, :, :, :]
_l_(582632)
_c_(582640, _a_(582634, _n_(582633, "loss", lambda: loss), "assign_add"), _n_(582635, "content_weight", lambda: content_weight) * _c_(582639, _n_(582636, "content_loss", lambda: content_loss), _n_(582637, "target_image_features", lambda: target_image_features), _n_(582638, "combination_features", lambda: combination_features)))
_l_(582641)

for layer_name in _n_(582642, "style_layers", lambda: style_layers):
    _l_(582664)

    layer_features = _n_(582643, "outputs_dict", lambda: outputs_dict)[_n_(582644, "layer_name", lambda: layer_name)]
    _l_(582645)
    style_ref_features = _n_(582646, "layer_features", lambda: layer_features)[1, :, :, :]
    _l_(582647)
    combination_features = _n_(582648, "layer_features", lambda: layer_features)[2, :, :, :]
    _l_(582649)
    sl = _c_(582653, _n_(582650, "style_loss", lambda: style_loss), _n_(582651, "style_ref_features", lambda: style_ref_features), _n_(582652, "combination_features", lambda: combination_features))
    _l_(582654)
    _c_(582662, _a_(582656, _n_(582655, "loss", lambda: loss), "assign_add"), (_n_(582657, "style_weight", lambda: style_weight) / _c_(582660, _n_(582658, "len", lambda: len), _n_(582659, "style_layers", lambda: style_layers))) * _n_(582661, "sl", lambda: sl))
    _l_(582663)
with _c_(582667, _a_(582666, _n_(582665, "tf", lambda: tf), "GradientTape")) as gtape:
    _l_(582680)

    _c_(582674, _a_(582669, _n_(582668, "loss", lambda: loss), "assign_add"), _n_(582670, "total_variation_weight", lambda: total_variation_weight) * _c_(582673, _n_(582671, "total_variation_loss", lambda: total_variation_loss), _n_(582672, "combination_image", lambda: combination_image)))
    _l_(582675)
    _c_(582678, _n_(582676, "print", lambda: print), 'loss = ', _n_(582677, "loss", lambda: loss))
    _l_(582679)

grads = _c_(582685, _a_(582682, _n_(582681, "gtape", lambda: gtape), "gradient"), _n_(582683, "loss", lambda: loss), _n_(582684, "combination_image", lambda: combination_image))
_l_(582686)
fetch_loss_and_grads = _c_(582692, _a_(582688, _n_(582687, "K", lambda: K), "function"), [_n_(582689, "combination_image", lambda: combination_image)], [_n_(582690, "loss", lambda: loss), _n_(582691, "grads", lambda: grads)])
_l_(582693)

class Evaluator(_n_(582694, "object", lambda: object)):
    _l_(582747)

    def __init__(self):
        _l_(582699)

        _n_(582695, "self", lambda: self).loss_value = None
        _l_(582696)
        _n_(582697, "self", lambda: self).grads_values = None
        _l_(582698)
    def loss(self, x):
        _l_(582730)

        assert _a_(582701, _n_(582700, "self", lambda: self), "loss_value") is None
        _l_(582702)
        x = _c_(582707, _a_(582704, _n_(582703, "x", lambda: x), "reshape"), (1, _n_(582705, "img_height", lambda: img_height), _n_(582706, "img_width", lambda: img_width), 3))
        _l_(582708)
        outs = _c_(582711, _n_(582709, "fetch_loss_and_grads", lambda: fetch_loss_and_grads), [_n_(582710, "x", lambda: x)])
        _l_(582712)
        loss_value = _n_(582713, "outs", lambda: outs)[0]
        _l_(582714)
        grad_values = _c_(582719, _a_(582718, _c_(582717, _a_(582716, _n_(582715, "outs", lambda: outs)[1], "flatten")), "astype"), 'float64')
        _l_(582720)
        _n_(582721, "self", lambda: self).loss_value = _n_(582722, "loss_value", lambda: loss_value)
        _l_(582723)
        _n_(582724, "self", lambda: self).grad_values = _n_(582725, "grad_values", lambda: grad_values)
        _l_(582726)
        aux = _a_(582728, _n_(582727, "self", lambda: self), "loss_value")
        _l_(582729)
        return aux
    def grads(self, x):
        _l_(582746)

        assert _a_(582732, _n_(582731, "self", lambda: self), "loss_value") is not None
        _l_(582733)
        grad_values = _c_(582738, _a_(582735, _n_(582734, "np", lambda: np), "copy"), _a_(582737, _n_(582736, "self", lambda: self), "grad_values"))
        _l_(582739)
        _n_(582740, "self", lambda: self).loss_value = None
        _l_(582741)
        _n_(582742, "self", lambda: self).grad_values = None
        _l_(582743)
        aux = _n_(582744, "grad_values", lambda: grad_values)
        _l_(582745)
        return aux
evaluator = _c_(582749, _n_(582748, "Evaluator", lambda: Evaluator))
_l_(582750)
try:
    from scipy.optimize import fmin_l_bfgs_b
    _l_(582752)

except ImportError:
    pass
try:
    import imageio
    _l_(582754)

except ImportError:
    pass
try:
    import time
    _l_(582756)

except ImportError:
    pass

result_prefix = 'my_result'
_l_(582757)
iterations = 20
_l_(582758)
x = _c_(582761, _n_(582759, "preprocess_image", lambda: preprocess_image), _n_(582760, "target_image_path", lambda: target_image_path))
_l_(582762)
x = _c_(582765, _a_(582764, _n_(582763, "x", lambda: x), "flatten")) 
_l_(582766) 

for i in _c_(582769, _n_(582767, "range", lambda: range), _n_(582768, "iterations", lambda: iterations)):
    _l_(582821)

    _c_(582772, _n_(582770, "print", lambda: print), 'Start iteration: ', _n_(582771, "i", lambda: i))
    _l_(582773)
    start_time = _c_(582776, _a_(582775, _n_(582774, "time", lambda: time), "time"))
    _l_(582777)
    x, min_val, info = _c_(582784, _n_(582778, "fmin_l_bfgs_b", lambda: fmin_l_bfgs_b), _a_(582780, _n_(582779, "evaluator", lambda: evaluator), "loss"), _n_(582781, "x", lambda: x), fprime=_a_(582783, _n_(582782, "evaluator", lambda: evaluator), "grads"), maxfun=20)
    _l_(582785)
    _c_(582788, _n_(582786, "print", lambda: print), 'Current value of loss function: ', _n_(582787, "min_val", lambda: min_val))
    _l_(582789)
    img = _c_(582796, _a_(582793, _c_(582792, _a_(582791, _n_(582790, "x", lambda: x), "copy")), "reshape"), (_n_(582794, "img_height", lambda: img_height), _n_(582795, "img_width", lambda: img_width), 3))
    _l_(582797)
    img = _c_(582800, _n_(582798, "deprocess_image", lambda: deprocess_image), _n_(582799, "img", lambda: img))
    _l_(582801)
    fname = _n_(582802, "result_prefix", lambda: result_prefix) + '_at_iteration_%d.png' % _n_(582803, "i", lambda: i)
    _l_(582804)
    _c_(582809, _a_(582806, _n_(582805, "imageio", lambda: imageio), "imwrite"), _n_(582807, "fname", lambda: fname), _n_(582808, "img", lambda: img))
    _l_(582810)
    end_time = _c_(582813, _a_(582812, _n_(582811, "time", lambda: time), "time"))
    _l_(582814)
    _c_(582819, _n_(582815, "print", lambda: print), 'Iteration %d completed in %ds' % (_n_(582816, "i", lambda: i), _n_(582817, "end_time", lambda: end_time) - _n_(582818, "start_time", lambda: start_time)))
    _l_(582820)