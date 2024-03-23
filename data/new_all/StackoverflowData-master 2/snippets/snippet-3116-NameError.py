#Source: https://stackoverflow.com/questions/44190555/tensorflow-version-1-1-0-skcompat-attributeerror
#create estimator
vggnet_classifier = learn.SKCompat(learn.Estimator(model_fn=vggnet_model, model_dir= "/tmp/vgg_net"))

# Set up logging for predictions
tensors_to_log = {"probabilities": "softmax_tensor"}
logging_hook = tf.train.LoggingTensorHook(tensors=tensors_to_log, every_n_iter=100)

#train model
vggnet_classifier.fit(
    x=X_train,
    y=y_train,
    batch_size=100,
    steps=2,
    monitors=[logging_hook])

# Configure the accuracy metric for evaluation
metrics = {
    "accuracy":
        learn.MetricSpec(metric_fn=tf.metrics.accuracy, prediction_key="classes"),}

# Evaluate the model and print results
eval_results = vggnet_classifier.evaluate(x=X_val, y=y_val, metrics=metrics)
print(eval_results)