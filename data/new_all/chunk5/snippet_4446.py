# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57628352/recieving-an-attribute-error-when-trying-to-add-a-new-view
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
try:
    from django.contrib import admin
    _l_(670177)

except ImportError:
    pass
try:
    from django.urls import path
    _l_(670179)

except ImportError:
    pass
try:
    from pages import views
    _l_(670181)

except ImportError:
    pass

urlpatterns = [
    _c_(670186, _n_(670182, "path", lambda: path), 'admin/', _a_(670185, _a_(670184, _n_(670183, "admin", lambda: admin), "site"), "urls")),
    _c_(670190, _n_(670187, "path", lambda: path), '', _a_(670189, _n_(670188, "views", lambda: views), "home"), name='home'),
]
_l_(670191)