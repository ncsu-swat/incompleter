# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model_checkpoint = "xlm-roberta-large-finetuned-conll03-english"
_l_(583987)
tokenizer = _c_(583991, _a_(583989, _n_(583988, "AutoTokenizer", lambda: AutoTokenizer), "from_pretrained"), _n_(583990, "model_checkpoint", lambda: model_checkpoint),add_prefix_space=True)
_l_(583992)