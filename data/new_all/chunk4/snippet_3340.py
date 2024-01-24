# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bert_model = _c_(624491, _a_(624487, _n_(624486, "BertForTokenClassification", lambda: BertForTokenClassification), "from_pretrained"), _n_(624488, "model_checkpoint", lambda: model_checkpoint),
                        id2label=_n_(624489, "id2label", lambda: id2label),
                        label2id=_n_(624490, "label2id", lambda: label2id)
)
_l_(624492)
_a_(624494, _n_(624493, "bert_model", lambda: bert_model), "config").output_hidden_states=True
_l_(624495)