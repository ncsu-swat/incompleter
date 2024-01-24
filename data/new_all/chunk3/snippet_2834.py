# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61739446/using-numpy-linspace-method-for-a-simpleaudio-project-i-get-a-typeerror-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(565059)

except ImportError:
    pass
try:
    import simpleaudio as sa
    _l_(565061)

except ImportError:
    pass

# calculate note frequencies
A_freq = 440
_l_(565062)
Csh_freq = _n_(565063, "A_freq", lambda: A_freq) * 2 ** (4 / 12)
_l_(565064)
E_freq = _n_(565065, "A_freq", lambda: A_freq) * 2 ** (7 / 12)
_l_(565066)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
_l_(565067)
T = 0.25
_l_(565068)
t = _c_(565074, _a_(565070, _n_(565069, "np", lambda: np), "linspace"), 0, _n_(565071, "T", lambda: T), _n_(565072, "T", lambda: T) * _n_(565073, "sample_rate", lambda: sample_rate), False)
_l_(565075)

# generate sine wave notes
A_note = _c_(565082, _a_(565077, _n_(565076, "np", lambda: np), "sin"), _n_(565078, "A_freq", lambda: A_freq) * _n_(565079, "t", lambda: t) * 2 * _a_(565081, _n_(565080, "np", lambda: np), "pi"))
_l_(565083)
Csh_note = _c_(565090, _a_(565085, _n_(565084, "np", lambda: np), "sin"), _n_(565086, "Csh_freq", lambda: Csh_freq) * _n_(565087, "t", lambda: t) * 2 * _a_(565089, _n_(565088, "np", lambda: np), "pi"))
_l_(565091)
E_note = _c_(565098, _a_(565093, _n_(565092, "np", lambda: np), "sin"), _n_(565094, "E_freq", lambda: E_freq) * _n_(565095, "t", lambda: t) * 2 * _a_(565097, _n_(565096, "np", lambda: np), "pi"))
_l_(565099)

# concatenate notes
audio = _c_(565105, _a_(565101, _n_(565100, "np", lambda: np), "hstack"), (_n_(565102, "A_note", lambda: A_note), _n_(565103, "Csh_note", lambda: Csh_note), _n_(565104, "E_note", lambda: E_note)))
_l_(565106)
# normalize to 16-bit range
audio *= 32767 / _c_(565113, _a_(565108, _n_(565107, "np", lambda: np), "max"), _c_(565112, _a_(565110, _n_(565109, "np", lambda: np), "abs"), _n_(565111, "audio", lambda: audio)))
_l_(565114)
# convert to 16-bit data
audio = _c_(565119, _a_(565116, _n_(565115, "audio", lambda: audio), "astype"), _a_(565118, _n_(565117, "np", lambda: np), "int16"))
_l_(565120)

# start playback
play_obj = _c_(565125, _a_(565122, _n_(565121, "sa", lambda: sa), "play_buffer"), _n_(565123, "audio", lambda: audio), 1, 2, _n_(565124, "sample_rate", lambda: sample_rate))
_l_(565126)

# wait for playback to finish before exiting
_c_(565129, _a_(565128, _n_(565127, "play_obj", lambda: play_obj), "wait_done"))
_l_(565130)