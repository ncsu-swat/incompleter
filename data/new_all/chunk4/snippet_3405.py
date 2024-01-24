# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74859282/got-typeerror-when-adding-return-indices-true-to-nn-maxpool2d-in-pytorch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
encoder = _c_(630360, _a_(630358, _c_(630357, _n_(630356, "Encoder", lambda: Encoder)), "to"), _n_(630359, "device", lambda: device))
_l_(630361)
decoder = _c_(630366, _a_(630364, _c_(630363, _n_(630362, "Decoder", lambda: Decoder)), "to"), _n_(630365, "device", lambda: device))
_l_(630367)
test_img = _c_(630371, _a_(630369, _n_(630368, "torch", lambda: torch), "unsqueeze"), _n_(630370, "train_data", lambda: train_data)[0], dim=0)
_l_(630372)
_c_(630377, _n_(630373, "print", lambda: print), _c_(630376, _n_(630374, "encoder", lambda: encoder), _n_(630375, "test_img", lambda: test_img)))
_l_(630378)