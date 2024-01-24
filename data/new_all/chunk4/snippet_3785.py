# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68146918/opts-self-remote-field-model-meta-attributeerror-str-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(644116)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(644118)

except ImportError:
    pass
try:
    from django.utils.html import mark_safe
    _l_(644120)

except ImportError:
    pass
try:
    from .models import Room, RoomType, Amenity, Facility, HouseRule, Photo
    _l_(644122)

except ImportError:
    pass


@_c_(644129, _a_(644124, _n_(644123, "admin", lambda: admin), "register"), _n_(644125, "RoomType", lambda: RoomType), _n_(644126, "Amenity", lambda: Amenity), _n_(644127, "Facility", lambda: Facility), _n_(644128, "HouseRule", lambda: HouseRule))
class ItemAdmin(_a_(644131, _n_(644130, "admin", lambda: admin), "ModelAdmin")):
    _l_(644139)

    """Register model classes inherited from the AbstractItem model"""

    list_display = ("name", "used_by")
    _l_(644132)

    def used_by(self, obj):
        _l_(644138)

        aux = _c_(644136, _a_(644135, _a_(644134, _n_(644133, "obj", lambda: obj), "rooms"), "count"))
        _l_(644137)
        return aux


@_c_(644143, _a_(644141, _n_(644140, "admin", lambda: admin), "register"), _n_(644142, "Photo", lambda: Photo))
class PhotoAdmin(_a_(644145, _n_(644144, "admin", lambda: admin), "ModelAdmin")):
    _l_(644155)

    """Register Photo model at admin panel"""

    list_display = ("__str__", "get_thumbnail")
    _l_(644146)

    def get_thumbnail(self, obj):
        _l_(644153)

        aux = _c_(644151, _n_(644147, "mark_safe", lambda: mark_safe), f'<img width="50px" src="{_a_(644150, _a_(644149, _n_(644148, "obj", lambda: obj), "file"), "url")}" />')
        _l_(644152)
        return aux

    get_thumbnail.short_description = "Thumbnail"
    _l_(644154)


class PhotoInlineAdmin(_a_(644157, _n_(644156, 'admin', lambda: admin), 'TabularInline')):
    _l_(644160)

    """Photo model's inline admin"""

    model = _n_(644158, 'Photo', lambda: Photo)
    _l_(644159)


@_c_(644164, _a_(644162, _n_(644161, 'admin', lambda: admin), 'register'), _n_(644163, 'Room', lambda: Room))
class RoomAdmin(_a_(644166, _n_(644165, 'admin', lambda: admin), 'ModelAdmin')):
    _l_(644188)

    """Register Room model at admin panel

    Filter by:
        instant_book      : BooleanField
        host.is_superhost : BooleanField
        city              : CharField
        room_type         : RoomType Model
        amenities         : Amenity Model
        facilities        : Facility Model
        house_rules       : HouseRule Model
        country           : CharField

    Search by:
        city              : exact
        host.username     : startwith

    Admin function :
        count_amenities   : return amenities count
        count_facilities  : return facilities count
        count_house_rules : return house_rules count
    """

    inlines = (_n_(644167, 'PhotoInlineAdmin', lambda: PhotoInlineAdmin),)
    _l_(644168)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )
    _l_(644169)

    raw_id_fields = ("host",)
    _l_(644170)

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    _l_(644171)
    list_filter = (
        "instant_book",
        "host__is_superhost",
        "city",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )
    _l_(644172)
    filter_horizontal = ("amenities", "facilities", "house_rules")
    _l_(644173)
    search_fields = ("=city", "^host__username")
    _l_(644174)

    def count_amenities(self, obj):
        _l_(644180)

        aux = _c_(644178, _a_(644177, _a_(644176, _n_(644175, 'obj', lambda: obj), 'amenities'), 'count'))
        _l_(644179)
        return aux

    def count_photos(self, obj):
        _l_(644186)

        aux = _c_(644184, _a_(644183, _a_(644182, _n_(644181, 'obj', lambda: obj), 'photos'), 'count'))
        _l_(644185)
        return aux

    count_photos.short_description = "Photo Count"
    _l_(644187)