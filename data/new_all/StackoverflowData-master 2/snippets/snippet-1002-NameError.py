#Source: https://stackoverflow.com/questions/57215427/attributeerror-kerastpumodel-object-has-no-attribute-ckpt-saved-epoch
model.compile(optimizer=tf.train.AdamOptimizer(learning_rate=1e-3), 
loss='categorical_crossentropy', metrics=['accuracy'])