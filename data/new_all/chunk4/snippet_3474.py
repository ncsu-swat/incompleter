# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(634382, _a_(634378, _n_(634377, "AutoModelForTokenClassification", lambda: AutoModelForTokenClassification), "from_pretrained"), _n_(634379, "model_checkpoint", lambda: model_checkpoint),id2label=_n_(634380, "id2label", lambda: id2label),label2id=_n_(634381, "label2id", lambda: label2id),ignore_mismatched_sizes=True)
_l_(634383)
device = _c_(634390, _a_(634385, _n_(634384, "torch", lambda: torch), "device"), "cuda" if _c_(634389, _a_(634388, _a_(634387, _n_(634386, "torch", lambda: torch), "cuda"), "is_available")) else "cpu")
_l_(634391)
_c_(634395, _a_(634393, _n_(634392, "model", lambda: model), "to"), _n_(634394, "device", lambda: device))
_l_(634396)