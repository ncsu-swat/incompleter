# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58683181/django-rest-framework-authentication-permissions-error-typeerror-str-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import permissions
    _l_(420403)

except ImportError:
    pass

class IsCurrentUserOwnerOrReadOnly(_a_(420405, _n_(420404, "permissions", lambda: permissions), "BasePermission")):
    _l_(420418)

    def has_object_permission(self, request, view, obj):
        _l_(420417)

        if _a_(420407, _n_(420406, "request", lambda: request), "method") in _a_(420409, _n_(420408, "permissions", lambda: permissions), "SAFE_METHODS"):
            _l_(420416)

            aux = True
            _l_(420410)
            # The method is a safe method
            return aux
        else:
            aux = _a_(420412, _n_(420411, "obj", lambda: obj), "owner") == _a_(420414, _n_(420413, "request", lambda: request), "user")
            _l_(420415)
            # The method is not a safe method
            # Only owners are granted permissions
            return aux