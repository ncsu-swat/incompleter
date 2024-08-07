#Source: https://stackoverflow.com/questions/56620409/nameerrorname-create-model-is-not-defined-i-have-tried-importing-model-fr
def train():

    enc_train, dec_train=data_utils.prepare_custom_data(
        gConfig['working_directory'])
    train_set = read_data(enc_train,dec_train)

def seq2seq_f(encoder_inputs,decoder_inputs,do_decode):
    return tf.nn.seq2seq.embedding_attention_seq2seq(
        encoder_inputs,decoder_inputs, cell,
        num_encoder_symbols=source_vocab_size,
        num_decoder_symbols=target_vocab_size,
        embedding_size=size,
        output_projection=output_projection,
        feed_previous=do_decode)

with tf.Session(config=config) as sess:
    model = create_model(sess,False)

    while True:
        sess.run(model)

        checkpoint_path = os.path.join(gConfig['working_directory'],'seq2seq.ckpt')
        model.saver.save(sess, checkpoint_path, global_step=model.global_step)