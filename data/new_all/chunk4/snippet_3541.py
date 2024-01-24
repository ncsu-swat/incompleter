# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#views.py



from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from django.shortcuts import render
  _l_(635511)

except ImportError:
  pass
try:
  from django.http import Http404, JsonResponse
  _l_(635513)

except ImportError:
  pass
try:
  from rest_framework.views import APIView
  _l_(635515)

except ImportError:
  pass
try:
  from rest_framework.response import Response
  _l_(635517)

except ImportError:
  pass
try:
  from django.contrib.auth import authenticate
  _l_(635519)

except ImportError:
  pass
try:
  from rest_framework_simplejwt.tokens import RefreshToken
  _l_(635521)

except ImportError:
  pass
try:
  from rest_framework.authentication import TokenAuthentication
  _l_(635523)

except ImportError:
  pass
try:
  from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAuthenticatedOrReadOnly,IsAuthenticated, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
  _l_(635525)

except ImportError:
  pass
try:
  from myapp.renderers import UserRenderer
  _l_(635527)

except ImportError:
  pass
try:
  from rest_framework import status
  _l_(635529)

except ImportError:
  pass
try:
  from rest_framework import permissions
  _l_(635531)

except ImportError:
  pass
try:
  from rest_framework import generics
  _l_(635533)

except ImportError:
  pass
try:
  from myapp.models import Airport, Flight, User, Passenger, Booking
  _l_(635535)

except ImportError:
  pass
try:
  from myapp.serializers import *
  _l_(635537)

except ImportError:
  pass
try:
  from myapp.permissions import IsOwnerOrAdmin
  _l_(635539)

except ImportError:
  pass
try:
  from rest_framework import viewsets
  _l_(635541)

except ImportError:
  pass



def get_tokens_for_user(user):
  _l_(635555)

  refresh = _c_(635545, _a_(635543, _n_(635542, "RefreshToken", lambda: RefreshToken), "for_user"), _n_(635544, "user", lambda: user))
  _l_(635546)
  aux = {
      'refresh': _c_(635549, _n_(635547, "str", lambda: str), _n_(635548, "refresh", lambda: refresh)),
      'access': _c_(635553, _n_(635550, "str", lambda: str), _a_(635552, _n_(635551, "refresh", lambda: refresh), "access_token")),
  }
  _l_(635554)
  return aux



# Create your views here.

class UserRegistrationView(_n_(635556, "APIView", lambda: APIView)):
  _l_(635583)

  renderer_classes = [_n_(635557, "UserRenderer", lambda: UserRenderer)]
  _l_(635558)
  def post(self, request, format=None):
    _l_(635582)

    serializer = _c_(635562, _n_(635559, "UserRegistrationSerializer", lambda: UserRegistrationSerializer), data=_a_(635561, _n_(635560, "request", lambda: request), "data"))
    _l_(635563)
    _c_(635566, _a_(635565, _n_(635564, "serializer", lambda: serializer), "is_valid"), raise_exception=True)
    _l_(635567)
    user = _c_(635570, _a_(635569, _n_(635568, "serializer", lambda: serializer), "save"))
    _l_(635571)
    token = _c_(635574, _n_(635572, "get_tokens_for_user", lambda: get_tokens_for_user), _n_(635573, "user", lambda: user))
    _l_(635575)
    aux = _c_(635580, _n_(635576, "Response", lambda: Response), {'token':_n_(635577, "token", lambda: token), 'msg':'Registration Successful'}, status=_a_(635579, _n_(635578, "status", lambda: status), "HTTP_201_CREATED"))
    _l_(635581)
    return aux

