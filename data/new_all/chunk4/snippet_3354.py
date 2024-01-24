# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75440754/typeerror-expected-str-bytes-or-os-pathlike-object-not-nonetype-after-using
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from gpt_index import GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, download_loader
    _l_(621166)

except ImportError:
    pass
try:
    from langchain import OpenAI
    _l_(621168)

except ImportError:
    pass
try:
    import logging
    _l_(621170)

except ImportError:
    pass
try:
    import sys
    _l_(621172)

except ImportError:
    pass
try:
    import os
    _l_(621174)

except ImportError:
    pass
try:
    import streamlit as st
    _l_(621176)

except ImportError:
    pass

_a_(621178, _n_(621177, "os", lambda: os), "environ")['OPENAI_API_KEY'] = "I am deleting my api key from this post"
_l_(621179)



fileup = _c_(621182, _a_(621181, _n_(621180, "st", lambda: st), "file_uploader"), label=" ")
_l_(621183)


SimpleDirectoryReader = _c_(621185, _n_(621184, "download_loader", lambda: download_loader), "SimpleDirectoryReader")
_l_(621186)
loader = _c_(621189, _n_(621187, "SimpleDirectoryReader", lambda: SimpleDirectoryReader), _n_(621188, "fileup", lambda: fileup))
_l_(621190)
documents = _c_(621193, _a_(621192, _n_(621191, "loader", lambda: loader), "load_data"))
_l_(621194)
index = _c_(621197, _n_(621195, "GPTSimpleVectorIndex", lambda: GPTSimpleVectorIndex), _n_(621196, "documents", lambda: documents))
_l_(621198)
_c_(621201, _a_(621200, _n_(621199, "index", lambda: index), "save_to_disk"), 'index.json')
_l_(621202)
question = _c_(621205, _a_(621204, _n_(621203, "st", lambda: st), "text_input"), "What do you want me to do with the file uploaded?")
_l_(621206)
response = _c_(621210, _a_(621208, _n_(621207, "index", lambda: index), "query"), _n_(621209, "question", lambda: question))
_l_(621211)
_c_(621215, _a_(621213, _n_(621212, "st", lambda: st), "write"), _n_(621214, "response", lambda: response))
_l_(621216)