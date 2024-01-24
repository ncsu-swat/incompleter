# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75141095/streamlit-spacy-causing-attributeerror-pathdistribution-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import streamlit as st
    _l_(599945)

except ImportError:
    pass
try:
    import fitz
    _l_(599947)

except ImportError:
    pass

def load_file(file):
    _l_(599973)

    doc = _c_(599953, _a_(599949, _n_(599948, "fitz", lambda: fitz), "open"), stream=_c_(599952, _a_(599951, _n_(599950, "uploaded_file", lambda: uploaded_file), "read")), filetype="pdf")    
    _l_(599954)    
    text = []
    _l_(599955)
    with _n_(599956, "doc", lambda: doc):
        _l_(599970)

        for page in _n_(599957, "doc", lambda: doc):
            _l_(599965)

            _c_(599963, _a_(599959, _n_(599958, "text", lambda: text), "append"), _c_(599962, _a_(599961, _n_(599960, "page", lambda: page), "get_text")))
            _l_(599964)
        text = _c_(599968, _a_(599966, "\n", "join"), _n_(599967, "text", lambda: text))
        _l_(599969)
    aux = _n_(599971, "text", lambda: text)
    _l_(599972)
    return aux

#####################################################################   

_c_(599976, _a_(599975, _n_(599974, "st", lambda: st), "title"), "Test app")
_l_(599977)

col1, col2 = _c_(599980, _a_(599979, _n_(599978, "st", lambda: st), "columns"), [1,1], gap='small')
_l_(599981)

with _n_(599982, "col1", lambda: col1):
    _l_(599991)

    with _c_(599985, _a_(599984, _n_(599983, "st", lambda: st), "expander"), "Description -", expanded=True):
        _l_(599990)

        _c_(599988, _a_(599987, _n_(599986, "st", lambda: st), "write"), "This is the description of the app.")
        _l_(599989)
with _n_(599992, "col2", lambda: col2):
    _l_(600005)

    with _c_(599995, _a_(599994, _n_(599993, "st", lambda: st), "form"), key="my_form"):
        _l_(600004)

        uploaded_file = _c_(599998, _a_(599997, _n_(599996, "st", lambda: st), "file_uploader"), "Upload",type='pdf', accept_multiple_files=False, label_visibility="collapsed")
        _l_(599999)
        submit_button = _c_(600002, _a_(600001, _n_(600000, "st", lambda: st), "form_submit_button"), label="Process")        
        _l_(600003)        
col1, col2 = _c_(600008, _a_(600007, _n_(600006, "st", lambda: st), "columns"), [1,3], gap='small')
_l_(600009)

with _n_(600010, "col1", lambda: col1):
    _l_(600015)

    _c_(600013, _a_(600012, _n_(600011, "st", lambda: st), "header"), "Metrics")
    _l_(600014)

with _n_(600016, "col2", lambda: col2):
    _l_(600032)

    _c_(600019, _a_(600018, _n_(600017, "st", lambda: st), "header"), "Text")
    _l_(600020)
    
    if _n_(600021, "uploaded_file", lambda: uploaded_file) is not None:
        _l_(600031)

        text = _c_(600024, _n_(600022, "load_file", lambda: load_file), _n_(600023, "uploaded_file", lambda: uploaded_file))
        _l_(600025)
        _c_(600029, _a_(600027, _n_(600026, "st", lambda: st), "text_area"), _n_(600028, "text", lambda: text))
        _l_(600030)