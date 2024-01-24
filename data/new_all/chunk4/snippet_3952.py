# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65006689/gensim-taggeddocument-list-generates-typeerror-nonetype-object-is-not-iterabl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class doc2vec_model(_n_(589786, "Doc2Vec", lambda: Doc2Vec)):
    _l_(589861)

    
    def train(self,path):
        _l_(589802)

        _n_(589787, "self", lambda: self)._path = _n_(589788, "path", lambda: path)
        _l_(589789)
        _c_(589792, _a_(589791, _n_(589790, "self", lambda: self), "_tagged_documents"))
        _l_(589793)

        _c_(589800, _a_(589797, _n_(589794, "super", lambda: super)(_n_(589795, "Doc2Vec", lambda: Doc2Vec), _n_(589796, "self", lambda: self)), "__init__"), _a_(589799, _n_(589798, "self", lambda: self), "_docs"), min_count = 100, 
                                     vector_size=300, 
                                     epochs = 20, 
                                     negative = 5, 
                                     workers=20, 
                                     sample = 1e-5,
                                     alpha=0.01,
                                     min_alpha=0.0001)
        _l_(589801)

    def _tagged_documents(self,):
        _l_(589860)

        _n_(589803, "self", lambda: self).file_l = [_n_(589804, "name", lambda: name) for name in _c_(589809, _a_(589806, _n_(589805, "glob", lambda: glob), "iglob"), _a_(589808, _n_(589807, "self", lambda: self), "_path"), recursive=True)]
        _l_(589810)
        _n_(589811, "self", lambda: self)._docs = [] 
        _l_(589812) 
        for f_id, path in _c_(589816, _n_(589813, "enumerate", lambda: enumerate), _a_(589815, _n_(589814, "self", lambda: self), "file_l")):
            _l_(589859)

            with _c_(589819, _n_(589817, "open", lambda: open), _n_(589818, "path", lambda: path),'r') as f:
                _l_(589858)

                docu = _c_(589822, _a_(589821, _n_(589820, "f", lambda: f), "read"))
                _l_(589823)
                docu = _c_(589826, _n_(589824, "norm_string", lambda: norm_string), _n_(589825, "docu", lambda: docu))
                _l_(589827)
                docu = _c_(589830, _a_(589829, _n_(589828, "docu", lambda: docu), "split"), ' ')
                _l_(589831)
                chunk_size = 200 
                _l_(589832) 
                chunk_l = [_n_(589833, "docu", lambda: docu)[_n_(589834, "i", lambda: i):_n_(589835, "i", lambda: i)+_n_(589836, "chunk_size", lambda: chunk_size)] for i in _c_(589842, _n_(589837, "range", lambda: range), 0,_c_(589840, _n_(589838, "len", lambda: len), _n_(589839, "docu", lambda: docu)),_n_(589841, "chunk_size", lambda: chunk_size))]
                _l_(589843)
                for c_id, docu_chunk in _c_(589846, _n_(589844, "enumerate", lambda: enumerate), _n_(589845, "chunk_l", lambda: chunk_l)):
                    _l_(589857)

                    _c_(589855, _a_(589849, _a_(589848, _n_(589847, "self", lambda: self), "_docs"), "append"), _c_(589854, _n_(589850, "TaggedDocument", lambda: TaggedDocument), words=_n_(589851, "docu_chunk", lambda: docu_chunk), tags=(f'DOC_{_n_(589852, "f_id", lambda: f_id)}_{_n_(589853, "c_id", lambda: c_id)}',)))
                    _l_(589856)