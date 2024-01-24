# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57689928/why-am-i-getting-this-error-attributeerror-str-object-has-no-attribute-deco
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(377408)

except ImportError:
    pass
try:
    from django.contrib.auth import views as auth_views
    _l_(377410)

except ImportError:
    pass
try:
    from django.urls import path, include
    _l_(377412)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(377414)

except ImportError:
    pass
try:
    from django.conf.urls.static import static
    _l_(377416)

except ImportError:
    pass
try:
    from users import views as user_views
    _l_(377418)

except ImportError:
    pass

urlpatterns = [
    _c_(377423, _n_(377419, "path", lambda: path), 'admin/', _a_(377422, _a_(377421, _n_(377420, "admin", lambda: admin), "site"), "urls")),
    # path('register/', user_views.register, name='register'),
    _c_(377427, _n_(377424, "path", lambda: path), 'register/', _c_(377426, _n_(377425, "include", lambda: include), 'users.urls')), # new url
    _c_(377431, _n_(377428, "path", lambda: path), 'profile/', _a_(377430, _n_(377429, "user_views", lambda: user_views), "profile"), name='profile'),
    _c_(377437, _n_(377432, "path", lambda: path), 'login/', _c_(377436, _a_(377435, _a_(377434, _n_(377433, "auth_views", lambda: auth_views), "LoginView"), "as_view"), template_name = 'users/login.html'), name='login'),
    _c_(377443, _n_(377438, "path", lambda: path), 'logout/', _c_(377442, _a_(377441, _a_(377440, _n_(377439, "auth_views", lambda: auth_views), "LogoutView"), "as_view"), template_name = 'users/logout.html'), name='logout'),
    _c_(377449, _n_(377444, "path", lambda: path), 'password-reset/', 
            _c_(377448, _a_(377447, _a_(377446, _n_(377445, "auth_views", lambda: auth_views), "PasswordResetView"), "as_view"), template_name = 'users/password_reset.html'), 
            name='password_reset'),
    _c_(377455, _n_(377450, "path", lambda: path), 'password-reset/done/', 
            _c_(377454, _a_(377453, _a_(377452, _n_(377451, "auth_views", lambda: auth_views), "PasswordResetDoneView"), "as_view"), template_name = 'users/password_reset_done.html'), 
            name='password_reset_done'),
    _c_(377461, _n_(377456, "path", lambda: path), 'password-reset-confirm/<uidb64>/<token>/', 
            _c_(377460, _a_(377459, _a_(377458, _n_(377457, "auth_views", lambda: auth_views), "PasswordResetConfirmView"), "as_view"), template_name = 'users/password_reset_confirm.html'), 
            name='password_reset_confirm'),
    _c_(377467, _n_(377462, "path", lambda: path), 'password-reset-complete/', 
                _c_(377466, _a_(377465, _a_(377464, _n_(377463, "auth_views", lambda: auth_views), "PasswordResetCompleteView"), "as_view"), template_name = 'users/password_reset_complete.html'), 
                name='password_reset_complete'),
    _c_(377471, _n_(377468, "path", lambda: path), '', _c_(377470, _n_(377469, "include", lambda: include), 'blog.urls')),

]
_l_(377472)

if _a_(377474, _n_(377473, "settings", lambda: settings), "DEBUG"):
    _l_(377489)

    urlpatterns += _c_(377480, _n_(377475, "static", lambda: static), _a_(377477, _n_(377476, "settings", lambda: settings), "STATIC_URL"), document_root=_a_(377479, _n_(377478, "settings", lambda: settings), "STATIC_ROOT"))
    _l_(377481)
    urlpatterns += _c_(377487, _n_(377482, "static", lambda: static), _a_(377484, _n_(377483, "settings", lambda: settings), "MEDIA_URL"), document_root=_a_(377486, _n_(377485, "settings", lambda: settings), "MEDIA_ROOT"))
    _l_(377488)