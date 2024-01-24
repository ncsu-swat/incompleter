# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(424849)

except ImportError:
    pass
try:
    from django.urls import path, include, re_path
    _l_(424851)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(424853)

except ImportError:
    pass
try:
    from django.conf.urls.static import static
    _l_(424855)

except ImportError:
    pass
try:
    from products import views
    _l_(424857)

except ImportError:
    pass
# from products.views import ProductListView, ProductDetailView

urlpatterns = [
    _c_(424862, _n_(424858, "path", lambda: path), 'admin/', _a_(424861, _a_(424860, _n_(424859, "admin", lambda: admin), "site"), "urls")),
    _c_(424866, _n_(424863, "path", lambda: path), '', _a_(424865, _n_(424864, "views", lambda: views), "home"), name='home'),
    _c_(424870, _n_(424867, "path", lambda: path), 'accounts/', _c_(424869, _n_(424868, "include", lambda: include), 'accounts.urls')),
    # path('products/', ProductListView.as_view()),
    _c_(424874, _n_(424871, "path", lambda: path), 'products/', _c_(424873, _n_(424872, "include", lambda: include), 'products.urls')),
    _c_(424878, _n_(424875, "path", lambda: path), 'auth/', _c_(424877, _n_(424876, "include", lambda: include), 'social_django.urls', namespace='social')),  # social django url for oauth etc
    _c_(424882, _n_(424879, "path", lambda: path), 'about/', _a_(424881, _n_(424880, "views", lambda: views), "about"), name='about'),
    _c_(424886, _n_(424883, "path", lambda: path), 'contact/', _a_(424885, _n_(424884, "views", lambda: views), "contact"), name='contact'),
    _c_(424890, _n_(424887, "path", lambda: path), 'ecom_home', _a_(424889, _n_(424888, "views", lambda: views), "ecom_home"), name='ecom_home'),
    _c_(424894, _n_(424891, "path", lambda: path), 'messages/', _c_(424893, _n_(424892, "include", lambda: include), 'qkchat.urls')),


] + _c_(424900, _n_(424895, "static", lambda: static), _a_(424897, _n_(424896, "settings", lambda: settings), "MEDIA_URL"), document_root=_a_(424899, _n_(424898, "settings", lambda: settings), "MEDIA_ROOT"))
_l_(424901)