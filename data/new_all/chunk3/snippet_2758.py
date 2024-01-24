# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64220944/importing-open-data-set-giving-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import opendatasets as od
    _l_(575239)

except ImportError:
    pass

dataset_url='https://www.kaggle.com/rohanrao/air-quality-data-in-india'
_l_(575240)
_c_(575243, _a_(575242, _n_(575241, "od", lambda: od), "download"), 'https://www.kaggle.com/rohanrao/air-quality-data-in-india')
_l_(575244)
data_dir = './air-quality-data-in-india'  
_l_(575245)  