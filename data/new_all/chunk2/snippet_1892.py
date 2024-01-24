# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42628141/attributeerror-module-tensorflow-has-no-attribute-streaming-accuracy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
accuracy = _c_(474737, _a_(474734, _n_(474733, "tf", lambda: tf), "streaming_accuracy"), _n_(474735, "y_pred", lambda: y_pred),_n_(474736, "y_true", lambda: y_true),name='acc')
_l_(474738)
recall = _c_(474743, _a_(474740, _n_(474739, "tf", lambda: tf), "streaming_recall"), _n_(474741, "y_pred", lambda: y_pred),_n_(474742, "y_true", lambda: y_true),name='acc')
_l_(474744)
precision = _c_(474749, _a_(474746, _n_(474745, "tf", lambda: tf), "streaming_precision"), _n_(474747, "y_pred", lambda: y_pred),_n_(474748, "y_true", lambda: y_true),name='acc')
_l_(474750)
confusion = _c_(474757, _a_(474752, _n_(474751, "tf", lambda: tf), "confuson_matrix"), _n_(474753, "Labels", lambda: Labels), _n_(474754, "y_pred", lambda: y_pred),num_classes=10,dtype=_a_(474756, _n_(474755, "tf", lambda: tf), "float32"),name='conf')
_l_(474758)