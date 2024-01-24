# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58280786/django-admin-typeerror-int-argument-must-be-a-string-a-bytes-like-object-or
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(666179, _a_(666177, _n_(666176, "admin", lambda: admin), "register"), _n_(666178, "Car", lambda: Car))
class CarAdmin(_a_(666181, _n_(666180, "admin", lambda: admin), "ModelAdmin")):
    _l_(666185)

    list_display = ('manufacturer', 'model', 'model_year', 'mileage', 'status', 'date_added', 'price', 'seller')
    _l_(666182)
    list_filter = ('manufacturer', 'status', 'transmission')
    _l_(666183)
    fieldsets = (
        ('General information', {
            'fields': ('car_images', 'manufacturer', 'model',
            'model_year', 'price', 'vin', 'mileage', 'transmission', 'engine_displacement', 
            'forced_induction', 'drivetrain', 'description', 'id',)
        }),
       ('Availability', {
            'fields': ('status', 'seller')
        }),
    )
    _l_(666184)