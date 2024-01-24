# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57515323/attributeerror-tuple-object-has-no-attribute-get
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CourseUpdateView(_n_(537879, "UpdateView", lambda: UpdateView)):
    _l_(537942)

    model = Course
    _l_(537880)
    form_class = CourseForm
    _l_(537881)
    template_name = 'instructor/course_update_form.html'
    _l_(537882)
    success_url = _c_(537883, reverse_lazy, 'instructor:course:list')
    _l_(537884)
    success_message = 'Se modificó con éxito el curso "{}".'
    _l_(537885)

    def get_form(self, form_class = None):
        _l_(537909)

        if _n_(537886, "form_class", lambda: form_class) is None:
            _l_(537891)

            form_class = _c_(537889, _a_(537888, _n_(537887, "self", lambda: self), "get_form_class"))
            _l_(537890)

        form = _c_(537896, _n_(537892, "form_class", lambda: form_class), **_c_(537895, _a_(537894, _n_(537893, "self", lambda: self), "get_form_kwargs")), title_valid = True)
        _l_(537897)
        for field in _c_(537901, _a_(537900, _a_(537899, _n_(537898, "form", lambda: form), "fields"), "keys")):
            _l_(537906)

            _a_(537903, _n_(537902, "form", lambda: form), "fields")[_n_(537904, "field", lambda: field)].required = False
            _l_(537905)
        aux = _n_(537907, "form", lambda: form)
        _l_(537908)

        return aux

    def form_valid(self, form):
        _l_(537941)

        obj = _c_(537912, _a_(537911, _n_(537910, "form", lambda: form), "save"), commit = False)
        _l_(537913)
        _n_(537914, "obj", lambda: obj).slug = _c_(537918, _n_(537915, "slugify", lambda: slugify), _a_(537917, _n_(537916, "obj", lambda: obj), "title"))
        _l_(537919)
        _c_(537922, _a_(537921, _n_(537920, "obj", lambda: obj), "save"))
        _l_(537923)

        _c_(537934, _a_(537925, _n_(537924, "messages", lambda: messages), "success"), _a_(537927, _n_(537926, "self", lambda: self), "request"), _c_(537933, _a_(537930, _a_(537929, _n_(537928, "self", lambda: self), "success_message"), "format"), _a_(537932, _n_(537931, "obj", lambda: obj), "title")))
        _l_(537935)
        aux = _c_(537939, _n_(537936, "redirect", lambda: redirect), _a_(537938, _n_(537937, "self", lambda: self), "success_url"))
        _l_(537940)
        return aux