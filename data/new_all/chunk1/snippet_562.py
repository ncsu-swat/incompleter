# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52898498/attributeerror-when-using-beautifulsoup
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import requests
  _l_(399907)

except ImportError:
  pass
try:
  from bs4 import BeautifulSoup
  _l_(399909)

except ImportError:
  pass

url = _c_(399912, _a_(399911, _n_(399910, "requests", lambda: requests), "get"), 'https://www.perfectimprints.com/custom-promos/20492/Beach-Balls.html')
_l_(399913)
source = _c_(399917, _n_(399914, "BeautifulSoup", lambda: BeautifulSoup), _a_(399916, _n_(399915, "url", lambda: url), "text"), 'html.parser')
_l_(399918)

product_feed = _c_(399921, _a_(399920, _n_(399919, "source", lambda: source), "find"), 'div', id_="pageBody")
_l_(399922)

products = _c_(399925, _a_(399924, _n_(399923, "product_feed", lambda: product_feed), "find_all"), 'div', class_="product_wrapper")
_l_(399926)

single_product = _n_(399927, "products", lambda: products)[0]
_l_(399928)

product_name = _c_(399931, _a_(399930, _n_(399929, "single_product", lambda: single_product), "find"), 'div', class_="product_name")
_l_(399932)
product_name = _a_(399935, _a_(399934, _n_(399933, "product_name", lambda: product_name), "a"), "text")
_l_(399936)

sku = _c_(399939, _a_(399938, _n_(399937, "single_product", lambda: single_product), "find"), 'div', class_="product_sku")
_l_(399940)
sku = _a_(399942, _n_(399941, "sku", lambda: sku), "text")
_l_(399943)

def get_product_details(product):
  _l_(399958)

  product_name = _a_(399948, _a_(399947, _c_(399946, _a_(399945, _n_(399944, "product", lambda: product), "find"), 'div', class_="product_name"), "a"), "text")
  _l_(399949)
  sku = _a_(399953, _c_(399952, _a_(399951, _n_(399950, "single_product", lambda: single_product), "find"), 'div', class_="product_sku"), "text")
  _l_(399954)
  aux = {
    "product_name": _n_(399955, "product_name", lambda: product_name),
    "sku": _n_(399956, "sku", lambda: sku)
  }
  _l_(399957)
  return aux

all_products = [_c_(399961, _n_(399959, "get_product_details", lambda: get_product_details), _n_(399960, "product", lambda: product)) for product in _n_(399962, "products", lambda: products)]
_l_(399963)
_c_(399966, _n_(399964, "print", lambda: print), _n_(399965, "all_products", lambda: all_products))
_l_(399967)