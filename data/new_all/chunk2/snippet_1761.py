# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57858987/how-to-fix-attributeerror-settings-object-has-no-attribute-root-urlconf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""producthunt URL Configuration

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
    _l_(426804)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(426806)

except ImportError:
    pass
try:
    from django.contrib.auth import views as auth_views
    _l_(426808)

except ImportError:
    pass
try:
    from links.views import LinkListView
    _l_(426810)

except ImportError:
    pass
try:
    from links.views import UserProfileDetailView
    _l_(426812)

except ImportError:
    pass
try:
    from django.contrib.auth.decorators import login_required as auth
    _l_(426814)

except ImportError:
    pass
try:
    from links.views import UserProfileEditView
    _l_(426816)

except ImportError:
    pass
try:
    from links.views import LinkCreateView, LinkDetailView
    _l_(426818)

except ImportError:
    pass
try:
    from links.views import LinkEditView
    _l_(426820)

except ImportError:
    pass
try:
    from links.views import LinkDeleteView
    _l_(426822)

except ImportError:
    pass

urlpatterns = [
    _c_(426827, _n_(426823, "url", lambda: url), r'^admin/', _a_(426826, _a_(426825, _n_(426824, "admin", lambda: admin), "site"), "urls")),
    _c_(426832, _n_(426828, "url", lambda: url), r'^$', _c_(426831, _a_(426830, _n_(426829, "LinkListView", lambda: LinkListView), "as_view")), name='home'),
    _c_(426836, _n_(426833, "url", lambda: url), r'^login/$', _a_(426835, _n_(426834, "auth_views", lambda: auth_views), "login"), name='login'),
    _c_(426840, _n_(426837, "url", lambda: url), r'^logout/$', _a_(426839, _n_(426838, "auth_views", lambda: auth_views), "logout"), name='logout'),
    _c_(426844, _n_(426841, "url", lambda: url), r'^accounts/', _c_(426843, _n_(426842, "include", lambda: include), 'registration.backends.simple.urls')),
    _c_(426849, _n_(426845, "url", lambda: url), r'^users/(?P<slug>\w+)/$', _c_(426848, _a_(426847, _n_(426846, "UserProfileDetailView", lambda: UserProfileDetailView), "as_view")),name='profile'),
    _c_(426856, _n_(426850, "url", lambda: url), r'^edit_profile/$', _c_(426855, _n_(426851, "auth", lambda: auth), _c_(426854, _a_(426853, _n_(426852, "UserProfileEditView", lambda: UserProfileEditView), "as_view"))), name='edit_profile'),
    _c_(426863, _n_(426857, "url", lambda: url), r'^link/submit/$', _c_(426862, _n_(426858, "auth", lambda: auth), _c_(426861, _a_(426860, _n_(426859, "LinkCreateView", lambda: LinkCreateView), "as_view"))), name='link_submit'),
    _c_(426868, _n_(426864, "url", lambda: url), r'^link/(?P<pk>\d+)/$', _c_(426867, _a_(426866, _n_(426865, "LinkDetailView", lambda: LinkDetailView), "as_view")), name='link_detail'),
    _c_(426875, _n_(426869, "url", lambda: url), r'^link/edit/(?P<pk>\d+)/$', _c_(426874, _n_(426870, "auth", lambda: auth), _c_(426873, _a_(426872, _n_(426871, "LinkEditView", lambda: LinkEditView), "as_view"))), name='link_edit'),
    _c_(426882, _n_(426876, "url", lambda: url), r'^link/delete/(?P<pk>\d+)/$', _c_(426881, _n_(426877, "auth", lambda: auth), _c_(426880, _a_(426879, _n_(426878, "LinkDeleteView", lambda: LinkDeleteView), "as_view"))), name='link_delete'),
    _c_(426886, _n_(426883, "url", lambda: url), r'^comments/', _c_(426885, _n_(426884, "include", lambda: include), 'django_comments.urls')),
]
_l_(426887)