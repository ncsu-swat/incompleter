# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51876460/getting-tensorflow-s-is-not-valid-scope-name-error-while-i-am-trying-to-creat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def train_linear_classifier_model(
    learning_rate,
    regularization_strength,
    steps,
    batch_size,
    training_examples,
    training_targets,
    validation_examples,
    validation_targets
):
    _l_(418855)

    periods = 10
    _l_(418710)
    steps_per_period = _n_(418711, "steps", lambda: steps) / _n_(418712, "periods", lambda: periods)
    _l_(418713)

    my_optimizer = _c_(418719, _a_(418716, _a_(418715, _n_(418714, "tf", lambda: tf), "train"), "FtrlOptimizer"), learning_rate=_n_(418717, "learning_rate", lambda: learning_rate), l1_regularization_strength=_n_(418718, "regularization_strength", lambda: regularization_strength))
    _l_(418720)
    my_optimizer = _c_(418726, _a_(418724, _a_(418723, _a_(418722, _n_(418721, "tf", lambda: tf), "contrib"), "estimator"), "clip_gradients_by_norm"), _n_(418725, "my_optimizer", lambda: my_optimizer), 5.0)
    _l_(418727)
    linear_classifier = _c_(418735, _a_(418730, _a_(418729, _n_(418728, "tf", lambda: tf), "estimator"), "LinearClassifier"), feature_columns=_c_(418733, _n_(418731, "construct_feature_columns", lambda: construct_feature_columns), _n_(418732, "training_examples", lambda: training_examples)),
      optimizer=_n_(418734, "my_optimizer", lambda: my_optimizer)
  )
    _l_(418736)


    training_input_fn = lambda: _c_(418741, _n_(418737, "my_input_fn", lambda: my_input_fn), _n_(418738, "training_examples", lambda: training_examples), 
                                          _n_(418739, "training_targets", lambda: training_targets)["SalePrice"], 
                                          batch_size=_n_(418740, "batch_size", lambda: batch_size))
    _l_(418742)
    predict_training_input_fn = lambda: _c_(418746, _n_(418743, "my_input_fn", lambda: my_input_fn), _n_(418744, "training_examples", lambda: training_examples), 
                                                  _n_(418745, "training_targets", lambda: training_targets)["SalePrice"], 
                                                  num_epochs=1, 
                                                  shuffle=False)
    _l_(418747)
    predict_validation_input_fn = lambda: _c_(418751, _n_(418748, "my_input_fn", lambda: my_input_fn), _n_(418749, "validation_examples", lambda: validation_examples), 
                                                    _n_(418750, "validation_targets", lambda: validation_targets)["SalePrice"], 
                                                    num_epochs=1, 
                                                    shuffle=False)
    _l_(418752)


    _c_(418754, _n_(418753, "print", lambda: print), "Training model...")
    _l_(418755)
    _c_(418757, _n_(418756, "print", lambda: print), "LogLoss (on validation data):")
    _l_(418758)
    training_log_losses = []
    _l_(418759)
    validation_log_losses = []
    _l_(418760)
    for period in _c_(418763, _n_(418761, "range", lambda: range), 0, _n_(418762, "periods", lambda: periods)):
        _l_(418770)

        _c_(418768, _a_(418765, _n_(418764, "linear_classifier", lambda: linear_classifier), "train"), input_fn=_n_(418766, "training_input_fn", lambda: training_input_fn),
        steps=_n_(418767, "steps_per_period", lambda: steps_per_period)
    )
        _l_(418769)
    # Take a break and compute predictions.
    training_probabilities = _c_(418774, _a_(418772, _n_(418771, "linear_classifier", lambda: linear_classifier), "predict"), input_fn=_n_(418773, "predict_training_input_fn", lambda: predict_training_input_fn))
    _l_(418775)
    training_probabilities = _c_(418780, _a_(418777, _n_(418776, "np", lambda: np), "array"), [_n_(418778, "item", lambda: item)['probabilities'] for item in _n_(418779, "training_probabilities", lambda: training_probabilities)])
    _l_(418781)

    validation_probabilities = _c_(418785, _a_(418783, _n_(418782, "linear_classifier", lambda: linear_classifier), "predict"), input_fn=_n_(418784, "predict_validation_input_fn", lambda: predict_validation_input_fn))
    _l_(418786)
    validation_probabilities = _c_(418791, _a_(418788, _n_(418787, "np", lambda: np), "array"), [_n_(418789, "item", lambda: item)['probabilities'] for item in _n_(418790, "validation_probabilities", lambda: validation_probabilities)])
    _l_(418792)

    # Compute training and validation loss.
    training_log_loss = _c_(418797, _a_(418794, _n_(418793, "metrics", lambda: metrics), "log_loss"), _n_(418795, "training_targets", lambda: training_targets), _n_(418796, "training_probabilities", lambda: training_probabilities))
    _l_(418798)
    validation_log_loss = _c_(418803, _a_(418800, _n_(418799, "metrics", lambda: metrics), "log_loss"), _n_(418801, "validation_targets", lambda: validation_targets), _n_(418802, "validation_probabilities", lambda: validation_probabilities))
    _l_(418804)
    # Occasionally print the current loss.
    _c_(418808, _n_(418805, "print", lambda: print), "  period %02d : %0.2f" % (_n_(418806, "period", lambda: period), _n_(418807, "validation_log_loss", lambda: validation_log_loss)))
    _l_(418809)
    # Add the loss metrics from this period to our list.
    _c_(418813, _a_(418811, _n_(418810, "training_log_losses", lambda: training_log_losses), "append"), _n_(418812, "training_log_loss", lambda: training_log_loss))
    _l_(418814)
    _c_(418818, _a_(418816, _n_(418815, "validation_log_losses", lambda: validation_log_losses), "append"), _n_(418817, "validation_log_loss", lambda: validation_log_loss))
    _l_(418819)
    _c_(418821, _n_(418820, "print", lambda: print), "Model training finished.")
    _l_(418822)

  # Output a graph of loss metrics over periods.
    _c_(418825, _a_(418824, _n_(418823, "plt", lambda: plt), "ylabel"), "LogLoss")
    _l_(418826)
    _c_(418829, _a_(418828, _n_(418827, "plt", lambda: plt), "xlabel"), "Periods")
    _l_(418830)
    _c_(418833, _a_(418832, _n_(418831, "plt", lambda: plt), "title"), "LogLoss vs. Periods")
    _l_(418834)
    _c_(418837, _a_(418836, _n_(418835, "plt", lambda: plt), "tight_layout"))
    _l_(418838)
    _c_(418842, _a_(418840, _n_(418839, "plt", lambda: plt), "plot"), _n_(418841, "training_log_losses", lambda: training_log_losses), label="training")
    _l_(418843)
    _c_(418847, _a_(418845, _n_(418844, "plt", lambda: plt), "plot"), _n_(418846, "validation_log_losses", lambda: validation_log_losses), label="validation")
    _l_(418848)
    _c_(418851, _a_(418850, _n_(418849, "plt", lambda: plt), "legend"))
    _l_(418852)
    aux = _n_(418853, "linear_classifier", lambda: linear_classifier)
    _l_(418854)

    return aux

linear_classifier = _c_(418861, _n_(418856, "train_linear_classifier_model", lambda: train_linear_classifier_model), learning_rate=0.1,
    regularization_strength=0.1,
    steps=300,
    batch_size=100,
    training_examples=_n_(418857, "training_examples", lambda: training_examples),
    training_targets=_n_(418858, "training_targets", lambda: training_targets),
    validation_examples=_n_(418859, "validation_examples", lambda: validation_examples),
    validation_targets = _n_(418860, "validation_targets", lambda: validation_targets))
_l_(418862)