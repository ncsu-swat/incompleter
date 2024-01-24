# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49222033/raise-typeerrorrepro-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
      from flask import Flask, jsonify, request
      _l_(599441)

except ImportError:
      pass
try:
      from server.model.product import Product, ProductSchema
      _l_(599443)

except ImportError:
      pass

app = _c_(599446, _n_(599444, "Flask", lambda: Flask), _n_(599445, "__name__", lambda: __name__))
_l_(599447)

products=[_c_(599449, _n_(599448, "Product", lambda: Product), 'a','b','c','d')]
_l_(599450)


@_c_(599453, _a_(599452, _n_(599451, "app", lambda: app), "route"), "/")
def hello_world():
      _l_(599455)

      aux = "Hello, World!"
      _l_(599454)
      return aux

@_c_(599458, _a_(599457, _n_(599456, "app", lambda: app), "route"), "/products", methods=['POST'])
def add_product():
      _l_(599474)

      product = _c_(599465, _a_(599461, _c_(599460, _n_(599459, "ProductSchema", lambda: ProductSchema)), "load"), _c_(599464, _a_(599463, _n_(599462, "request", lambda: request), "get_json")))
      _l_(599466)
      _c_(599471, _a_(599468, _n_(599467, "products", lambda: products), "append"), _a_(599470, _n_(599469, "product", lambda: product), "data"))
      _l_(599472)
      aux = "", 204
      _l_(599473)
      return aux

@_c_(599477, _a_(599476, _n_(599475, "app", lambda: app), "route"), "/products")
def get_products():
      _l_(599485)

      schema = _c_(599479, _n_(599478, "ProductSchema", lambda: ProductSchema), many=True)
      _l_(599480)
      aux = _c_(599483, _n_(599481, "jsonify", lambda: jsonify), _n_(599482, "products", lambda: products))
      _l_(599484)
      return aux

if _n_(599486, "__name__", lambda: __name__) == "__main__":
      _l_(599491)

      _c_(599489, _a_(599488, _n_(599487, "app", lambda: app), "run"))
      _l_(599490)