# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70862542/typeerror-user-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(617578, "login_required", lambda: login_required)
def payment(request):
    _l_(617715)

    saved_address = _c_(617584, _a_(617581, _a_(617580, _n_(617579, "BillingAddress", lambda: BillingAddress), "objects"), "get_or_create"), user=_a_(617583, _n_(617582, "request", lambda: request), "user"))[0]
    _l_(617585)
    if not _c_(617588, _a_(617587, _n_(617586, "saved_address", lambda: saved_address), "is_fully_filled")):
        _l_(617597)

        _c_(617592, _a_(617590, _n_(617589, "messages", lambda: messages), "info"), _n_(617591, "request", lambda: request),f'Please complete shipping address!')
        _l_(617593)
        aux = _c_(617595, _n_(617594, 'redirect', lambda: redirect), 'checkout')
        _l_(617596)
        return aux
    if not _c_(617602, _a_(617601, _a_(617600, _a_(617599, _n_(617598, 'request', lambda: request), 'user'), 'profile'), 'is_fully_filled')):
        _l_(617611)

        _c_(617606, _a_(617604, _n_(617603, 'messages', lambda: messages), 'info'), _n_(617605, 'request', lambda: request),f'Please complete profile details!')
        _l_(617607)
        aux = _c_(617609, _n_(617608, 'redirect', lambda: redirect), 'profile')
        _l_(617610)
        return aux
    
    store_id = '$$$$$$$$$$$$$$$'
    _l_(617612)
    API_key= '$$$$$$$$$$$$$$$@ssl'
    _l_(617613)
    mypayment = _c_(617617, _n_(617614, 'SSLCSession', lambda: SSLCSession), sslc_is_sandbox=True, sslc_store_id=_n_(617615, 'store_id', lambda: store_id), sslc_store_pass=_n_(617616, 'API_key', lambda: API_key))
    _l_(617618)
    
    
    status_url= _c_(617623, _a_(617620, _n_(617619, 'request', lambda: request), 'build_absolute_uri'), _c_(617622, _n_(617621, 'reverse', lambda: reverse), 'complete'))
    _l_(617624)
    _c_(617631, _a_(617626, _n_(617625, 'mypayment', lambda: mypayment), 'set_urls'), success_url=_n_(617627, 'status_url', lambda: status_url), fail_url=_n_(617628, 'status_url', lambda: status_url), cancel_url=_n_(617629, 'status_url', lambda: status_url), ipn_url=_n_(617630, 'status_url', lambda: status_url))
    _l_(617632)
    
    order_qs=_c_(617638, _a_(617635, _a_(617634, _n_(617633, 'Order', lambda: Order), 'objects'), 'filter'), user=_a_(617637, _n_(617636, 'request', lambda: request), 'user'),ordered=False)
    _l_(617639)
    order_items=_c_(617643, _a_(617642, _a_(617641, _n_(617640, 'order_qs', lambda: order_qs)[0], 'orderitems'), 'all'))
    _l_(617644)
    order_item_count=_c_(617648, _a_(617647, _a_(617646, _n_(617645, 'order_qs', lambda: order_qs)[0], 'orderitems'), 'count'))
    _l_(617649)
    order_total=_c_(617652, _a_(617651, _n_(617650, 'order_qs', lambda: order_qs)[0], 'get_totals'))
    _l_(617653)
    _c_(617661, _a_(617655, _n_(617654, 'mypayment', lambda: mypayment), 'set_product_integration'), total_amount=_c_(617658, _n_(617656, 'Decimal', lambda: Decimal), _n_(617657, 'order_total', lambda: order_total)), currency='BDT', product_category='Mixed', product_name=_n_(617659, 'order_items', lambda: order_items), num_of_item=_n_(617660, 'order_item_count', lambda: order_item_count), shipping_method='Courier', product_profile='None')
    _l_(617662)
    
    current_user=_a_(617664, _n_(617663, 'request', lambda: request), 'user')
    _l_(617665)
    
    _c_(617690, _a_(617667, _n_(617666, 'mypayment', lambda: mypayment), 'set_customer_info'), name=_a_(617670, _a_(617669, _n_(617668, 'current_user', lambda: current_user), 'profile'), 'full_name'), email=_n_(617671, 'current_user', lambda: current_user), address1=_a_(617674, _a_(617673, _n_(617672, 'current_user', lambda: current_user), 'profile'), 'address_1'), address2=_a_(617677, _a_(617676, _n_(617675, 'current_user', lambda: current_user), 'profile'), 'address_1'), city=_a_(617680, _a_(617679, _n_(617678, 'current_user', lambda: current_user), 'profile'), 'city'), postcode=_a_(617683, _a_(617682, _n_(617681, 'current_user', lambda: current_user), 'profile'), 'zipcode'), country=_a_(617686, _a_(617685, _n_(617684, 'current_user', lambda: current_user), 'profile'), 'country'), phone=_a_(617689, _a_(617688, _n_(617687, 'current_user', lambda: current_user), 'profile'), 'phone'))
    _l_(617691)
    
    _c_(617705, _a_(617693, _n_(617692, 'mypayment', lambda: mypayment), 'set_shipping_info'), shipping_to=_a_(617696, _a_(617695, _n_(617694, 'current_user', lambda: current_user), 'profile'), 'full_name'), address=_a_(617698, _n_(617697, 'saved_address', lambda: saved_address), 'address'), city=_a_(617700, _n_(617699, 'saved_address', lambda: saved_address), 'city'), postcode=_a_(617702, _n_(617701, 'saved_address', lambda: saved_address), 'zipcode'), country=_a_(617704, _n_(617703, 'saved_address', lambda: saved_address), 'country'))
    _l_(617706)

    response_data = _c_(617709, _a_(617708, _n_(617707, 'mypayment', lambda: mypayment), 'init_payment'))
    _l_(617710)
    aux = _c_(617713, _n_(617711, 'render', lambda: render), _n_(617712, 'request', lambda: request),'payment/payment.html',context={})
    _l_(617714)
    



    return aux