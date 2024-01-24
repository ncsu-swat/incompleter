# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyDataset(_a_(580049, _a_(580048, _a_(580047, _n_(580046, "torch", lambda: torch), "utils"), "data"), "Dataset")):
    _l_(580097)

    def __init__(self, examples):
        _l_(580064)

        _n_(580050, "self", lambda: self).encodings = _n_(580051, "examples", lambda: examples)
        _l_(580052)
        _c_(580056, _n_(580053, "print", lambda: print), _a_(580055, _n_(580054, "self", lambda: self), "encodings"))
        _l_(580057)
        _c_(580059, _n_(580058, "print", lambda: print))
        _l_(580060)
        _n_(580061, "self", lambda: self).labels = _n_(580062, "examples", lambda: examples)['labels']
        _l_(580063)

    def __getitem__(self, idx):
        _l_(580090)

        item = {_n_(580065, "k", lambda: k): _c_(580070, _a_(580067, _n_(580066, "torch", lambda: torch), "tensor"), _n_(580068, "v", lambda: v)[_n_(580069, "idx", lambda: idx)]) for k, v in _c_(580074, _a_(580073, _a_(580072, _n_(580071, "self", lambda: self), "encodings"), "items"))}
        _l_(580075)
        _c_(580078, _n_(580076, "print", lambda: print), _n_(580077, "item", lambda: item))
        _l_(580079)
        _n_(580080, "item", lambda: item)["labels"] = _c_(580086, _a_(580082, _n_(580081, "torch", lambda: torch), "tensor"), [_a_(580084, _n_(580083, "self", lambda: self), "labels")[_n_(580085, "idx", lambda: idx)]])
        _l_(580087)
        aux = _n_(580088, "item", lambda: item)
        _l_(580089)
        return aux

    def __len__(self):
        _l_(580096)

        aux = _c_(580094, _n_(580091, "len", lambda: len), _a_(580093, _n_(580092, "self", lambda: self), "labels"))
        _l_(580095)

        return aux