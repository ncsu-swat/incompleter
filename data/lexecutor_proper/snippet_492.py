# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12578908/separation-of-business-logic-and-data-access-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Book:
   _l_(63285)

   author = _c_(63278, _a_(63277, models, "ForeignKey"), User)
   _l_(63279)
   title = _c_(63281, _a_(63280, models, "CharField"), max_length=125)
   _l_(63282)

   class Meta:
      _l_(63284)

      app_label = "library"
      _l_(63283)
try:
   from library.models import Book
   _l_(63287)

except ImportError:
   pass

def get_books(limit=None, **filters):
   _l_(63295)

   """ simple service function for retrieving books can be widely extended """
   aux = _c_(63292, _a_(63290, _a_(63289, _n_(63288, "Book", lambda: Book), "objects"), "filter"), **_n_(63291, "filters", lambda: filters))[:_n_(63293, "limit", lambda: limit)]  # list[:None] will return the entire list
   _l_(63294)  # list[:None] will return the entire list
   return aux  # list[:None] will return the entire list
try:
   from library.services import get_books
   _l_(63297)

except ImportError:
   pass

class BookListView(_n_(63298, "ListView", lambda: ListView)):
   _l_(63302)

   """ simple view, e.g. implement a _build and _apply filters function """
   queryset = _c_(63300, _n_(63299, "get_books", lambda: get_books))
   _l_(63301)

