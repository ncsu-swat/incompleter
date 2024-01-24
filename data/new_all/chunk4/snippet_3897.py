# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65725015/typeerror-module-object-is-not-callable-django-3-render-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
BASE_DIR = _c_(630326, _a_(630316, _a_(630315, _n_(630314, "os", lambda: os), "path"), "dirname"), _c_(630325, _a_(630319, _a_(630318, _n_(630317, "os", lambda: os), "path"), "dirname"), _c_(630324, _a_(630322, _a_(630321, _n_(630320, "os", lambda: os), "path"), "abspath"), _n_(630323, "__file__", lambda: __file__))))
_l_(630327)
TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [_c_(630332, _a_(630330, _a_(630329, _n_(630328, "os", lambda: os), "path"), "join"), _n_(630331, "BASE_DIR", lambda: BASE_DIR), 'templates')],
    'APP_DIRS': False,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.contrib.sessions'
        ],
    },
},
]
_l_(630333)