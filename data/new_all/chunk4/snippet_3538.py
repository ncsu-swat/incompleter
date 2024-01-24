# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#models.py


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import email
  _l_(600985)

except ImportError:
  pass
try:
  from pyexpat import model
  _l_(600987)

except ImportError:
  pass
try:
  from django.db import models
  _l_(600989)

except ImportError:
  pass
try:
  from django.conf import settings
  _l_(600991)

except ImportError:
  pass
try:
  from django.db.models.signals import post_save
  _l_(600993)

except ImportError:
  pass
try:
  from django.dispatch import receiver
  _l_(600995)

except ImportError:
  pass
try:
  from django.contrib.auth.models import (
      BaseUserManager, AbstractBaseUser
  )
  _l_(600997)

except ImportError:
  pass

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),)
_l_(600998)

class UserManager(_n_(600999, "BaseUserManager", lambda: BaseUserManager)):
  _l_(601062)

  def create_user(self, email, name,contact_number,gender,address,state,city,country,pincode,dob ,password=None, password2=None):
    _l_(601035)

    
    if not _n_(601000, "email", lambda: email):
      _l_(601004)

      raise _c_(601002, _n_(601001, "ValueError", lambda: ValueError), 'User must have an email address')
      _l_(601003)

    user = _c_(601020, _a_(601006, _n_(601005, "self", lambda: self), "model"), email=_c_(601010, _a_(601008, _n_(601007, "self", lambda: self), "normalize_email"), _n_(601009, "email", lambda: email)),
        name=_n_(601011, "name", lambda: name),
        contact_number=_n_(601012, "contact_number", lambda: contact_number),
        gender=_n_(601013, "gender", lambda: gender),
        address=_n_(601014, "address", lambda: address),
        state=_n_(601015, "state", lambda: state),
        city=_n_(601016, "city", lambda: city),
        country=_n_(601017, "country", lambda: country),
        pincode=_n_(601018, "pincode", lambda: pincode),
        dob=_n_(601019, "dob", lambda: dob),
        
    )
    _l_(601021)

    _c_(601025, _a_(601023, _n_(601022, "user", lambda: user), "set_password"), _n_(601024, "password", lambda: password))
    _l_(601026)
    
    _c_(601031, _a_(601028, _n_(601027, "user", lambda: user), "save"), using=_a_(601030, _n_(601029, "self", lambda: self), "_db"))
    _l_(601032)
    aux = _n_(601033, "user", lambda: user)
    _l_(601034)
    return aux

  def create_superuser(self, email, name,contact_number,gender,address,state,city,country,pincode,dob , password=None):
    _l_(601061)

     
    user = _c_(601049, _a_(601037, _n_(601036, "self", lambda: self), "create_user"), _n_(601038, "email", lambda: email),
        
        name=_n_(601039, "name", lambda: name),
        contact_number=_n_(601040, "contact_number", lambda: contact_number),
        gender=_n_(601041, "gender", lambda: gender),
        address=_n_(601042, "address", lambda: address),
        state=_n_(601043, "state", lambda: state),
        city=_n_(601044, "city", lambda: city),
        country=_n_(601045, "country", lambda: country),
        pincode=_n_(601046, "pincode", lambda: pincode),
        dob=_n_(601047, "dob", lambda: dob),
        password=_n_(601048, "password", lambda: password),
        
    )
    _l_(601050)
    _n_(601051, "user", lambda: user).is_admin = True
    _l_(601052)
    _c_(601057, _a_(601054, _n_(601053, "user", lambda: user), "save"), using=_a_(601056, _n_(601055, "self", lambda: self), "_db"))
    _l_(601058)
    aux = _n_(601059, "user", lambda: user)
    _l_(601060)
    return aux



