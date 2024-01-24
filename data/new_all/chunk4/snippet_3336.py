# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ori_label_list = []
_l_(602076)
for line in _n_(602077, "train_set", lambda: train_set):
    _l_(602081)

    ori_label_list += [_n_(602078, "entity", lambda: entity)['tag'] for entity in _n_(602079, "line", lambda: line)[1]]
    _l_(602080)

ori_label_list = _c_(602088, _n_(602082, "sorted", lambda: sorted), _c_(602087, _n_(602083, "list", lambda: list), _c_(602086, _n_(602084, "set", lambda: set), _n_(602085, "ori_label_list", lambda: ori_label_list))))
_l_(602089)

label_list = []
_l_(602090)
for prefix in 'BI':
    _l_(602095)

    label_list += [_n_(602091, "prefix", lambda: prefix) + '-' + _n_(602092, "x", lambda: x) for x in _n_(602093, "ori_label_list", lambda: ori_label_list)]
    _l_(602094)
label_list += ['O']
_l_(602096)
label_list = _c_(602103, _n_(602097, "sorted", lambda: sorted), _c_(602102, _n_(602098, "list", lambda: list), _c_(602101, _n_(602099, "set", lambda: set), _n_(602100, "label_list", lambda: label_list))))
_l_(602104)
label2id = {_n_(602105, "n", lambda: n):_n_(602106, "i", lambda: i) for i,n in _c_(602109, _n_(602107, "enumerate", lambda: enumerate), _n_(602108, "label_list", lambda: label_list))}
_l_(602110)
id2label= {_n_(602111, "i", lambda: i):_n_(602112, "n", lambda: n) for i,n in _c_(602115, _n_(602113, "enumerate", lambda: enumerate), _n_(602114, "label_list", lambda: label_list))}
_l_(602116)