# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75522713/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-when-trying-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(593051)

except ImportError:
    pass
try:
    import numpy as np
    _l_(593053)

except ImportError:
    pass
try:
    from sklearn.svm import SVR
    _l_(593055)

except ImportError:
    pass
try:
    from sklearn.metrics import mean_squared_error
    _l_(593057)

except ImportError:
    pass
try:
    from pyswarms.single.global_best import GlobalBestPSO
    _l_(593059)

except ImportError:
    pass

# Load the input and output data from a CSV file
# data = pd.read_csv('data.csv')

# Separate the input and output data

X=_a_(593061, _n_(593060, "d3", lambda: d3), "iloc")[:,:11]
_l_(593062)
y=_a_(593064, _n_(593063, "d3", lambda: d3), "iloc")[:,-1]
_l_(593065)


# Define the fitness function to optimize the SVR model
def svr_fitness_function(params):
    _l_(593098)

    # Extract the SVR hyperparameters from the input vector
    C = _n_(593066, "params", lambda: params)[0]
    _l_(593067)
    gamma = _n_(593068, "params", lambda: params)[1]
    _l_(593069)
    epsilon = _n_(593070, "params", lambda: params)[2]
    _l_(593071)
    
    # Create a new SVR model with the given hyperparameters
    model = _c_(593078, _n_(593072, "SVR", lambda: SVR), C=_n_(593073, "C", lambda: C), gamma=_c_(593076, _a_(593075, _n_(593074, "gamma", lambda: gamma), "all")), epsilon=_n_(593077, "epsilon", lambda: epsilon))
    _l_(593079)
    
    # Train the model on the input and output data
    _c_(593084, _a_(593081, _n_(593080, "model", lambda: model), "fit"), _n_(593082, "X", lambda: X), _n_(593083, "y", lambda: y))
    _l_(593085)
    
    # Use the trained model to make predictions on the input data
    y_pred = _c_(593089, _a_(593087, _n_(593086, "model", lambda: model), "predict"), _n_(593088, "X", lambda: X))
    _l_(593090)
    
    # Calculate the mean squared error of the predictions
    mse = _c_(593094, _n_(593091, "mean_squared_error", lambda: mean_squared_error), _n_(593092, "y", lambda: y), _n_(593093, "y_pred", lambda: y_pred))
    _l_(593095)
    aux = -_n_(593096, "mse", lambda: mse)
    _l_(593097)
    
    # Return the negative of the mean squared error as the fitness value
    return aux

# Set up the PSO optimizer
n_particles = 20
_l_(593099)
max_iter = 100
_l_(593100)
bounds = (_c_(593103, _a_(593102, _n_(593101, "np", lambda: np), "array"), [0.1, 0.1, 0.1]), _c_(593106, _a_(593105, _n_(593104, "np", lambda: np), "array"), [10, 10, 1]))
_l_(593107)
optimizer = _c_(593110, _n_(593108, "GlobalBestPSO", lambda: GlobalBestPSO), n_particles=_n_(593109, "n_particles", lambda: n_particles), dimensions=3, options={'c1': 0.5, 'c2': 0.3, 'w': 0.9})
_l_(593111)

# Run the PSO optimizer to find the optimal SVR hyperparameters
best_cost, best_params = _c_(593116, _a_(593113, _n_(593112, "optimizer", lambda: optimizer), "optimize"), _n_(593114, "svr_fitness_function", lambda: svr_fitness_function), iters=_n_(593115, "max_iter", lambda: max_iter))
_l_(593117)

# Print the optimal SVR hyperparameters and the corresponding mean squared error
_c_(593120, _n_(593118, "print", lambda: print), 'Optimal SVR hyperparameters:', _n_(593119, "best_params", lambda: best_params))
_l_(593121)
_c_(593124, _n_(593122, "print", lambda: print), 'Corresponding mean squared error:', -_n_(593123, "best_cost", lambda: best_cost))
_l_(593125)