# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74169850/mongodb-with-django-typeerror-model-instances-without-primary-key-value-are-un
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': '<name>',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': f'mongodb+srv://{_n_(580470, "mongodb_username", lambda: mongodb_username)}:{_n_(580471, "mongodb_password", lambda: mongodb_password)}@{_n_(580472, "mongodb_cluster", lambda: mongodb_cluster)}/?retryWrites=true',
                'uuidRepresentation': 'standard',
                'waitQueueTimeoutMS': 30000
            }
        }
}
_l_(580473)