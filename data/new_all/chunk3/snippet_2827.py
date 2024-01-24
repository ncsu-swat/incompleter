# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61927908/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess
    _l_(535413)

except ImportError:
    pass
try:
    import joblib
    _l_(535415)

except ImportError:
    pass

_c_(535418, _n_(535416, "save_d2v_to_s3_current_doc2vec_model", lambda: save_d2v_to_s3_current_doc2vec_model), _n_(535417, "model_doc", lambda: model_doc),"doc2vec_model")
_l_(535419)

def save_d2v_to_s3_current_doc2vec_model(model,fname):
    _l_(535448)

    model_name = _n_(535420, "fname", lambda: fname)
    _l_(535421)
    _c_(535426, _a_(535423, _n_(535422, "joblib", lambda: joblib), "dump"), _n_(535424, "model", lambda: model),_n_(535425, "model_name", lambda: model_name))
    _l_(535427)
    s3_base_path = 's3://sd-flikku/datalake/current_doc2vec_model'
    _l_(535428)
    path = _n_(535429, "s3_base_path", lambda: s3_base_path)+'/'+_n_(535430, "model_name", lambda: model_name)
    _l_(535431)
    command = _c_(535437, _a_(535436, _c_(535435, _a_(535432, "aws s3 cp {} {}", "format"), _n_(535433, "model_name", lambda: model_name),_n_(535434, "path", lambda: path)), "split"))
    _l_(535438)
    _c_(535441, _n_(535439, "print", lambda: print), 'saving...'+_n_(535440, "model_name", lambda: model_name))
    _l_(535442)
    _c_(535446, _a_(535444, _n_(535443, "subprocess", lambda: subprocess), "call"), _n_(535445, "command", lambda: command))
    _l_(535447)