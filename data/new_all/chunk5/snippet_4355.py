# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59260545/attributeerror-module-object-has-no-attribute-signature-tensorflow1-15-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(703259, _n_(703256, "load_model", lambda: load_model), "../../deepposekit-data/datasets/fly/best_model_densenet.h5",
    augmenter=_n_(703257, "augmenter", lambda: augmenter),
    generator=_n_(703258, "data_generator", lambda: data_generator),
)
_l_(703260)