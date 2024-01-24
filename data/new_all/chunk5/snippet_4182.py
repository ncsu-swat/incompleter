# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61943976/how-to-pass-element-tree-to-other-function-typeerror-elementtree-object-is-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TestXMl(_a_(653866, _n_(653865, "http", lambda: http), "Controller")):
    _l_(653897)

    @_c_(653868, _a_(653867, http, "route"), '/xml/download/report', type='http', auth="user")
    @serialize_exception
    def sale_xml_download(self, model, id, filename=None, **kw):
        _l_(653896)

        filename = 'Test%s.xml'%('Test')
        _l_(653869)
        records= _c_(653874, _a_(653873, _a_(653872, _a_(653871, _n_(653870, "http", lambda: http), "request"), "env")['sale.order'], "search"), [('some_attribute', '=', True)])
        _l_(653875)
        if _n_(653876, "records", lambda: records):
            _l_(653884)

            xml_record = _c_(653881, _a_(653880, _a_(653879, _a_(653878, _n_(653877, "http", lambda: http), "request"), "env")['sale.order'], "_xml_download"))
            _l_(653882)
        else:
            xml_record = 'Test'
            _l_(653883)
        filename = 'Test%s.xml'%('Test')
        _l_(653885)

        headers = [
                ('Content-Type', 'application/xml'),
                ('Content-Disposition', _c_(653888, _n_(653886, "content_disposition", lambda: content_disposition), _n_(653887, "filename", lambda: filename))),
                ('charset', 'utf-8'),
            ]
        _l_(653889)
        aux = _c_(653894, _a_(653891, _n_(653890, "request", lambda: request), "make_response"), _n_(653892, "xml_record", lambda: xml_record), headers=_n_(653893, "headers", lambda: headers), cookies=None)
        _l_(653895)
        return aux