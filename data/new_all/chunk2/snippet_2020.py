# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69448637/amazon-sagemaker-typeerror-cant-pickle-dict-keys-objects
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
sc = _c_(437033, _n_(437032, "SparkContext", lambda: SparkContext), appName='microsegment-job')
_l_(437034)
rdd = _c_(437038, _a_(437036, _n_(437035, "sc", lambda: sc), "textFile"), _n_(437037, "dataset_path", lambda: dataset_path))
_l_(437039)
header = _c_(437042, _a_(437041, _n_(437040, "rdd", lambda: rdd), "first"))
_l_(437043)
cols = _c_(437047, _a_(437045, _n_(437044, "header", lambda: header), "split"), _n_(437046, "delimiter", lambda: delimiter))
_l_(437048)

cols_dict = {_n_(437049, "cols", lambda: cols)[_n_(437050, "i", lambda: i)]: _n_(437051, "i", lambda: i) for i in _c_(437056, _n_(437052, "range", lambda: range), _c_(437055, _n_(437053, "len", lambda: len), _n_(437054, "cols", lambda: cols)))}
_l_(437057)

other_kpis = []
_l_(437058)
for i in _n_(437059, "cols", lambda: cols):
    _l_(437073)

    if _n_(437060, "i", lambda: i) in _n_(437061, "filter_cond", lambda: filter_cond) or _n_(437062, "i", lambda: i) == 'CONSUMER_ID':
        _l_(437064)

        continue
        _l_(437063)
    if _n_(437065, "i", lambda: i) == 'eventids':
        _l_(437067)

        break
        _l_(437066)
    _c_(437071, _a_(437069, _n_(437068, "other_kpis", lambda: other_kpis), "append"), _n_(437070, "i", lambda: i))
    _l_(437072)

def return_row(z):
    _l_(437096)

    temp = _c_(437077, _a_(437075, _n_(437074, "z", lambda: z), "split"), _n_(437076, "delimiter", lambda: delimiter))
    _l_(437078)
    row = [_c_(437083, _n_(437079, "float", lambda: float), _n_(437080, "temp", lambda: temp)[_n_(437081, "cols_dict", lambda: cols_dict)[_n_(437082, "kpi", lambda: kpi)]]) if _n_(437084, "temp", lambda: temp)[_n_(437085, "cols_dict", lambda: cols_dict)[_n_(437086, "kpi", lambda: kpi)]] != '' else 0.0 for kpi in (_n_(437087, "kpi_list", lambda: kpi_list) + _n_(437088, "other_kpis", lambda: other_kpis))] + [
        _n_(437089, "temp", lambda: temp)[_n_(437090, "cols_dict", lambda: cols_dict)['eventids']]] + [_n_(437091, "temp", lambda: temp)[_n_(437092, "cols_dict", lambda: cols_dict)['conversions']]]
    _l_(437093)
    aux = _n_(437094, "row", lambda: row)
    _l_(437095)
    return aux

rdd_splitted = _c_(437104, _a_(437102, _c_(437101, _a_(437098, _n_(437097, "rdd", lambda: rdd), "filter"), lambda z: _n_(437099, "header", lambda: header) not in _n_(437100, "z", lambda: z)), "map"), _n_(437103, "return_row", lambda: return_row))
_l_(437105)
eids = _c_(437118, _a_(437117, _c_(437116, _a_(437115, _c_(437114, _a_(437107, _n_(437106, "rdd_splitted", lambda: rdd_splitted), "flatMap"), lambda x: _c_(437113, _a_(437112, _n_(437108, "x", lambda: x)[_c_(437111, _n_(437109, "len", lambda: len), _n_(437110, "x", lambda: x)) - 2], "split"), "|")), "distinct")), "collect")) # Exception thrown in this line
_l_(437119) # Exception thrown in this line