# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75320868/attributeerror-module-click-utils-has-no-attribute-expand-args-when-im-t
# Loop over the contents of the directory containing the resumes, filtering by .pdf or .doc(x)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for resume in _c_(413313, _n_(413304, "list", lambda: list), _c_(413312, _n_(413305, "filter", lambda: filter), lambda x: _n_(413306, "extension", lambda: extension) in _n_(413307, "x", lambda: x), _c_(413311, _a_(413309, _n_(413308, "os", lambda: os), "listdir"), _n_(413310, "PROJECT_DIR", lambda: PROJECT_DIR) + '/CV'))):
    _l_(413347)

    if _n_(413314, "extension", lambda: extension) == 'pdf':
        _l_(413337)

        # Read in every resume with pdf extension in the directory
        _c_(413323, _a_(413316, _n_(413315, "resume_texts", lambda: resume_texts), "append"), _c_(413322, _n_(413317, "nlp", lambda: nlp), _c_(413321, _n_(413318, "extract_text_from_pdf", lambda: extract_text_from_pdf), _n_(413319, "PROJECT_DIR", lambda: PROJECT_DIR) + '/CV/' + _n_(413320, "resume", lambda: resume))))
        _l_(413324)
    elif 'doc' in _n_(413325, "extension", lambda: extension):
        _l_(413336)

        # Read in every resume with .doc or .docx extension in the directory
        _c_(413334, _a_(413327, _n_(413326, "resume_texts", lambda: resume_texts), "append"), _c_(413333, _n_(413328, "nlp", lambda: nlp), _c_(413332, _n_(413329, "extract_text_from_word", lambda: extract_text_from_word), _n_(413330, "PROJECT_DIR", lambda: PROJECT_DIR) + '/CV/' + _n_(413331, "resume", lambda: resume))))
        _l_(413335)
    _c_(413345, _a_(413339, _n_(413338, "resume_names", lambda: resume_names), "append"), _c_(413344, _a_(413343, _c_(413342, _a_(413341, _n_(413340, "resume", lambda: resume), "split"), '_')[0], "capitalize")))
    _l_(413346)