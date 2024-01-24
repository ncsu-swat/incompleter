# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73704946/typeerror-type-object-is-not-iterable-drf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from rest_framework import serializers
  _l_(471079)

except ImportError:
  pass
try:
  from .models import Movie, Actor, Reviews
  _l_(471081)

except ImportError:
  pass

class ActorSerializer(_a_(471083, _n_(471082, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(471088)

  class Meta:
    _l_(471087)

    model = _n_(471084, "Actor", lambda: Actor)
    _l_(471085)
    fields = '__all__'
    _l_(471086)

class ReviewsSerializer(_a_(471090, _n_(471089, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(471095)

  class Meta:
    _l_(471094)

    model = _n_(471091, "Reviews", lambda: Reviews)
    _l_(471092)
    fields = '__all__'
    _l_(471093)

class MovieSerializer(_a_(471097, _n_(471096, "serializers", lambda: serializers), "ModelSerializer")):
  _l_(471114)

  actors = _c_(471099, _n_(471098, "ActorSerializer", lambda: ActorSerializer), many=True)
  _l_(471100)
  average_reviews = _c_(471103, _a_(471102, _n_(471101, "serializers", lambda: serializers), "SerializerMethodField"))
  _l_(471104)
  def get_average_reviews(self,obj):
    _l_(471109)

    aux = _c_(471107, _a_(471106, _n_(471105, "obj", lambda: obj), "average_reviews"))
    _l_(471108)
    return aux
  class Meta:
    _l_(471113)

    model = _n_(471110, "Movie", lambda: Movie)
    _l_(471111)
    fields = '__all__'
    _l_(471112)