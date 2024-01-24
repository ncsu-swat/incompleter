# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67339396/typeerror-in-string-requires-string-as-left-operand-not-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(352294)

except ImportError:
    pass
try:
    import json
    _l_(352296)

except ImportError:
    pass
try:
    import wikipedia
    _l_(352298)

except ImportError:
    pass
#from datetime import datetime

response = _c_(352301, _a_(352300, _n_(352299, "requests", lambda: requests), "get"), "https://data.nasa.gov/resource/y77d-th95.json")
_l_(352302)
meteorite_page = _c_(352307, _a_(352304, _n_(352303, "json", lambda: json), "loads"), _a_(352306, _n_(352305, "response", lambda: response), "text"))
_l_(352308)

# Helper Functions
def get_meteorites(type = "all"):
    _l_(352321)

    if _n_(352309, "type", lambda: type) == "all":
        _l_(352318)

        names = [_n_(352310, "mtrt", lambda: mtrt)["name"] for mtrt in _n_(352311, "meteorite_page", lambda: meteorite_page)]
        _l_(352312)
    else:
        names = [_n_(352313, "mtrt", lambda: mtrt)["name"] for mtrt in _n_(352314, "meteorite_page", lambda: meteorite_page) if _n_(352315, "type", lambda: type) in _n_(352316, "mtrt", lambda: mtrt)["recclass"]]
        _l_(352317)
        
    aux = _n_(352319, "names", lambda: names)
    _l_(352320)
    return aux

def sort_by_feature(type):
    _l_(352332)

    if _n_(352322, "type", lambda: type) == "year":
        _l_(352329)

        feature = [_n_(352323, "mtrt", lambda: mtrt)["year"] for mtrt in _n_(352324, "meteorite_page", lambda: meteorite_page)]   
        _l_(352325)   
    else:
        feature = [_n_(352326, "mtrt", lambda: mtrt)["mass"] for mtrt in _n_(352327, "meteorite_page", lambda: meteorite_page)]
        _l_(352328)
        
    aux = _n_(352330, "feature", lambda: feature)
    _l_(352331)
    return aux
# Choice functions
def print_all():
    _l_(352350)

    all_names = _c_(352335, _n_(352333, "get_meteorites", lambda: get_meteorites), _n_(352334, "type", lambda: type))
    _l_(352336)
    for index, name in _c_(352339, _n_(352337, "enumerate", lambda: enumerate), _n_(352338, "all_names", lambda: all_names)):
        _l_(352345)

        _c_(352343, _n_(352340, "print", lambda: print), f"{_n_(352341, 'index', lambda: index) + 1}: {_n_(352342, 'name', lambda: name)}")
        _l_(352344)
    _c_(352348, _n_(352346, "print", lambda: print), _n_(352347, "all_names", lambda: all_names))
    _l_(352349)
def print_by_class():
    _l_(352373)

    type = _c_(352354, _a_(352353, _c_(352352, _n_(352351, "input", lambda: input), "Enter a class (See this page for classification names/details --> stackoverflow made me take out this link): "), "upper"))
    _l_(352355)
    all_names = _c_(352358, _n_(352356, "get_meteorites", lambda: get_meteorites), _n_(352357, "type", lambda: type))
    _l_(352359)
    _c_(352362, _n_(352360, "print", lambda: print), f"All {_n_(352361, 'type', lambda: type)} meteorites: ")
    _l_(352363)
    for index, name in _c_(352366, _n_(352364, "enumerate", lambda: enumerate), _n_(352365, "all_names", lambda: all_names)):
        _l_(352372)

        _c_(352370, _n_(352367, "print", lambda: print), f"{_n_(352368, 'index', lambda: index) + 1}: {_n_(352369, 'name', lambda: name)}")
        _l_(352371)
def sort_by_year():
    _l_(352390)

    all_years = _c_(352375, _n_(352374, "sort_by_feature", lambda: sort_by_feature), "year")
    _l_(352376)
    for index, year in _c_(352379, _n_(352377, "enumerate", lambda: enumerate), _n_(352378, "all_years", lambda: all_years)):
        _l_(352385)

        _c_(352383, _n_(352380, "print", lambda: print), f"{_n_(352381, 'index', lambda: index) + 1}: {_n_(352382, 'year', lambda: year)}")
        _l_(352384)
    _c_(352388, _n_(352386, "print", lambda: print), _n_(352387, "all_years", lambda: all_years))
    _l_(352389)
def sort_by_mass():
    _l_(352407)

    all_masses = _c_(352392, _n_(352391, "sort_by_feature", lambda: sort_by_feature), "mass")
    _l_(352393)
    for index, mass in _c_(352396, _n_(352394, "enumerate", lambda: enumerate), _n_(352395, "all_masses", lambda: all_masses)):
        _l_(352402)

        _c_(352400, _n_(352397, "print", lambda: print), f"{_n_(352398, 'index', lambda: index) + 1}: {_n_(352399, 'mass', lambda: mass)}")
        _l_(352401)
    _c_(352405, _n_(352403, "print", lambda: print), _n_(352404, "all_masses", lambda: all_masses))
    _l_(352406)
