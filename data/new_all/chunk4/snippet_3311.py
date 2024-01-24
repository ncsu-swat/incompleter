# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75876808/typeerror-unsupported-operand-types-for-rv-continuous-frozen-and-rv-con
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(624533, _a_(624532, _n_(624531, "Doc2Vec", lambda: Doc2Vec), "load"), 'doc2vec.model')
_l_(624534)
v1 = _c_(624540, _a_(624536, _n_(624535, "model", lambda: model), "infer_vector"), _c_(624539, _a_(624538, _n_(624537, "resume", lambda: resume), "split")))
_l_(624541)
v2 = _c_(624547, _a_(624543, _n_(624542, "model", lambda: model), "infer_vector"), _c_(624546, _a_(624545, _n_(624544, "jd_df", lambda: jd_df)['data'][0], "split")))
_l_(624548)
cosine_similarity = _c_(624559, _a_(624550, _n_(624549, "np", lambda: np), "dot"), _c_(624554, _a_(624552, _n_(624551, "np", lambda: np), "array"), _n_(624553, "v1", lambda: v1)), _c_(624558, _a_(624556, _n_(624555, "np", lambda: np), "array"), _n_(624557, "v2", lambda: v2))) / (_c_(624565, _n_(624560, "norm", lambda: norm), _c_(624564, _a_(624562, _n_(624561, "np", lambda: np), "array"), _n_(624563, "v1", lambda: v1))) * _c_(624571, _n_(624566, "norm", lambda: norm), _c_(624570, _a_(624568, _n_(624567, "np", lambda: np), "array"), _n_(624569, "v2", lambda: v2))))
_l_(624572)
_c_(624577, _n_(624573, "print", lambda: print), _c_(624576, _n_(624574, "round", lambda: round), _n_(624575, "cosine_similarity", lambda: cosine_similarity), 3))
_l_(624578)