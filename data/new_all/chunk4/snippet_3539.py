# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#serializers.py


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from rest_framework import serializers
  _l_(605582)

except ImportError:
  pass
try:
  from myapp.models import Airport, Flight, User, Passenger, Booking
  _l_(605584)

except ImportError:
  pass


class UserRegistrationSerializer(_a_(605586, _n_(605585, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(605621)

  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = _c_(605589, _a_(605588, _n_(605587, "serializers", lambda: serializers), "CharField"), style={'input_type':'password'}, write_only=True)
  _l_(605590)
  class Meta:
    _l_(605595)

    model = _n_(605591, "User", lambda: User)
    _l_(605592)
    fields=['email','name','contact_number','gender','address','state','city','country','pincode','dob','password', 'password2']
    _l_(605593)
    extra_kwargs={
      'password':{'write_only':True}
    }
    _l_(605594)

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    _l_(605613)

    password = _c_(605598, _a_(605597, _n_(605596, "attrs", lambda: attrs), "get"), 'password')
    _l_(605599)
    password2 = _c_(605602, _a_(605601, _n_(605600, "attrs", lambda: attrs), "get"), 'password2')
    _l_(605603)
    if _n_(605604, "password", lambda: password) != _n_(605605, "password2", lambda: password2):
      _l_(605610)

      raise _c_(605608, _a_(605607, _n_(605606, "serializers", lambda: serializers), "ValidationError"), "Password and Confirm Password doesn't match")
      _l_(605609)
    aux = _n_(605611, "attrs", lambda: attrs)
    _l_(605612)
    return aux

  def create(self, validate_data):
    _l_(605620)

    aux = _c_(605618, _a_(605616, _a_(605615, _n_(605614, "User", lambda: User), "objects"), "create_user"), **_n_(605617, "validate_data", lambda: validate_data))
    _l_(605619)
    return aux

class UserLoginSerializer(_a_(605623, _n_(605622, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(605632)

  email = _c_(605626, _a_(605625, _n_(605624, "serializers", lambda: serializers), "EmailField"), max_length=255)
  _l_(605627)
  class Meta:
    _l_(605631)

    model = _n_(605628, "User", lambda: User)
    _l_(605629)
    fields = ['email', 'password']
    _l_(605630)

# class UserProfileSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = '__all__'



class AirportSerializer(_a_(605634, _n_(605633, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(605639)

  class Meta:
    _l_(605638)

    model = _n_(605635, "Airport", lambda: Airport)
    _l_(605636)
    fields = '__all__'
    _l_(605637)

class FlightSerializer(_a_(605641, _n_(605640, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(605646)

  class Meta:
    _l_(605645)

    model = _n_(605642, "Flight", lambda: Flight)
    _l_(605643)
    fields = '__all__'
    _l_(605644)

class UserSerializer(_a_(605648, _n_(605647, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(605653)

  class Meta:
    _l_(605652)

    model= _n_(605649, "User", lambda: User)
    _l_(605650)
    fields = '__all__'
    _l_(605651)

class PassengerSerializer(_a_(605655, _n_(605654, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(605663)

  user = _c_(605657, _n_(605656, "UserSerializer", lambda: UserSerializer), read_only=False)
  _l_(605658)
  class Meta:
    _l_(605662)

    model= _n_(605659, "Passenger", lambda: Passenger)
    _l_(605660)
    fields = '__all__'
    _l_(605661)

class BookingSerializer(_a_(605665, _n_(605664, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(605670)

  class Meta:
    _l_(605669)

    model= _n_(605666, "Booking", lambda: Booking)
    _l_(605667)
    fields = '__all__'
    _l_(605668)