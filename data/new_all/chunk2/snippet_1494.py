# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50956724/typeerror-not-supported-between-instances-of-numpy-ndarray-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import aubio
    _l_(428796)

except ImportError:
    pass
try:
    import numpy as num
    _l_(428798)

except ImportError:
    pass
try:
    import pyaudio
    _l_(428800)

except ImportError:
    pass
try:
    import sys
    _l_(428802)

except ImportError:
    pass

# Some constants for setting the PyAudio and the
# Aubio.
BUFFER_SIZE = 2048
_l_(428803)
CHANNELS = 1
_l_(428804)
FORMAT = _a_(428806, _n_(428805, "pyaudio", lambda: pyaudio), "paFloat32")
_l_(428807)
METHOD = "default"
_l_(428808)
SAMPLE_RATE = 44100
_l_(428809)
HOP_SIZE = _n_(428810, "BUFFER_SIZE", lambda: BUFFER_SIZE)//2
_l_(428811)
PERIOD_SIZE_IN_FRAME = _n_(428812, "HOP_SIZE", lambda: HOP_SIZE)
_l_(428813)
index = 0
_l_(428814)

def main(args):
    _l_(428888)


    # Initiating PyAudio object.
    pA = _c_(428817, _a_(428816, _n_(428815, "pyaudio", lambda: pyaudio), "PyAudio"))
    _l_(428818)
    # Open the microphone stream.
    mic = _c_(428825, _a_(428820, _n_(428819, "pA", lambda: pA), "open"), format=_n_(428821, "FORMAT", lambda: FORMAT), channels=_n_(428822, "CHANNELS", lambda: CHANNELS),
                  rate=_n_(428823, "SAMPLE_RATE", lambda: SAMPLE_RATE), input=True,
                  frames_per_buffer=_n_(428824, "PERIOD_SIZE_IN_FRAME", lambda: PERIOD_SIZE_IN_FRAME))
    _l_(428826)

    # Initiating Aubio's pitch detection object.
    pDetection = _c_(428833, _a_(428828, _n_(428827, "aubio", lambda: aubio), "pitch"), _n_(428829, "METHOD", lambda: METHOD), _n_(428830, "BUFFER_SIZE", lambda: BUFFER_SIZE),
                             _n_(428831, "HOP_SIZE", lambda: HOP_SIZE), _n_(428832, "SAMPLE_RATE", lambda: SAMPLE_RATE))
    _l_(428834)
    # Set unit.
    _c_(428837, _a_(428836, _n_(428835, "pDetection", lambda: pDetection), "set_unit"), "Hz")
    _l_(428838)
    # Frequency under -40 dB will considered
    # as a silence.
    _c_(428841, _a_(428840, _n_(428839, "pDetection", lambda: pDetection), "set_silence"), -40)
    _l_(428842)

    # Infinite loop!
    while True:
        _l_(428887)


        # Always listening to the microphone.
        data = _c_(428846, _a_(428844, _n_(428843, "mic", lambda: mic), "read"), _n_(428845, "PERIOD_SIZE_IN_FRAME", lambda: PERIOD_SIZE_IN_FRAME))
        _l_(428847)
        # Convert into number that Aubio understand.
        samples = _c_(428853, _a_(428849, _n_(428848, "num", lambda: num), "fromstring"), _n_(428850, "data", lambda: data),
                                 dtype=_a_(428852, _n_(428851, "aubio", lambda: aubio), "float_type"))
        _l_(428854)
        # Finally get the pitch.
        pitch = _c_(428857, _n_(428855, "pDetection", lambda: pDetection), _n_(428856, "samples", lambda: samples))[0]
        _l_(428858)
        # Compute the energy (volume)
        # of the current frame.
        volume = _c_(428862, _a_(428860, _n_(428859, "num", lambda: num), "sum"), _n_(428861, "samples", lambda: samples)**2)/_c_(428865, _n_(428863, "len", lambda: len), _n_(428864, "samples", lambda: samples))
        _l_(428866)
        # Format the volume output so it only
        # displays at most six numbers behind 0.
        volume = _c_(428869, _a_(428867, "{:6f}", "format"), _n_(428868, "volume", lambda: volume))
        _l_(428870)

        answer = _c_(428873, _n_(428871, "pitch_detection", lambda: pitch_detection), _n_(428872, "samples", lambda: samples))
        _l_(428874)

        # Finally print the pitch and the volume.
        _c_(428885, _n_(428875, "print", lambda: print), _c_(428878, _n_(428876, "str", lambda: str), _n_(428877, "pitch", lambda: pitch)) + " " + _c_(428881, _n_(428879, "str", lambda: str), _n_(428880, "volume", lambda: volume)) + _c_(428884, _n_(428882, "str", lambda: str), _n_(428883, "answer", lambda: answer)))
        _l_(428886)


def pitch_detection(samples):
    _l_(428904)

    colordict = {
        (0.0, 13.99): "Red",
        (14.00, 250.00): "Blue",
    }
    _l_(428889)

    for index, key in _c_(428892, _n_(428890, "enumerate", lambda: enumerate), _n_(428891, "colordict", lambda: colordict), start=0):
        _l_(428903)

        if _n_(428893, "samples", lambda: samples) > _n_(428894, "colordict", lambda: colordict)[_n_(428895, "key", lambda: key)][0] and _n_(428896, "samples", lambda: samples) < _n_(428897, "colordict", lambda: colordict)[_n_(428898, "key", lambda: key)][1]:
            _l_(428901)

            aux = _n_(428899, "key", lambda: key)
            _l_(428900)
            return aux
        aux = "Not Found"
        _l_(428902)
        return aux


if _n_(428905, "__name__", lambda: __name__) == "__main__":
    _l_(428911)

    _c_(428909, _n_(428906, "main", lambda: main), _a_(428908, _n_(428907, "sys", lambda: sys), "argv"))
    _l_(428910)