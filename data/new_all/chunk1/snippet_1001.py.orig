#Source: https://stackoverflow.com/questions/57215427/attributeerror-kerastpumodel-object-has-no-attribute-ckpt-saved-epoch
model = tf.contrib.tpu.keras_to_tpu_model(
model,
strategy=tf.contrib.tpu.TPUDistributionStrategy(
    tf.contrib.cluster_resolver.TPUClusterResolver(TPU_WORKER)))