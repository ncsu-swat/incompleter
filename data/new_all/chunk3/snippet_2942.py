# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57515323/attributeerror-tuple-object-has-no-attribute-get
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CourseForm(_a_(548755, _n_(548754, "forms", lambda: forms), "ModelForm")):
    _l_(548808)

    class Meta:
        _l_(548770)

        model = Course
        _l_(548756)
        fields = ['title', 'subtitle', 'image', 'description', 'status']
        _l_(548757)

        widgets = {
            'title': _c_(548759, _a_(548758, forms, "TextInput"), attrs = {'class': 'form-control', 'placeholder': 'Titulo'}),
            'subtitle': _c_(548761, _a_(548760, forms, "TextInput"), attrs = {'class': 'form-control', 'placeholder': 'Subtitulo'}),
            'image': _c_(548763, _a_(548762, forms, "FileInput"), attrs = {'class': 'custom-file-input'}),
            'description': _c_(548765, _a_(548764, forms, "Textarea"), attrs = {'class': 'form-control', 'placeholder': 'Descripcion'}),
            'status': _c_(548767, _a_(548766, forms, "Select"), attrs = {'class': 'custom-select'}),
        }
        _l_(548768)

        labels = {'title': '', 'subtitle': '', 'image': '', 'description': ''}
        _l_(548769)

    def __init__(self, *args, **kwargs):
        _l_(548786)

        _n_(548771, "self", lambda: self).title_valid = False 
        _l_(548772) 
        if 'title_valid' in _n_(548773, "kwargs", lambda: kwargs):
            _l_(548779)

            _n_(548774, "self", lambda: self).title_valid = _c_(548777, _a_(548776, _n_(548775, "kwargs", lambda: kwargs), "pop"), 'title_valid')
            _l_(548778)

        _c_(548784, _a_(548781, _n_(548780, "super", lambda: super)(), "__init__"), _n_(548782, "args", lambda: args), _n_(548783, "kwargs", lambda: kwargs))
        _l_(548785)

    def clean_title(self):
        _l_(548807)

        title = _a_(548788, _n_(548787, "self", lambda: self), "cleaned_data")['title']
        _l_(548789)
        if _a_(548791, _n_(548790, "self", lambda: self), "title_valid"):
            _l_(548804)

            if _c_(548798, _a_(548797, _c_(548796, _a_(548794, _a_(548793, _n_(548792, "Course", lambda: Course), "objects"), "filter"), title = _n_(548795, "title", lambda: title)), "exists")):
                _l_(548803)

                raise _c_(548801, _a_(548800, _n_(548799, "forms", lambda: forms), "ValidationError"), 'Ya existe un curso registrado con ese titulo, elige otro.')
                _l_(548802)
        aux = _n_(548805, "title", lambda: title)
        _l_(548806)

        return aux