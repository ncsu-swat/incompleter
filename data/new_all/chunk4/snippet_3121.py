# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43557978/getting-error-as-typeerror-at-add-follow-1-init-takes-1-positional-argu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""stratinum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
try:
    from django.conf.urls import url, include
    _l_(606272)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(606274)

except ImportError:
    pass
try:
    from imagec import views as imagec_views
    _l_(606276)

except ImportError:
    pass
try:
    from contact import views as contact_views
    _l_(606278)

except ImportError:
    pass
try:
    from django.conf.urls.static import static
    _l_(606280)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(606282)

except ImportError:
    pass
try:
    from django.core.urlresolvers import reverse
    _l_(606284)

except ImportError:
    pass


_c_(606287, _a_(606286, _n_(606285, "admin", lambda: admin), "autodiscover"))
_l_(606288)

urlpatterns = [
    _c_(606293, _n_(606289, "url", lambda: url), r'^admin/', _a_(606292, _a_(606291, _n_(606290, "admin", lambda: admin), "site"), "urls")),
    _c_(606297, _n_(606294, "url", lambda: url), r'^$', _a_(606296, _n_(606295, "imagec_views", lambda: imagec_views), "home"), name='home'),
    _c_(606301, _n_(606298, "url", lambda: url), r'^about/$', _a_(606300, _n_(606299, "imagec_views", lambda: imagec_views), "about"), name='about'),
    _c_(606305, _n_(606302, "url", lambda: url), r'^detail/$', _a_(606304, _n_(606303, "imagec_views", lambda: imagec_views), "detail"), name='detail'),
    _c_(606309, _n_(606306, "url", lambda: url), r'^profile/$', _a_(606308, _n_(606307, "imagec_views", lambda: imagec_views), "userProfile"), name='profile'),
    _c_(606313, _n_(606310, "url", lambda: url), r'^create_form/$', _a_(606312, _n_(606311, "imagec_views", lambda: imagec_views), "create_form"), name='create_form'),
    _c_(606317, _n_(606314, "url", lambda: url), r'^contact/$', _a_(606316, _n_(606315, "contact_views", lambda: contact_views), "contact"), name='contact'),
    _c_(606321, _n_(606318, "url", lambda: url), r'^userProfile/$', _a_(606320, _n_(606319, "contact_views", lambda: contact_views), "contact"), name='userProfile'),
    _c_(606325, _n_(606322, "url", lambda: url), r'^accounts/', _c_(606324, _n_(606323, "include", lambda: include), 'allauth.urls')),
    _c_(606329, _n_(606326, "url", lambda: url), '', _c_(606328, _n_(606327, "include", lambda: include), 'social.apps.django_app.urls', namespace='social')),
    _c_(606333, _n_(606330, "url", lambda: url), '', _c_(606332, _n_(606331, "include", lambda: include), 'django.contrib.auth.urls', namespace='auth')),
    _c_(606337, _n_(606334, "url", lambda: url), r'^$', _a_(606336, _n_(606335, "imagec_views", lambda: imagec_views), "ListaFollow"), name="lista_follow"),
    _c_(606341, _n_(606338, "url", lambda: url), r'^add_follow/(?P<id>\d{1,})/$', _a_(606340, _n_(606339, "imagec_views", lambda: imagec_views), "AddFollow"), name='add_follow'),
    _c_(606345, _n_(606342, "url", lambda: url), r'^remove_follow/(?P<id>\d{1,})/$', _a_(606344, _n_(606343, "imagec_views", lambda: imagec_views), "RemoveFollow"), name='remove_follow')

]
_l_(606346)
if _a_(606348, _n_(606347, "settings", lambda: settings), "DEBUG"):
    _l_(606363)

    urlpatterns += _c_(606354, _n_(606349, "static", lambda: static), _a_(606351, _n_(606350, "settings", lambda: settings), "STATIC_URL"), document_root=_a_(606353, _n_(606352, "settings", lambda: settings), "STATIC_ROOT"))
    _l_(606355)
    urlpatterns += _c_(606361, _n_(606356, "static", lambda: static), _a_(606358, _n_(606357, "settings", lambda: settings), "MEDIA_URL"), document_root=_a_(606360, _n_(606359, "settings", lambda: settings), "MEDIA_ROOT"))
    _l_(606362)