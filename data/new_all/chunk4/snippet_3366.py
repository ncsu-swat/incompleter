# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75237185/typeerror-init-missing-1-required-argument-id-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Cart(_n_(606615, "CartTemplate", lambda: CartTemplate)):
  _l_(606773)

  def __init__(self, items, **properties):
    _l_(606711)

    # Set Form properties and Data Bindings.
    _c_(606619, _a_(606617, _n_(606616, "self", lambda: self), "init_components"), **_n_(606618, "properties", lambda: properties))
    _l_(606620)
    _n_(606621, "self", lambda: self).order = []
    _l_(606622)
    _n_(606623, "self", lambda: self).items_1 = _n_(606624, "items", lambda: items)
    _l_(606625)
    _n_(606626, "self", lambda: self).items_2 = _n_(606627, "items", lambda: items)
    _l_(606628)
    _n_(606629, "self", lambda: self).items_3 = _n_(606630, "items", lambda: items)
    _l_(606631)

  
    if not _a_(606633, _n_(606632, "self", lambda: self), "items_1"):
      _l_(606640)

      _a_(606635, _n_(606634, "self", lambda: self), "empty_cart_panel").visible = True
      _l_(606636)
      _a_(606638, _n_(606637, "self", lambda: self), "column_panel_1").visible = False
      _l_(606639)
    
    _a_(606642, _n_(606641, "self", lambda: self), "repeating_panel_1").items = _a_(606644, _n_(606643, "self", lambda: self), "items_1")
    _l_(606645)
    _a_(606647, _n_(606646, "self", lambda: self), "repeating_panel_2").items = _a_(606649, _n_(606648, "self", lambda: self), "items_2")
    _l_(606650)
    _a_(606652, _n_(606651, "self", lambda: self), "repeating_panel_3").items = _a_(606654, _n_(606653, "self", lambda: self), "items_3")
    _l_(606655)
    
    
    _n_(606656, "self", lambda: self).subtotal_1 = _c_(606662, _n_(606657, "sum", lambda: sum), (_n_(606658, "dairy", lambda: dairy)['price'] * _n_(606659, "item", lambda: item)['quantity'] for item in _a_(606661, _n_(606660, "self", lambda: self), "items_1")))
    _l_(606663)
    
    _n_(606664, "self", lambda: self).subtotal_2 = _c_(606670, _n_(606665, "sum", lambda: sum), (_n_(606666, "fruit", lambda: fruit)['price'] * _n_(606667, "item", lambda: item)['quantity'] for item in _a_(606669, _n_(606668, "self", lambda: self), "items_2")))
    _l_(606671)
    
    _n_(606672, "self", lambda: self).subtotal_3 = _c_(606678, _n_(606673, "sum", lambda: sum), (_n_(606674, "vegetable", lambda: vegetable)['price'] * _n_(606675, "item", lambda: item)['quantity'] for item in _a_(606677, _n_(606676, "self", lambda: self), "items_3")))
    _l_(606679)
    
    _n_(606680, "self", lambda: self).subtotal = _a_(606682, _n_(606681, "self", lambda: self), "subtotal_1") + _a_(606684, _n_(606683, "self", lambda: self), "subtotal_2") + _a_(606686, _n_(606685, "self", lambda: self), "subtotal_3")
    _l_(606687)
    _a_(606689, _n_(606688, "self", lambda: self), "subtotal_label").text = f"AED {_a_(606691, _n_(606690, 'self', lambda: self), 'subtotal'):.02f}"
    _l_(606692)
    
    if _a_(606694, _n_(606693, "self", lambda: self), "subtotal") >= 40:
      _l_(606705)

      _a_(606696, _n_(606695, "self", lambda: self), "shipping_label").text = 'FREE'     
      _l_(606697)     
    else: #add $5 shipping
      _a_(606699, _n_(606698, "self", lambda: self), "shipping_label").text = "$5.00"
      _l_(606700)
      _n_(606701, "self", lambda: self).subtotal = _a_(606703, _n_(606702, "self", lambda: self), "subtotal") + 5
      _l_(606704)
      
    _a_(606707, _n_(606706, "self", lambda: self), "total_label").text = f"${_a_(606709, _n_(606708, 'self', lambda: self), 'subtotal'):.02f}"
    _l_(606710)

  def shop_button_click(self, **event_args):
    _l_(606717)

    """This method is called when the button is clicked"""
    _c_(606715, _a_(606714, _c_(606713, _n_(606712, "get_open_form", lambda: get_open_form)), "title_link_click"))
    _l_(606716)

  def checkout_button_click(self, **event_args):
    _l_(606772)

    """This method is called when the button is clicked"""  
    for i in _a_(606719, _n_(606718, "self", lambda: self), "items"):
      _l_(606741)

      _c_(606725, _a_(606722, _a_(606721, _n_(606720, "self", lambda: self), "order"), "append"), {'name':_n_(606723, "dairy", lambda: dairy)['name'], 'quantity':_n_(606724, "i", lambda: i)['quantity']})
      _l_(606726)
      _c_(606732, _a_(606729, _a_(606728, _n_(606727, "self", lambda: self), "order"), "append"), {'name':_n_(606730, "fruit", lambda: fruit)['name'], 'quantity':_n_(606731, "i", lambda: i)['quantity']})
      _l_(606733)
      _c_(606739, _a_(606736, _a_(606735, _n_(606734, "self", lambda: self), "order"), "append"), {'name':_n_(606737, "vegetable", lambda: vegetable)['name'], 'quantity':_n_(606738, "i", lambda: i)['quantity']})
      _l_(606740)
    try:
      _l_(606751)

      charge = _c_(606747, _a_(606744, _a_(606743, _n_(606742, "stripe", lambda: stripe), "checkout"), "charge"), amount=_a_(606746, _n_(606745, "self", lambda: self), "subtotal")*100,
                                      currency="AED",
                                      shipping_address=True,
                                      title="Fresh Fields")
      _l_(606748)
    except:
      _l_(606750)

      aux = ""
      _l_(606749)
      return aux
    
    _c_(606757, _a_(606754, _a_(606753, _n_(606752, "anvil", lambda: anvil), "server"), "call"), 'charge_user', _n_(606755, "token", lambda: token), _n_(606756, "user", lambda: user)["email"])
    _l_(606758)

    _c_(606760, _n_(606759, "get_open_form", lambda: get_open_form)).cart_items = []
    _l_(606761)
    _c_(606765, _a_(606764, _c_(606763, _n_(606762, "get_open_form", lambda: get_open_form)), "cart_link_click"))
    _l_(606766)
    _c_(606770, _a_(606769, _c_(606768, _n_(606767, "Notification", lambda: Notification), "Your order has been received!"), "show"))
    _l_(606771)