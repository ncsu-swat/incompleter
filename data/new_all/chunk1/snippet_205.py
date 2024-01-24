# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64175246/keras-model-fit-giving-out-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SiameseNet(_a_(381664, _a_(381663, _a_(381662, _n_(381661, "tf", lambda: tf), "keras"), "layers"), "Layer")):
  _l_(381687)


  def __init__(self, model):
    _l_(381672)

    _n_(381665, "self", lambda: self).model = _n_(381666, "model", lambda: model)  # This is the image feature extraction model (similar to InceptionV3)
    _l_(381667)  # This is the image feature extraction model (similar to InceptionV3)
    _c_(381670, _a_(381669, _n_(381668, "super", lambda: super)(), "__init__"))
    _l_(381671)

  def call(self, feat):
    _l_(381686)

    feats = _c_(381676, _a_(381674, _n_(381673, "self", lambda: self), "model"), _n_(381675, "feat", lambda: feat)[0])
    _l_(381677)
    nfeats = _c_(381681, _a_(381679, _n_(381678, "self", lambda: self), "model"), _n_(381680, "feat", lambda: feat)[1])
    _l_(381682)
    aux = [_n_(381683, "feats", lambda: feats), _n_(381684, "nfeats", lambda: nfeats)]
    _l_(381685)

    return aux