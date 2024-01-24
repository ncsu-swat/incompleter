# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70621634/typeerror-forward-got-an-unexpected-keyword-argument-input-ids
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
tokenizer = _c_(394364, _a_(394363, _a_(394362, _n_(394361, "tr", lambda: tr), "RobertaTokenizer"), "from_pretrained"), "/home/pc/unbiased_toxic_roberta")
_l_(394365)
train_encodings = _c_(394368, _n_(394366, "tokenizer", lambda: tokenizer), _n_(394367, "train_texts", lambda: train_texts), truncation=True, padding=True, max_length=512, return_tensors="pt")
_l_(394369)


class SEDataset(_a_(394373, _a_(394372, _a_(394371, _n_(394370, "torch", lambda: torch), "utils"), "data"), "Dataset")):
    _l_(394409)

    def __init__(self, encodings, labels):
        _l_(394380)

        _n_(394374, "self", lambda: self).encodings = _n_(394375, "encodings", lambda: encodings)
        _l_(394376)
        _n_(394377, "self", lambda: self).labels = _n_(394378, "labels", lambda: labels)
        _l_(394379)

    def __getitem__(self, idx):
        _l_(394402)

        item = {_n_(394381, "key", lambda: key): _c_(394386, _a_(394383, _n_(394382, "torch", lambda: torch), "tensor"), _n_(394384, "val", lambda: val)[_n_(394385, "idx", lambda: idx)]) for key, val in _c_(394390, _a_(394389, _a_(394388, _n_(394387, "self", lambda: self), "encodings"), "items"))}
        _l_(394391)
        _n_(394392, "item", lambda: item)['labels'] = _c_(394398, _a_(394394, _n_(394393, "torch", lambda: torch), "tensor"), _a_(394396, _n_(394395, "self", lambda: self), "labels")[_n_(394397, "idx", lambda: idx)])
        _l_(394399)
        aux = _n_(394400, "item", lambda: item)
        _l_(394401)
        return aux

    def __len__(self):
        _l_(394408)

        aux = _c_(394406, _n_(394403, "len", lambda: len), _a_(394405, _n_(394404, "self", lambda: self), "labels"))
        _l_(394407)
        return aux

train_data = _c_(394413, _n_(394410, "SEDataset", lambda: SEDataset), _n_(394411, "train_encodings", lambda: train_encodings), _n_(394412, "train_labels", lambda: train_labels))
_l_(394414)



def compute_metrics(eval_pred):
    _l_(394432)

    
    logits, labels = _n_(394415, "eval_pred", lambda: eval_pred)
    _l_(394416)
   

    predictions = _c_(394420, _a_(394418, _n_(394417, "np", lambda: np), "argmax"), _n_(394419, "logits", lambda: logits), axis=-1)
    _l_(394421)
    
    acc = _c_(394426, _a_(394423, _n_(394422, "np", lambda: np), "sum"), _n_(394424, "predictions", lambda: predictions) == _n_(394425, "labels", lambda: labels)) / _a_(394428, _n_(394427, "predictions", lambda: predictions), "shape")[0]
    _l_(394429)
    aux = {"accuracy" : _n_(394430, "acc", lambda: acc)}
    _l_(394431)
    
    return aux