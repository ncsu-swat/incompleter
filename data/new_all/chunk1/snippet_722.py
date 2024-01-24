# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43326698/saving-uploaded-base64-data-gives-typeerror-a-bytes-like-object-is-required-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
app = _c_(391076, _n_(391074, "Flask", lambda: Flask), _n_(391075, "__name__", lambda: __name__))
_l_(391077)
UPLOAD_FOLDER = _a_(391079, _n_(391078, "app", lambda: app), "root_path") + '/images/'
_l_(391080)

@_c_(391083, _a_(391082, _n_(391081, "app", lambda: app), "route"), '/', methods=['GET', 'POST'])
def index():
    _l_(391136)

    if _a_(391085, _n_(391084, "request", lambda: request), "method") == 'POST':
        _l_(391132)

        image_base = _c_(391090, _a_(391087, _n_(391086, "json", lambda: json), "loads"), _a_(391089, _n_(391088, "request", lambda: request), "form")['file'])['output']['image']
        _l_(391091)
        image_base = _n_(391092, "image_base", lambda: image_base)[_c_(391095, _a_(391094, _n_(391093, "image_base", lambda: image_base), "find"), ',')+1:]
        _l_(391096)
        file_data = _c_(391100, _a_(391098, _n_(391097, "io", lambda: io), "StringIO"), _n_(391099, "image_base", lambda: image_base))
        _l_(391101)
        file = _c_(391108, _n_(391102, "FileStorage", lambda: FileStorage), _n_(391103, "file_data", lambda: file_data), filename=_c_(391107, _a_(391105, _n_(391104, "json", lambda: json), "loads"), _n_(391106, "from_form", lambda: from_form))['output']['name'])
        _l_(391109)
        filename = _c_(391113, _n_(391110, "secure_filename", lambda: secure_filename), _a_(391112, _n_(391111, "file", lambda: file), "filename"))
        _l_(391114)
        _c_(391124, _a_(391116, _n_(391115, "file", lambda: file), "save"), _c_(391123, _a_(391119, _a_(391118, _n_(391117, "os", lambda: os), "path"), "join"), _a_(391121, _n_(391120, "app", lambda: app), "config")['UPLOAD_FOLDER'], _n_(391122, "filename", lambda: filename)))
        _l_(391125)
        aux = _c_(391130, _n_(391126, "redirect", lambda: redirect), _c_(391129, _n_(391127, "url_for", lambda: url_for), 'uploaded_file', filename=_n_(391128, "filename", lambda: filename)))
        _l_(391131)
        return aux
    aux = _c_(391134, _n_(391133, "render_template", lambda: render_template), 'index.html', methods=['GET', 'POST'])
    _l_(391135)

    return aux