class User(_n_(601063, "AbstractBaseUser", lambda: AbstractBaseUser)):
  _l_(601144)

  email = _c_(601066, _a_(601065, _n_(601064, "models", lambda: models), "EmailField"), verbose_name='Email',max_length=255,unique=True)
  _l_(601067)
  name = _c_(601070, _a_(601069, _n_(601068, "models", lambda: models), "CharField"), max_length=200)
  _l_(601071)
  contact_number= _c_(601074, _a_(601073, _n_(601072, "models", lambda: models), "IntegerField"))
  _l_(601075)
  gender = _c_(601079, _a_(601077, _n_(601076, "models", lambda: models), "IntegerField"), choices=_n_(601078, "GENDER_CHOICES", lambda: GENDER_CHOICES))
  _l_(601080)
  address= _c_(601083, _a_(601082, _n_(601081, "models", lambda: models), "CharField"), max_length=100)
  _l_(601084)
  state=_c_(601087, _a_(601086, _n_(601085, "models", lambda: models), "CharField"), max_length=100)
  _l_(601088)
  city=_c_(601091, _a_(601090, _n_(601089, "models", lambda: models), "CharField"), max_length=100)
  _l_(601092)
  country=_c_(601095, _a_(601094, _n_(601093, "models", lambda: models), "CharField"), max_length=100)
  _l_(601096)
  pincode= _c_(601099, _a_(601098, _n_(601097, "models", lambda: models), "IntegerField"))
  _l_(601100)
  dob = _c_(601103, _a_(601102, _n_(601101, "models", lambda: models), "DateField"))
  _l_(601104)


  # is_staff = models.BooleanField(default=False)
  is_active = _c_(601107, _a_(601106, _n_(601105, "models", lambda: models), "BooleanField"), default=True)
  _l_(601108)
  is_admin = _c_(601111, _a_(601110, _n_(601109, "models", lambda: models), "BooleanField"), default=False)
  _l_(601112)
  created_at = _c_(601115, _a_(601114, _n_(601113, "models", lambda: models), "DateTimeField"), auto_now_add=True)
  _l_(601116)
  updated_at = _c_(601119, _a_(601118, _n_(601117, "models", lambda: models), "DateTimeField"), auto_now=True)
  _l_(601120)

  objects = _c_(601122, _n_(601121, "UserManager", lambda: UserManager))
  _l_(601123)

  USERNAME_FIELD = 'email'
  _l_(601124)
  REQUIRED_FIELDS = ['name','contact_number','gender','address','state','city','country','pincode','dob']
  _l_(601125)

  def __str__(self):
    _l_(601129)

    aux = _a_(601127, _n_(601126, "self", lambda: self), "email")
    _l_(601128)
    return aux

  def has_perm(self, perm, obj=None):
    _l_(601134)

    "Does the user have a specific permission?"
    _l_(601130)
    aux = _a_(601132, _n_(601131, "self", lambda: self), "is_admin")
    _l_(601133)
    # Simplest possible answer: Yes, always
    return aux

  def has_module_perms(self, app_label):
    _l_(601137)

    "Does the user have permissions to view the app `app_label`?"
    _l_(601135)
    aux = True
    _l_(601136)
    # Simplest possible answer: Yes, always
    return aux

  @_n_(601138, "property", lambda: property)
  def is_staff(self):
    _l_(601143)

    "Is the user a member of staff?"
    _l_(601139)
    aux = _a_(601141, _n_(601140, "self", lambda: self), "is_admin")
    _l_(601142)
    # Simplest possible answer: All admins are staff
    return aux


# Create your models here.
class Airport(_a_(601146, _n_(601145, "models", lambda: models), "Model")):
  _l_(601159)

  Airport_name=_c_(601149, _a_(601148, _n_(601147, "models", lambda: models), "CharField"), max_length=100)
  _l_(601150)
  country=_c_(601153, _a_(601152, _n_(601151, "models", lambda: models), "CharField"), max_length=100)
  _l_(601154)

  def __str__(self):
    _l_(601158)

    aux = _a_(601156, _n_(601155, "self", lambda: self), "Airport_name")
    _l_(601157)
    return aux

