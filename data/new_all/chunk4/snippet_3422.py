# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74611572/bayesianoptimization-search-errors-out-typeerror-float-object-is-not-subscri
# Search hyperparameters

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
SEED = 121
_l_(589229)

# NN

tuner_nn = _c_(589233, _n_(589230, "BayesianOptimization", lambda: BayesianOptimization), _n_(589231, "nn_builder", lambda: nn_builder),
objective = 'val_loss',
max_trials = 20,
seed = _n_(589232, "SEED", lambda: SEED),
directory = '/Users/myuser/Documents/kerastuner',
overwrite = True
)
_l_(589234)

_c_(589241, _a_(589236, _n_(589235, "tuner_nn", lambda: tuner_nn), "search"), _n_(589237, "x_train", lambda: x_train), _n_(589238, "y_train", lambda: y_train), epochs=50, validation_data=(_n_(589239, "x_val", lambda: x_val), ), verbose=0, callbacks=[_n_(589240, "Earlystopping", lambda: Earlystopping)])
_l_(589242)

## Build model based on the optimized hyperparameters

besthp_nn = _c_(589245, _a_(589244, _n_(589243, "tuner_nn", lambda: tuner_nn), "get_best_hyperparameters"))[0]
_l_(589246)
model_nn = _c_(589251, _a_(589249, _a_(589248, _n_(589247, "tuner_nn", lambda: tuner_nn), "hypermodel"), "build"), _n_(589250, "besthp_nn", lambda: besthp_nn))
_l_(589252)

# lstm

tuner_lstm = _c_(589256, _n_(589253, "BayesianOptimization", lambda: BayesianOptimization), _n_(589254, "lstm_builder", lambda: lstm_builder),
objective = 'val_loss',
max_trials = 20,
seed = _n_(589255, "SEED", lambda: SEED),
directory = '/Users/myuser/Documents/kerastuner')
_l_(589257)

_c_(589265, _a_(589259, _n_(589258, "tuner_lstm", lambda: tuner_lstm), "search"), _n_(589260, "x_train", lambda: x_train), _n_(589261, "y_train", lambda: y_train), epochs=50, validation_data=(_n_(589262, "x_val", lambda: x_val), _n_(589263, "y_val", lambda: y_val)), verbose=0, callbacks=[_n_(589264, "Earlystopping", lambda: Earlystopping)])
_l_(589266)

## Build model based on the optimized hyperparameters

besthp_lstm = _c_(589269, _a_(589268, _n_(589267, "tuner_lstm", lambda: tuner_lstm), "get_best_hyperparameters"))[0]
_l_(589270)
model_lstm = _c_(589275, _a_(589273, _a_(589272, _n_(589271, "tuner_lstm", lambda: tuner_lstm), "hypermodel"), "build"), _n_(589274, "besthp_lstm", lambda: besthp_lstm))
_l_(589276)

# gru

tuner_gru = _c_(589280, _n_(589277, "BayesianOptimization", lambda: BayesianOptimization), _n_(589278, "gru_builder", lambda: gru_builder),
objective = 'val_loss',
max_trials = 20,
seed = _n_(589279, "SEED", lambda: SEED),
directory = '/Users/myuser/Documents/kerastuner')
_l_(589281)

_c_(589289, _a_(589283, _n_(589282, "tuner_gru", lambda: tuner_gru), "search"), _n_(589284, "x_train", lambda: x_train), _n_(589285, "y_train", lambda: y_train), epochs=50, validation_data=(_n_(589286, "x_val", lambda: x_val), _n_(589287, "y_val", lambda: y_val)), verbose=0, callbacks=[_n_(589288, "Earlystopping", lambda: Earlystopping)])
_l_(589290)

## Build model based on the optimized hyperparameters

besthp_gru = _c_(589293, _a_(589292, _n_(589291, "tuner_gru", lambda: tuner_gru), "get_best_hyperparameters"))[0]
_l_(589294)
model_gru = _c_(589299, _a_(589297, _a_(589296, _n_(589295, "tuner_gru", lambda: tuner_gru), "hypermodel"), "build"), _n_(589298, "besthp_gru", lambda: besthp_gru))
_l_(589300)