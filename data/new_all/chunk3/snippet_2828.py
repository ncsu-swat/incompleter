# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61927908/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(530659, _n_(530658, "load_d2v", lambda: load_d2v), "doc2vec_model")
_l_(530660)

def load_d2v(fname):
    _l_(530690)

    model_name = _n_(530661, "fname", lambda: fname)
    _l_(530662)
    s3_base_path='s3://sd-flikku/datalake/current_doc2vec_model'
    _l_(530663)
    path = _n_(530664, "s3_base_path", lambda: s3_base_path)+'/'+_n_(530665, "model_name", lambda: model_name)  
    _l_(530666)  
    command = _c_(530672, _a_(530671, _c_(530670, _a_(530667, "aws s3 cp {} {}", "format"), _n_(530668, "path", lambda: path),_n_(530669, "model_name", lambda: model_name)), "split"))
    _l_(530673)
    _c_(530676, _n_(530674, "print", lambda: print), 'loading...'+_n_(530675, "model_name", lambda: model_name))
    _l_(530677)
    _c_(530681, _a_(530679, _n_(530678, "subprocess", lambda: subprocess), "call"), _n_(530680, "command", lambda: command))
    _l_(530682)
    model=_c_(530686, _a_(530684, _n_(530683, "joblib", lambda: joblib), "load"), _n_(530685, "model_name", lambda: model_name))
    _l_(530687)
    aux = _n_(530688, "model", lambda: model)
    _l_(530689)
    return aux