# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyDataset(_a_(589413, _a_(589412, _a_(589411, _n_(589410, "torch", lambda: torch), "utils"), "data"), "Dataset")):
    _l_(589449)

    def __init__(self, examples):
        _l_(589420)

        _n_(589414, "self", lambda: self).encodings = _n_(589415, "examples", lambda: examples)
        _l_(589416)
        _n_(589417, "self", lambda: self).labels = _n_(589418, "examples", lambda: examples)['labels']
        _l_(589419)

    def __getitem__(self, idx):
        _l_(589442)

        item = {_n_(589421, "k", lambda: k): _c_(589426, _a_(589423, _n_(589422, "torch", lambda: torch), "tensor"), _n_(589424, "v", lambda: v)[_n_(589425, "idx", lambda: idx)]) for k, v in _c_(589430, _a_(589429, _a_(589428, _n_(589427, "self", lambda: self), "encodings"), "items"))}
        _l_(589431)
        _n_(589432, "item", lambda: item)["labels"] = _c_(589438, _a_(589434, _n_(589433, "torch", lambda: torch), "tensor"), [_a_(589436, _n_(589435, "self", lambda: self), "labels")[_n_(589437, "idx", lambda: idx)]])
        _l_(589439)
        aux = _n_(589440, "item", lambda: item)
        _l_(589441)
        return aux

    def __len__(self):
        _l_(589448)

        aux = _c_(589446, _n_(589443, "len", lambda: len), _a_(589445, _n_(589444, "self", lambda: self), "labels"))
        _l_(589447)

        return aux

train_data=_c_(589452, _n_(589450, "MyDataset", lambda: MyDataset), _n_(589451, "train_data", lambda: train_data))
_l_(589453)