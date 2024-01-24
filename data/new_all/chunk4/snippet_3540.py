# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#admin.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from django.contrib import admin
  _l_(640965)

except ImportError:
  pass
try:
  from .models import Airport, Booking, Flight, User, Passenger
  _l_(640967)

except ImportError:
  pass
try:
  from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
  _l_(640969)

except ImportError:
  pass

class UserModelAdmin(_n_(640970, "BaseUserAdmin", lambda: BaseUserAdmin)):
  _l_(640978)

  # The fields to be used in displaying the User model.staff= models.BooleanField(default=False)
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  list_display = ('id', 'email', 'name', 'is_admin','is_active')
  _l_(640971)
  list_filter = ('is_admin',)
  _l_(640972)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('name', 'contact_number', 'gender', 'dob','address', 'state', 'city', 'country', 'pincode',)}),
      ('Permissions', {'fields': ('is_admin',)}),
  )
  _l_(640973)
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name', 'password1', 'password2',),
      }),
  )
  _l_(640974)
  search_fields = ('email',)
  _l_(640975)
  ordering = ('email', 'id')
  _l_(640976)
  filter_horizontal = ()
  _l_(640977)



# Register your models here.
_c_(640984, _a_(640981, _a_(640980, _n_(640979, "admin", lambda: admin), "site"), "register"), _n_(640982, "User", lambda: User),_n_(640983, "UserModelAdmin", lambda: UserModelAdmin))
_l_(640985)
_c_(640993, _a_(640988, _a_(640987, _n_(640986, "admin", lambda: admin), "site"), "register"), [_n_(640989, "Airport", lambda: Airport),_n_(640990, "Flight", lambda: Flight),_n_(640991, "Passenger", lambda: Passenger),_n_(640992, "Booking", lambda: Booking)])
_l_(640994)