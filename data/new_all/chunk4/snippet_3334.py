# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model_checkpoint = "SpanBERT/spanbert-base-cased"
_l_(614629)
tokenizer = _c_(614633, _a_(614631, _n_(614630, "BertTokenizer", lambda: BertTokenizer), "from_pretrained"), _n_(614632, "model_checkpoint", lambda: model_checkpoint),add_prefix_space=True)
_l_(614634)