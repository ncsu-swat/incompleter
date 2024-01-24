# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43679070/typeerror-not-all-arguments-converted-during-string-formatting-during-uploadi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pymysql as psl
    _l_(398057)

except ImportError:
    pass
con6s = _c_(398060, _a_(398059, _n_(398058, "psl", lambda: psl), "connect"), host='myhost',database='mydatabase',user='usr',passwd='12345')
_l_(398061)
c6s = _c_(398064, _a_(398063, _n_(398062, "con6s", lambda: con6s), "cursor"))
_l_(398065)
_c_(398081, _a_(398067, _n_(398066, "c6s", lambda: c6s), "execute"), "INSERT INTO %s (stmp,dat,tm,tc,mc,sd,rp,st,stf,stt) VALUES(?,?,?,?,?,?,?,?,?,?)" % _c_(398070, _n_(398068, "str", lambda: str), _n_(398069, "db", lambda: db)), (_n_(398071, "stmp", lambda: stmp),_n_(398072, "dat", lambda: dat),_n_(398073, "tm", lambda: tm),_n_(398074, "tc", lambda: tc),_n_(398075, "mc", lambda: mc),_n_(398076, "sd", lambda: sd),_n_(398077, "rp", lambda: rp),_n_(398078, "st", lambda: st),_n_(398079, "stf", lambda: stf),_n_(398080, "stt", lambda: stt)))
_l_(398082)
_c_(398085, _a_(398084, _n_(398083, "con6s", lambda: con6s), "commit"))
_l_(398086)
_c_(398089, _a_(398088, _n_(398087, "con6s", lambda: con6s), "close"))
_l_(398090)