# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51277748/keras-attributeerror-tensor-object-has-no-attribute-log
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def base_model():
   _l_(443503)

   model = _c_(443470, _n_(443469, "Sequential", lambda: Sequential))
   _l_(443471)
   _c_(443478, _a_(443473, _n_(443472, "model", lambda: model), "add"), _c_(443477, _n_(443474, "Dense", lambda: Dense), 50, input_dim=_a_(443476, _n_(443475, "X_train", lambda: X_train), "shape")[1], init='normal',     activation='sigmoid'))
   _l_(443479)
   _c_(443484, _a_(443481, _n_(443480, "model", lambda: model), "add"), _c_(443483, _n_(443482, "Dropout", lambda: Dropout), 0.5))
   _l_(443485)

   _c_(443490, _a_(443487, _n_(443486, "model", lambda: model), "add"), _c_(443489, _n_(443488, "Dense", lambda: Dense), 1, init='normal'))
   _l_(443491)
   sgd = _c_(443493, _n_(443492, "SGD", lambda: SGD), lr=0.01, momentum=0.8, decay=0.1, nesterov=False)
   _l_(443494)
   _c_(443499, _a_(443496, _n_(443495, "model", lambda: model), "compile"), loss=_n_(443497, "rmsle", lambda: rmsle), optimizer = _n_(443498, "sgd", lambda: sgd))# )'adam') #
   _l_(443500)# )'adam') #
   aux = _n_(443501, "model", lambda: model)
   _l_(443502)
   return aux

keras = _c_(443506, _n_(443504, "KerasRegressor", lambda: KerasRegressor), build_fn=_n_(443505, "base_model", lambda: base_model), nb_epoch=80, batch_size=1,verbose=1)
_l_(443507)
_c_(443512, _a_(443509, _n_(443508, "keras", lambda: keras), "fit"), _n_(443510, "X_train", lambda: X_train) ,_n_(443511, "y_train", lambda: y_train))
_l_(443513)