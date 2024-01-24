# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71832875/attributeerror-nonetype-object-has-no-attribute-read-python-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from cProfile import label
    _l_(343195)

except ImportError:
    pass
try:
    from doctest import master
    _l_(343197)

except ImportError:
    pass
try:
    from importlib.metadata import files
    _l_(343199)

except ImportError:
    pass
try:
    from pydoc import text
    _l_(343201)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(343203)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(343205)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(343207)

except ImportError:
    pass
try:
    from functools import partial
    _l_(343209)

except ImportError:
    pass
try:
    import numpy as np
    _l_(343211)

except ImportError:
    pass
try:
    from tkinter.filedialog import asksaveasfile
    _l_(343213)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(343215)

except ImportError:
    pass
try:
    import wave
    _l_(343217)

except ImportError:
    pass
try:
    import math
    _l_(343219)

except ImportError:
    pass
try:
    import contextlib
    _l_(343221)

except ImportError:
    pass
try:
    import warnings
    _l_(343223)

except ImportError:
    pass
 
outname =  (r"filtered.wav")
_l_(343224)
 



def fileaudio():
    _l_(343236)

    global fname1
    _l_(343225)
    fname1 = _c_(343228, _a_(343227, _n_(343226, "filedialog", lambda: filedialog), "askopenfilename"), filetypes=(("Audio files", "*.wav;*.mp3"),
                                               ("All files", "*.*") ))
    _l_(343229)
    _c_(343232, _n_(343230, "print", lambda: print), _n_(343231, "fname1", lambda: fname1))
    _l_(343233)
    aux = _n_(343234, "fname1", lambda: fname1)
    _l_(343235)
    
    return aux
  


_c_(343240, _a_(343238, _n_(343237, "warnings", lambda: warnings), "simplefilter"), "ignore", _n_(343239, "DeprecationWarning", lambda: DeprecationWarning))
_l_(343241)


      
    # Change label contents
    



root =_c_(343243, _n_(343242, "Tk", lambda: Tk))
_l_(343244)
_c_(343247, _a_(343246, _n_(343245, "root", lambda: root), "geometry"), "1280x800")
_l_(343248)
_c_(343251, _a_(343250, _n_(343249, "root", lambda: root), "resizable"), False,False)
_l_(343252)
_c_(343255, _a_(343254, _n_(343253, "root", lambda: root), "title"), "Audio filter")
_l_(343256)
_c_(343259, _a_(343258, _n_(343257, "root", lambda: root), "configure"), background="white")
_l_(343260)


    

#icon
image_icon=_c_(343262, _n_(343261, "PhotoImage", lambda: PhotoImage), file="filter.png")
_l_(343263)
_c_(343267, _a_(343265, _n_(343264, "root", lambda: root), "iconphoto"), False,_n_(343266, "image_icon", lambda: image_icon))
_l_(343268)

#logo
photo=_c_(343270, _n_(343269, "PhotoImage", lambda: PhotoImage), file="filter.png")
_l_(343271)
myimage=_c_(343274, _n_(343272, "Label", lambda: Label), image=_n_(343273, "photo", lambda: photo),background="white")
_l_(343275)
_c_(343278, _a_(343277, _n_(343276, "myimage", lambda: myimage), "pack"), padx=5,pady=5)
_l_(343279)

#name
_c_(343283, _a_(343282, _c_(343281, _n_(343280, "Label", lambda: Label), text="Audio filter",font="ariel 30 bold",background="black",fg="white"), "pack"))
_l_(343284)

#entry box
def runlow():
    _l_(343426)

    cutOffFrequency = 400.0
    _l_(343285)
    



# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean

    def running_mean(x, windowSize):
        _l_(343300)


        cumsum = _c_(343292, _a_(343287, _n_(343286, "np", lambda: np), "cumsum"), _c_(343291, _a_(343289, _n_(343288, "np", lambda: np), "insert"), _n_(343290, "x", lambda: x), 0, 0)) 
        _l_(343293) 
        aux = (_n_(343294, "cumsum", lambda: cumsum)[_n_(343295, "windowSize", lambda: windowSize):] - _n_(343296, "cumsum", lambda: cumsum)[:-_n_(343297, "windowSize", lambda: windowSize)]) / _n_(343298, "windowSize", lambda: windowSize)
        _l_(343299)

        return aux



