# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63519415/error-as-typeerror-cannot-pickle-thread-rlock-object
# create model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(551325, _n_(551323, "KerasClassifier", lambda: KerasClassifier), build_fn=_n_(551324, "model", lambda: model), verbose=0)
_l_(551326)

# define the grid search parameters
batch_size = [10, 20, 40, 60, 80, 100]
_l_(551327)
epochs = [10, 50, 100]
_l_(551328)
param_grid = _c_(551332, _n_(551329, "dict", lambda: dict), batch_size=_n_(551330, "batch_size", lambda: batch_size), epochs=_n_(551331, "epochs", lambda: epochs))
_l_(551333)
grid = _c_(551337, _n_(551334, "GridSearchCV", lambda: GridSearchCV), estimator=_n_(551335, "model", lambda: model), param_grid=_n_(551336, "param_grid", lambda: param_grid), n_jobs=-1, cv=3)
_l_(551338)
grid_result = _c_(551343, _a_(551340, _n_(551339, "grid", lambda: grid), "fit"), _n_(551341, "x_train_noisy", lambda: x_train_noisy), _n_(551342, "y_train", lambda: y_train))
_l_(551344)


# summarize results
_c_(551350, _n_(551345, "print", lambda: print), "Best: %f using %s" % (_a_(551347, _n_(551346, "grid_result", lambda: grid_result), "best_score_"), _a_(551349, _n_(551348, "grid_result", lambda: grid_result), "best_params_")))
_l_(551351)
means = _a_(551353, _n_(551352, "grid_result", lambda: grid_result), "cv_results_")['mean_test_score']
_l_(551354)
stds = _a_(551356, _n_(551355, "grid_result", lambda: grid_result), "cv_results_")['std_test_score']
_l_(551357)
params = _a_(551359, _n_(551358, "grid_result", lambda: grid_result), "cv_results_")['params']
_l_(551360)
for mean, stdev, param in _c_(551365, _n_(551361, "zip", lambda: zip), _n_(551362, "means", lambda: means), _n_(551363, "stds", lambda: stds), _n_(551364, "params", lambda: params)):
    _l_(551372)

    _c_(551370, _n_(551366, "print", lambda: print), "%f (%f) with: %r" % (_n_(551367, "mean", lambda: mean), _n_(551368, "stdev", lambda: stdev), _n_(551369, "param", lambda: param)))
    _l_(551371)