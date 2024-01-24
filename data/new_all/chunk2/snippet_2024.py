# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68994258/django-typeerror-httpresponseforbidden-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import Pattern
    _l_(432414)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(432416)

except ImportError:
    pass
try:
    from django.urls import path, include
    _l_(432418)

except ImportError:
    pass
try:
    from django.contrib.auth import views as auth_views
    _l_(432420)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(432422)

except ImportError:
    pass
try:
    from django.conf.urls.static import static
    _l_(432424)

except ImportError:
    pass
try:
    from Users import views as user_views
    _l_(432426)

except ImportError:
    pass


urlpatterns = [
    _c_(432431, _n_(432427, "path", lambda: path), 'admin/', _a_(432430, _a_(432429, _n_(432428, "admin", lambda: admin), "site"), "urls")),
    _c_(432435, _n_(432432, "path", lambda: path), '', _c_(432434, _n_(432433, "include", lambda: include), 'Job.urls')),
    _c_(432439, _n_(432436, "path", lambda: path), 'register/', _a_(432438, _n_(432437, "user_views", lambda: user_views), "register"), name="Register"),
    _c_(432445, _n_(432440, "path", lambda: path), 'login/', _c_(432444, _a_(432443, _a_(432442, _n_(432441, "auth_views", lambda: auth_views), "LoginView"), "as_view"), template_name='Users/login.html'), name='Login'),
    _c_(432451, _n_(432446, "path", lambda: path), 'Logout/', _c_(432450, _a_(432449, _a_(432448, _n_(432447, "auth_views", lambda: auth_views), "LogoutView"), "as_view"), template_name='Users/index.html'), name='Logout'),
    _c_(432455, _n_(432452, "path", lambda: path), 'profile/', _a_(432454, _n_(432453, "user_views", lambda: user_views), "Profile"), name="Profile_Page"),
    _c_(432461, _n_(432456, "path", lambda: path), 'Password-reset/', _c_(432460, _a_(432459, _a_(432458, _n_(432457, "auth_views", lambda: auth_views), "PasswordResetView"), "as_view"), template_name='Users/password_reset.html'), name='password_reset'),
    _c_(432467, _n_(432462, "path", lambda: path), 'Password-reset/done/', _c_(432466, _a_(432465, _a_(432464, _n_(432463, "auth_views", lambda: auth_views), "PasswordResetDoneView"), "as_view"), template_name='Users/password_reset_done.html'), name='password_reset_done'),
    _c_(432473, _n_(432468, "path", lambda: path), 'Password-reset-confirm/<uidb64>/<token>/', _c_(432472, _a_(432471, _a_(432470, _n_(432469, "auth_views", lambda: auth_views), "PasswordResetConfirmView"), "as_view"), template_name='Users/password_reset_confirm.html'), name='password_reset_confirm'),
]
_l_(432474)


if _a_(432476, _n_(432475, "settings", lambda: settings), "DEBUG"):
    _l_(432484)

    urlpatterns += _c_(432482, _n_(432477, "static", lambda: static), _a_(432479, _n_(432478, "settings", lambda: settings), "MEDIA_URL"),
                          document_root=_a_(432481, _n_(432480, "settings", lambda: settings), "MEDIA_ROOT"))
    _l_(432483)