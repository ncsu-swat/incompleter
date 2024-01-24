# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
train_set = [
    [
        _n_(623738, "x", lambda: x)['text'],
        [{'start': _n_(623739, "y", lambda: y)["start"], 'end': _n_(623740, "y", lambda: y)["end"], 'tag': _n_(623741, "y", lambda: y)["label"], 'text': _n_(623742, "y", lambda: y)["ngram"]} for y in _n_(623743, "x", lambda: x)['spans']]
    ] for x in _n_(623744, "train_data", lambda: train_data)
]
_l_(623745)