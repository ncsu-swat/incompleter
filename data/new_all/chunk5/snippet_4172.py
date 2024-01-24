# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62040934/flask-response-throws-filenotfounderror-even-status-of-response-is-200
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(697520, _a_(697519, _n_(697518, "app", lambda: app), "route"), "/render/<filter_name>", methods=["POST"])
def render(filter_name: _n_(697521, "str", lambda: str)):
    _l_(697609)

    if _a_(697523, _n_(697522, "request", lambda: request), "method") == "POST":
        _l_(697608)

        f = _a_(697525, _n_(697524, "request", lambda: request), "files")["file"]
        _l_(697526)

        with _c_(697528, _n_(697527, "TemporaryDirectory", lambda: TemporaryDirectory)) as tempdir:
            _l_(697607)

            in_dir = _c_(697531, _n_(697529, "TemporaryDirectory", lambda: TemporaryDirectory), dir=_n_(697530, "tempdir", lambda: tempdir))
            _l_(697532)
            out_dir = _c_(697535, _n_(697533, "TemporaryDirectory", lambda: TemporaryDirectory), dir=_n_(697534, "tempdir", lambda: tempdir))
            _l_(697536)

            image = _c_(697544, _a_(697538, _n_(697537, "Image", lambda: Image), "open"), _c_(697543, _n_(697539, "BytesIO", lambda: BytesIO), _c_(697542, _a_(697541, _n_(697540, "f", lambda: f), "read"))))
            _l_(697545)

            _c_(697550, _a_(697547, _n_(697546, "image", lambda: image), "save"), _a_(697549, _n_(697548, "in_dir", lambda: in_dir), "name") + "/image.jpg", "JPEG")
            _l_(697551)

            _c_(697558, _n_(697552, "render_mp4", lambda: render_mp4), _a_(697554, _n_(697553, "in_dir", lambda: in_dir), "name"), _a_(697556, _n_(697555, "out_dir", lambda: out_dir), "name"), _n_(697557, "filter_name", lambda: filter_name))
            _l_(697559)


            filename = "image_" + _n_(697560, "filter_name", lambda: filter_name) + ".mp4"
            _l_(697561)

            _c_(697564, _n_(697562, "print", lambda: print), _n_(697563, "filename", lambda: filename))
            _l_(697565)

            fout = _c_(697574, _n_(697566, "open", lambda: open), _c_(697573, _a_(697569, _a_(697568, _n_(697567, "os", lambda: os), "path"), "join"), _a_(697571, _n_(697570, "out_dir", lambda: out_dir), "name"), _n_(697572, "filename", lambda: filename)), "rb")
            _l_(697575)
            _c_(697577, _n_(697576, "print", lambda: print), 'a')
            _l_(697578)
            response = _c_(697583, _n_(697579, "make_response", lambda: make_response), _c_(697582, _a_(697581, _n_(697580, "fout", lambda: fout), "read")))
            _l_(697584)
            _c_(697586, _n_(697585, "print", lambda: print), 'b')
            _l_(697587)
            _c_(697591, _a_(697590, _a_(697589, _n_(697588, "response", lambda: response), "headers"), "set"), "Content-Type", "video/mp4")
            _l_(697592)
            _c_(697594, _n_(697593, "print", lambda: print), 'c')
            _l_(697595)
            _c_(697600, _a_(697598, _a_(697597, _n_(697596, "response", lambda: response), "headers"), "set"), "Content-Disposition", "attachment", filename=_n_(697599, "filename", lambda: filename))
            _l_(697601)
            _c_(697603, _n_(697602, "print", lambda: print), 'd')
            _l_(697604)
            aux = _n_(697605, "response", lambda: response)
            _l_(697606)
            return aux