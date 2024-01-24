# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65569574/beautifulsoup-initialization-type-error-trouble-troubleshooting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(550338)

except ImportError:
    pass
try:
    from PandasBasketball.stats import player_stats
    _l_(550340)

except ImportError:
    pass

dfs = [_c_(550346, _n_(550341, "player_stats", lambda: player_stats), _c_(550345, _a_(550343, _n_(550342, "requests", lambda: requests), "get"), _n_(550344, "url", lambda: url)), "per_minute") for url in _n_(550347, "full_player_urls", lambda: full_player_urls)[600:]]
_l_(550348)
all_stats = _c_(550352, _a_(550350, _n_(550349, "pd", lambda: pd), "concat"), _n_(550351, "dfs", lambda: dfs))
_l_(550353)
_n_(550354, "all_stats", lambda: all_stats)[::500]
_l_(550355)