# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57446324/pinoroenviro-typeerror-argument-should-be-integer-or-bytes-like-object-not-s
#!/usr/bin/env python

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(404921)

except ImportError:
    pass
try:
    import colorsys
    _l_(404923)

except ImportError:
    pass
try:
    import os
    _l_(404925)

except ImportError:
    pass
try:
    import sys
    _l_(404927)

except ImportError:
    pass
try:
    import ST7735
    _l_(404929)

except ImportError:
    pass
try:
    import ltr559
    _l_(404931)

except ImportError:
    pass
try:
    from bme280 import BME280
    _l_(404933)

except ImportError:
    pass
try:
    from pms5003 import PMS5003
    _l_(404935)

except ImportError:
    pass
try:
    from enviroplus import gas
    _l_(404937)

except ImportError:
    pass
try:
    from subprocess import PIPE, Popen
    _l_(404939)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(404941)

except ImportError:
    pass
try:
    from PIL import ImageDraw
    _l_(404943)

except ImportError:
    pass
try:
    from PIL import ImageFont
    _l_(404945)

except ImportError:
    pass

_c_(404947, _n_(404946, "print", lambda: print), """all-in-one.py - Displays readings from all of Enviro plus' sensors

Press Ctrl+C to exit!

""")
_l_(404948)

# BME280 temperature/pressure/humidity sensor
bme280 = _c_(404950, _n_(404949, "BME280", lambda: BME280))
_l_(404951)

# PMS5003 particulate sensor
pms5003 = _c_(404953, _n_(404952, "PMS5003", lambda: PMS5003))
_l_(404954)

# Create ST7735 LCD display class
st7735 = _c_(404957, _a_(404956, _n_(404955, "ST7735", lambda: ST7735), "ST7735"), port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)
_l_(404958)

# Initialize display
_c_(404961, _a_(404960, _n_(404959, "st7735", lambda: st7735), "begin"))
_l_(404962)

WIDTH = _a_(404964, _n_(404963, "st7735", lambda: st7735), "width")
_l_(404965)
HEIGHT = _a_(404967, _n_(404966, "st7735", lambda: st7735), "height")
_l_(404968)

# Set up canvas and font
img = _c_(404973, _a_(404970, _n_(404969, "Image", lambda: Image), "new"), 'RGB', (_n_(404971, "WIDTH", lambda: WIDTH), _n_(404972, "HEIGHT", lambda: HEIGHT)), color=(0, 0, 0))
_l_(404974)
draw = _c_(404978, _a_(404976, _n_(404975, "ImageDraw", lambda: ImageDraw), "Draw"), _n_(404977, "img", lambda: img))
_l_(404979)
path = _c_(404988, _a_(404982, _a_(404981, _n_(404980, "os", lambda: os), "path"), "dirname"), _c_(404987, _a_(404985, _a_(404984, _n_(404983, "os", lambda: os), "path"), "realpath"), _n_(404986, "__file__", lambda: __file__)))
_l_(404989)
font = _c_(404993, _a_(404991, _n_(404990, "ImageFont", lambda: ImageFont), "truetype"), _n_(404992, "path", lambda: path) + "/fonts/Asap/Asap-Bold.ttf", 20)
_l_(404994)

message = ""
_l_(404995)

# The position of the top bar
top_pos = 25
_l_(404996)


