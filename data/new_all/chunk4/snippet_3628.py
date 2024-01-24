# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71058823/typeerror-unsupported-operand-types-for-set-and-set-returning-multiple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fastapi import FastAPI
    _l_(622106)

except ImportError:
    pass
try:
    from riplir import generate_ad
    _l_(622108)

except ImportError:
    pass


app = _c_(622110, _n_(622109, "FastAPI", lambda: FastAPI))
_l_(622111)


@_c_(622114, _a_(622113, _n_(622112, "app", lambda: app), "get"), "/generate_snippet")
async def creative_ad_api(product_type: _n_(622115, "str", lambda: str), product_name: _n_(622116, "str", lambda: str) , platform: _n_(622117, "str", lambda: str), audience: _n_(622118, "str", lambda: str)):
    _l_(622128)

    snippet = _c_(622124, _n_(622119, "generate_ad", lambda: generate_ad), {_n_(622120, "product_type", lambda: product_type)} + {_n_(622121, "product_name", lambda: product_name)} + {_n_(622122, "platform", lambda: platform)} + {_n_(622123, "audience", lambda: audience)})
    _l_(622125)
    aux = {
        "message": _n_(622126, "snippet", lambda: snippet),
        }
    _l_(622127)
    
    return aux

# uvicorn riplir_api:app --reload