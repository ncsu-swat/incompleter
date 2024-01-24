# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73524142/typeerror-an-integer-is-required-got-type-str-in-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(358915, _a_(358914, _n_(358913, "client", lambda: client), "command"), aliases=['bal'])
async def balance(ctx):
  _l_(358952)


  with _c_(358917, _n_(358916, "open", lambda: open), "balance.json", "r") as bal:
    _l_(358951)

    
    user = _a_(358919, _n_(358918, "ctx", lambda: ctx), "author")
    _l_(358920)
    users = await _c_(358922, _n_(358921, "get_balance_data", lambda: get_balance_data))#line-45
    _l_(358923)#line-45
    balance = _n_(358924, "users", lambda: users)[_c_(358928, _n_(358925, "str", lambda: str), _a_(358927, _n_(358926, "user", lambda: user), "id"))]["balance"] = 0
    _l_(358929)
    
    embedbalance = _c_(358939, _a_(358931, _n_(358930, "discord", lambda: discord), "Embed"), titles=f"{_a_(358934, _a_(358933, _n_(358932, 'ctx', lambda: ctx), 'author'), 'name')}'s balance", color=_c_(358938, _a_(358937, _a_(358936, _n_(358935, "discord", lambda: discord), "Color"), "blue")))
    _l_(358940)
    _c_(358944, _a_(358942, _n_(358941, "embedbalance", lambda: embedbalance), "add_field"), name="balance", value=_n_(358943, "balance", lambda: balance))
    _l_(358945)
    await _c_(358949, _a_(358947, _n_(358946, "ctx", lambda: ctx), "send"), embed=_n_(358948, "embedbalance", lambda: embedbalance))
    _l_(358950)
async def get_balance_data():
  _l_(358971)

  with _c_(358954, _n_(358953, "open", lambda: open), "balance.json", "w") as balance:
    _l_(358968)

    users = _c_(358960, _a_(358956, _n_(358955, "json", lambda: json), "loads"), _c_(358959, _a_(358958, _n_(358957, "balance", lambda: balance), "read")))
    _l_(358961)
    _c_(358966, _a_(358963, _n_(358962, "json", lambda: json), "dump"), _n_(358964, "users", lambda: users), _n_(358965, "balance", lambda: balance))
    _l_(358967)
  aux = _n_(358969, "users", lambda: users)
  _l_(358970)

  return aux

_c_(358975, _a_(358973, _n_(358972, "client", lambda: client), "run"), _n_(358974, "token", lambda: token))
_l_(358976)