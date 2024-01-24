# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70302409/elasticsearch-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
doc_dir = "GRIs/"  # contains 2 .pdfs
_l_(394322)  # contains 2 .pdfs

with _c_(394324, _n_(394323, "open", lambda: open), 'filt_gri.txt', 'r') as filehandle:
    _l_(394332)

    tags = [_c_(394327, _a_(394326, _n_(394325, "current_place", lambda: current_place), "rstrip")) for current_place in _c_(394330, _a_(394329, _n_(394328, "filehandle", lambda: filehandle), "readlines"))]
    _l_(394331)


doc_classifier = _c_(394335, _n_(394333, "TransformersDocumentClassifier", lambda: TransformersDocumentClassifier), model_name_or_path="cross-encoder/nli-distilroberta-base",
                                                task="zero-shot-classification",
                                                labels=_n_(394334, "tags", lambda: tags),
                                                batch_size=2)
_l_(394336)

# convert to Document using a fieldmap for custom content fields the classification should run on
docs_to_classify = [_c_(394340, _a_(394338, _n_(394337, "Document", lambda: Document), "from_dict"), _n_(394339, "d", lambda: d)) for d in _n_(394341, "docs_sliding_window", lambda: docs_sliding_window)]
_l_(394342)

# classify using gpu, batch_size makes sure we do not run out of memory
classified_docs = _c_(394346, _a_(394344, _n_(394343, "doc_classifier", lambda: doc_classifier), "predict"), _n_(394345, "docs_to_classify", lambda: docs_to_classify))
_l_(394347)

# let's see how it looks: there should be a classification result in the meta entry containing labels and scores.
_c_(394352, _n_(394348, "print", lambda: print), _c_(394351, _a_(394350, _n_(394349, "classified_docs", lambda: classified_docs)[0], "to_dict")))
_l_(394353)

all_docs = _c_(394356, _n_(394354, "convert_files_to_dicts", lambda: convert_files_to_dicts), dir_path=_n_(394355, "doc_dir", lambda: doc_dir))
_l_(394357)

preprocessor_sliding_window = _c_(394359, _n_(394358, "PreProcessor", lambda: PreProcessor), split_overlap=3,
                                           split_length=10,
                                           split_respect_sentence_boundary=False,
                                           split_by='passage')
_l_(394360)