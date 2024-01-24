# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64055916/typeerror-with-dense-block-of-densenet-in-tensorflow-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class DenseBlock(_n_(528120, "Layer", lambda: Layer)):
  _l_(528179)


  def __init__(self, nb_layers, nb_filter, growth_rate, dropout_rate=None, grow_nb_filters=True, **kwargs):
    _l_(528149)


    _c_(528126, _a_(528124, _n_(528121, "super", lambda: super)(_n_(528122, "DenseBlock", lambda: DenseBlock), _n_(528123, "self", lambda: self)), "__init__"), **_n_(528125, "kwargs", lambda: kwargs))
    _l_(528127)
    _n_(528128, "self", lambda: self).nb_layers = _n_(528129, "nb_layers", lambda: nb_layers)
    _l_(528130)
    _n_(528131, "self", lambda: self).growth_rate =_n_(528132, "growth_rate", lambda: growth_rate)
    _l_(528133)
    _n_(528134, "self", lambda: self).nb_filter = _n_(528135, "nb_filter", lambda: nb_filter)
    _l_(528136)
    _n_(528137, "self", lambda: self).grow_nb_filters = _n_(528138, "grow_nb_filters", lambda: grow_nb_filters)
    _l_(528139)
    _n_(528140, "self", lambda: self).conv_blocks = [_c_(528144, _n_(528141, "ConvBlock", lambda: ConvBlock), _n_(528142, "growth_rate", lambda: growth_rate), _n_(528143, "dropout_rate", lambda: dropout_rate)) for i in _c_(528147, _n_(528145, "range", lambda: range), _n_(528146, "nb_layers", lambda: nb_layers))]
    _l_(528148)

  def call(self, inputs):
    _l_(528178)

    concat_feat = _c_(528155, _a_(528151, _n_(528150, "tf", lambda: tf), "cast"), _n_(528152, "inputs", lambda: inputs), dtype=_a_(528154, _n_(528153, "tf", lambda: tf), "float32"))
    _l_(528156)
    for conv in _a_(528158, _n_(528157, "self", lambda: self), "conv_blocks"):
      _l_(528173)


      x = _n_(528159, "conv", lambda: conv)
      _l_(528160)
      concat_feat = _c_(528165, _a_(528162, _n_(528161, "tf", lambda: tf), "concat"), [_n_(528163, "concat_feat", lambda: concat_feat), _n_(528164, "x", lambda: x)], -1)
      _l_(528166)

      if _a_(528168, _n_(528167, "self", lambda: self), "grow_nb_filters"):
        _l_(528172)

        _n_(528169, "self", lambda: self).nb_filter += _n_(528170, "self", lambda: self).growth_rate
        _l_(528171)
    aux = _n_(528174, "concat_feat", lambda: concat_feat), _a_(528176, _n_(528175, "self", lambda: self), "nb_filter")
    _l_(528177)

    return aux