# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62040934/flask-response-throws-filenotfounderror-even-status-of-response-is-200
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(705548, _a_(705547, _n_(705546, "app", lambda: app), "route"), "/render/<filter_name>", methods=["POST"])
def render(filter_name: _n_(705549, "str", lambda: str)):
    _l_(705629)

    if _a_(705551, _n_(705550, "request", lambda: request), "method") == "POST":
        _l_(705628)

        f = _a_(705553, _n_(705552, "request", lambda: request), "files")["file"]
        _l_(705554)

        tempdir = _c_(705557, _a_(705556, _n_(705555, "tempfile", lambda: tempfile), "mkdtemp"))
        _l_(705558)
        in_dir = _c_(705562, _a_(705560, _n_(705559, "tempfile", lambda: tempfile), "mkdtemp"), prefix="image_", dir=_n_(705561, "tempdir", lambda: tempdir))
        _l_(705563)
        out_dir = _c_(705567, _a_(705565, _n_(705564, "tempfile", lambda: tempfile), "mkdtemp"), prefix="image_", dir=_n_(705566, "tempdir", lambda: tempdir))
        _l_(705568)

        image = _c_(705576, _a_(705570, _n_(705569, "Image", lambda: Image), "open"), _c_(705575, _n_(705571, "BytesIO", lambda: BytesIO), _c_(705574, _a_(705573, _n_(705572, "f", lambda: f), "read"))))
        _l_(705577)
        _c_(705582, _a_(705579, _n_(705578, "image", lambda: image), "save"), _a_(705581, _n_(705580, "in_dir", lambda: in_dir), "name") + "/image.jpg", "JPEG")
        _l_(705583)

        _c_(705590, _n_(705584, "render_mp4", lambda: render_mp4), _a_(705586, _n_(705585, "in_dir", lambda: in_dir), "name"), _a_(705588, _n_(705587, "out_dir", lambda: out_dir), "name"), _n_(705589, "filter_name", lambda: filter_name))
        _l_(705591)

        filename = "image_" + _n_(705592, "filter_name", lambda: filter_name) + ".mp4"
        _l_(705593)
        fout = _c_(705602, _n_(705594, "open", lambda: open), _c_(705601, _a_(705597, _a_(705596, _n_(705595, "os", lambda: os), "path"), "join"), _a_(705599, _n_(705598, "out_dir", lambda: out_dir), "name"), _n_(705600, "filename", lambda: filename)), "rb")
        _l_(705603)

        response = _c_(705608, _n_(705604, "make_response", lambda: make_response), _c_(705607, _a_(705606, _n_(705605, "fout", lambda: fout), "read")))
        _l_(705609)
        _c_(705613, _a_(705612, _a_(705611, _n_(705610, "response", lambda: response), "headers"), "set"), "Content-Type", "video/mp4")
        _l_(705614)
        _c_(705619, _a_(705617, _a_(705616, _n_(705615, "response", lambda: response), "headers"), "set"), "Content-Disposition", "attachment", filename=_n_(705618, "filename", lambda: filename))
        _l_(705620)
        _c_(705624, _a_(705622, _n_(705621, "shutil", lambda: shutil), "rmtree"), _n_(705623, "tempdir", lambda: tempdir))
        _l_(705625)
        aux = _n_(705626, "response", lambda: response)
        _l_(705627)

        return aux