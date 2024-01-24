# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54424933/typeerror-conv2dlayer-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
deconv4 = _c_(396379, _n_(396374, "Conv2d", lambda: Conv2d), _n_(396375, "deconv3_bn_relu", lambda: deconv3_bn_relu), 3, [5, 5], act=_a_(396377, _n_(396376, "tf", lambda: tf), "tanh"), padding='SAME', 
W_init=_n_(396378, "w_init", lambda: w_init), name='deconv4')
_l_(396380)

flow = _n_(396381, "deconv4", lambda: deconv4)[:, :, :, 0:2] 
_l_(396382) 