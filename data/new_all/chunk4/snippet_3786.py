# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68146918/opts-self-remote-field-model-meta-attributeerror-str-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(585635)

except ImportError:
    pass
try:
    from django.urls import reverse
    _l_(585637)

except ImportError:
    pass
try:
    from django_countries.fields import CountryField
    _l_(585639)

except ImportError:
    pass
try:
    from core.models import AbstractTimeStamp
    _l_(585641)

except ImportError:
    pass


class AbstractItem(_n_(585642, "AbstractTimeStamp", lambda: AbstractTimeStamp)):
    _l_(585653)

    """Abstract Item Model

    Inherit:
        AbstractTimeStamp

    Fields:
        name       : CharField
        created_at : DateTimeField
        updated_at : DateTimeField

    Method:
        __str__ : return name
    """

    name = _c_(585645, _a_(585644, _n_(585643, "models", lambda: models), "CharField"), max_length=80, unique=True)
    _l_(585646)

    class Meta:
        _l_(585648)

        abstract = True
        _l_(585647)

    def __str__(self):
        _l_(585652)

        aux = _a_(585650, _n_(585649, "self", lambda: self), "name")
        _l_(585651)
        return aux


class RoomType(_n_(585654, "AbstractItem", lambda: AbstractItem)):
    _l_(585657)

    """RoomType Model

    Inherit:
        AbstractItem
    """

    class Meta:
        _l_(585656)

        verbose_name = "Room Type"
        _l_(585655)


class Amenity(_n_(585658, "AbstractItem", lambda: AbstractItem)):
    _l_(585661)

    """Amenity Model

    Inherit:
        AbstractItem
    """

    class Meta:
        _l_(585660)

        verbose_name_plural = "Amenities"
        _l_(585659)


class Facility(_n_(585662, "AbstractItem", lambda: AbstractItem)):
    _l_(585665)

    """Facility Model

    Inherit:
        AbstractItem
    """

    class Meta:
        _l_(585664)

        verbose_name_plural = "Facilities"
        _l_(585663)


class HouseRule(_n_(585666, "AbstractItem", lambda: AbstractItem)):
    _l_(585669)

    """HouseRule Model

    Inherit:
        AbstractItem
    """

    class Meta:
        _l_(585668)

        verbose_name = "House Rule"
        _l_(585667)


class Photo(_n_(585670, "AbstractTimeStamp", lambda: AbstractTimeStamp)):
    _l_(585689)

    """Photo Model

    Inherit:
        AbstractTimeStamp

    Fields:
        caption    : CharField
        file       : ImageField
        room       : Room Model (1:N)
        created_at : DateTimeField
        updated_at : DateTimeField

    Method:
        __str__ : return caption
    """

    caption = _c_(585673, _a_(585672, _n_(585671, "models", lambda: models), "CharField"), max_length=80)
    _l_(585674)
    file = _c_(585677, _a_(585676, _n_(585675, "models", lambda: models), "ImageField"), upload_to="room_photos")
    _l_(585678)
    room = _c_(585683, _a_(585680, _n_(585679, "models", lambda: models), "ForeignKey"), "Room", related_name="photos", on_delete=_a_(585682, _n_(585681, "models", lambda: models), "CASCADE"))
    _l_(585684)

    def __str__(self):
        _l_(585688)

        aux = _a_(585686, _n_(585685, "self", lambda: self), "caption")
        _l_(585687)
        return aux


