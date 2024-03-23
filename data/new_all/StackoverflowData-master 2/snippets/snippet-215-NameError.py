#Source: https://stackoverflow.com/questions/67037067/attributeerror-module-tensorflow-keras-mixed-precision-has-no-attribute-set
policy = tf.keras.mixed_precision.Policy('mixed_float16')
mixed_precision.set_global_policy(policy)