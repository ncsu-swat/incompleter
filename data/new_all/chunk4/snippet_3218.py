# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77284708/custom-peephole-lstm-layer-returns-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(588727)

except ImportError:
    pass

class PeepholeLSTM(_a_(588731, _a_(588730, _a_(588729, _n_(588728, "tf", lambda: tf), "keras"), "layers"), "Layer")):
    _l_(589001)

    def __init__(self, units, activation='tanh', return_sequences=False, **kwargs):
        _l_(588753)

        _c_(588737, _a_(588735, _n_(588732, "super", lambda: super)(_n_(588733, "PeepholeLSTM", lambda: PeepholeLSTM), _n_(588734, "self", lambda: self)), "__init__"), **_n_(588736, "kwargs", lambda: kwargs))
        _l_(588738)
        _n_(588739, "self", lambda: self).units = _n_(588740, "units", lambda: units)
        _l_(588741)
        _n_(588742, "self", lambda: self).activation = _c_(588748, _a_(588746, _a_(588745, _a_(588744, _n_(588743, "tf", lambda: tf), "keras"), "activations"), "get"), _n_(588747, "activation", lambda: activation))
        _l_(588749)
        _n_(588750, "self", lambda: self).return_sequences = _n_(588751, "return_sequences", lambda: return_sequences)
        _l_(588752)

    def build(self, input_shape):
        _l_(588868)

        input_dim = _n_(588754, "input_shape", lambda: input_shape)[-1]
        _l_(588755)

        # Create weights for the LSTM cell
        _n_(588756, "self", lambda: self).Wf = _c_(588762, _a_(588758, _n_(588757, "self", lambda: self), "add_weight"), name='Wf', shape=(_n_(588759, "input_dim", lambda: input_dim), _a_(588761, _n_(588760, "self", lambda: self), "units")), initializer='glorot_uniform')
        _l_(588763)
        _n_(588764, "self", lambda: self).Uf = _c_(588771, _a_(588766, _n_(588765, "self", lambda: self), "add_weight"), name='Uf', shape=(_a_(588768, _n_(588767, "self", lambda: self), "units"), _a_(588770, _n_(588769, "self", lambda: self), "units")), initializer='orthogonal')
        _l_(588772)
        _n_(588773, "self", lambda: self).bf = _c_(588778, _a_(588775, _n_(588774, "self", lambda: self), "add_weight"), name='bf', shape=(_a_(588777, _n_(588776, "self", lambda: self), "units"),), initializer='zeros')
        _l_(588779)

        _n_(588780, "self", lambda: self).Wi = _c_(588786, _a_(588782, _n_(588781, "self", lambda: self), "add_weight"), name='Wi', shape=(_n_(588783, "input_dim", lambda: input_dim), _a_(588785, _n_(588784, "self", lambda: self), "units")), initializer='glorot_uniform')
        _l_(588787)
        _n_(588788, "self", lambda: self).Ui = _c_(588795, _a_(588790, _n_(588789, "self", lambda: self), "add_weight"), name='Ui', shape=(_a_(588792, _n_(588791, "self", lambda: self), "units"), _a_(588794, _n_(588793, "self", lambda: self), "units")), initializer='orthogonal')
        _l_(588796)
        _n_(588797, "self", lambda: self).bi = _c_(588802, _a_(588799, _n_(588798, "self", lambda: self), "add_weight"), name='bi', shape=(_a_(588801, _n_(588800, "self", lambda: self), "units"),), initializer='zeros')
        _l_(588803)

        _n_(588804, "self", lambda: self).Wc = _c_(588810, _a_(588806, _n_(588805, "self", lambda: self), "add_weight"), name='Wc', shape=(_n_(588807, "input_dim", lambda: input_dim), _a_(588809, _n_(588808, "self", lambda: self), "units")), initializer='glorot_uniform')
        _l_(588811)
        _n_(588812, "self", lambda: self).Uc = _c_(588819, _a_(588814, _n_(588813, "self", lambda: self), "add_weight"), name='Uc', shape=(_a_(588816, _n_(588815, "self", lambda: self), "units"), _a_(588818, _n_(588817, "self", lambda: self), "units")), initializer='orthogonal')
        _l_(588820)
        _n_(588821, "self", lambda: self).bc = _c_(588826, _a_(588823, _n_(588822, "self", lambda: self), "add_weight"), name='bc', shape=(_a_(588825, _n_(588824, "self", lambda: self), "units"),), initializer='zeros')
        _l_(588827)

        _n_(588828, "self", lambda: self).Wo = _c_(588834, _a_(588830, _n_(588829, "self", lambda: self), "add_weight"), name='Wo', shape=(_n_(588831, "input_dim", lambda: input_dim), _a_(588833, _n_(588832, "self", lambda: self), "units")), initializer='glorot_uniform')
        _l_(588835)
        _n_(588836, "self", lambda: self).Uo = _c_(588843, _a_(588838, _n_(588837, "self", lambda: self), "add_weight"), name='Uo', shape=(_a_(588840, _n_(588839, "self", lambda: self), "units"), _a_(588842, _n_(588841, "self", lambda: self), "units")), initializer='orthogonal')
        _l_(588844)
        _n_(588845, "self", lambda: self).bo = _c_(588850, _a_(588847, _n_(588846, "self", lambda: self), "add_weight"), name='bo', shape=(_a_(588849, _n_(588848, "self", lambda: self), "units"),), initializer='zeros')
        _l_(588851)

        _n_(588852, "self", lambda: self).c_peephole = _c_(588857, _a_(588854, _n_(588853, "self", lambda: self), "add_weight"), name='c_peephole', shape=(_a_(588856, _n_(588855, "self", lambda: self), "units"),), initializer='zeros')
        _l_(588858)
        _n_(588859, "self", lambda: self).o_peephole = _c_(588864, _a_(588861, _n_(588860, "self", lambda: self), "add_weight"), name='o_peephole', shape=(_a_(588863, _n_(588862, "self", lambda: self), "units"),), initializer='zeros')
        _l_(588865)

        _n_(588866, "self", lambda: self).built = True
        _l_(588867)

    def call(self, inputs):
        _l_(589000)

        # Initialize states
        batch_size, seq_length, _ = _a_(588870, _n_(588869, "inputs", lambda: inputs), "shape")
        _l_(588871)
        h_tm1 = _c_(588877, _a_(588873, _n_(588872, "tf", lambda: tf), "zeros"), shape=(_n_(588874, "batch_size", lambda: batch_size), _a_(588876, _n_(588875, "self", lambda: self), "units")))
        _l_(588878)
        c_tm1 = _c_(588884, _a_(588880, _n_(588879, "tf", lambda: tf), "zeros"), shape=(_n_(588881, "batch_size", lambda: batch_size), _a_(588883, _n_(588882, "self", lambda: self), "units")))
        _l_(588885)

        outputs = []
        _l_(588886)

        for t in _c_(588889, _n_(588887, "range", lambda: range), _n_(588888, "seq_length", lambda: seq_length)):
            _l_(588989)

            x_t = _n_(588890, "inputs", lambda: inputs)[:, _n_(588891, "t", lambda: t), :]
            _l_(588892)
            f = _c_(588912, _a_(588894, _n_(588893, "tf", lambda: tf), "sigmoid"), _c_(588900, _a_(588896, _n_(588895, "tf", lambda: tf), "matmul"), _n_(588897, "x_t", lambda: x_t), _a_(588899, _n_(588898, "self", lambda: self), "Wf")) + _c_(588906, _a_(588902, _n_(588901, "tf", lambda: tf), "matmul"), _n_(588903, "h_tm1", lambda: h_tm1), _a_(588905, _n_(588904, "self", lambda: self), "Uf")) + _a_(588908, _n_(588907, "self", lambda: self), "bf") + _a_(588910, _n_(588909, "self", lambda: self), "c_peephole") * _n_(588911, "c_tm1", lambda: c_tm1))
            _l_(588913)
            i = _c_(588930, _a_(588915, _n_(588914, "tf", lambda: tf), "sigmoid"), _c_(588921, _a_(588917, _n_(588916, "tf", lambda: tf), "matmul"), _n_(588918, "x_t", lambda: x_t), _a_(588920, _n_(588919, "self", lambda: self), "Wi")) + _c_(588927, _a_(588923, _n_(588922, "tf", lambda: tf), "matmul"), _n_(588924, "h_tm1", lambda: h_tm1), _a_(588926, _n_(588925, "self", lambda: self), "Ui")) + _a_(588929, _n_(588928, "self", lambda: self), "bi"))
            _l_(588931)
            c = _n_(588932, "f", lambda: f) * _n_(588933, "c_tm1", lambda: c_tm1) + _n_(588934, "i", lambda: i) * _c_(588951, _a_(588936, _n_(588935, "self", lambda: self), "activation"), _c_(588942, _a_(588938, _n_(588937, "tf", lambda: tf), "matmul"), _n_(588939, "x_t", lambda: x_t), _a_(588941, _n_(588940, "self", lambda: self), "Wc")) + _c_(588948, _a_(588944, _n_(588943, "tf", lambda: tf), "matmul"), _n_(588945, "h_tm1", lambda: h_tm1), _a_(588947, _n_(588946, "self", lambda: self), "Uc")) + _a_(588950, _n_(588949, "self", lambda: self), "bc"))
            _l_(588952)
            o = _c_(588972, _a_(588954, _n_(588953, "tf", lambda: tf), "sigmoid"), _c_(588960, _a_(588956, _n_(588955, "tf", lambda: tf), "matmul"), _n_(588957, "x_t", lambda: x_t), _a_(588959, _n_(588958, "self", lambda: self), "Wo")) + _c_(588966, _a_(588962, _n_(588961, "tf", lambda: tf), "matmul"), _n_(588963, "h_tm1", lambda: h_tm1), _a_(588965, _n_(588964, "self", lambda: self), "Uo")) + _a_(588968, _n_(588967, "self", lambda: self), "bo") + _a_(588970, _n_(588969, "self", lambda: self), "o_peephole") * _n_(588971, "c", lambda: c))
            _l_(588973)
            h = _n_(588974, "o", lambda: o) * _c_(588978, _a_(588976, _n_(588975, "self", lambda: self), "activation"), _n_(588977, "c", lambda: c))
            _l_(588979)

            _c_(588983, _a_(588981, _n_(588980, "outputs", lambda: outputs), "append"), _n_(588982, "h", lambda: h))
            _l_(588984)
            h_tm1 = _n_(588985, "h", lambda: h)
            _l_(588986)
            c_tm1 = _n_(588987, "c", lambda: c)
            _l_(588988)

        if _a_(588991, _n_(588990, "self", lambda: self), "return_sequences"):
            _l_(588999)

            aux = _c_(588995, _a_(588993, _n_(588992, "tf", lambda: tf), "stack"), _n_(588994, "outputs", lambda: outputs), axis=1)
            _l_(588996)
            return aux
        else:
            aux = _n_(588997, "h", lambda: h)
            _l_(588998)
            return aux