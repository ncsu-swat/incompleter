# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77311999/attributeerror-when-initializing-a-custom-decoder-class-in-tensorflow-with-non-d
# The decoder
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""
The decoder's job is to generate predictions for the next token at each 
location in the target sequence.

The Decoder Structure:
1. It looks up embeddings for each token in the target sequence.
2. It uses an RNN to process the target sequence, and keep track of what it has generated so far.
3. It uses RNN output as the "query" to the attention layer, when attending to the encoder's output.
4. At each location in the output it predicts the next token.

Note:
When training, the model predicts the next word at each location. So it's 
important that the information only flows in one direction through the model. 
The decoder uses a unidirectional (not bidirectional) 
RNN to process the target sequence.

> When running inference with this model it produces one word at a time, 
and those are fed back into the model.
"""

class Decoder(_a_(599266, _a_(599265, _a_(599264, _n_(599263, "tf", lambda: tf), "keras"), "layers"), "Layer")):
  _l_(599365)

  
  @_n_(599267, "classmethod", lambda: classmethod)
  def add_method(cls, fun):
    _l_(599277)

    _c_(599273, _n_(599268, "setattr", lambda: setattr), _n_(599269, "cls", lambda: cls), _a_(599271, _n_(599270, "fun", lambda: fun), "__name__"), _n_(599272, "fun", lambda: fun))
    _l_(599274)
    aux = _n_(599275, "fun", lambda: fun)
    _l_(599276)
    return aux

  def __init__(self, text_processor, units):
    _l_(599364)

    _c_(599282, _a_(599281, _n_(599278, "super", lambda: super)(_n_(599279, "Decoder", lambda: Decoder), _n_(599280, "self", lambda: self)), "__init__"))
    _l_(599283)
    _n_(599284, "self", lambda: self).text_processor = _n_(599285, "text_processor", lambda: text_processor)  # Tokenizer
    _l_(599286)  # Tokenizer
    _n_(599287, "self", lambda: self).vocab_size = _a_(599289, _n_(599288, "text_processor", lambda: text_processor), "size")  # Vocab size
    _l_(599290)  # Vocab size
    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/StringLookup
    _n_(599291, "self", lambda: self).word_to_id = _c_(599302, _a_(599295, _a_(599294, _a_(599293, _n_(599292, "tf", lambda: tf), "keras"), "layers"), "StringLookup"), vocabulary=_a_(599297, _n_(599296, "text_processor", lambda: text_processor), "vocab"),
        mask_token=_a_(599299, _n_(599298, "text_processor", lambda: text_processor), "mask_token"),
        oov_token=_a_(599301, _n_(599300, "text_processor", lambda: text_processor), "unk_token"))
    _l_(599303)
    
    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/StringLookup
    _n_(599304, "self", lambda: self).id_to_word = _c_(599315, _a_(599308, _a_(599307, _a_(599306, _n_(599305, "tf", lambda: tf), "keras"), "layers"), "StringLookup"), vocabulary=_a_(599310, _n_(599309, "text_processor", lambda: text_processor), "vocab"),
        mask_token=_a_(599312, _n_(599311, "text_processor", lambda: text_processor), "mask_token"),
        oov_token=_a_(599314, _n_(599313, "text_processor", lambda: text_processor), "unk_token"),
        invert=True)
    _l_(599316)
    
    _n_(599317, "self", lambda: self).start_token = _c_(599321, _a_(599319, _n_(599318, "self", lambda: self), "word_to_id"), _n_(599320, "START_TOKEN", lambda: START_TOKEN))
    _l_(599322)
    _n_(599323, "self", lambda: self).end_token = _c_(599327, _a_(599325, _n_(599324, "self", lambda: self), "word_to_id"), _n_(599326, "END_TOKEN", lambda: END_TOKEN))
    _l_(599328)

    _n_(599329, "self", lambda: self).units = _n_(599330, "units", lambda: units)
    _l_(599331)


    # 1. The embedding layer converts token IDs to vectors
    _n_(599332, "self", lambda: self).embedding = _c_(599340, _a_(599336, _a_(599335, _a_(599334, _n_(599333, "tf", lambda: tf), "keras"), "layers"), "Embedding"), _a_(599338, _n_(599337, "self", lambda: self), "vocab_size"),
                                               _n_(599339, "units", lambda: units), mask_zero=True)
    _l_(599341)

    # 2. The RNN keeps track of what's been generated so far.
    _n_(599342, "self", lambda: self).rnn = _c_(599348, _a_(599346, _a_(599345, _a_(599344, _n_(599343, "tf", lambda: tf), "keras"), "layers"), "GRU"), _n_(599347, "units", lambda: units),
                                   return_sequences=True,
                                   return_state=True,
                                   recurrent_initializer='glorot_uniform')
    _l_(599349)

    # 3. The RNN output will be the query for the attention layer.
    _n_(599350, "self", lambda: self).attention = _c_(599353, _n_(599351, "CrossAttention", lambda: CrossAttention), _n_(599352, "units", lambda: units))
    _l_(599354)

    # 4. This fully connected layer produces the logits for each
    # output token.
    _n_(599355, "self", lambda: self).output_layer = _c_(599362, _a_(599359, _a_(599358, _a_(599357, _n_(599356, "tf", lambda: tf), "keras"), "layers"), "Dense"), _a_(599361, _n_(599360, "self", lambda: self), "vocab_size"))
    _l_(599363)