# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75909808/attributeerror-countvectorizer-object-has-no-attribute-get-feature-names
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.decomposition import LatentDirichletAllocation
    _l_(539385)

except ImportError:
    pass
vectorizer = _c_(539387, _n_(539386, "CountVectorizer", lambda: CountVectorizer), analyzer='word',       
            min_df=3,# minimum required occurences of a word 
            stop_words='english',# remove stop words
            lowercase=True,# convert all words to lowercase
            token_pattern='[a-zA-Z0-9]{3,}',# num chars > 3
            max_features=5000,# max number of unique words
            )
_l_(539388)


data_matrix = _c_(539392, _a_(539390, _n_(539389, "vectorizer", lambda: vectorizer), "fit_transform"), _n_(539391, "df_clean", lambda: df_clean)['question_lemmatize_clean'])
_l_(539393)

                                                                    
lda_model = _c_(539395, _n_(539394, "LatentDirichletAllocation", lambda: LatentDirichletAllocation), n_components=10, # Number of topics
            learning_method='online',
            random_state=20,       
            n_jobs = -1  # Use all available CPUs
            )
_l_(539396)
    
    
lda_output = _c_(539400, _a_(539398, _n_(539397, "lda_model", lambda: lda_model), "fit_transform"), _n_(539399, "data_matrix", lambda: data_matrix))
_l_(539401)
try:
    import pyLDAvis
    _l_(539403)

except ImportError:
    pass
try:
    import pyLDAvis.sklearn
    _l_(539405)

except ImportError:
    pass
_c_(539408, _a_(539407, _n_(539406, "pyLDAvis", lambda: pyLDAvis), "enable_notebook"))
_l_(539409)
_c_(539415, _a_(539411, _a_(539410, pyLDAvis, "sklearn"), "prepare"), _n_(539412, "lda_model", lambda: lda_model), _n_(539413, "data_matrix", lambda: data_matrix), _n_(539414, "vectorizer", lambda: vectorizer), mds='tsne')    
_l_(539416)    