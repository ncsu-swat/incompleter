# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50950043/typeerror-nonetype-object-is-not-subscriptable-odoo-11-custom-report
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from odoo import api, fields, models
    _l_(578774)

except ImportError:
    pass
try:
    import logging
    _l_(578776)

except ImportError:
    pass

_logger = _c_(578780, _a_(578778, _n_(578777, "logging", lambda: logging), "getLogger"), _n_(578779, "__name__", lambda: __name__))
_l_(578781)
class SockValuationReport(_a_(578783, _n_(578782, "models", lambda: models), "TransientModel")):
    _l_(578851)

    _name = 'report.stock_valuation_flora'
    _l_(578784)
    _description = 'Sotck valuation report for floravert'
    _l_(578785)

    @_a_(578787, _n_(578786, "api", lambda: api), "multi")
    def render_report(self):
        _l_(578850)

        products = _c_(578791, _a_(578790, _a_(578789, _n_(578788, "self", lambda: self), "env")['product.template'], "search"), [])
        _l_(578792)
        data = {}
        _l_(578793)
        categ_dict = {}
        _l_(578794)
        for product in _n_(578795, "products", lambda: products):
            _l_(578829)

            valuation = 0
            _l_(578796)
            if(_a_(578799, _a_(578798, _n_(578797, "product", lambda: product), "categ_id"), "name") in _n_(578800, "categ_dict", lambda: categ_dict)):
                _l_(578828)

                valuation = _a_(578802, _n_(578801, "product", lambda: product), "standard_price") * _a_(578804, _n_(578803, "product", lambda: product), "qty_available")
                _l_(578805)
                _n_(578806, "categ_dict", lambda: categ_dict)[_a_(578809, _a_(578808, _n_(578807, "product", lambda: product), "categ_id"), "name")]['valuation'] = _n_(578810, "categ_dict", lambda: categ_dict)[_a_(578813, _a_(578812, _n_(578811, "product", lambda: product), "categ_id"), "name")]['valuation'] + _n_(578814, "valuation", lambda: valuation)
                _l_(578815)
            else:
                _n_(578816, "categ_dict", lambda: categ_dict)[_a_(578819, _a_(578818, _n_(578817, "product", lambda: product), "categ_id"), "name")] = {'categ_name':_a_(578822, _a_(578821, _n_(578820, "product", lambda: product), "categ_id"), "name"), 'valuation':_a_(578824, _n_(578823, "product", lambda: product), "standard_price") * _a_(578826, _n_(578825, "product", lambda: product), "qty_available")}
                _l_(578827)
        _n_(578830, "data", lambda: data)['products'] = _n_(578831, "products", lambda: products)
        _l_(578832)
        _n_(578833, "data", lambda: data)['categ_value']= _n_(578834, "categ_dict", lambda: categ_dict)
        _l_(578835)
        _c_(578839, _a_(578837, _n_(578836, "_logger", lambda: _logger), "info"), _n_(578838, "data", lambda: data))
        _l_(578840)
        aux = _c_(578848, _a_(578845, _c_(578844, _a_(578843, _a_(578842, _n_(578841, "self", lambda: self), "env"), "ref"), 'stock_printer.report_stock_product_valuation'), "report_action"), _n_(578846, "self", lambda: self),data=_n_(578847, "data", lambda: data))
        _l_(578849)
        return aux