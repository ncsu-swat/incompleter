#Source: https://stackoverflow.com/questions/64175246/keras-model-fit-giving-out-typeerror-nonetype-object-is-not-callable
image_input = tf.keras.layers.Input(shape=(299,299,3), name='image_input')
negative_input = tf.keras.layers.Input(shape=(299,299,3), name='negative_input')

siamese = SiameseNet(image_features_extract_model)([image_input, negative_input])

model = tf.keras.Model(inputs=[image_input, negative_input], outputs=siamese)

model.compile(optimizer=tf.keras.optimizers.Adam(), loss=triplet_loss, metrics=['accuracy'])