# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
train_examples ={'texts':[_n_(606579, "x", lambda: x)[0] for x in _n_(606580, "train_set", lambda: train_set)],'tag_names':[_n_(606581, "x", lambda: x)[1] for x in _n_(606582, "train_set", lambda: train_set)]}
_l_(606583)
train_data = _c_(606587, _n_(606584, "tokenize_and_align_labels", lambda: tokenize_and_align_labels), _n_(606585, "train_examples", lambda: train_examples),_n_(606586, "label2id", lambda: label2id))
_l_(606588)
_=_c_(606591, _a_(606590, _n_(606589, "train_data", lambda: train_data), "pop"), 'offset_mapping')
_l_(606592)