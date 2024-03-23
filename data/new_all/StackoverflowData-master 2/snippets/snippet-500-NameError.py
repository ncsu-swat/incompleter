#Source: https://stackoverflow.com/questions/75936866/attributeerror-tensor-name-is-undefined-when-eager-execution-is-enabled
with tf.control_dependencies(update_ops):
    with tf.GradientTape() as tape:
        optimizer = tf.keras.optimizers.SGD(lr, 0.9)
        train_op = optimizer.minimize(loss, var_list=[labels, outputs], tape=tape)
        del tape