# from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174

    def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):
        _l_(343335)




        if _n_(343301, "sample_width", lambda: sample_width) == 1:
            _l_(343313)


            dtype = _a_(343303, _n_(343302, "np", lambda: np), "uint8") # unsigned char
            _l_(343304) # unsigned char

        elif _n_(343305, "sample_width", lambda: sample_width) == 2:
            _l_(343312)


            dtype = _a_(343307, _n_(343306, "np", lambda: np), "int16") # signed 2-byte short
            _l_(343308) # signed 2-byte short

        else:

            raise _c_(343310, _n_(343309, "ValueError", lambda: ValueError), "Only supports 8 and 16 bit audio formats.")
            _l_(343311)



        channels = _c_(343318, _a_(343315, _n_(343314, "np", lambda: np), "fromstring"), _n_(343316, "raw_bytes", lambda: raw_bytes), dtype=_n_(343317, "dtype", lambda: dtype))
        _l_(343319)



        if _n_(343320, "interleaved", lambda: interleaved):
            _l_(343334)


        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data

            _n_(343321, "channels", lambda: channels).shape = (_n_(343322, "n_frames", lambda: n_frames), _n_(343323, "n_channels", lambda: n_channels))
            _l_(343324)

            channels = _a_(343326, _n_(343325, "channels", lambda: channels), "T")
            _l_(343327)

        else:

        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1

            _n_(343328, "channels", lambda: channels).shape = (_n_(343329, "n_channels", lambda: n_channels), _n_(343330, "n_frames", lambda: n_frames))
            _l_(343331)
            aux = _n_(343332, "channels", lambda: channels)
            _l_(343333)
            return aux



    



    with _c_(343342, _a_(343337, _n_(343336, "contextlib", lambda: contextlib), "closing"), _c_(343341, _a_(343339, _n_(343338, "wave", lambda: wave), "open"), _n_(343340, "fname1", lambda: fname1),'rb')) as spf:
        _l_(343425)


        sampleRate = _c_(343345, _a_(343344, _n_(343343, "spf", lambda: spf), "getframerate"))
        _l_(343346)

        ampWidth = _c_(343349, _a_(343348, _n_(343347, "spf", lambda: spf), "getsampwidth"))
        _l_(343350)

        nChannels = _c_(343353, _a_(343352, _n_(343351, "spf", lambda: spf), "getnchannels"))
        _l_(343354)

        nFrames = _c_(343357, _a_(343356, _n_(343355, "spf", lambda: spf), "getnframes"))
        _l_(343358)



    # Extract Raw Audio from multi-channel Wav File

        signal = _c_(343363, _a_(343360, _n_(343359, "spf", lambda: spf), "readframes"), _n_(343361, "nFrames", lambda: nFrames)*_n_(343362, "nChannels", lambda: nChannels))
        _l_(343364)

        _c_(343367, _a_(343366, _n_(343365, "spf", lambda: spf), "close"))
        _l_(343368)

        channels = _c_(343374, _n_(343369, "interpret_wav", lambda: interpret_wav), _n_(343370, "signal", lambda: signal), _n_(343371, "nFrames", lambda: nFrames), _n_(343372, "nChannels", lambda: nChannels), _n_(343373, "ampWidth", lambda: ampWidth), True)
        _l_(343375)



    # get window size

    # from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter

        freqRatio = (_n_(343376, "cutOffFrequency", lambda: cutOffFrequency)/_n_(343377, "sampleRate", lambda: sampleRate))
        _l_(343378)

        N = _c_(343385, _n_(343379, "int", lambda: int), _c_(343383, _a_(343381, _n_(343380, "math", lambda: math), "sqrt"), 0.196196 + _n_(343382, "freqRatio", lambda: freqRatio)**2)/_n_(343384, "freqRatio", lambda: freqRatio))
        _l_(343386)



    # Use moviung average (only on first channel)

        filtered = _c_(343394, _a_(343391, _c_(343390, _n_(343387, "running_mean", lambda: running_mean), _n_(343388, "channels", lambda: channels)[0], _n_(343389, "N", lambda: N)), "astype"), _a_(343393, _n_(343392, "channels", lambda: channels), "dtype"))
        _l_(343395)



        wav_file = _c_(343399, _a_(343397, _n_(343396, "wave", lambda: wave), "open"), _n_(343398, "outname", lambda: outname), "w")
        _l_(343400)

        _c_(343412, _a_(343402, _n_(343401, "wav_file", lambda: wav_file), "setparams"), (1, _n_(343403, "ampWidth", lambda: ampWidth), _n_(343404, "sampleRate", lambda: sampleRate), _n_(343405, "nFrames", lambda: nFrames), _c_(343408, _a_(343407, _n_(343406, "spf", lambda: spf), "getcomptype")), _c_(343411, _a_(343410, _n_(343409, "spf", lambda: spf), "getcompname"))))
        _l_(343413)

        _c_(343419, _a_(343415, _n_(343414, "wav_file", lambda: wav_file), "writeframes"), _c_(343418, _a_(343417, _n_(343416, "filtered", lambda: filtered), "tobytes"), 'C'))
        _l_(343420)

        _c_(343423, _a_(343422, _n_(343421, "wav_file", lambda: wav_file), "close"))
        _l_(343424)

#button
record=_c_(343432, _a_(343431, _c_(343430, _n_(343427, "Button", lambda: Button), _n_(343428, "root", lambda: root),font="ariel 20",text="Input",bg="black",fg="white",border=0,command=_n_(343429, "fileaudio", lambda: fileaudio)), "pack"), pady=30)
_l_(343433)
record2=_c_(343439, _a_(343438, _c_(343437, _n_(343434, "Button", lambda: Button), _n_(343435, "root", lambda: root),font="ariel 20",text="Filter",bg="black",fg="white",border=0,command=_n_(343436, "runlow", lambda: runlow)), "pack"), pady=30)
_l_(343440)

#functions to integrate





# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean









_c_(343443, _a_(343442, _n_(343441, "root", lambda: root), "mainloop"))
_l_(343444)