# Displays data and text on the 0.96" LCD
def display_text(variable, data, unit):
    _l_(405090)

    # Maintain length of list
    _n_(404997, "values", lambda: values)[_n_(404998, "variable", lambda: variable)] = _n_(404999, "values", lambda: values)[_n_(405000, "variable", lambda: variable)][1:] + [_n_(405001, "data", lambda: data)]
    _l_(405002)
    # Scale the values for the variable between 0 and 1
    colours = [(_n_(405003, "v", lambda: v) - _c_(405007, _n_(405004, "min", lambda: min), _n_(405005, "values", lambda: values)[_n_(405006, "variable", lambda: variable)]) + 1) / (_c_(405011, _n_(405008, "max", lambda: max), _n_(405009, "values", lambda: values)[_n_(405010, "variable", lambda: variable)])
               - _c_(405015, _n_(405012, "min", lambda: min), _n_(405013, "values", lambda: values)[_n_(405014, "variable", lambda: variable)]) + 1) for v in _n_(405016, "values", lambda: values)[_n_(405017, "variable", lambda: variable)]]
    _l_(405018)
    # Format the variable name and value
    message = _c_(405023, _a_(405019, "{}: {:.1f} {}", "format"), _n_(405020, "variable", lambda: variable)[:4], _n_(405021, "data", lambda: data), _n_(405022, "unit", lambda: unit))
    _l_(405024)
    _c_(405027, _n_(405025, "print", lambda: print), _n_(405026, "message", lambda: message))
    _l_(405028)
    _c_(405033, _a_(405030, _n_(405029, "draw", lambda: draw), "rectangle"), (0, 0, _n_(405031, "WIDTH", lambda: WIDTH), _n_(405032, "HEIGHT", lambda: HEIGHT)), (255, 255, 255))
    _l_(405034)
    for i in _c_(405039, _n_(405035, "range", lambda: range), _c_(405038, _n_(405036, "len", lambda: len), _n_(405037, "colours", lambda: colours))):
        _l_(405078)

        # Convert the values to colours from red to blue
        colour = (1.0 - _n_(405040, "colours", lambda: colours)[_n_(405041, "i", lambda: i)]) * 0.6
        _l_(405042)
        r, g, b = [_c_(405045, _n_(405043, "int", lambda: int), _n_(405044, "x", lambda: x) * 255.0) for x in _c_(405049, _a_(405047, _n_(405046, "colorsys", lambda: colorsys), "hsv_to_rgb"), _n_(405048, "colour", lambda: colour),
                   1.0, 1.0)]
        _l_(405050)
        # Draw a 1-pixel wide rectangle of colour
        _c_(405060, _a_(405052, _n_(405051, "draw", lambda: draw), "rectangle"), (_n_(405053, "i", lambda: i), _n_(405054, "top_pos", lambda: top_pos), _n_(405055, "i", lambda: i)+1, _n_(405056, "HEIGHT", lambda: HEIGHT)), (_n_(405057, "r", lambda: r), _n_(405058, "g", lambda: g), _n_(405059, "b", lambda: b)))
        _l_(405061)
        # Draw a line graph in black
        line_y = _n_(405062, "HEIGHT", lambda: HEIGHT) - (_n_(405063, "top_pos", lambda: top_pos) + (_n_(405064, "colours", lambda: colours)[_n_(405065, "i", lambda: i)] * (_n_(405066, "HEIGHT", lambda: HEIGHT) - _n_(405067, "top_pos", lambda: top_pos))))\
                 + _n_(405068, "top_pos", lambda: top_pos)
        _l_(405069)
        _c_(405076, _a_(405071, _n_(405070, "draw", lambda: draw), "rectangle"), (_n_(405072, "i", lambda: i), _n_(405073, "line_y", lambda: line_y), _n_(405074, "i", lambda: i)+1, _n_(405075, "line_y", lambda: line_y)+1), (0, 0, 0))
        _l_(405077)
    # Write the text at the top in black
    _c_(405083, _a_(405080, _n_(405079, "draw", lambda: draw), "text"), (0, 0), _n_(405081, "message", lambda: message), font=_n_(405082, "font", lambda: font), fill=(0, 0, 0))
    _l_(405084)
    _c_(405088, _a_(405086, _n_(405085, "st7735", lambda: st7735), "display"), _n_(405087, "img", lambda: img))
    _l_(405089)


# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    _l_(405109)

    process = _c_(405093, _n_(405091, "Popen", lambda: Popen), ['vcgencmd', 'measure_temp'], stdout=_n_(405092, "PIPE", lambda: PIPE))
    _l_(405094)
    output, _error = _c_(405097, _a_(405096, _n_(405095, "process", lambda: process), "communicate"))
    _l_(405098)
    aux = _c_(405107, _n_(405099, "float", lambda: float), _n_(405100, "output", lambda: output)[_c_(405103, _a_(405102, _n_(405101, "output", lambda: output), "index"), '=') + 1:_c_(405106, _a_(405105, _n_(405104, "output", lambda: output), "rindex"), "'")])
    _l_(405108)
    return aux


# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 0.8
_l_(405110)

cpu_temps = [0] * 5
_l_(405111)

delay = 0.5  # Debounce the proximity tap
_l_(405112)  # Debounce the proximity tap
mode = 0  # The starting mode
_l_(405113)  # The starting mode
last_page = 0
_l_(405114)
light = 1
_l_(405115)

# Create a values dict to store the data
variables = ["temperature",
             "pressure",
             "humidity",
             "light",
             "oxidised",
             "reduced",
             "nh3",
             "pm1",
             "pm25",
             "pm10"]
