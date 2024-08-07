#Source: https://stackoverflow.com/questions/68146918/opts-self-remote-field-model-meta-attributeerror-str-object-has-no-attr
from django.db import models

# Create your models here.
#New
from django.urls import reverse
from django_countries.fields import CountryField
from core.models import AbstractTimeStamp


class AbstractItem(AbstractTimeStamp):
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

    name = models.CharField(max_length=80, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Model

    Inherit:
        AbstractItem
    """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    """Amenity Model

    Inherit:
        AbstractItem
    """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Model

    Inherit:
        AbstractItem
    """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """HouseRule Model

    Inherit:
        AbstractItem
    """

    class Meta:
        verbose_name = "House Rule"


class Photo(AbstractTimeStamp):
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

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(AbstractTimeStamp):
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

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()

        if len(all_reviews) == 0:
            return 0

        all_ratings = 0

        for review in all_reviews:
            all_ratings += review.rating_average()

        return round(all_ratings / len(all_reviews), 2)

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except Exception:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos