# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41323764/django-error-typeerror-init-got-an-unexpected-keyword-argument-attrs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.forms import ModelForm, TextInput, TextInput, EmailField
    _l_(403180)

except ImportError:
    pass
try:
    from .models import Contact
    _l_(403182)

except ImportError:
    pass

class ContactForm(_n_(403183, "ModelForm", lambda: ModelForm)):
    _l_(403196)

    class Meta:
        _l_(403195)

        model = _n_(403184, "Contact", lambda: Contact)
        _l_(403185)
        fields = ('your_name', 'your_email', 'your_subject', 'your_comment')
        _l_(403186)
        widgets = {
            'your_name' : _c_(403188, _n_(403187, "TextInput", lambda: TextInput), attrs={'placeholder': 'Name *', 'class': 'form-control'}),
            'your_email' : _c_(403190, _n_(403189, "EmailField", lambda: EmailField), attrs={'placeholder': 'Email *', 'class': 'form-control'}),
            'your_subject' : _c_(403192, _n_(403191, "TextInput", lambda: TextInput), attrs={'placeholder': 'Subject *', 'class': 'form-control'}),
            'your_comment' : _c_(403193, Textarea, attrs={'placeholder': 'Comment *', 'class': 'form-control'}),
        }
        _l_(403194)