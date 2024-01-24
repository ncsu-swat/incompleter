# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68239345/typeerror-after-converting-python-game-to-executable
# -*- mode: python -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = _c_(428091, _n_(428080, "Analysis", lambda: Analysis), [_c_(428085, _a_(428083, _a_(428082, _n_(428081, "os", lambda: os), "path"), "join"), _n_(428084, "HOMEPATH", lambda: HOMEPATH),'support/_mountzlib.py'), _c_(428090, _a_(428088, _a_(428087, _n_(428086, "os", lambda: os), "path"), "join"), _n_(428089, "HOMEPATH", lambda: HOMEPATH),'support/useUnicode.py'), 'icinga.py'],
             pathex=['/home/user/projects/icinga_python/releases/v2.1'])
_l_(428092)
pyz = _c_(428096, _n_(428093, "PYZ", lambda: PYZ), _a_(428095, _n_(428094, "a", lambda: a), "pure"))
_l_(428097)
exe = _c_(428112, _n_(428098, "EXE", lambda: EXE), _n_(428099, "pyz", lambda: pyz),
          _a_(428101, _n_(428100, "a", lambda: a), "scripts"),
          _a_(428103, _n_(428102, "a", lambda: a), "binaries"),
          _a_(428105, _n_(428104, "a", lambda: a), "zipfiles"),
          _a_(428107, _n_(428106, "a", lambda: a), "datas"),
          name=_c_(428111, _a_(428110, _a_(428109, _n_(428108, "os", lambda: os), "path"), "join"), 'dist', 'myscript'),
          debug=False,
          strip=False,
          upx=True,
          console=1 )
_l_(428113)