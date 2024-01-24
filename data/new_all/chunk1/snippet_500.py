# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75936866/attributeerror-tensor-name-is-undefined-when-eager-execution-is-enabled
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(392072, _a_(392070, _n_(392069, "tf", lambda: tf), "control_dependencies"), _n_(392071, "update_ops", lambda: update_ops)):
    _l_(392093)

    with _c_(392075, _a_(392074, _n_(392073, "tf", lambda: tf), "GradientTape")) as tape:
        _l_(392092)

        optimizer = _c_(392081, _a_(392079, _a_(392078, _a_(392077, _n_(392076, "tf", lambda: tf), "keras"), "optimizers"), "SGD"), _n_(392080, "lr", lambda: lr), 0.9)
        _l_(392082)
        train_op = _c_(392089, _a_(392084, _n_(392083, "optimizer", lambda: optimizer), "minimize"), _n_(392085, "loss", lambda: loss), var_list=[_n_(392086, "labels", lambda: labels), _n_(392087, "outputs", lambda: outputs)], tape=_n_(392088, "tape", lambda: tape))
        _l_(392090)
        del tape
        _l_(392091)