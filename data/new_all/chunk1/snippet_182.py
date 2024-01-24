# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64665776/typeerror-cant-pickle-weakref-objects-when-pickling-a-deep-learning-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(415648, _n_(415647, "Sequential", lambda: Sequential))
_l_(415649)

_c_(415654, _a_(415651, _n_(415650, "model", lambda: model), "add"), _c_(415653, _n_(415652, "Dense", lambda: Dense), 30,activation='relu') )
_l_(415655)
_c_(415660, _a_(415657, _n_(415656, "model", lambda: model), "add"), _c_(415659, _n_(415658, "Dropout", lambda: Dropout), 0.5) ) 
_l_(415661) 
_c_(415666, _a_(415663, _n_(415662, "model", lambda: model), "add"), _c_(415665, _n_(415664, "Dense", lambda: Dense), 20,activation='relu') )
_l_(415667)
_c_(415672, _a_(415669, _n_(415668, "model", lambda: model), "add"), _c_(415671, _n_(415670, "Dropout", lambda: Dropout), 0.5) ) 
_l_(415673) 
_c_(415678, _a_(415675, _n_(415674, "model", lambda: model), "add"), _c_(415677, _n_(415676, "Dense", lambda: Dense), 20,activation='relu') )
_l_(415679)
_c_(415684, _a_(415681, _n_(415680, "model", lambda: model), "add"), _c_(415683, _n_(415682, "Dropout", lambda: Dropout), 0.5) )     
_l_(415685)     
_c_(415690, _a_(415687, _n_(415686, "model", lambda: model), "add"), _c_(415689, _n_(415688, "Dense", lambda: Dense), 1,activation='sigmoid') )
_l_(415691)

_c_(415694, _a_(415693, _n_(415692, "model", lambda: model), "compile"), optimizer='adam',loss='binary_crossentropy',metrics=['accuracy']) 
_l_(415695) 