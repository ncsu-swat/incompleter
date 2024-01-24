# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58902206/get-form-in-modeladmin-causing-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CustomMemoAdmin(_a_(565404, _n_(565403, "admin", lambda: admin), "ModelAdmin")):
    _l_(565417)

    form = AdminMemoForm
    _l_(565405)

    def get_form(self, request, obj=None, **kwargs):
        _l_(565416)

        form = _c_(565411, _a_(565407, _n_(565406, "super", lambda: super)(), "get_form"), _n_(565408, "request", lambda: request), _n_(565409, "obj", lambda: obj), **_n_(565410, "kwargs", lambda: kwargs))
        _l_(565412)
        aux = _c_(565414, _n_(565413, "form", lambda: form))
        _l_(565415)
    #     if not request.user.is_superuser:
    #         self.fields = (
    #             'title',
    #             'content',
    #             'important',
    #             'receiver',
    #             'read',
    #             'unread',
    #             'word_file',
    #         )
    #     self.filter_horizontal = ('casino',)
        return aux