class Flight(_a_(601161, _n_(601160, "models", lambda: models), "Model")):
  _l_(601211)


  flight_number = _c_(601164, _a_(601163, _n_(601162, "models", lambda: models), "CharField"), max_length=100,unique=True)
  _l_(601165)
  depart_date_time = _c_(601168, _a_(601167, _n_(601166, "models", lambda: models), "DateTimeField"), auto_now_add=True)
  _l_(601169)
  arrival_date_time = _c_(601172, _a_(601171, _n_(601170, "models", lambda: models), "DateTimeField"), auto_now_add=True)
  _l_(601173)
  origin = _c_(601176, _a_(601175, _n_(601174, "models", lambda: models), "CharField"), max_length=100, blank=True, default='')
  _l_(601177)
  destination = _c_(601180, _a_(601179, _n_(601178, "models", lambda: models), "CharField"), max_length=100, blank=True, default='')
  _l_(601181)
  price = _c_(601184, _a_(601183, _n_(601182, "models", lambda: models), "IntegerField"))
  _l_(601185)
  airline_name = _c_(601188, _a_(601187, _n_(601186, "models", lambda: models), "CharField"), max_length=100, blank=True, default='')
  _l_(601189)
  total_seats = _c_(601192, _a_(601191, _n_(601190, "models", lambda: models), "IntegerField"))
  _l_(601193)
  available_seats =  _c_(601196, _a_(601195, _n_(601194, "models", lambda: models), "IntegerField"))
  _l_(601197)
  
  
  airport=_c_(601203, _a_(601199, _n_(601198, "models", lambda: models), "ForeignKey"), _n_(601200, "Airport", lambda: Airport),on_delete=_a_(601202, _n_(601201, "models", lambda: models), "CASCADE"))
  _l_(601204)

  def __str__(self):
    _l_(601210)

    aux = _c_(601208, _n_(601205, "str", lambda: str), _a_(601207, _n_(601206, "self", lambda: self), "flight_number"))
    _l_(601209)
    return aux

   

class Passenger(_a_(601213, _n_(601212, "models", lambda: models), "Model")):
  _l_(601246)

  name = _c_(601216, _a_(601215, _n_(601214, "models", lambda: models), "CharField"), max_length=100,blank=True, default='')
  _l_(601217)
  contact_number= _c_(601220, _a_(601219, _n_(601218, "models", lambda: models), "IntegerField"))
  _l_(601221)
  email = _c_(601224, _a_(601223, _n_(601222, "models", lambda: models), "EmailField"), max_length=254)
  _l_(601225)
  
  gender = _c_(601229, _a_(601227, _n_(601226, "models", lambda: models), "IntegerField"), choices=_n_(601228, "GENDER_CHOICES", lambda: GENDER_CHOICES))
  _l_(601230)
  age= _c_(601233, _a_(601232, _n_(601231, "models", lambda: models), "IntegerField"))
  _l_(601234)
  user=_c_(601240, _a_(601236, _n_(601235, "models", lambda: models), "ForeignKey"), _n_(601237, "User", lambda: User),on_delete=_a_(601239, _n_(601238, "models", lambda: models), "CASCADE"))
  _l_(601241)

  def __str__(self):
    _l_(601245)

    aux = _a_(601243, _n_(601242, "self", lambda: self), "name")  
    _l_(601244)  
    return aux  


class Booking(_a_(601248, _n_(601247, "models", lambda: models), "Model")):
  _l_(601284)

  user =_c_(601254, _a_(601250, _n_(601249, "models", lambda: models), "ForeignKey"), _n_(601251, "User", lambda: User),on_delete=_a_(601253, _n_(601252, "models", lambda: models), "CASCADE"))
  _l_(601255)
  flights =_c_(601261, _a_(601257, _n_(601256, "models", lambda: models), "ForeignKey"), _n_(601258, "Flight", lambda: Flight),on_delete=_a_(601260, _n_(601259, "models", lambda: models), "CASCADE"))
  _l_(601262)
  passenger =_c_(601266, _a_(601264, _n_(601263, "models", lambda: models), "ManyToManyField"), _n_(601265, "Passenger", lambda: Passenger))
  _l_(601267)
  booking_number= _c_(601270, _a_(601269, _n_(601268, "models", lambda: models), "CharField"), max_length= 100,default=0, blank= True)
  _l_(601271)
  booking_time = _c_(601274, _a_(601273, _n_(601272, "models", lambda: models), "DateTimeField"), auto_now_add=True)
  _l_(601275)
  no_of_passengers= _c_(601278, _a_(601277, _n_(601276, "models", lambda: models), "IntegerField"), default=0, blank= True)
  _l_(601279)

  def __str__(self):
    _l_(601283)

    aux = _a_(601281, _n_(601280, "self", lambda: self), "booking_number")
    _l_(601282)
    return aux