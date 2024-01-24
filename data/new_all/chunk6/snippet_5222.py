# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56620409/nameerrorname-create-model-is-not-defined-i-have-tried-importing-model-fr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def train():
    _l_(349775)


    enc_train, dec_train=_c_(349768, _a_(349766, _n_(349765, "data_utils", lambda: data_utils), "prepare_custom_data"), _n_(349767, "gConfig", lambda: gConfig)['working_directory'])
    _l_(349769)
    train_set = _c_(349773, _n_(349770, "read_data", lambda: read_data), _n_(349771, "enc_train", lambda: enc_train),_n_(349772, "dec_train", lambda: dec_train))
    _l_(349774)

def seq2seq_f(encoder_inputs,decoder_inputs,do_decode):
    _l_(349790)

    aux = _c_(349788, _a_(349779, _a_(349778, _a_(349777, _n_(349776, "tf", lambda: tf), "nn"), "seq2seq"), "embedding_attention_seq2seq"), _n_(349780, "encoder_inputs", lambda: encoder_inputs),_n_(349781, "decoder_inputs", lambda: decoder_inputs), _n_(349782, "cell", lambda: cell),
        num_encoder_symbols=_n_(349783, "source_vocab_size", lambda: source_vocab_size),
        num_decoder_symbols=_n_(349784, "target_vocab_size", lambda: target_vocab_size),
        embedding_size=_n_(349785, "size", lambda: size),
        output_projection=_n_(349786, "output_projection", lambda: output_projection),
        feed_previous=_n_(349787, "do_decode", lambda: do_decode))
    _l_(349789)
    return aux

with _c_(349794, _a_(349792, _n_(349791, "tf", lambda: tf), "Session"), config=_n_(349793, "config", lambda: config)) as sess:
    _l_(349820)

    model = _c_(349797, _n_(349795, "create_model", lambda: create_model), _n_(349796, "sess", lambda: sess),False)
    _l_(349798)

    while True:
        _l_(349819)

        _c_(349802, _a_(349800, _n_(349799, "sess", lambda: sess), "run"), _n_(349801, "model", lambda: model))
        _l_(349803)

        checkpoint_path = _c_(349808, _a_(349806, _a_(349805, _n_(349804, "os", lambda: os), "path"), "join"), _n_(349807, "gConfig", lambda: gConfig)['working_directory'],'seq2seq.ckpt')
        _l_(349809)
        _c_(349817, _a_(349812, _a_(349811, _n_(349810, "model", lambda: model), "saver"), "save"), _n_(349813, "sess", lambda: sess), _n_(349814, "checkpoint_path", lambda: checkpoint_path), global_step=_a_(349816, _n_(349815, "model", lambda: model), "global_step"))
        _l_(349818)