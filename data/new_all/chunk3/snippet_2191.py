# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51064323/tensorflow-typeerror-cannot-serialize-io-textiowrapper-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x_ = [ _c_(575255, _a_(575249, _n_(575248, "tf", lambda: tf), "placeholder"), _a_(575251, _n_(575250, "tf", lambda: tf), "int32"), shape=[None,], name=_c_(575254, _a_(575252, 'x{}', "format"), _n_(575253, "i", lambda: i))) for i in _c_(575258, _n_(575256, "range", lambda: range), _n_(575257, "xseq_len", lambda: xseq_len))]
_l_(575259)
y_ = [ _c_(575267, _a_(575261, _n_(575260, "tf", lambda: tf), "placeholder"), _a_(575263, _n_(575262, "tf", lambda: tf), "int32"), shape=[None,], name=_c_(575266, _a_(575264, 'y{}', "format"), _n_(575265, "i", lambda: i))) for i in _c_(575270, _n_(575268, "range", lambda: range), _n_(575269, "yseq_len", lambda: yseq_len))]
_l_(575271)
decoder_inputs = [_c_(575277, _a_(575273, _n_(575272, "tf", lambda: tf), "zeros_like"), _n_(575274, "x_", lambda: x_)[0], dtype=_a_(575276, _n_(575275, "tf", lambda: tf), "int32"), name = "GO")] + _n_(575278, "y_", lambda: y_)[:-1]
_l_(575279)
keep_prob = _c_(575284, _a_(575281, _n_(575280, "tf", lambda: tf), "placeholder"), _a_(575283, _n_(575282, "tf", lambda: tf), "float32"))
_l_(575285)
basic_cell = _c_(575297, _a_(575289, _a_(575288, _a_(575287, _n_(575286, "tf", lambda: tf), "contrib"), "rnn"), "DropoutWrapper"), _c_(575295, _a_(575293, _a_(575292, _a_(575291, _n_(575290, "tf", lambda: tf), "contrib"), "rnn"), "BasicLSTMCell"), _n_(575294, "emb_dim", lambda: emb_dim)),output_keep_prob=_n_(575296, "keep_prob", lambda: keep_prob))
_l_(575298)

stacked_lstm = _c_(575304, _a_(575302, _a_(575301, _a_(575300, _n_(575299, "tf", lambda: tf), "nn"), "rnn_cell"), "MultiRNNCell"), [_n_(575303, "basic_cell", lambda: basic_cell)]*3)
_l_(575305)


with _c_(575308, _a_(575307, _n_(575306, "tf", lambda: tf), "variable_scope"), 'decoder') as scope:
    _l_(575323)

    decode_outputs, decode_states = _c_(575317, _a_(575310, _n_(575309, "seq2seq", lambda: seq2seq), "embedding_rnn_seq2seq"), _n_(575311, "x_", lambda: x_),_n_(575312, "decoder_inputs", lambda: decoder_inputs), _n_(575313, "stacked_lstm", lambda: stacked_lstm),
                                        _n_(575314, "xvocab_size", lambda: xvocab_size), _n_(575315, "yvocab_size", lambda: yvocab_size), _n_(575316, "emb_dim", lambda: emb_dim))
    _l_(575318)
    _c_(575321, _a_(575320, _n_(575319, "scope", lambda: scope), "reuse_variables"))
    _l_(575322)