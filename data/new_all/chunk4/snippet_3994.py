# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64139685/python-h2o-script-typeerrors-at-end-closing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import h2o
    _l_(585255)

except ImportError:
    pass
_c_(585258, _a_(585257, _n_(585256, "h2o", lambda: h2o), "init"))
_l_(585259)
try:
    from h2o.estimators.glm import H2OGeneralizedLinearEstimator
    _l_(585261)

except ImportError:
    pass
prostate = _c_(585264, _a_(585263, _n_(585262, "h2o", lambda: h2o), "import_file"), "https://h2o-public-test-data.s3.amazonaws.com/smalldata/prostate/prostate.csv")
_l_(585265)
_n_(585266, "prostate", lambda: prostate)['CAPSULE'] = _c_(585269, _a_(585268, _n_(585267, "prostate", lambda: prostate)['CAPSULE'], "asfactor"))
_l_(585270)
_n_(585271, "prostate", lambda: prostate)['RACE'] = _c_(585274, _a_(585273, _n_(585272, "prostate", lambda: prostate)['RACE'], "asfactor"))
_l_(585275)
_n_(585276, "prostate", lambda: prostate)['DCAPS'] = _c_(585279, _a_(585278, _n_(585277, "prostate", lambda: prostate)['DCAPS'], "asfactor"))
_l_(585280)
_n_(585281, "prostate", lambda: prostate)['DPROS'] = _c_(585284, _a_(585283, _n_(585282, "prostate", lambda: prostate)['DPROS'], "asfactor"))
_l_(585285)
predictors = ["AGE", "RACE", "VOL", "GLEASON"]
_l_(585286)
response_col = "CAPSULE"
_l_(585287)
glm_model = _c_(585289, _n_(585288, "H2OGeneralizedLinearEstimator", lambda: H2OGeneralizedLinearEstimator), family="binomial", lambda_= 0, compute_p_values=True)
_l_(585290)
_c_(585296, _a_(585292, _n_(585291, "glm_model", lambda: glm_model), "train"), _n_(585293, "predictors", lambda: predictors), _n_(585294, "response_col", lambda: response_col), training_frame= _n_(585295, "prostate", lambda: prostate))
_l_(585297)
_c_(585299, _n_(585298, "print", lambda: print), 'Finished')
_l_(585300)