# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73993987/attributeerror-module-google-cloud-vision-v1-has-no-attribute-feature
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import io
    _l_(586848)

except ImportError:
    pass
try:
    from google.cloud import vision_v1
    _l_(586850)

except ImportError:
    pass

def sample_batch_annotate_files(file_path="path/to/your/document.pdf"):
    _l_(586929)

    """Perform batch file annotation."""
    client = _c_(586853, _a_(586852, _n_(586851, "vision_v1", lambda: vision_v1), "ImageAnnotatorClient"))
    _l_(586854)
    # Supported mime_type: application/pdf, image/tiff, image/gif
    mime_type = "application/pdf"
    _l_(586855)
    with _c_(586859, _a_(586857, _n_(586856, "io", lambda: io), "open"), _n_(586858, "file_path", lambda: file_path), "rb") as f:
        _l_(586864)

        content = _c_(586862, _a_(586861, _n_(586860, "f", lambda: f), "read"))
        _l_(586863)
    input_config = {"mime_type": _n_(586865, "mime_type", lambda: mime_type), "content": _n_(586866, "content", lambda: content)}
    _l_(586867)
    features = [{"type_": _a_(586871, _a_(586870, _a_(586869, _n_(586868, "vision_v1", lambda: vision_v1), "Feature"), "Type"), "DOCUMENT_TEXT_DETECTION")}]
    _l_(586872)
    # The service can process up to 5 pages per document file. Here we specify
    # the first, second, and last page of the document to be processed.
    pages = [1, 2, -1]
    _l_(586873)
    requests = [{"input_config": _n_(586874, "input_config", lambda: input_config), "features": _n_(586875, "features", lambda: features), "pages": _n_(586876, "pages", lambda: pages)}]
    _l_(586877)
    response = _c_(586881, _a_(586879, _n_(586878, "client", lambda: client), "batch_annotate_files"), requests=_n_(586880, "requests", lambda: requests))
    _l_(586882)
    for image_response in _a_(586885, _a_(586884, _n_(586883, "response", lambda: response), "responses")[0], "responses"):
        _l_(586928)

        _c_(586892, _n_(586886, "print", lambda: print), _c_(586891, _a_(586887, u"Full text: {}", "format"), _a_(586890, _a_(586889, _n_(586888, "image_response", lambda: image_response), "full_text_annotation"), "text")))
        _l_(586893)
        for page in _a_(586896, _a_(586895, _n_(586894, "image_response", lambda: image_response), "full_text_annotation"), "pages"):
            _l_(586927)

            for block in _a_(586898, _n_(586897, "page", lambda: page), "blocks"):
                _l_(586926)

                _c_(586904, _n_(586899, "print", lambda: print), _c_(586903, _a_(586900, u"\nBlock confidence: {}", "format"), _a_(586902, _n_(586901, "block", lambda: block), "confidence")))
                _l_(586905)
                for par in _a_(586907, _n_(586906, "block", lambda: block), "paragraphs"):
                    _l_(586925)

                    _c_(586913, _n_(586908, "print", lambda: print), _c_(586912, _a_(586909, u"\tParagraph confidence: {}", "format"), _a_(586911, _n_(586910, "par", lambda: par), "confidence")))
                    _l_(586914)
                    for word in _a_(586916, _n_(586915, "par", lambda: par), "words"):
                        _l_(586924)

                        _c_(586922, _n_(586917, "print", lambda: print), _c_(586921, _a_(586918, u"\t\tWord confidence: {}", "format"), _a_(586920, _n_(586919, "word", lambda: word), "confidence")))
                        _l_(586923)