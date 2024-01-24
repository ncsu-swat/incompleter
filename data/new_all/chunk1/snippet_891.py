# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51990034/simple-lstm-model-no-attr-named-xlacompile-in-name-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(407848, _n_(407847, "Sequential", lambda: Sequential))
_l_(407849)
_c_(407856, _a_(407851, _n_(407850, "model", lambda: model), "add"), _c_(407855, _n_(407852, "Embedding", lambda: Embedding), 400001, _n_(407853, "emb_dim", lambda: emb_dim), trainable=False, input_length = 56, weights = [_n_(407854, "emb_matrix", lambda: emb_matrix)]))
_l_(407857)
_c_(407862, _a_(407859, _n_(407858, "model", lambda: model), "add"), _c_(407861, _n_(407860, "LSTM", lambda: LSTM), 128, return_sequences=False))
_l_(407863)
_c_(407868, _a_(407865, _n_(407864, "model", lambda: model), "add"), _c_(407867, _n_(407866, "Dense", lambda: Dense), 5, activation='softmax'))
_l_(407869)
_c_(407872, _a_(407871, _n_(407870, "model", lambda: model), "summary"))
_l_(407873)
_c_(407878, _a_(407875, _n_(407874, "model", lambda: model), "fit"), _n_(407876, "train_in", lambda: train_in), _n_(407877, "train_out", lambda: train_out), epochs = 50, batch_size = 32, shuffle=True)
_l_(407879)