# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71143690/typeerror-expected-int32-passed-to-parameter-size-of-op-slice-got-4608-0
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def ourmodel(numberOfLSTMcells=3,n_timesteps_in=3000,n_features=61):
    _l_(393308)


    inp =_c_(393269, _n_(393266, "Input", lambda: Input), shape=(_n_(393267, "n_timesteps_in", lambda: n_timesteps_in), _n_(393268, "n_features", lambda: n_features)))
    _l_(393270)
    lstm= _c_(393275, _c_(393273, _n_(393271, "LSTM", lambda: LSTM), _n_(393272, "numberOfLSTMcells", lambda: numberOfLSTMcells),return_sequences=True, return_state=False), _n_(393274, "inp", lambda: inp))
    _l_(393276)
    flatten=_c_(393280, _c_(393278, _n_(393277, "Flatten", lambda: Flatten)), _n_(393279, "lstm", lambda: lstm))
    _l_(393281)
    fc=_c_(393285, _c_(393283, _n_(393282, "Dense", lambda: Dense), 64,activation='relu'), _n_(393284, "flatten", lambda: flatten))
    _l_(393286)
    fc=_c_(393290, _c_(393288, _n_(393287, "Dense", lambda: Dense), 32,activation='relu'), _n_(393289, "fc", lambda: fc))
    _l_(393291)
    out=_c_(393295, _c_(393293, _n_(393292, "Dense", lambda: Dense), 1,activation='sigmoid'), _n_(393294, "fc", lambda: fc))
    _l_(393296)

    model = _c_(393300, _n_(393297, "Model", lambda: Model), inputs=_n_(393298, "inp", lambda: inp), outputs=_n_(393299, "out", lambda: out))
    _l_(393301)
    _c_(393304, _a_(393303, _n_(393302, "model", lambda: model), "compile"), loss='binary_crossentropy', optimizer='adam', 
                  metrics=['accuracy'])
    _l_(393305)
    aux = _n_(393306, "model", lambda: model)
    _l_(393307)
    return aux

model=_c_(393310, _n_(393309, "ourmodel", lambda: ourmodel))
_l_(393311)
_c_(393316, _a_(393313, _n_(393312, "model", lambda: model), "fit"), _n_(393314, "data_array", lambda: data_array),y=_n_(393315, "label_array", lambda: label_array),batch_size=1024*0.1,epochs=50,verbose=0)
_l_(393317)