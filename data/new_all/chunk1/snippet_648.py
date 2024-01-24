# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72495248/databricks-spark-python-pyspark-serializers-py-attributeerror-str-object-has
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from hyperopt import fmin, tpe, hp, SparkTrials, Trials, STATUS_OK
  _l_(384158)

except ImportError:
  pass
try:
  from hyperopt.pyll import scope
  _l_(384160)

except ImportError:
  pass
try:
  from math import exp
  _l_(384162)

except ImportError:
  pass
try:
  import mlflow.xgboost
  _l_(384164)

except ImportError:
  pass
try:
  import numpy as np
  _l_(384166)

except ImportError:
  pass
try:
  import xgboost as xgb
  _l_(384168)

except ImportError:
  pass
 
_a_(384170, _n_(384169, "pyspark", lambda: pyspark), "InheritableThread")  
_l_(384171)  
#mlflow.set_experiment("/Shared/experiments/ichi")
search_space = {
  'max_depth': _c_(384177, _a_(384173, _n_(384172, "scope", lambda: scope), "int"), _c_(384176, _a_(384175, _n_(384174, "hp", lambda: hp), "quniform"), 'max_depth', 4, 100, 1)),
  'learning_rate': _c_(384180, _a_(384179, _n_(384178, "hp", lambda: hp), "loguniform"), 'learning_rate', -3, 0),
  'reg_alpha': _c_(384183, _a_(384182, _n_(384181, "hp", lambda: hp), "loguniform"), 'reg_alpha', -5, -1),
  'reg_lambda': _c_(384186, _a_(384185, _n_(384184, "hp", lambda: hp), "loguniform"), 'reg_lambda', -6, -1),
  'min_child_weight': _c_(384189, _a_(384188, _n_(384187, "hp", lambda: hp), "loguniform"), 'min_child_weight', -1, 3),
  'objective': 'binary:logistic',
  'seed': 123, # Set a seed for deterministic training
}
_l_(384190)
 
def train_model(params):
  _l_(384253)

  # With MLflow autologging, hyperparameters and the trained model are automatically logged to MLflow.
  _c_(384193, _a_(384192, _a_(384191, mlflow, "xgboost"), "autolog"))
  _l_(384194)
  with _c_(384197, _a_(384196, _n_(384195, "mlflow", lambda: mlflow), "start_run"), nested=True):
    _l_(384252)

    train = _c_(384202, _a_(384199, _n_(384198, "xgb", lambda: xgb), "DMatrix"), data=_n_(384200, "X_train", lambda: X_train), label=_n_(384201, "y_train", lambda: y_train))
    _l_(384203)
    validation = _c_(384208, _a_(384205, _n_(384204, "xgb", lambda: xgb), "DMatrix"), data=_n_(384206, "X_val", lambda: X_val), label=_n_(384207, "y_val", lambda: y_val))
    _l_(384209)
    # Pass in the validation set so xgb can track an evaluation metric. XGBoost terminates training when the evaluation metric
    # is no longer improving.
    booster = _c_(384215, _a_(384211, _n_(384210, "xgb", lambda: xgb), "train"), params=_n_(384212, "params", lambda: params), dtrain=_n_(384213, "train", lambda: train), num_boost_round=1000,\
                        evals=[(_n_(384214, "validation", lambda: validation), "validation")], early_stopping_rounds=50)
    _l_(384216)
    validation_predictions = _c_(384220, _a_(384218, _n_(384217, "booster", lambda: booster), "predict"), _n_(384219, "validation", lambda: validation))
    _l_(384221)
    auc_score = _c_(384225, _n_(384222, "roc_auc_score", lambda: roc_auc_score), _n_(384223, "y_val", lambda: y_val), _n_(384224, "validation_predictions", lambda: validation_predictions))
    _l_(384226)
    _c_(384230, _a_(384228, _n_(384227, "mlflow", lambda: mlflow), "log_metric"), 'auc', _n_(384229, "auc_score", lambda: auc_score))
    _l_(384231)
 
    signature = _c_(384238, _n_(384232, "infer_signature", lambda: infer_signature), _n_(384233, "X_train", lambda: X_train), _c_(384237, _a_(384235, _n_(384234, "booster", lambda: booster), "predict"), _n_(384236, "train", lambda: train)))
    _l_(384239)
    _c_(384244, _a_(384241, _a_(384240, mlflow, "xgboost"), "log_model"), _n_(384242, "booster", lambda: booster), "model", signature=_n_(384243, "signature", lambda: signature))
    _l_(384245)
    aux = {'status': _n_(384246, "STATUS_OK", lambda: STATUS_OK), 'loss': -1*_n_(384247, "auc_score", lambda: auc_score), 'booster': _c_(384250, _a_(384249, _n_(384248, "booster", lambda: booster), "attributes"))}
    _l_(384251)
    
    # Set the loss to -1*auc_score so fmin maximizes the auc_score
    return aux
 
# Greater parallelism will lead to speedups, but a less optimal hyperparameter sweep. 
# A reasonable value for parallelism is the square root of max_evals.
spark_trials = _c_(384255, _n_(384254, "SparkTrials", lambda: SparkTrials), parallelism=10)
_l_(384256)
 
# Run fmin within an MLflow run context so that each hyperparameter configuration is logged as a child run of a parent
# run called "xgboost_models" .
with _c_(384259, _a_(384258, _n_(384257, "mlflow", lambda: mlflow), "start_run"), run_name='xgboost_models'):
  _l_(384268)

  best_params = _c_(384266, _n_(384260, "fmin", lambda: fmin), fn=_n_(384261, "train_model", lambda: train_model), 
    space=_n_(384262, "search_space", lambda: search_space), 
    algo=_a_(384264, _n_(384263, "tpe", lambda: tpe), "suggest"), 
    max_evals=96,
    trials=_n_(384265, "spark_trials", lambda: spark_trials),
  )
  _l_(384267)