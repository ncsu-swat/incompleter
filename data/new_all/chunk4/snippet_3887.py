# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65946763/attributeerror-str-object-has-no-attribute-get-in-discord-bot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(628933, _a_(628932, _n_(628931, "bot", lambda: bot), "command"))
async def bestPct(ctx, firstName=None, lastName=None, server=None, region=None):
    _l_(628958)

    if _c_(628939, _n_(628934, "all", lambda: all), [_n_(628935, "firstName", lambda: firstName), _n_(628936, "lastName", lambda: lastName), _n_(628937, "server", lambda: server), _n_(628938, "region", lambda: region)]):
        _l_(628951)

        message = _c_(628948, _a_(628941, _n_(628940, "fflogs_request", lambda: fflogs_request), "best_percentile_of"), _c_(628945, _a_(628942, "{} {}", "format"), _n_(628943, "firstName", lambda: firstName), _n_(628944, "lastName", lambda: lastName)), _n_(628946, "server", lambda: server), _n_(628947, "region", lambda: region))
        _l_(628949)
    else:
        message = """Usage: !bestPct <firstName> <lastName> <server> <region>"""
        _l_(628950)
    await _c_(628956, _a_(628954, _a_(628953, _n_(628952, "ctx", lambda: ctx), "channel"), "send"), _n_(628955, "message", lambda: message))
    _l_(628957)