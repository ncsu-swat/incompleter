#Source: https://stackoverflow.com/questions/77311999/attributeerror-when-initializing-a-custom-decoder-class-in-tensorflow-with-non-d
# The decoder
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

class Decoder(tf.keras.layers.Layer):
  
  @classmethod
  def add_method(cls, fun):
    setattr(cls, fun.__name__, fun)
    return fun

  def __init__(self, text_processor, units):
    super(Decoder, self).__init__()
    self.text_processor = text_processor  # Tokenizer
    self.vocab_size = text_processor.size  # Vocab size
    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/StringLookup
    self.word_to_id = tf.keras.layers.StringLookup(
        vocabulary=text_processor.vocab,
        mask_token=text_processor.mask_token,
        oov_token=text_processor.unk_token)
    
    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/StringLookup
    self.id_to_word = tf.keras.layers.StringLookup(
        vocabulary=text_processor.vocab,
        mask_token=text_processor.mask_token,
        oov_token=text_processor.unk_token,
        invert=True)
    
    self.start_token = self.word_to_id(START_TOKEN)
    self.end_token = self.word_to_id(END_TOKEN)

    self.units = units


    # 1. The embedding layer converts token IDs to vectors
    self.embedding = tf.keras.layers.Embedding(self.vocab_size,
                                               units, mask_zero=True)

    # 2. The RNN keeps track of what's been generated so far.
    self.rnn = tf.keras.layers.GRU(units,
                                   return_sequences=True,
                                   return_state=True,
                                   recurrent_initializer='glorot_uniform')

    # 3. The RNN output will be the query for the attention layer.
    self.attention = CrossAttention(units)

    # 4. This fully connected layer produces the logits for each
    # output token.
    self.output_layer = tf.keras.layers.Dense(self.vocab_size)
 