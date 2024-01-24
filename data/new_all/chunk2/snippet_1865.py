# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47267198/attributeerror-bool-object-has-no-attribute-read-when-calling-requests-post
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
upload_headers = {'Authorization':'Bearer' + ' ' + _n_(468830, "access_token", lambda: access_token), 'X-Backtory-Storage-Id':'48378438**********'}
_l_(468831)
upload_data = {'fileItems[0].fileToUpload': _c_(468833, _n_(468832, "open", lambda: open), 'file.txt', 'rb'), 'fileItems[0].path': r'/path1/', 'fileItems[0].replacing': True}
_l_(468834)
upload_response = _c_(468839, _a_(468836, _n_(468835, "requests", lambda: requests), "post"), "http://storage.backtory.com/files", files=_n_(468837, "upload_data", lambda: upload_data), headers=_n_(468838, "upload_headers", lambda: upload_headers))
_l_(468840)
_c_(468843, _n_(468841, "print", lambda: print), _n_(468842, "upload_r", lambda: upload_r))
_l_(468844)