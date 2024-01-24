# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62484518/i-get-a-type-error-when-posting-data-using-via-rest-it-says-i-may-have-a-writab
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Certificate(_a_(529553, _n_(529552, "models", lambda: models), "Model")):
    _l_(529661)

    certificate_name = _c_(529555, _a_(529554, models, "CharField"), max_length=50)
    _l_(529556)
    template_img = _c_(529558, _a_(529557, models, "ImageField"), blank=True, default='', upload_to='certificate_templates')
    _l_(529559)
    template_url = _c_(529561, _a_(529560, models, "URLField"), blank=True, default='')
    _l_(529562)
    names_file = _c_(529564, _a_(529563, models, "FileField"), blank=True, default='', upload_to='names_files')
    _l_(529565)
    names_csv = _c_(529567, _a_(529566, models, "TextField"), blank=True, default='')
    _l_(529568)
    Y_RATIO = 1.6268
    _l_(529569)

    def get_remote_image(self):
        _l_(529621)

        if _a_(529571, _n_(529570, "self", lambda: self), "template_url") and not _a_(529573, _n_(529572, "self", lambda: self), "template_img"):
            _l_(529620)

            img_result = _c_(529578, _a_(529575, _n_(529574, "requests", lambda: requests), "get"), _a_(529577, _n_(529576, "self", lambda: self), "template_url"))
            _l_(529579)
            img_name = _c_(529585, _a_(529582, _a_(529581, _n_(529580, "os", lambda: os), "path"), "basename"), _a_(529584, _n_(529583, "self", lambda: self), "template_url"))
            _l_(529586)
            with _c_(529594, _n_(529587, "open", lambda: open), _c_(529593, _a_(529590, _a_(529589, _n_(529588, "os", lambda: os), "path"), "join"), _n_(529591, "TEMP_DIR", lambda: TEMP_DIR), _n_(529592, "img_name", lambda: img_name)), 'wb') as img_file:
                _l_(529601)

                _c_(529599, _a_(529596, _n_(529595, "img_file", lambda: img_file), "write"), _a_(529598, _n_(529597, "img_result", lambda: img_result), "content"))
                _l_(529600)
            _c_(529614, _a_(529604, _a_(529603, _n_(529602, "self", lambda: self), "template_img"), "save"), _n_(529605, "img_name", lambda: img_name),
                _c_(529613, _n_(529606, "open", lambda: open), _c_(529612, _a_(529609, _a_(529608, _n_(529607, "os", lambda: os), "path"), "join"), _n_(529610, "TEMP_DIR", lambda: TEMP_DIR), _n_(529611, "img_name", lambda: img_name)), 'rb')
                )
            _l_(529615)
            _c_(529618, _a_(529617, _n_(529616, "self", lambda: self), "save"))
            _l_(529619)


    def clean(self):
        _l_(529638)

        if not _a_(529623, _n_(529622, "self", lambda: self), "template_img") and not _a_(529625, _n_(529624, "self", lambda: self), "template_url"):
            _l_(529629)

            raise _c_(529627, _n_(529626, "ValidationError", lambda: ValidationError), {'template_img': 'Either one of template_img or template_url should have a value.'})
            _l_(529628)
        if not _a_(529631, _n_(529630, "self", lambda: self), "names_csv") and not _a_(529633, _n_(529632, "self", lambda: self), "names_file"):
            _l_(529637)

            raise _c_(529635, _n_(529634, "ValidationError", lambda: ValidationError), {'names_csv': 'Either one of names_csv or names_file should have a value.'})
            _l_(529636)


    def save(self):
        _l_(529660)

        if _a_(529640, _n_(529639, "self", lambda: self), "template_url") and not _a_(529642, _n_(529641, "self", lambda: self), "template_img"):
            _l_(529659)

            _c_(529645, _a_(529644, _n_(529643, "self", lambda: self), "get_remote_image"))
            _l_(529646)
            _c_(529651, _a_(529650, _n_(529647, "super", lambda: super)(_n_(529648, "Certificate", lambda: Certificate), _n_(529649, "self", lambda: self)), "save"))
            _l_(529652)
        else:
            _c_(529657, _a_(529656, _n_(529653, "super", lambda: super)(_n_(529654, "Certificate", lambda: Certificate), _n_(529655, "self", lambda: self)), "save"))
            _l_(529658)