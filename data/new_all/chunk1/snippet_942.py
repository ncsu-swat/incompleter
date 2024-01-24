# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72198110/typeerror-cannot-pickle-thread-lock-object-while-using-pool-map-over-a-metho
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def return_brands_of_product(self,product):
        _l_(400407)

        if _n_(400388, "product", lambda: product)['_source']['brand_id'] != "" and _n_(400389, "product", lambda: product)['_source']['brand_id'] not in _a_(400391, _n_(400390, "self", lambda: self), "brands_ids"):
                _l_(400406)

                _c_(400398, _a_(400394, _a_(400393, _n_(400392, "self", lambda: self), "brands"), "append"), {"brand_id":_n_(400395, "product", lambda: product)['_source']['brand_id'],"name":_n_(400396, "product", lambda: product)['_source']['brand'][0]['name']
                                    ,"en_name":_n_(400397, "product", lambda: product)['_source']['brand'][0]['en_name']})
                _l_(400399)
                _c_(400404, _a_(400402, _a_(400401, _n_(400400, "self", lambda: self), "brands_ids"), "append"), _n_(400403, "product", lambda: product)['_source']['brand_id'])
                _l_(400405)

instance = _c_(400410, _n_(400408, "GenerateBrandsFromCategories", lambda: GenerateBrandsFromCategories), _n_(400409, "cat", lambda: cat)['_id'])
_l_(400411)
products = _c_(400414, _a_(400413, _n_(400412, "instance", lambda: instance), "return_products_by_cat_id"))
_l_(400415)
_c_(400421, _a_(400417, _n_(400416, "pool", lambda: pool), "map"), _a_(400419, _n_(400418, "instance", lambda: instance), "return_brands_of_product"), _n_(400420, "products", lambda: products))
_l_(400422)