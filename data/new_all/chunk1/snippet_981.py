# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59338360/how-do-i-resolve-typeerror-not-supported-between-instances-of-int-and-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CustomModelCheckpoint(_n_(398168, "Callback", lambda: Callback)):
    _l_(398198)


    def __init__(self, model_parallel, path):
        _l_(398183)


        _c_(398173, _a_(398172, _n_(398169, "super", lambda: super)(_n_(398170, "CustomModelCheckpoint", lambda: CustomModelCheckpoint), _n_(398171, "self", lambda: self)), "__init__"))
        _l_(398174)

        _n_(398175, "self", lambda: self).save_model = _n_(398176, "model_parallel", lambda: model_parallel)
        _l_(398177)
        _n_(398178, "self", lambda: self).path = _n_(398179, "path", lambda: path)
        _l_(398180)
        _n_(398181, "self", lambda: self).nb_epoch = 0
        _l_(398182)

    def on_epoch_end(self, epoch, logs=None):
        _l_(398197)

        _n_(398184, "self", lambda: self).nb_epoch += 1
        _l_(398185)
        _c_(398195, _a_(398188, _a_(398187, _n_(398186, "self", lambda: self), "save_model"), "save"), _a_(398190, _n_(398189, "self", lambda: self), "path") + _c_(398194, _n_(398191, "str", lambda: str), _a_(398193, _n_(398192, "self", lambda: self), "nb_epoch")) + '.hdf5')
        _l_(398196)


i3d = _c_(398200, _n_(398199, "i3d_modified", lambda: i3d_modified), weights = 'rgb_imagenet_and_kinetics')
_l_(398201)
model = _c_(398205, _a_(398203, _n_(398202, "i3d", lambda: i3d), "i3d_flattened"), num_classes = _n_(398204, "num_classes", lambda: num_classes))
_l_(398206)
optim = _c_(398208, _n_(398207, "SGD", lambda: SGD), lr = 0.01, momentum = 0.9)
_l_(398209)

reduce_lr = _c_(398211, _n_(398210, "ReduceLROnPlateau", lambda: ReduceLROnPlateau), monitor='val_loss', factor = 0.1, patience = 10)
_l_(398212)
csvlogger = _c_(398215, _n_(398213, "CSVLogger", lambda: CSVLogger), 'i3d_'+_n_(398214, "model_name", lambda: model_name)+'.csv')
_l_(398216)