class Room(_n_(585690, "AbstractTimeStamp", lambda: AbstractTimeStamp)):
    _l_(585837)

    """Room Model

    Inherit:
        AbstractTimeStamp

    Fields:
        name         : CharField
        description  : TextField
        country      : CountryField
        city         : CharField
        price        : IntegerField
        address      : CharField
        guests       : IntegerField
        beds         : IntegerField
        bedrooms     : IntegerField
        baths        : IntegerField
        check_in     : TimeField
        check_out    : TimeField
        instant_book : BooleanField
        host         : users app User model (1:N)
        room_type    : RoomType model (1:N)
        amenities    : Amenity model (N:N)
        facilities   : Facility model (N:N)
        house_rules  : HouseRule model(N:N)
        created_at   : DateTimeField
        updated_at   : DateTimeField

    Method:
        __str__      : return name
        save         : change capitalized city name and save
        total_rating : return all reviews rating avg
        first_photo  : return room's first photo file url
    """

    name = _c_(585693, _a_(585692, _n_(585691, "models", lambda: models), "CharField"), max_length=140)
    _l_(585694)
    description = _c_(585697, _a_(585696, _n_(585695, "models", lambda: models), "TextField"))
    _l_(585698)
    country = _c_(585700, _n_(585699, "CountryField", lambda: CountryField))
    _l_(585701)
    city = _c_(585704, _a_(585703, _n_(585702, "models", lambda: models), "CharField"), max_length=80)
    _l_(585705)
    price = _c_(585708, _a_(585707, _n_(585706, "models", lambda: models), "IntegerField"))
    _l_(585709)
    address = _c_(585712, _a_(585711, _n_(585710, "models", lambda: models), "CharField"), max_length=140)
    _l_(585713)
    guests = _c_(585716, _a_(585715, _n_(585714, "models", lambda: models), "IntegerField"))
    _l_(585717)
    beds = _c_(585720, _a_(585719, _n_(585718, "models", lambda: models), "IntegerField"))
    _l_(585721)
    bedrooms = _c_(585724, _a_(585723, _n_(585722, "models", lambda: models), "IntegerField"))
    _l_(585725)
    baths = _c_(585728, _a_(585727, _n_(585726, "models", lambda: models), "IntegerField"))
    _l_(585729)
    check_in = _c_(585732, _a_(585731, _n_(585730, "models", lambda: models), "TimeField"))
    _l_(585733)
    check_out = _c_(585736, _a_(585735, _n_(585734, "models", lambda: models), "TimeField"))
    _l_(585737)
    instant_book = _c_(585740, _a_(585739, _n_(585738, "models", lambda: models), "BooleanField"), default=False)
    _l_(585741)
    host = _c_(585746, _a_(585743, _n_(585742, "models", lambda: models), "ForeignKey"), "users.User", related_name="rooms", on_delete=_a_(585745, _n_(585744, "models", lambda: models), "CASCADE")
    )
    _l_(585747)
    room_type = _c_(585752, _a_(585749, _n_(585748, "models", lambda: models), "ForeignKey"), "RoomType", related_name="rooms", on_delete=_a_(585751, _n_(585750, "models", lambda: models), "SET_NULL"), null=True
    )
    _l_(585753)
    amenities = _c_(585756, _a_(585755, _n_(585754, "models", lambda: models), "ManyToManyField"), "Amenity", related_name="rooms", blank=True)
    _l_(585757)
    facilities = _c_(585760, _a_(585759, _n_(585758, "models", lambda: models), "ManyToManyField"), "Facility", related_name="rooms", blank=True)
    _l_(585761)
    house_rules = _c_(585764, _a_(585763, _n_(585762, "models", lambda: models), "ManyToManyField"), "HouseRule", related_name="rooms", blank=True)
    _l_(585765)

    def __str__(self):
        _l_(585769)

        aux = _a_(585767, _n_(585766, "self", lambda: self), "name")
        _l_(585768)
        return aux

    def save(self, *args, **kwargs):
        _l_(585783)

        _n_(585770, "self", lambda: self).city = _c_(585775, _a_(585772, _n_(585771, "str", lambda: str), "capitalize"), _a_(585774, _n_(585773, "self", lambda: self), "city"))
        _l_(585776)
        _c_(585781, _a_(585778, _n_(585777, "super", lambda: super)(), "save"), *_n_(585779, "args", lambda: args), **_n_(585780, "kwargs", lambda: kwargs))
        _l_(585782)

    def get_absolute_url(self):
        _l_(585789)

        aux = _c_(585787, _n_(585784, "reverse", lambda: reverse), "rooms:detail", kwargs={"pk": _a_(585786, _n_(585785, "self", lambda: self), "pk")})
        _l_(585788)
        return aux

    def total_rating(self):
        _l_(585814)

        all_reviews = _c_(585793, _a_(585792, _a_(585791, _n_(585790, "self", lambda: self), "reviews"), "all"))
        _l_(585794)

        if _c_(585797, _n_(585795, "len", lambda: len), _n_(585796, "all_reviews", lambda: all_reviews)) == 0:
            _l_(585799)

            aux = 0
            _l_(585798)
            return aux

        all_ratings = 0
        _l_(585800)

        for review in _n_(585801, "all_reviews", lambda: all_reviews):
            _l_(585806)

            all_ratings += _c_(585804, _a_(585803, _n_(585802, "review", lambda: review), "rating_average"))
            _l_(585805)
        aux = _c_(585812, _n_(585807, "round", lambda: round), _n_(585808, "all_ratings", lambda: all_ratings) / _c_(585811, _n_(585809, "len", lambda: len), _n_(585810, "all_reviews", lambda: all_reviews)), 2)
        _l_(585813)

        return aux

    def first_photo(self):
        _l_(585828)

        try:
            _l_(585827)

            (photo,) = _c_(585818, _a_(585817, _a_(585816, _n_(585815, "self", lambda: self), "photos"), "all"))[:1]
            _l_(585819)
            aux = _a_(585822, _a_(585821, _n_(585820, "photo", lambda: photo), "file"), "url")
            _l_(585823)
            return aux
        except _n_(585824, "Exception", lambda: Exception):
            _l_(585826)

            aux = None
            _l_(585825)
            return aux

    def get_next_four_photos(self):
        _l_(585836)

        photos = _c_(585832, _a_(585831, _a_(585830, _n_(585829, "self", lambda: self), "photos"), "all"))[1:5]
        _l_(585833)
        aux = _n_(585834, "photos", lambda: photos)
        _l_(585835)
        return aux