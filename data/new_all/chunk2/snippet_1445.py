# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57537309/typeerror-str-returned-non-string-type-magicmock
# mocks.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
image_mock = _c_(471198, _a_(471196, _n_(471195, "mock", lambda: mock), "MagicMock"), spec=_n_(471197, "File", lambda: File), name='FileMock')
_l_(471199)
_n_(471200, "image_mock", lambda: image_mock).name = 'dummy.jpg'
_l_(471201)

storage_mock = _c_(471205, _a_(471203, _n_(471202, "mock", lambda: mock), "MagicMock"), spec=_n_(471204, "Storage", lambda: Storage), name='StorageMock')
_l_(471206)
_n_(471207, "storage_mock", lambda: storage_mock).url = _c_(471210, _a_(471209, _n_(471208, "mock", lambda: mock), "MagicMock"), name='url')
_l_(471211)
_a_(471213, _n_(471212, "storage_mock", lambda: storage_mock), "url").return_value = '/tmp/dummy.jpg'
_l_(471214)