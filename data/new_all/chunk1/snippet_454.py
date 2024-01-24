# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53671612/apriori-model-has-typeerror-unorderable-types-float-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dataset = _c_(396227, _a_(396226, _n_(396225, "pd", lambda: pd), "read_csv"), "Market_Basket_Optimisation.csv", header = None)
_l_(396228)
transactions =[]
_l_(396229)
for i in _c_(396231, _n_(396230, "range", lambda: range), 0,7501):
      _l_(396244)

      _c_(396242, _a_(396233, _n_(396232, "transactions", lambda: transactions), "append"), [_c_(396239, _n_(396234, "str", lambda: str), _a_(396236, _n_(396235, "dataset", lambda: dataset), "values")[_n_(396237, "i", lambda: i),_n_(396238, "j", lambda: j)]) for j in _c_(396241, _n_(396240, "range", lambda: range), 0,20)])
      _l_(396243)
try:
      from apyori import apriori
      _l_(396246)

except ImportError:
      pass
rules = _c_(396249, _n_(396247, "apriori", lambda: apriori), _n_(396248, "transactions", lambda: transactions),min_support=0.003,min_confidence=0.2,min_lift=3,min_lenght=2)
_l_(396250)
res= _c_(396253, _n_(396251, "list", lambda: list), _n_(396252, "rules", lambda: rules))
_l_(396254)