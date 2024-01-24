# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70445787/jupyternotebook-filenotfounderror-winerror-3-the-system-cannot-find-the-path
#SETUP PATHS
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
POS_PATH = _c_(398017, _a_(398016, _a_(398015, _n_(398014, "os", lambda: os), "path"), "join"), 'data', 'positive')
_l_(398018)
NEG_PATH = _c_(398022, _a_(398021, _a_(398020, _n_(398019, "os", lambda: os), "path"), "join"), 'data', 'negative')
_l_(398023)
ANC_PATH = _c_(398027, _a_(398026, _a_(398025, _n_(398024, "os", lambda: os), "path"), "join"), 'data','anchor')
_l_(398028)


#MAKE DIRECTORIES
_c_(398032, _a_(398030, _n_(398029, "os", lambda: os), "makedirs"), _n_(398031, "POS_PATH", lambda: POS_PATH))
_l_(398033)
_c_(398037, _a_(398035, _n_(398034, "os", lambda: os), "makedirs"), _n_(398036, "NEG_PATH", lambda: NEG_PATH))
_l_(398038)
_c_(398042, _a_(398040, _n_(398039, "os", lambda: os), "makedirs"), _n_(398041, "ANC_PATH", lambda: ANC_PATH))
_l_(398043)