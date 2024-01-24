# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64175246/keras-model-fit-giving-out-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
image_input = _c_(411811, _a_(411810, _a_(411809, _a_(411808, _n_(411807, "tf", lambda: tf), "keras"), "layers"), "Input"), shape=(299,299,3), name='image_input')
_l_(411812)
negative_input = _c_(411817, _a_(411816, _a_(411815, _a_(411814, _n_(411813, "tf", lambda: tf), "keras"), "layers"), "Input"), shape=(299,299,3), name='negative_input')
_l_(411818)

siamese = _c_(411824, _c_(411821, _n_(411819, "SiameseNet", lambda: SiameseNet), _n_(411820, "image_features_extract_model", lambda: image_features_extract_model)), [_n_(411822, "image_input", lambda: image_input), _n_(411823, "negative_input", lambda: negative_input)])
_l_(411825)

model = _c_(411832, _a_(411828, _a_(411827, _n_(411826, "tf", lambda: tf), "keras"), "Model"), inputs=[_n_(411829, "image_input", lambda: image_input), _n_(411830, "negative_input", lambda: negative_input)], outputs=_n_(411831, "siamese", lambda: siamese))
_l_(411833)

_c_(411842, _a_(411835, _n_(411834, "model", lambda: model), "compile"), optimizer=_c_(411840, _a_(411839, _a_(411838, _a_(411837, _n_(411836, "tf", lambda: tf), "keras"), "optimizers"), "Adam")), loss=_n_(411841, "triplet_loss", lambda: triplet_loss), metrics=['accuracy'])
_l_(411843)