# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46795862/constrained-optimization-for-word2vec-giving-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
emb = _c_(567179, _a_(567169, _n_(567168, "tf", lambda: tf), "Variable"), _c_(567178, _a_(567171, _n_(567170, "tf", lambda: tf), "random_uniform"), [_a_(567173, _n_(567172, "opts", lambda: opts), "vocab_size"), _a_(567175, _n_(567174, "opts", lambda: opts), "emb_dim")], -_n_(567176, "init_width", lambda: init_width), _n_(567177, "init_width", lambda: init_width)),
    name="emb")
_l_(567180)
_n_(567181, "self", lambda: self)._emb = _n_(567182, "emb", lambda: emb)
_l_(567183)

sm_w_t = _c_(567197, _a_(567185, _n_(567184, "tf", lambda: tf), "Variable"), _c_(567194, _a_(567187, _n_(567186, "tf", lambda: tf), "random_uniform"), [_a_(567189, _n_(567188, "opts", lambda: opts), "vocab_size"), _a_(567191, _n_(567190, "opts", lambda: opts), "emb_dim")], -_n_(567192, "init_width", lambda: init_width), _n_(567193, "init_width", lambda: init_width)),
    name="sm_w_t", dtype=_a_(567196, _n_(567195, "tf", lambda: tf), "float32"))
_l_(567198)
_n_(567199, "self", lambda: self)._sm_w_t = _n_(567200, "sm_w_t", lambda: sm_w_t)
_l_(567201)