def meteorite_data():
    _l_(352439)

    
    meteorite_name = _c_(352409, _n_(352408, "input", lambda: input), "Enter the name of a meteorite: ")
    _l_(352410)
    
    for mtrt in _n_(352411, "meteorite_page", lambda: meteorite_page):
        _l_(352423)

        if _n_(352412, "meteorite_name", lambda: meteorite_name) in _n_(352413, "mtrt", lambda: mtrt)['name']:
            _l_(352422)

            for key in _n_(352414, "mtrt", lambda: mtrt):
                _l_(352421)

                _c_(352419, _n_(352415, "print", lambda: print), f"{_n_(352416, 'key', lambda: key)}: {_n_(352417, 'mtrt', lambda: mtrt)[_n_(352418, 'key', lambda: key)]}")
                _l_(352420)
    
    _c_(352425, _n_(352424, "print", lambda: print), "Wikipedia Summary: ")
    _l_(352426)
    try:
        _l_(352438)

        _c_(352432, _n_(352427, "print", lambda: print), _c_(352431, _a_(352429, _n_(352428, "wikipedia", lambda: wikipedia), "summary"), f"{_n_(352430, 'meteorite_name', lambda: meteorite_name)} (meteorite)"))
        _l_(352433)
    except:
        _l_(352437)

        _c_(352435, _n_(352434, "print", lambda: print), "No Wikipedia page could be found.")
        _l_(352436)

# User interface
def start_interface():
    _l_(352520)


    _c_(352441, _n_(352440, "print", lambda: print), "Meteorite Data Explorer")
    _l_(352442)
    _c_(352444, _n_(352443, "print", lambda: print), "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    _l_(352445)
   
    while True:
        _l_(352519)

        _c_(352447, _n_(352446, "print", lambda: print), "̲M̲e̲n̲u̲ ̲")
        _l_(352448)
        _c_(352450, _n_(352449, "print", lambda: print), "1. List the names of all Earth meteorite landings")
        _l_(352451)
        _c_(352453, _n_(352452, "print", lambda: print), "2. See all meteorites in one class")
        _l_(352454)
        _c_(352456, _n_(352455, "print", lambda: print), "3. Organize meteorites from oldest to newest")
        _l_(352457)
        _c_(352459, _n_(352458, "print", lambda: print), "4. Organize meteorites from biggest to smallest")
        _l_(352460)
        _c_(352462, _n_(352461, "print", lambda: print), "5. Access the data of an individual meteorite")
        _l_(352463)
        _c_(352465, _n_(352464, "print", lambda: print), "0. Quit")
        _l_(352466)
        choice = _c_(352468, _n_(352467, "input", lambda: input), "Select an option: ")
        _l_(352469)
        
        if _n_(352470, "choice", lambda: choice) == "1":
            _l_(352518)

            _c_(352472, _n_(352471, "print_all", lambda: print_all))
            _l_(352473)
        elif _n_(352474, "choice", lambda: choice) == "2":
            _l_(352517)

            _c_(352476, _n_(352475, "print_by_class", lambda: print_by_class))
            _l_(352477)
            _c_(352479, _n_(352478, "print", lambda: print), '')
            _l_(352480)
        elif _n_(352481, "choice", lambda: choice) == "3":
            _l_(352516)

            _c_(352483, _n_(352482, "sort_by_year", lambda: sort_by_year))
            _l_(352484)
            _c_(352486, _n_(352485, "print", lambda: print), '')
            _l_(352487)
        elif _n_(352488, "choice", lambda: choice) == "4":
            _l_(352515)

            _c_(352490, _n_(352489, "sort_by_mass", lambda: sort_by_mass))
            _l_(352491)
            _c_(352493, _n_(352492, "print", lambda: print), '')
            _l_(352494)
        elif _n_(352495, "choice", lambda: choice) == "5":
            _l_(352514)

            _c_(352497, _n_(352496, "meteorite_data", lambda: meteorite_data))
            _l_(352498)
            _c_(352500, _n_(352499, "print", lambda: print), '')
            _l_(352501)
        elif _n_(352502, "choice", lambda: choice) == "0":
            _l_(352513)

            _c_(352504, _n_(352503, "print", lambda: print), "Exit")
            _l_(352505)
            break
            _l_(352506)
        else:
            _c_(352508, _n_(352507, "print", lambda: print), "That is not an option.")
            _l_(352509)
            _c_(352511, _n_(352510, "print", lambda: print), "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            _l_(352512)

if _n_(352521, "__name__", lambda: __name__) == "__main__":
    _l_(352525)

    _c_(352523, _n_(352522, "start_interface", lambda: start_interface))
    _l_(352524)