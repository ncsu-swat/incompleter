# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74859282/got-typeerror-when-adding-return-indices-true-to-nn-maxpool2d-in-pytorch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
encoder = _c_(591244, _a_(591242, _c_(591241, _n_(591240, "Encoder", lambda: Encoder)), "to"), _n_(591243, "device", lambda: device))
_l_(591245)
decoder = _c_(591250, _a_(591248, _c_(591247, _n_(591246, "Decoder", lambda: Decoder)), "to"), _n_(591249, "device", lambda: device))
_l_(591251)
test_img = _c_(591255, _a_(591253, _n_(591252, "torch", lambda: torch), "unsqueeze"), _n_(591254, "train_data", lambda: train_data)[0], dim=0)
_l_(591256)
codes = _c_(591259, _n_(591257, "encoder", lambda: encoder), _n_(591258, "test_img", lambda: test_img))
_l_(591260)
_c_(591266, _n_(591261, "print", lambda: print), _a_(591265, _c_(591264, _n_(591262, "decoder", lambda: decoder), _n_(591263, "codes", lambda: codes)), "shape"))
_l_(591267)