_l_(405116)

values = {}
_l_(405117)

for v in _n_(405118, "variables", lambda: variables):
    _l_(405123)

    _n_(405119, "values", lambda: values)[_n_(405120, "v", lambda: v)] = [1] * _n_(405121, "WIDTH", lambda: WIDTH)
    _l_(405122)

# The main loop
try:
    _l_(405335)

    while True:
        _l_(405328)

        proximity = _c_(405126, _a_(405125, _n_(405124, "ltr559", lambda: ltr559), "get_proximity"))
        _l_(405127)

        # If the proximity crosses the threshold, toggle the mode
        if _n_(405128, "proximity", lambda: proximity) > 1500 and _c_(405131, _a_(405130, _n_(405129, "time", lambda: time), "time")) - _n_(405132, "last_page", lambda: last_page) > _n_(405133, "delay", lambda: delay):
            _l_(405143)

            mode += 1
            _l_(405134)
            mode %= _c_(405137, _n_(405135, "len", lambda: len), _n_(405136, "variables", lambda: variables))
            _l_(405138)
            last_page = _c_(405141, _a_(405140, _n_(405139, "time", lambda: time), "time"))
            _l_(405142)

        # One mode for each variable
        if _n_(405144, "mode", lambda: mode) == 0:
            _l_(405177)

            variable = "temperature"
            _l_(405145)
            unit = "C"
            _l_(405146)
            cpu_temp = _c_(405148, _n_(405147, "get_cpu_temperature", lambda: get_cpu_temperature))
            _l_(405149)
            # Smooth out with some averaging to decrease jitter
            cpu_temps = _n_(405150, "cpu_temps", lambda: cpu_temps)[1:] + [_n_(405151, "cpu_temp", lambda: cpu_temp)]
            _l_(405152)
            avg_cpu_temp = _c_(405155, _n_(405153, "sum", lambda: sum), _n_(405154, "cpu_temps", lambda: cpu_temps)) / _c_(405160, _n_(405156, "float", lambda: float), _c_(405159, _n_(405157, "len", lambda: len), _n_(405158, "cpu_temps", lambda: cpu_temps)))
            _l_(405161)
            raw_temp = _c_(405164, _a_(405163, _n_(405162, "bme280", lambda: bme280), "get_temperature"))
            _l_(405165)
            data = _n_(405166, "raw_temp", lambda: raw_temp) - ((_n_(405167, "avg_cpu_temp", lambda: avg_cpu_temp) - _n_(405168, "raw_temp", lambda: raw_temp)) / _n_(405169, "factor", lambda: factor))
            _l_(405170)
            _c_(405175, _n_(405171, "display_text", lambda: display_text), _n_(405172, "variable", lambda: variable), _n_(405173, "data", lambda: data), _n_(405174, "unit", lambda: unit))
            _l_(405176)

        if _n_(405178, "mode", lambda: mode) == 1:
            _l_(405191)

            variable = "pressure"
            _l_(405179)
            unit = "hPa"
            _l_(405180)
            data = _c_(405183, _a_(405182, _n_(405181, "bme280", lambda: bme280), "get_pressure"))
            _l_(405184)
            _c_(405189, _n_(405185, "display_text", lambda: display_text), _n_(405186, "variable", lambda: variable), _n_(405187, "data", lambda: data), _n_(405188, "unit", lambda: unit))
            _l_(405190)

        if _n_(405192, "mode", lambda: mode) == 2:
            _l_(405205)

            variable = "humidity"
            _l_(405193)
            unit = "%"
            _l_(405194)
            data = _c_(405197, _a_(405196, _n_(405195, "bme280", lambda: bme280), "get_humidity"))
            _l_(405198)
            _c_(405203, _n_(405199, "display_text", lambda: display_text), _n_(405200, "variable", lambda: variable), _n_(405201, "data", lambda: data), _n_(405202, "unit", lambda: unit))
            _l_(405204)

        if _n_(405206, "mode", lambda: mode) == 3:
            _l_(405222)

            variable = "light"
            _l_(405207)
            unit = "Lux"
            _l_(405208)
            if _n_(405209, "proximity", lambda: proximity) < 10:
                _l_(405215)

                data = _c_(405212, _a_(405211, _n_(405210, "ltr559", lambda: ltr559), "get_lux"))
                _l_(405213)
            else:
                data = 1
                _l_(405214)
            _c_(405220, _n_(405216, "display_text", lambda: display_text), _n_(405217, "variable", lambda: variable), _n_(405218, "data", lambda: data), _n_(405219, "unit", lambda: unit))
            _l_(405221)

        if _n_(405223, "mode", lambda: mode) == 4:
            _l_(405239)

            variable = "oxidised"
            _l_(405224)
            unit = "kO"
            _l_(405225)
            data = _c_(405228, _a_(405227, _n_(405226, "gas", lambda: gas), "read_all"))
            _l_(405229)
            data = _a_(405231, _n_(405230, "data", lambda: data), "oxidising") / 1000
            _l_(405232)
            _c_(405237, _n_(405233, "display_text", lambda: display_text), _n_(405234, "variable", lambda: variable), _n_(405235, "data", lambda: data), _n_(405236, "unit", lambda: unit))
            _l_(405238)

        if _n_(405240, "mode", lambda: mode) == 5:
            _l_(405256)

            variable = "reduced"
            _l_(405241)
            unit = "kO"
            _l_(405242)
            data = _c_(405245, _a_(405244, _n_(405243, "gas", lambda: gas), "read_all"))
            _l_(405246)
            data = _a_(405248, _n_(405247, "data", lambda: data), "reducing") / 1000
            _l_(405249)
            _c_(405254, _n_(405250, "display_text", lambda: display_text), _n_(405251, "variable", lambda: variable), _n_(405252, "data", lambda: data), _n_(405253, "unit", lambda: unit))
            _l_(405255)

        if _n_(405257, "mode", lambda: mode) == 6:
            _l_(405273)

            variable = "nh3"
            _l_(405258)
            unit = "kO"
            _l_(405259)
            data = _c_(405262, _a_(405261, _n_(405260, "gas", lambda: gas), "read_all"))
            _l_(405263)
            data = _a_(405265, _n_(405264, "data", lambda: data), "nh3") / 1000
            _l_(405266)
            _c_(405271, _n_(405267, "display_text", lambda: display_text), _n_(405268, "variable", lambda: variable), _n_(405269, "data", lambda: data), _n_(405270, "unit", lambda: unit))
            _l_(405272)

        if _n_(405274, "mode", lambda: mode) == 7:
            _l_(405291)

            variable = "pm1"
            _l_(405275)
            unit = "ug/m3"
            _l_(405276)
            data = _c_(405279, _a_(405278, _n_(405277, "pms5003", lambda: pms5003), "read"))
            _l_(405280)
            data = _c_(405283, _a_(405282, _n_(405281, "data", lambda: data), "pm_ug_per_m3"), 1.0)
            _l_(405284)
            _c_(405289, _n_(405285, "display_text", lambda: display_text), _n_(405286, "variable", lambda: variable), _n_(405287, "data", lambda: data), _n_(405288, "unit", lambda: unit))
            _l_(405290)

        if _n_(405292, "mode", lambda: mode) == 8:
            _l_(405309)

            variable = "pm25"
            _l_(405293)
            unit = "ug/m3"
            _l_(405294)
            data = _c_(405297, _a_(405296, _n_(405295, "pms5003", lambda: pms5003), "read"))
            _l_(405298)
            data = _c_(405301, _a_(405300, _n_(405299, "data", lambda: data), "pm_ug_per_m3"), 2.5)
            _l_(405302)
            _c_(405307, _n_(405303, "display_text", lambda: display_text), _n_(405304, "variable", lambda: variable), _n_(405305, "data", lambda: data), _n_(405306, "unit", lambda: unit))
            _l_(405308)

        if _n_(405310, "mode", lambda: mode) == 9:
            _l_(405327)

            variable = "pm10"
            _l_(405311)
            unit = "ug/m3"
            _l_(405312)
            data = _c_(405315, _a_(405314, _n_(405313, "pms5003", lambda: pms5003), "read"))
            _l_(405316)
            data = _c_(405319, _a_(405318, _n_(405317, "data", lambda: data), "pm_ug_per_m3"), 10)
            _l_(405320)
            _c_(405325, _n_(405321, "display_text", lambda: display_text), _n_(405322, "variable", lambda: variable), _n_(405323, "data", lambda: data), _n_(405324, "unit", lambda: unit))
            _l_(405326)

# Exit cleanly
except _n_(405329, "KeyboardInterrupt", lambda: KeyboardInterrupt):
    _l_(405334)

    _c_(405332, _a_(405331, _n_(405330, "sys", lambda: sys), "exit"), 0)
    _l_(405333)