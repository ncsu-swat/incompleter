# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59494717/typeerror-tensor-object-is-not-callable-keras-bert
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
inputs = _a_(378070, _n_(378069, "model", lambda: model), "inputs")[:2] 
_l_(378071) 
layer_output = _a_(378075, _c_(378074, _a_(378073, _n_(378072, "model", lambda: model), "get_layer"), 'Encoder-12-FeedForward-Norm'), "output")  
_l_(378076)  
input_layer= _c_(378083, _c_(378081, _a_(378079, _a_(378078, _n_(378077, "keras", lambda: keras), "layers"), "Input"), shape=(_n_(378080, "SEQ_LEN", lambda: SEQ_LEN),768)), _n_(378082, "layer_output", lambda: layer_output))
_l_(378084)
conv_layer= _c_(378090, _c_(378088, _a_(378087, _a_(378086, _n_(378085, "keras", lambda: keras), "layers"), "Conv1D"), 100, kernel_size=3, activation='relu', data_format='channels_first'), _n_(378089, "input_layer", lambda: input_layer))   
_l_(378091)   
maxpool_layer = _c_(378097, _c_(378095, _a_(378094, _a_(378093, _n_(378092, "keras", lambda: keras), "layers"), "MaxPooling1D"), pool_size=4), _n_(378096, "conv_layer", lambda: conv_layer))
_l_(378098)
flat_layer= _c_(378104, _c_(378102, _a_(378101, _a_(378100, _n_(378099, "keras", lambda: keras), "layers"), "Flatten")), _n_(378103, "maxpool_layer", lambda: maxpool_layer))
_l_(378105)
outputs = _c_(378111, _c_(378109, _a_(378108, _a_(378107, _n_(378106, "keras", lambda: keras), "layers"), "Dense"), units=3, activation='softmax'), _n_(378110, "flat_layer", lambda: flat_layer))
_l_(378112)
model = _c_(378118, _a_(378115, _a_(378114, _n_(378113, "keras", lambda: keras), "models"), "Model"), _n_(378116, "inputs", lambda: inputs), _n_(378117, "outputs", lambda: outputs))
_l_(378119)
_c_(378125, _a_(378121, _n_(378120, "model", lambda: model), "compile"), _c_(378124, _n_(378122, "RAdam", lambda: RAdam), learning_rate =_n_(378123, "LR", lambda: LR)),loss='sparse_categorical_crossentropy',metrics=['sparse_categorical_accuracy'])
_l_(378126)