class UserLoginView(_n_(635584, "APIView", lambda: APIView)):
  _l_(635629)

  renderer_classes = [_n_(635585, "UserRenderer", lambda: UserRenderer)]
  _l_(635586)
  def post(self, request, format=None):
    _l_(635628)

    serializer = _c_(635590, _n_(635587, "UserLoginSerializer", lambda: UserLoginSerializer), data=_a_(635589, _n_(635588, "request", lambda: request), "data"))
    _l_(635591)
    _c_(635594, _a_(635593, _n_(635592, "serializer", lambda: serializer), "is_valid"), raise_exception=True)
    _l_(635595)
    email = _c_(635599, _a_(635598, _a_(635597, _n_(635596, "serializer", lambda: serializer), "data"), "get"), 'email')
    _l_(635600)
    password = _c_(635604, _a_(635603, _a_(635602, _n_(635601, "serializer", lambda: serializer), "data"), "get"), 'password')
    _l_(635605)
    user = _c_(635609, _n_(635606, "authenticate", lambda: authenticate), email=_n_(635607, "email", lambda: email), password=_n_(635608, "password", lambda: password))
    _l_(635610)
    if _n_(635611, "user", lambda: user) is not None:
      _l_(635627)

      token = _c_(635614, _n_(635612, "get_tokens_for_user", lambda: get_tokens_for_user), _n_(635613, "user", lambda: user))
      _l_(635615)
      aux = _c_(635620, _n_(635616, "Response", lambda: Response), {'token':_n_(635617, "token", lambda: token), 'msg':'Login Success'}, status=_a_(635619, _n_(635618, "status", lambda: status), "HTTP_200_OK"))
      _l_(635621)
      return aux
    else:
      aux = _c_(635625, _n_(635622, "Response", lambda: Response), {'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=_a_(635624, _n_(635623, "status", lambda: status), "HTTP_404_NOT_FOUND"))
      _l_(635626)
      return aux


class UserProfileView(_n_(635630, "APIView", lambda: APIView)):
  _l_(635648)

  renderer_classes = [_n_(635631, "UserRenderer", lambda: UserRenderer)]
  _l_(635632)
  permission_classes = [_n_(635633, "IsAuthenticated", lambda: IsAuthenticated)]
  _l_(635634)
  def get(self, request, format=None):
    _l_(635647)

    serializer = _c_(635638, _n_(635635, "UserSerializer", lambda: UserSerializer), _a_(635637, _n_(635636, "request", lambda: request), "user"))
    _l_(635639)
    aux = _c_(635645, _n_(635640, "Response", lambda: Response), _a_(635642, _n_(635641, "serializer", lambda: serializer), "data"), status=_a_(635644, _n_(635643, "status", lambda: status), "HTTP_200_OK"))
    _l_(635646)
    return aux


class UserListCreateAPIView(_a_(635650, _n_(635649, "generics", lambda: generics), "ListCreateAPIView")):
  _l_(635659)

  permission_classes = [_n_(635651, "IsAdminUser", lambda: IsAdminUser)]
  _l_(635652)
  queryset = _c_(635656, _a_(635655, _a_(635654, _n_(635653, "User", lambda: User), "objects"), "all"))
  _l_(635657)
  serializer_class = UserSerializer
  _l_(635658)

class UserRetrtieveUpdateDestroyAPIView(_a_(635661, _n_(635660, "generics", lambda: generics), "RetrieveUpdateDestroyAPIView")):
  _l_(635668)

  
  queryset = _c_(635665, _a_(635664, _a_(635663, _n_(635662, "User", lambda: User), "objects"), "all"))
  _l_(635666)
  serializer_class = UserSerializer
  _l_(635667)








class FlightListCreateAPIView(_a_(635670, _n_(635669, "generics", lambda: generics), "ListCreateAPIView")):
  _l_(635679)

  
  queryset = _c_(635674, _a_(635673, _a_(635672, _n_(635671, "Flight", lambda: Flight), "objects"), "all"))
  _l_(635675)
  serializer_class = FlightSerializer
  _l_(635676)
  
  permission_classes= [_n_(635677, "DjangoModelPermissions", lambda: DjangoModelPermissions)]
  _l_(635678)


class FlightRetrtieveUpdateDestroyAPIView(_a_(635681, _n_(635680, "generics", lambda: generics), "RetrieveUpdateDestroyAPIView")):
  _l_(635688)

  
  queryset = _c_(635685, _a_(635684, _a_(635683, _n_(635682, "Flight", lambda: Flight), "objects"), "all"))
  _l_(635686)
  serializer_class = FlightSerializer
  _l_(635687)

class AirportListCreateAPIView(_a_(635690, _n_(635689, "generics", lambda: generics), "ListCreateAPIView")):
  _l_(635697)

  queryset = _c_(635694, _a_(635693, _a_(635692, _n_(635691, "Airport", lambda: Airport), "objects"), "all"))
  _l_(635695)
  serializer_class = AirportSerializer
  _l_(635696)

class AirportRetrtieveUpdateDestroyAPIView(_a_(635699, _n_(635698, "generics", lambda: generics), "RetrieveUpdateDestroyAPIView")):
  _l_(635706)

  
  queryset = _c_(635703, _a_(635702, _a_(635701, _n_(635700, "Airport", lambda: Airport), "objects"), "all"))
  _l_(635704)
  serializer_class = AirportSerializer
  _l_(635705)





class PassengerListCreateAPIView(_a_(635708, _n_(635707, "generics", lambda: generics), "ListCreateAPIView")):
  _l_(635715)

  queryset = _c_(635712, _a_(635711, _a_(635710, _n_(635709, "Passenger", lambda: Passenger), "objects"), "all"))
  _l_(635713)
  serializer_class = PassengerSerializer
  _l_(635714)

class PassengerRetrtieveUpdateDestroyAPIView(_a_(635717, _n_(635716, "generics", lambda: generics), "RetrieveUpdateDestroyAPIView")):
  _l_(635724)

  queryset = _c_(635721, _a_(635720, _a_(635719, _n_(635718, "Passenger", lambda: Passenger), "objects"), "all"))
  _l_(635722)
  serializer_class = PassengerSerializer
  _l_(635723)



class BookingRetrtieveUpdateDestroyAPIView(_a_(635726, _n_(635725, "generics", lambda: generics), "RetrieveUpdateDestroyAPIView")):
  _l_(635733)

  queryset = _c_(635730, _a_(635729, _a_(635728, _n_(635727, "Booking", lambda: Booking), "objects"), "all"))
  _l_(635731)
  serializer_class = BookingSerializer
  _l_(635732)



class BookViewSet(_a_(635735, _n_(635734, "viewsets", lambda: viewsets), "ModelViewSet")):
  _l_(635826)

  
  # queryset = Book.objects.all()
  serializer_class = BookingSerializer
  _l_(635736)
  # print(serializer_class)
  def get_queryset(self):
    _l_(635744)

    book = _c_(635740, _a_(635739, _a_(635738, _n_(635737, "Booking", lambda: Booking), "objects"), "all"))
    _l_(635741)
    aux = _n_(635742, "book", lambda: book) 
    _l_(635743) 
    return aux 

  def create(self, request, *args, **kwargs):
    _l_(635825)

    data = _a_(635746, _n_(635745, "request", lambda: request), "data")
    _l_(635747)

    user = _c_(635752, _a_(635750, _a_(635749, _n_(635748, "User", lambda: User), "objects"), "get"), id=_n_(635751, "data", lambda: data)["user"])
    _l_(635753)
    flightdetails = _c_(635758, _a_(635756, _a_(635755, _n_(635754, "Flight", lambda: Flight), "objects"), "get"), id=_n_(635757, "data", lambda: data)["flights"])
    _l_(635759)
    # bookingdetails = Booking.objects.get(no_of_passengers=data["no_of_passengers"])

    
    new_book = _c_(635767, _a_(635762, _a_(635761, _n_(635760, "Booking", lambda: Booking), "objects"), "create"), booking_number= _n_(635763, "data", lambda: data)["booking_number"],
        no_of_passengers= _n_(635764, "data", lambda: data)["no_of_passengers"],
        user=_n_(635765, "user", lambda: user),
        flights=_n_(635766, "flightdetails", lambda: flightdetails),
    )
    _l_(635768)
    _c_(635771, _a_(635770, _n_(635769, "new_book", lambda: new_book), "save"))
    _l_(635772)
    for passenger in _n_(635773, "data", lambda: data)["passenger"]:
      _l_(635824)

      passenger_book= _c_(635783, _a_(635776, _a_(635775, _n_(635774, "Passenger", lambda: Passenger), "objects"), "create"), user = _n_(635777, "user", lambda: user),
          name= _n_(635778, "passenger", lambda: passenger)["name"],
          contact_number = _n_(635779, "passenger", lambda: passenger)["contact_number"],
          email = _n_(635780, "passenger", lambda: passenger)["email"],
          gender = _n_(635781, "passenger", lambda: passenger)["gender"],
          age = _n_(635782, "passenger", lambda: passenger)["age"]

      )
      _l_(635784)
      _c_(635789, _a_(635787, _a_(635786, _n_(635785, "new_book", lambda: new_book), "passenger"), "add"), _n_(635788, "passenger_book", lambda: passenger_book))
      _l_(635790)

      if _a_(635792, _n_(635791, "flightdetails", lambda: flightdetails), "available_seats") < _c_(635795, _n_(635793, "len", lambda: len), _n_(635794, "data", lambda: data)["passenger"]):
        _l_(635801)

        aux = _c_(635799, _n_(635796, "Response", lambda: Response), {"data": "No seats available", "status": _a_(635798, _n_(635797, "status", lambda: status), "HTTP_400_BAD_REQUEST")})
        _l_(635800)
        return aux
      update_seats = _a_(635803, _n_(635802, "flightdetails", lambda: flightdetails), "available_seats") - _n_(635804, "data", lambda: data)["no_of_passengers"]
      _l_(635805)
      _n_(635806, "flightdetails", lambda: flightdetails).available_seats = _n_(635807, "update_seats", lambda: update_seats)
      _l_(635808)
      _c_(635811, _a_(635810, _n_(635809, "flightdetails", lambda: flightdetails), "save"))
      _l_(635812)
      serializers = _c_(635815, _n_(635813, "BookingSerializer", lambda: BookingSerializer), _n_(635814, "new_book", lambda: new_book))
      _l_(635816)
      aux = _c_(635822, _n_(635817, "Response", lambda: Response), {"data": _a_(635819, _n_(635818, "serializers", lambda: serializers), "data"), "status": _a_(635821, _n_(635820, "status", lambda: status), "HTTP_201_CREATED")})
      _l_(635823)
      return aux