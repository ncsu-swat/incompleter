# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63164902/getting-typeerror-expected-int32-got-none-of-type-nonetype-instead
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class encoder_decoder(_a_(568831, _a_(568830, _n_(568829, "tf", lambda: tf), "keras"), "Model")):
  _l_(568931)

  def __init__(self,embedding_size,encoder_inputs_length,output_length,vocab_size,output_vocab_size,score_fun,units):
    _l_(568899)

    _c_(568836, _a_(568835, _n_(568832, "super", lambda: super)(_n_(568833, "encoder_decoder", lambda: encoder_decoder),_n_(568834, "self", lambda: self)), "__init__"))
    _l_(568837)
    _n_(568838, "self", lambda: self).vocab_size = _n_(568839, "vocab_size", lambda: vocab_size)
    _l_(568840)
    _n_(568841, "self", lambda: self).enc_units = _n_(568842, "units", lambda: units)
    _l_(568843)
    _n_(568844, "self", lambda: self).embedding_size = _n_(568845, "embedding_size", lambda: embedding_size)
    _l_(568846)
    _n_(568847, "self", lambda: self).encoder_inputs_length = _n_(568848, "encoder_inputs_length", lambda: encoder_inputs_length)
    _l_(568849)
    _n_(568850, "self", lambda: self).output_length = _n_(568851, "output_length", lambda: output_length)
    _l_(568852)
    _n_(568853, "self", lambda: self).lstm_output = 0
    _l_(568854)
    _n_(568855, "self", lambda: self).state_h = 0
    _l_(568856)
    _n_(568857, "self", lambda: self).state_c = 0
    _l_(568858)
    _n_(568859, "self", lambda: self).output_vocab_size = _n_(568860, "output_vocab_size", lambda: output_vocab_size)
    _l_(568861)
    _n_(568862, "self", lambda: self).dec_units = _n_(568863, "units", lambda: units)
    _l_(568864)
    _n_(568865, "self", lambda: self).score_fun = _n_(568866, "score_fun", lambda: score_fun)
    _l_(568867)
    _n_(568868, "self", lambda: self).att_units = _n_(568869, "units", lambda: units)
    _l_(568870)
    _n_(568871, "self", lambda: self).encoder=_c_(568881, _n_(568872, "Encoder", lambda: Encoder), _a_(568874, _n_(568873, "self", lambda: self), "vocab_size"),_a_(568876, _n_(568875, "self", lambda: self), "embedding_size"),_a_(568878, _n_(568877, "self", lambda: self), "enc_units"),_a_(568880, _n_(568879, "self", lambda: self), "encoder_inputs_length"))
    _l_(568882)
    _n_(568883, "self", lambda: self).decoder = _c_(568897, _n_(568884, "Decoder", lambda: Decoder), _a_(568886, _n_(568885, "self", lambda: self), "output_vocab_size"), _a_(568888, _n_(568887, "self", lambda: self), "embedding_size"), _a_(568890, _n_(568889, "self", lambda: self), "output_length"), _a_(568892, _n_(568891, "self", lambda: self), "dec_units") ,_a_(568894, _n_(568893, "self", lambda: self), "score_fun") ,_a_(568896, _n_(568895, "self", lambda: self), "att_units"))
    _l_(568898)
  
  def call(self,data):
    _l_(568930)

    input,output = _n_(568900, "data", lambda: data)[0],_n_(568901, "data", lambda: data)[1]
    _l_(568902)
    encoder_hidden = _c_(568908, _a_(568905, _a_(568904, _n_(568903, "self", lambda: self), "encoder"), "initialize_states"), _a_(568907, _n_(568906, "input", lambda: input), "shape")[0])
    _l_(568909)
    encoder_output,encoder_hidden,encoder_cell = _c_(568914, _a_(568911, _n_(568910, "self", lambda: self), "encoder"), _n_(568912, "input", lambda: input),_n_(568913, "encoder_hidden", lambda: encoder_hidden))
    _l_(568915)
    decoder_hidden = _n_(568916, "encoder_hidden", lambda: encoder_hidden)
    _l_(568917)
    decoder_cell =_n_(568918, "encoder_cell", lambda: encoder_cell)
    _l_(568919)
    decoder_output = _c_(568926, _a_(568921, _n_(568920, "self", lambda: self), "decoder"), _n_(568922, "output", lambda: output),_n_(568923, "encoder_output", lambda: encoder_output),_n_(568924, "decoder_hidden", lambda: decoder_hidden),_n_(568925, "decoder_cell", lambda: decoder_cell))
    _l_(568927)
    aux = _n_(568928, "decoder_output", lambda: decoder_output)
    _l_(568929)
    return aux