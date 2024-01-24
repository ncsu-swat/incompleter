# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64685727/tensorflow-2-2-0-rc4-attributeerror-module-tensorflow-compat-v1-has-no-attrib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow.compat.v1 as tf
    _l_(586931)

except ImportError:
    pass
_c_(586934, _a_(586933, _n_(586932, "tf", lambda: tf), "disable_v2_behavior")) 
_l_(586935) 



# Building the seq2seq model
def seq2seq_model(inputs, targets, keep_prob, batch_size, sequence_length, answers_num_words, questions_num_words, encoder_embedding_size, decoder_embedding_size, rnn_size, num_layers, questionswords2int):
    _l_(586994)

    encoder_embedded_input = _c_(586946, _a_(586939, _a_(586938, _a_(586937, _n_(586936, "tf", lambda: tf), "contrib"), "layers"), "embed_sequence"), _n_(586940, "inputs", lambda: inputs),
                                                              _n_(586941, "answers_num_words", lambda: answers_num_words) + 1,
                                                              _n_(586942, "encoder_embedding_size", lambda: encoder_embedding_size),
                                                              initializer = _c_(586945, _a_(586944, _n_(586943, "tf", lambda: tf), "random_uniform_initializer"), 0, 1))
    _l_(586947)
    encoder_state = _c_(586954, _n_(586948, "encoder_rnn", lambda: encoder_rnn), _n_(586949, "encoder_embedded_input", lambda: encoder_embedded_input), _n_(586950, "rnn_size", lambda: rnn_size), _n_(586951, "num_layers", lambda: num_layers), _n_(586952, "keep_prob", lambda: keep_prob), _n_(586953, "sequence_length", lambda: sequence_length))
    _l_(586955)
    preprocessed_targets = _c_(586960, _n_(586956, "preprocess_targets", lambda: preprocess_targets), _n_(586957, "targets", lambda: targets), _n_(586958, "questionswords2int", lambda: questionswords2int), _n_(586959, "batch_size", lambda: batch_size))
    _l_(586961)
    decoder_embeddings_matrix = _c_(586969, _a_(586963, _n_(586962, "tf", lambda: tf), "Variable"), _c_(586968, _a_(586965, _n_(586964, "tf", lambda: tf), "random_uniform"), [_n_(586966, "questions_num_words", lambda: questions_num_words) + 1, _n_(586967, "decoder_embedding_size", lambda: decoder_embedding_size)], 0, 1))
    _l_(586970)
    decoder_embedded_input = _c_(586976, _a_(586973, _a_(586972, _n_(586971, "tf", lambda: tf), "nn"), "embedding_lookup"), _n_(586974, "decoder_embeddings_matrix", lambda: decoder_embeddings_matrix), _n_(586975, "preprocessed_targets", lambda: preprocessed_targets))
    _l_(586977)
    training_predictions, test_predictions = _c_(586989, _n_(586978, "decoder_rnn", lambda: decoder_rnn), _n_(586979, "decoder_embedded_input", lambda: decoder_embedded_input),
                                                         _n_(586980, "decoder_embeddings_matrix", lambda: decoder_embeddings_matrix),
                                                         _n_(586981, "encoder_state", lambda: encoder_state),
                                                         _n_(586982, "questions_num_words", lambda: questions_num_words),
                                                         _n_(586983, "sequence_length", lambda: sequence_length),
                                                         _n_(586984, "rnn_size", lambda: rnn_size),
                                                         _n_(586985, "num_layers", lambda: num_layers),
                                                         _n_(586986, "questionswords2int", lambda: questionswords2int),
                                                         _n_(586987, "keep_prob", lambda: keep_prob),
                                                         _n_(586988, "batch_size", lambda: batch_size))
    _l_(586990)
    aux = _n_(586991, "training_predictions", lambda: training_predictions), _n_(586992, "test_predictions", lambda: test_predictions)
    _l_(586993)
    return aux