# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75842262/i-am-getting-an-attribute-error-when-creating-a-pytorch-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from torch import nn
  _l_(607658)

except ImportError:
  pass
try:
  import segmentation_models_pytorch as smp
  _l_(607660)

except ImportError:
  pass
try:
  from segmentation_models_pytorch.losses import DiceLoss
  _l_(607662)

except ImportError:
  pass
class segmentationmodels():
  _l_(607704)

  def __init__(self):
    _l_(607676)

    _c_(607667, _a_(607666, _n_(607663, "super", lambda: super)(_n_(607664, "segmentationmodels", lambda: segmentationmodels),_n_(607665, "self", lambda: self)), "__init__"))
    _l_(607668)
    _n_(607669, "self", lambda: self).arc=_c_(607674, _a_(607671, _n_(607670, "smp", lambda: smp), "Unet"), encoder_name=_n_(607672, "ENCODER", lambda: ENCODER),
        encoder_weights=_n_(607673, "weights", lambda: weights),
        in_channels=3,
        classes=1,
        activation=None
    )
    _l_(607675)
  def forward(self,images,mask=None):
    _l_(607703)

    logits=_c_(607680, _a_(607678, _n_(607677, "self", lambda: self), "arc"), _n_(607679, "images", lambda: images))
    _l_(607681)
    if _n_(607682, "mask", lambda: mask) != None:
      _l_(607700)

      loss1=_c_(607687, _c_(607684, _n_(607683, "DiceLoss", lambda: DiceLoss), mode='binary'), _n_(607685, "logits", lambda: logits),_n_(607686, "mask", lambda: mask))
      _l_(607688)
      loss2=_c_(607694, _c_(607691, _a_(607690, _n_(607689, "nn", lambda: nn), "BCEWithLogitsLoss")), _n_(607692, "logits", lambda: logits),_n_(607693, "mask", lambda: mask))
      _l_(607695)
      aux = _n_(607696, "logits", lambda: logits),_n_(607697, "loss1", lambda: loss1)+_n_(607698, "loss2", lambda: loss2)
      _l_(607699)
      return aux
    aux = _n_(607701, "logits", lambda: logits)
    _l_(607702)
    return aux
model=_c_(607706, _n_(607705, "segmentationmodels", lambda: segmentationmodels))
_l_(607707)
_c_(607711, _a_(607709, _n_(607708, "model", lambda: model), "to"), _n_(607710, "DEVICE", lambda: DEVICE))
_l_(607712)