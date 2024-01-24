# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51095346/attributeerror-cant-pickle-local-object-op-make-py-thunk-locals-rval-while
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
log_dose = _c_(472491, _a_(472490, _n_(472489, "np", lambda: np), "array"), [-.86, -.3, -.05, .73])
_l_(472492)
log_dose_shared = _c_(472495, _n_(472493, "shared", lambda: shared), _n_(472494, "log_dose", lambda: log_dose))
_l_(472496)
n = 5 * _c_(472500, _a_(472498, _n_(472497, "np", lambda: np), "ones"), 4, dtype = _n_(472499, "int", lambda: int))
_l_(472501)
n_shared = _c_(472504, _n_(472502, "shared", lambda: shared), _n_(472503, "n", lambda: n))
_l_(472505)
deaths = _c_(472508, _a_(472507, _n_(472506, "np", lambda: np), "array"), [0, 1, 3, 5])
_l_(472509)

with _c_(472511, _n_(472510, "Model", lambda: Model)) as bioassay_model:
    _l_(472530)

    # Logit model parameters
    alpha = _c_(472513, _n_(472512, "Normal", lambda: Normal), 'alpha', 0, sd = 100)
    _l_(472514)
    beta = _c_(472516, _n_(472515, "Normal", lambda: Normal), 'beta', 0, sd = 100)
    _l_(472517)
    # Calculate probabilities of death
    theta = _c_(472522, _n_(472518, "invlogit", lambda: invlogit), _n_(472519, "alpha", lambda: alpha) + _n_(472520, "beta", lambda: beta) * _n_(472521, "log_dose_shared", lambda: log_dose_shared))
    _l_(472523)
    # Data likelihood
    obs_death = _c_(472528, _n_(472524, "Binomial", lambda: Binomial), 'obs_death', n = _n_(472525, "n_shared", lambda: n_shared), p = _n_(472526, "theta", lambda: theta), observed = _n_(472527, "deaths", lambda: deaths))
    _l_(472529)

with _n_(472531, "bioassay_model", lambda: bioassay_model):
    _l_(472545)

    # Obtain starting values via MAP
    start = _c_(472534, _n_(472532, "find_MAP", lambda: find_MAP), model = _n_(472533, "bioassay_model", lambda: bioassay_model))
    _l_(472535)
    # Instantiate sampler
    step = _c_(472538, _a_(472537, _n_(472536, "pm", lambda: pm), "Metropolis"))
    _l_(472539)
    # Draw 2000 posterior samples
    bioassay_trace = _c_(472543, _n_(472540, "sample", lambda: sample), 50000, step = _n_(472541, "step", lambda: step), start = _n_(472542, "start", lambda: start))
    _l_(472544)