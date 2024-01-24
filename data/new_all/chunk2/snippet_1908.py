# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39101535/typeerror-unorderable-types-nonetype-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import urllib.request
  _l_(438852)

except ImportError:
  pass
try:
  import json
  _l_(438854)

except ImportError:
  pass

def printResults(data):
  _l_(438900)

  # Use the json module to load the string data into a dictionary
  theJSON = _c_(438860, _a_(438856, _n_(438855, "json", lambda: json), "loads"), _c_(438859, _a_(438858, _n_(438857, "data", lambda: data), "decode")))
  _l_(438861)

  # now we can access the contents of the JSON like any other Python object
  if "title" in _n_(438862, "theJSON", lambda: theJSON)["metadata"]:
    _l_(438867)

    _c_(438865, _n_(438863, "print", lambda: print), _n_(438864, "theJSON", lambda: theJSON)["metadata"]["title"])
    _l_(438866)

  # output the number of events, plus the magnitude and each event name  
  count = _n_(438868, "theJSON", lambda: theJSON)["metadata"]["count"];
  _l_(438869)
  _c_(438874, _n_(438870, "print", lambda: print), _c_(438873, _n_(438871, "str", lambda: str), _n_(438872, "count", lambda: count)) + " events recorded")
  _l_(438875)

  # for each event, print the place where it occurred
  for i in _n_(438876, "theJSON", lambda: theJSON)["features"]:
    _l_(438881)

    _c_(438879, _n_(438877, "print", lambda: print), _n_(438878, "i", lambda: i)["properties"]["place"])
    _l_(438880)

  # print only the events where at least 1 person reported feeling something
  _c_(438883, _n_(438882, "print", lambda: print), "Events that were felt:")
  _l_(438884)
  for i in _n_(438885, "theJSON", lambda: theJSON)["features"]:
    _l_(438899)

    feltReports = _n_(438886, "i", lambda: i)["properties"]["felt"]
    _l_(438887)
    if (_n_(438888, "feltReports", lambda: feltReports) != None) & (_n_(438889, "feltReports", lambda: feltReports) > 0):
      _l_(438898)

      _c_(438896, _n_(438890, "print", lambda: print), "%2.1f" % _n_(438891, "i", lambda: i)["properties"]["mag"], _n_(438892, "i", lambda: i)["properties"]["place"], " reported " + _c_(438895, _n_(438893, "str", lambda: str), _n_(438894, "feltReports", lambda: feltReports)) + " times")
      _l_(438897)


def main():
  _l_(438933)

  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
  _l_(438901)

  # Open the URL and read the data
  webUrl = _c_(438905, _a_(438903, _a_(438902, urllib, "request"), "urlopen"), _n_(438904, "urlData", lambda: urlData))
  _l_(438906)
  _c_(438911, _n_(438907, "print", lambda: print), _c_(438910, _a_(438909, _n_(438908, "webUrl", lambda: webUrl), "getcode")))
  _l_(438912)
  if (_c_(438915, _a_(438914, _n_(438913, "webUrl", lambda: webUrl), "getcode")) == 200):
    _l_(438932)

    data = _c_(438918, _a_(438917, _n_(438916, "webUrl", lambda: webUrl), "read"))
    _l_(438919)
    # print out our customized results
    _c_(438922, _n_(438920, "printResults", lambda: printResults), _n_(438921, "data", lambda: data))
    _l_(438923)
  else:
    _c_(438930, _n_(438924, "print", lambda: print), "Received an error from server, cannot retrieve results " + _c_(438929, _n_(438925, "str", lambda: str), _c_(438928, _a_(438927, _n_(438926, "webUrl", lambda: webUrl), "getcode"))))
    _l_(438931)

if _n_(438934, "__name__", lambda: __name__) == "__main__":
  _l_(438938)

  _c_(438936, _n_(438935, "main", lambda: main))
  _l_(438937)