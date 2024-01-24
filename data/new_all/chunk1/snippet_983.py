# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59338360/how-do-i-resolve-typeerror-not-supported-between-instances-of-int-and-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(388539, _a_(388531, _n_(388530, "model", lambda: model), "fit_generator"), generator = _n_(388532, "train_generator", lambda: train_generator),
    #validation_data=val_generator,
    epochs = _n_(388533, "epochs", lambda: epochs), 
    steps_per_epoch = 17, 
    callbacks = [_n_(388534, "csvlogger", lambda: csvlogger), _n_(388535, "reduce_lr", lambda: reduce_lr), _n_(388536, "model_checkpoint", lambda: model_checkpoint)], 
    max_queue_size = 48,
    workers = _c_(388538, _n_(388537, "cpu_count", lambda: cpu_count)) - 2,
    use_multiprocessing = True,
)
_l_(388540)

_c_(388546, _n_(388541, "print", lambda: print), _c_(388545, _a_(388543, _n_(388542, "model", lambda: model), "evaluate_generator"), generator = _n_(388544, "test_generator", lambda: test_generator)))
_l_(388547)