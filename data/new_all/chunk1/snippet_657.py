# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67064352/my-data-from-script-returns-none-attributeerror-nonetype-object-has-no-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
html_doc = """
    <script>
      var modelData = {
        "hlsUrl": "null",
        "account": "4LH7J44IYPAGEZEY6E3UL"
      }
  </script>
"""
_l_(387573)

soup = _c_(387576, _n_(387574, "BeautifulSoup", lambda: BeautifulSoup), _n_(387575, "html_doc", lambda: html_doc), "html.parser")
_l_(387577)
# locate the script, get the contents
script_text = _a_(387581, _c_(387580, _a_(387579, _n_(387578, "soup", lambda: soup), "select_one"), "script"), "contents")[0]
_l_(387582)

# get javascript object inside the script
model_data = _c_(387588, _a_(387584, _n_(387583, "re", lambda: re), "search"), r"modelData = ({.*?});", _n_(387585, "script_text", lambda: script_text), flags=_a_(387587, _n_(387586, "re", lambda: re), "S"))
_l_(387589)
_c_(387592, _n_(387590, "print", lambda: print), _n_(387591, "model_data", lambda: model_data)) # RETURNS None - why?
_l_(387593) # RETURNS None - why?
model_data = _c_(387596, _a_(387595, _n_(387594, "model_data", lambda: model_data), "group"), 1)
_l_(387597)

# "convert" the javascript object to json-valid object
model_data = _c_(387605, _a_(387599, _n_(387598, "re", lambda: re), "sub"), r"^\s*([^:\s]+):", r'"\1":', _c_(387602, _a_(387601, _n_(387600, "model_data", lambda: model_data), "replace"), "'", '"'), flags=_a_(387604, _n_(387603, "re", lambda: re), "M")
)
_l_(387606)

# json decode the object
model_data = _c_(387610, _a_(387608, _n_(387607, "json", lambda: json), "loads"), _n_(387609, "model_data", lambda: model_data))
_l_(387611)

# print the data
_c_(387614, _n_(387612, "print", lambda: print), _n_(387613, "model_data", lambda: model_data)["account"])
_l_(387615)