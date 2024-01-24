# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75934628/typeerror-fastapi-sample-fails-during-loading
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fastapi import FastAPI
    _l_(621321)

except ImportError:
    pass

app = _c_(621323, _n_(621322, "FastAPI", lambda: FastAPI))
_l_(621324)


@_c_(621327, _a_(621326, _n_(621325, "app", lambda: app), "get"), "/")
async def root():
    _l_(621329)

    aux = {"message": "Hello World"}
    _l_(621328)
    return aux