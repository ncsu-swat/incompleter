# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71832875/attributeerror-nonetype-object-has-no-attribute-read-python-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from cProfile import label
    _l_(374369)

except ImportError:
    pass
try:
    from doctest import master
    _l_(374371)

except ImportError:
    pass
try:
    from importlib.metadata import files
    _l_(374373)

except ImportError:
    pass
try:
    from pydoc import text
    _l_(374375)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(374377)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(374379)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(374381)

except ImportError:
    pass
try:
    from functools import partial
    _l_(374383)

except ImportError:
    pass
try:
    import numpy as np
    _l_(374385)

except ImportError:
    pass
try:
    from tkinter.filedialog import asksaveasfile
    _l_(374387)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(374389)

except ImportError:
    pass
try:
    import wave
    _l_(374391)

except ImportError:
    pass
try:
    import math
    _l_(374393)

except ImportError:
    pass
try:
    import contextlib
    _l_(374395)

except ImportError:
    pass
try:
    import warnings
    _l_(374397)

except ImportError:
    pass
 
outname =  (r"filtered.wav")
_l_(374398)
 



def fileaudio():
    _l_(374410)

    global fname1
    _l_(374399)
    fname1 = _c_(374402, _a_(374401, _n_(374400, "filedialog", lambda: filedialog), "askopenfilename"), filetypes=(("Audio files", "*.wav;*.mp3"),
                                               ("All files", "*.*") ))
    _l_(374403)
    _c_(374406, _n_(374404, "print", lambda: print), _n_(374405, "fname1", lambda: fname1))
    _l_(374407)
    aux = _n_(374408, "fname1", lambda: fname1)
    _l_(374409)
    
    return aux
  


_c_(374414, _a_(374412, _n_(374411, "warnings", lambda: warnings), "simplefilter"), "ignore", _n_(374413, "DeprecationWarning", lambda: DeprecationWarning))
_l_(374415)


      
    # Change label contents
    



root =_c_(374417, _n_(374416, "Tk", lambda: Tk))
_l_(374418)
_c_(374421, _a_(374420, _n_(374419, "root", lambda: root), "geometry"), "1280x800")
_l_(374422)
_c_(374425, _a_(374424, _n_(374423, "root", lambda: root), "resizable"), False,False)
_l_(374426)
_c_(374429, _a_(374428, _n_(374427, "root", lambda: root), "title"), "Audio filter")
_l_(374430)
_c_(374433, _a_(374432, _n_(374431, "root", lambda: root), "configure"), background="white")
_l_(374434)


    

#icon
image_icon=_c_(374436, _n_(374435, "PhotoImage", lambda: PhotoImage), file="filter.png")
_l_(374437)
_c_(374441, _a_(374439, _n_(374438, "root", lambda: root), "iconphoto"), False,_n_(374440, "image_icon", lambda: image_icon))
_l_(374442)

#logo
photo=_c_(374444, _n_(374443, "PhotoImage", lambda: PhotoImage), file="filter.png")
_l_(374445)
myimage=_c_(374448, _n_(374446, "Label", lambda: Label), image=_n_(374447, "photo", lambda: photo),background="white")
_l_(374449)
_c_(374452, _a_(374451, _n_(374450, "myimage", lambda: myimage), "pack"), padx=5,pady=5)
_l_(374453)

#name
_c_(374457, _a_(374456, _c_(374455, _n_(374454, "Label", lambda: Label), text="Audio filter",font="ariel 30 bold",background="black",fg="white"), "pack"))
_l_(374458)

#entry box
def runlow():
    _l_(374600)

    cutOffFrequency = 400.0
    _l_(374459)
    



# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean

    def running_mean(x, windowSize):
        _l_(374474)


        cumsum = _c_(374466, _a_(374461, _n_(374460, "np", lambda: np), "cumsum"), _c_(374465, _a_(374463, _n_(374462, "np", lambda: np), "insert"), _n_(374464, "x", lambda: x), 0, 0)) 
        _l_(374467) 
        aux = (_n_(374468, "cumsum", lambda: cumsum)[_n_(374469, "windowSize", lambda: windowSize):] - _n_(374470, "cumsum", lambda: cumsum)[:-_n_(374471, "windowSize", lambda: windowSize)]) / _n_(374472, "windowSize", lambda: windowSize)
        _l_(374473)

        return aux



