# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64429461/typeerror-iteration-over-a-0-d-tensor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(397626, _n_(397622, "print", lambda: print), _c_(397625, _n_(397623, "len", lambda: len), _n_(397624, "train_ds", lambda: train_ds))) # 44
_l_(397627) # 44
_c_(397632, _n_(397628, "print", lambda: print), _c_(397631, _n_(397629, "len", lambda: len), _n_(397630, "valid_ds", lambda: valid_ds))) # 22
_l_(397633) # 22


class LSTMClassifier(_a_(397635, _n_(397634, "nn", lambda: nn), "Module")):
    _l_(397743)


    def __init__(self, embed_size, hidden_size, vocab_size, num_layers, num_classes, batch_size):
        _l_(397693)

        _c_(397640, _a_(397639, _n_(397636, "super", lambda: super)(_n_(397637, "LSTMClassifier", lambda: LSTMClassifier), _n_(397638, "self", lambda: self)), "__init__"))
        _l_(397641)

        _n_(397642, "self", lambda: self).embed_size = _n_(397643, "embed_size", lambda: embed_size)
        _l_(397644)
        _n_(397645, "self", lambda: self).hidden_size = _n_(397646, "hidden_size", lambda: hidden_size)
        _l_(397647)
        _n_(397648, "self", lambda: self).batch_size = _n_(397649, "batch_size", lambda: batch_size)
        _l_(397650)
        _n_(397651, "self", lambda: self).num_layers = _n_(397652, "num_layers", lambda: num_layers)
        _l_(397653)
        _n_(397654, "self", lambda: self).embedding = _c_(397659, _a_(397656, _n_(397655, "nn", lambda: nn), "Embedding"), _n_(397657, "vocab_size", lambda: vocab_size), _n_(397658, "embed_size", lambda: embed_size)) # a lookup table
        _l_(397660) # a lookup table

        _n_(397661, "self", lambda: self).lstm = _c_(397667, _a_(397663, _n_(397662, "nn", lambda: nn), "LSTM"), _n_(397664, "embed_size", lambda: embed_size), _n_(397665, "hidden_size", lambda: hidden_size), _n_(397666, "num_layers", lambda: num_layers), dropout=0.3, bidirectional=True)
        _l_(397668)

        _n_(397669, "self", lambda: self).fc = _c_(397686, _a_(397671, _n_(397670, "nn", lambda: nn), "Sequential"), _c_(397675, _a_(397673, _n_(397672, "nn", lambda: nn), "Linear"), 2*_n_(397674, "hidden_size", lambda: hidden_size), 100),
            _c_(397678, _a_(397677, _n_(397676, "nn", lambda: nn), "ReLU")),
            _c_(397681, _a_(397680, _n_(397679, "nn", lambda: nn), "Dropout"), p=0.2),
            _c_(397685, _a_(397683, _n_(397682, "nn", lambda: nn), "Linear"), 100, _n_(397684, "num_classes", lambda: num_classes))
        )
        _l_(397687)

        _n_(397688, "self", lambda: self).hidden = _c_(397691, _a_(397690, _n_(397689, "self", lambda: self), "init_hidden"))
        _l_(397692)

    def init_hidden(self):
        _l_(397721)

        h = _c_(397704, _n_(397694, "to_var", lambda: to_var), _c_(397703, _a_(397696, _n_(397695, "torch", lambda: torch), "zeros"), (2*_a_(397698, _n_(397697, "self", lambda: self), "num_layers"), _a_(397700, _n_(397699, "self", lambda: self), "batch_size"), _a_(397702, _n_(397701, "self", lambda: self), "hidden_size"))))
        _l_(397705)
        c = _c_(397716, _n_(397706, "to_var", lambda: to_var), _c_(397715, _a_(397708, _n_(397707, "torch", lambda: torch), "zeros"), (2*_a_(397710, _n_(397709, "self", lambda: self), "num_layers"), _a_(397712, _n_(397711, "self", lambda: self), "batch_size"), _a_(397714, _n_(397713, "self", lambda: self), "hidden_size"))))
        _l_(397717)
        aux = _n_(397718, "h", lambda: h), _n_(397719, "c", lambda: c)
        _l_(397720)
        return aux

    def forward(self, x):
        _l_(397742)

        x = _c_(397725, _a_(397723, _n_(397722, "self", lambda: self), "embedding"), _n_(397724, "x", lambda: x))
        _l_(397726)
        x, _n_(397727, "self", lambda: self).hidden = _c_(397733, _a_(397729, _n_(397728, "self", lambda: self), "lstm"), _n_(397730, "x", lambda: x), _a_(397732, _n_(397731, "self", lambda: self), "hidden"))
        _l_(397734)
        x = _c_(397738, _a_(397736, _n_(397735, "self", lambda: self), "fc"), _n_(397737, "x", lambda: x)[-1]) # select the last output
        _l_(397739) # select the last output
        aux = _n_(397740, "x", lambda: x)
        _l_(397741)
        return aux