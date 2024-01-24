# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#urls.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path, include
    _l_(597033)

except ImportError:
    pass
try:
    from myapp.views import *
    _l_(597035)

except ImportError:
    pass
try:
    from rest_framework import routers
    _l_(597037)

except ImportError:
    pass





router = _c_(597040, _a_(597039, _n_(597038, "routers", lambda: routers), "DefaultRouter"))
_l_(597041)
_c_(597045, _a_(597043, _n_(597042, "router", lambda: router), "register"), 'booking', _n_(597044, "BookViewSet", lambda: BookViewSet), basename='MyModel')
_l_(597046)
urlpatterns = [

    _c_(597051, _n_(597047, "path", lambda: path), 'register/', _c_(597050, _a_(597049, _n_(597048, "UserRegistrationView", lambda: UserRegistrationView), "as_view")), name='register'),
    _c_(597056, _n_(597052, "path", lambda: path), 'login/', _c_(597055, _a_(597054, _n_(597053, "UserLoginView", lambda: UserLoginView), "as_view")), name='login'),
    _c_(597061, _n_(597057, "path", lambda: path), 'profile/', _c_(597060, _a_(597059, _n_(597058, "UserProfileView", lambda: UserProfileView), "as_view")), name='profile'),
    _c_(597066, _n_(597062, "path", lambda: path), 'flight/', _c_(597065, _a_(597064, _n_(597063, "FlightListCreateAPIView", lambda: FlightListCreateAPIView), "as_view"))),
    _c_(597071, _n_(597067, "path", lambda: path), 'flight_info/<int:pk>/', _c_(597070, _a_(597069, _n_(597068, "FlightRetrtieveUpdateDestroyAPIView", lambda: FlightRetrtieveUpdateDestroyAPIView), "as_view"))),
    _c_(597076, _n_(597072, "path", lambda: path), 'customer/', _c_(597075, _a_(597074, _n_(597073, "UserListCreateAPIView", lambda: UserListCreateAPIView), "as_view"))),
    _c_(597081, _n_(597077, "path", lambda: path), 'customer_info/<int:pk>/', _c_(597080, _a_(597079, _n_(597078, "UserRetrtieveUpdateDestroyAPIView", lambda: UserRetrtieveUpdateDestroyAPIView), "as_view"))),
    _c_(597086, _n_(597082, "path", lambda: path), 'passenger/', _c_(597085, _a_(597084, _n_(597083, "PassengerListCreateAPIView", lambda: PassengerListCreateAPIView), "as_view"))),
    _c_(597091, _n_(597087, "path", lambda: path), 'passenger_info/<int:pk>/', _c_(597090, _a_(597089, _n_(597088, "PassengerRetrtieveUpdateDestroyAPIView", lambda: PassengerRetrtieveUpdateDestroyAPIView), "as_view"))),
    
    _c_(597096, _n_(597092, "path", lambda: path), 'booking_info/<int:pk>/', _c_(597095, _a_(597094, _n_(597093, "BookingRetrtieveUpdateDestroyAPIView", lambda: BookingRetrtieveUpdateDestroyAPIView), "as_view"))),
    #path('booking/', BookingAPIView.as_view()),
    _c_(597102, _n_(597097, "path", lambda: path), '', _c_(597101, _n_(597098, "include", lambda: include), _a_(597100, _n_(597099, "router", lambda: router), "urls"))),
    

    
    
    
]
_l_(597103)