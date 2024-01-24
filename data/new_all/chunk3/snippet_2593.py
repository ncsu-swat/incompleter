# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70277732/glob-filenames-attributeerror-str-object-has-no-attribute-content
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(560166, _n_(560165, "open", lambda: open), 'filt_gri.txt', 'r') as filehandle:
    _l_(560174)

    tags = [_c_(560169, _a_(560168, _n_(560167, "current_place", lambda: current_place), "rstrip")) for current_place in _c_(560172, _a_(560171, _n_(560170, "filehandle", lambda: filehandle), "readlines"))]
    _l_(560173)

doc_classifier = _c_(560177, _n_(560175, "TransformersDocumentClassifier", lambda: TransformersDocumentClassifier), model_name_or_path="cross-encoder/nli-distilroberta-base",
                                                task="zero-shot-classification",
                                                labels=_n_(560176, "tags", lambda: tags),
                                                batch_size=16)
_l_(560178)

classified_docs = _c_(560182, _a_(560180, _n_(560179, "doc_classifier", lambda: doc_classifier), "predict"), _n_(560181, "docs_to_classify", lambda: docs_to_classify))
_l_(560183)

all_docs = _c_(560186, _n_(560184, "convert_files_to_dicts", lambda: convert_files_to_dicts), dir_path=_n_(560185, "doc_dir", lambda: doc_dir))
_l_(560187)

preprocessor_sliding_window = _c_(560189, _n_(560188, "PreProcessor", lambda: PreProcessor), split_overlap=3,
                                           split_length=10,
                                           split_respect_sentence_boundary=False,
                                           split_by='passage')
_l_(560190)