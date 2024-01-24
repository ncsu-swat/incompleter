# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63528707/attributeerror-unaryop-object-has-no-attribute-evaluate-when-using-eval-fun
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for test_ind, case_data in _c_(576274, _a_(576273, _n_(576272, "test_df", lambda: test_df), "iterrows")):
      _l_(576295)

      case_data = _a_(576278, _c_(576277, _a_(576276, _n_(576275, "case_data", lambda: case_data), "to_frame")), "T")
      _l_(576279)
      rule = "Ask_before>-0.4843681 & 0.5255821<=BidVol_before<=0.07581073 & Volume>0.1107559"
      _l_(576280)
      _c_(576283, _n_(576281, "print", lambda: print), _n_(576282, "case_data", lambda: case_data), "case_data")
      _l_(576284)
      if _c_(576290, _a_(576289, _c_(576288, _a_(576286, _n_(576285, "case_data", lambda: case_data), "eval"), _n_(576287, "rule", lambda: rule)), "all")) == True:
            _l_(576294)

            _c_(576292, _n_(576291, "print", lambda: print), "TRUE")
            _l_(576293)