# from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174

    def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):
        _l_(374509)




        if _n_(374475, "sample_width", lambda: sample_width) == 1:
            _l_(374487)


            dtype = _a_(374477, _n_(374476, "np", lambda: np), "uint8") # unsigned char
            _l_(374478) # unsigned char

        elif _n_(374479, "sample_width", lambda: sample_width) == 2:
            _l_(374486)


            dtype = _a_(374481, _n_(374480, "np", lambda: np), "int16") # signed 2-byte short
            _l_(374482) # signed 2-byte short

        else:

            raise _c_(374484, _n_(374483, "ValueError", lambda: ValueError), "Only supports 8 and 16 bit audio formats.")
            _l_(374485)



        channels = _c_(374492, _a_(374489, _n_(374488, "np", lambda: np), "fromstring"), _n_(374490, "raw_bytes", lambda: raw_bytes), dtype=_n_(374491, "dtype", lambda: dtype))
        _l_(374493)



        if _n_(374494, "interleaved", lambda: interleaved):
            _l_(374508)


        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data

            _n_(374495, "channels", lambda: channels).shape = (_n_(374496, "n_frames", lambda: n_frames), _n_(374497, "n_channels", lambda: n_channels))
            _l_(374498)

            channels = _a_(374500, _n_(374499, "channels", lambda: channels), "T")
            _l_(374501)

        else:

        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1

            _n_(374502, "channels", lambda: channels).shape = (_n_(374503, "n_channels", lambda: n_channels), _n_(374504, "n_frames", lambda: n_frames))
            _l_(374505)
            aux = _n_(374506, "channels", lambda: channels)
            _l_(374507)
            return aux



    



    with _c_(374516, _a_(374511, _n_(374510, "contextlib", lambda: contextlib), "closing"), _c_(374515, _a_(374513, _n_(374512, "wave", lambda: wave), "open"), _n_(374514, "fname1", lambda: fname1),'rb')) as spf:
        _l_(374599)


        sampleRate = _c_(374519, _a_(374518, _n_(374517, "spf", lambda: spf), "getframerate"))
        _l_(374520)

        ampWidth = _c_(374523, _a_(374522, _n_(374521, "spf", lambda: spf), "getsampwidth"))
        _l_(374524)

        nChannels = _c_(374527, _a_(374526, _n_(374525, "spf", lambda: spf), "getnchannels"))
        _l_(374528)

        nFrames = _c_(374531, _a_(374530, _n_(374529, "spf", lambda: spf), "getnframes"))
        _l_(374532)



    # Extract Raw Audio from multi-channel Wav File

        signal = _c_(374537, _a_(374534, _n_(374533, "spf", lambda: spf), "readframes"), _n_(374535, "nFrames", lambda: nFrames)*_n_(374536, "nChannels", lambda: nChannels))
        _l_(374538)

        _c_(374541, _a_(374540, _n_(374539, "spf", lambda: spf), "close"))
        _l_(374542)

        channels = _c_(374548, _n_(374543, "interpret_wav", lambda: interpret_wav), _n_(374544, "signal", lambda: signal), _n_(374545, "nFrames", lambda: nFrames), _n_(374546, "nChannels", lambda: nChannels), _n_(374547, "ampWidth", lambda: ampWidth), True)
        _l_(374549)



    # get window size

    # from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter

        freqRatio = (_n_(374550, "cutOffFrequency", lambda: cutOffFrequency)/_n_(374551, "sampleRate", lambda: sampleRate))
        _l_(374552)

        N = _c_(374559, _n_(374553, "int", lambda: int), _c_(374557, _a_(374555, _n_(374554, "math", lambda: math), "sqrt"), 0.196196 + _n_(374556, "freqRatio", lambda: freqRatio)**2)/_n_(374558, "freqRatio", lambda: freqRatio))
        _l_(374560)



    # Use moviung average (only on first channel)

        filtered = _c_(374568, _a_(374565, _c_(374564, _n_(374561, "running_mean", lambda: running_mean), _n_(374562, "channels", lambda: channels)[0], _n_(374563, "N", lambda: N)), "astype"), _a_(374567, _n_(374566, "channels", lambda: channels), "dtype"))
        _l_(374569)



        wav_file = _c_(374573, _a_(374571, _n_(374570, "wave", lambda: wave), "open"), _n_(374572, "outname", lambda: outname), "w")
        _l_(374574)

        _c_(374586, _a_(374576, _n_(374575, "wav_file", lambda: wav_file), "setparams"), (1, _n_(374577, "ampWidth", lambda: ampWidth), _n_(374578, "sampleRate", lambda: sampleRate), _n_(374579, "nFrames", lambda: nFrames), _c_(374582, _a_(374581, _n_(374580, "spf", lambda: spf), "getcomptype")), _c_(374585, _a_(374584, _n_(374583, "spf", lambda: spf), "getcompname"))))
        _l_(374587)

        _c_(374593, _a_(374589, _n_(374588, "wav_file", lambda: wav_file), "writeframes"), _c_(374592, _a_(374591, _n_(374590, "filtered", lambda: filtered), "tobytes"), 'C'))
        _l_(374594)

        _c_(374597, _a_(374596, _n_(374595, "wav_file", lambda: wav_file), "close"))
        _l_(374598)

#button
record=_c_(374606, _a_(374605, _c_(374604, _n_(374601, "Button", lambda: Button), _n_(374602, "root", lambda: root),font="ariel 20",text="Input",bg="black",fg="white",border=0,command=_n_(374603, "fileaudio", lambda: fileaudio)), "pack"), pady=30)
_l_(374607)
record2=_c_(374613, _a_(374612, _c_(374611, _n_(374608, "Button", lambda: Button), _n_(374609, "root", lambda: root),font="ariel 20",text="Filter",bg="black",fg="white",border=0,command=_n_(374610, "runlow", lambda: runlow)), "pack"), pady=30)
_l_(374614)

#functions to integrate





# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean









_c_(374617, _a_(374616, _n_(374615, "root", lambda: root), "mainloop"))
_l_(374618)