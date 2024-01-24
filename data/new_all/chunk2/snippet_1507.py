# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49309748/nameerror-name-django-filters-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(436838)

except ImportError:
    pass
try:
    from django.contrib.postgres.search import SearchVectorField, SearchQuery
    _l_(436840)

except ImportError:
    pass
try:
    from django_filters import FilterSet
    _l_(436842)

except ImportError:
    pass



class Table1(_a_(436844, _n_(436843, "models", lambda: models), "Model"), _a_(436846, _n_(436845, "django_filters", lambda: django_filters), "FilterSet")):
    _l_(436867)

    field1 = _c_(436849, _a_(436848, _n_(436847, "models", lambda: models), "IntegerField"), db_column='field1', blank=True, null=True)  
    _l_(436850)  
    field2 = _c_(436853, _a_(436852, _n_(436851, "models", lambda: models), "NullBooleanField"), db_column='field2')  
    _l_(436854)  
    field3= _c_(436857, _a_(436856, _n_(436855, "models", lambda: models), "IntegerField"), db_column='field3', blank=True, null=True)  
    _l_(436858)  
    field4= _c_(436861, _a_(436860, _n_(436859, "models", lambda: models), "TextField"), db_column='field4', blank=True, null=False, primary_key=True)  
    _l_(436862)  

    #def __str__(self):
     #   return self.sid

    class Meta:
        _l_(436866)

        managed = False
        _l_(436863)
        db_table = 'Table1'
        _l_(436864)
        unique_together = (('field1', 'field2', 'field3', 'field4'),)
        _l_(436865)