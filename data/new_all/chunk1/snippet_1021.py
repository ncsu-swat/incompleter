# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53522130/python-numpy-error-typeerror-numpy-float64-object-cannot-be-interpreted-as-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import glob
    _l_(385739)

except ImportError:
    pass
try:
    import numpy as np
    _l_(385741)

except ImportError:
    pass
try:
    from matplotlib import pyplot as plt
    _l_(385743)

except ImportError:
    pass
try:
    import scipy.io.wavfile as wav
    _l_(385745)

except ImportError:
    pass
try:
    from numpy.lib import stride_tricks
    _l_(385747)

except ImportError:
    pass

""" short time fourier transform of audio signal """
def stft(sig, frameSize, overlapFac=0.5, window=_a_(385749, _n_(385748, "np", lambda: np), "hanning")):
    _l_(385817)

    win = _c_(385752, _n_(385750, "window", lambda: window), _n_(385751, "frameSize", lambda: frameSize))
    _l_(385753)
    hopSize = _c_(385761, _n_(385754, "int", lambda: int), _n_(385755, "frameSize", lambda: frameSize) - _c_(385760, _a_(385757, _n_(385756, "np", lambda: np), "floor"), _n_(385758, "overlapFac", lambda: overlapFac) * _n_(385759, "frameSize", lambda: frameSize)))
    _l_(385762)

    # zeros at beginning (thus center of 1st window should be for sample nr. 0)
    samples = _c_(385773, _a_(385764, _n_(385763, "np", lambda: np), "append"), _c_(385771, _a_(385766, _n_(385765, "np", lambda: np), "zeros"), _c_(385770, _a_(385768, _n_(385767, "np", lambda: np), "floor"), _n_(385769, "frameSize", lambda: frameSize)/2.0)), _n_(385772, "sig", lambda: sig))
    _l_(385774)
    # cols for windowing
    cols = _c_(385784, _a_(385776, _n_(385775, "np", lambda: np), "ceil"), (_c_(385779, _n_(385777, "len", lambda: len), _n_(385778, "samples", lambda: samples)) - _n_(385780, "frameSize", lambda: frameSize)) / _c_(385783, _n_(385781, "float", lambda: float), _n_(385782, "hopSize", lambda: hopSize))) + 1
    _l_(385785)
    # zeros at end (thus samples can be fully covered by frames)
    samples = _c_(385793, _a_(385787, _n_(385786, "np", lambda: np), "append"), _n_(385788, "samples", lambda: samples), _c_(385792, _a_(385790, _n_(385789, "np", lambda: np), "zeros"), _n_(385791, "frameSize", lambda: frameSize)))
    _l_(385794)

    frames = _c_(385807, _a_(385806, _c_(385805, _a_(385796, _n_(385795, "stride_tricks", lambda: stride_tricks), "as_strided"), _n_(385797, "samples", lambda: samples), shape=(_n_(385798, "cols", lambda: cols), _n_(385799, "frameSize", lambda: frameSize)), strides=(_a_(385801, _n_(385800, "samples", lambda: samples), "strides")[0]*_n_(385802, "hopSize", lambda: hopSize), _a_(385804, _n_(385803, "samples", lambda: samples), "strides")[0])), "copy"))
    _l_(385808)
    frames *= _n_(385809, "win", lambda: win)
    _l_(385810)
    aux = _c_(385815, _a_(385813, _a_(385812, _n_(385811, "np", lambda: np), "fft"), "rfft"), _n_(385814, "frames", lambda: frames))    
    _l_(385816)    

    return aux    

""" scale frequency axis logarithmically """    
def logscale_spec(spec, sr=44100, factor=20.):
    _l_(385926)

    timebins, freqbins = _c_(385821, _a_(385819, _n_(385818, "np", lambda: np), "shape"), _n_(385820, "spec", lambda: spec))
    _l_(385822)

    scale = _c_(385826, _a_(385824, _n_(385823, "np", lambda: np), "linspace"), 0, 1, _n_(385825, "freqbins", lambda: freqbins)) ** _n_(385827, "factor", lambda: factor)
    _l_(385828)
    scale *= (_n_(385829, "freqbins", lambda: freqbins)-1)/_c_(385832, _n_(385830, "max", lambda: max), _n_(385831, "scale", lambda: scale))
    _l_(385833)
    scale = _c_(385840, _a_(385835, _n_(385834, "np", lambda: np), "unique"), _c_(385839, _a_(385837, _n_(385836, "np", lambda: np), "round"), _n_(385838, "scale", lambda: scale)))
    _l_(385841)

    # create spectrogram with new freq bins
    newspec = _c_(385851, _a_(385843, _n_(385842, "np", lambda: np), "complex128"), _c_(385850, _a_(385845, _n_(385844, "np", lambda: np), "zeros"), [_n_(385846, "timebins", lambda: timebins), _c_(385849, _n_(385847, "len", lambda: len), _n_(385848, "scale", lambda: scale))]))
    _l_(385852)
    for i in _c_(385857, _n_(385853, "range", lambda: range), 0, _c_(385856, _n_(385854, "len", lambda: len), _n_(385855, "scale", lambda: scale))):
        _l_(385883)

        if _n_(385858, "i", lambda: i) == _c_(385861, _n_(385859, "len", lambda: len), _n_(385860, "scale", lambda: scale))-1:
            _l_(385882)

            _n_(385862, "newspec", lambda: newspec)[:,_n_(385863, "i", lambda: i)] = _c_(385869, _a_(385865, _n_(385864, "np", lambda: np), "sum"), _n_(385866, "spec", lambda: spec)[:,_n_(385867, "scale", lambda: scale)[_n_(385868, "i", lambda: i)]:], axis=1)
            _l_(385870)
        else:        
            _n_(385871, "newspec", lambda: newspec)[:,_n_(385872, "i", lambda: i)] = _c_(385880, _a_(385874, _n_(385873, "np", lambda: np), "sum"), _n_(385875, "spec", lambda: spec)[:,_n_(385876, "scale", lambda: scale)[_n_(385877, "i", lambda: i)]:_n_(385878, "scale", lambda: scale)[_n_(385879, "i", lambda: i)+1]], axis=1)
            _l_(385881)

    # list center freq of bins
    allfreqs = _c_(385893, _a_(385885, _n_(385884, "np", lambda: np), "abs"), _c_(385891, _a_(385888, _a_(385887, _n_(385886, "np", lambda: np), "fft"), "fftfreq"), _n_(385889, "freqbins", lambda: freqbins)*2, 1./_n_(385890, "sr", lambda: sr))[:_n_(385892, "freqbins", lambda: freqbins)+1])
    _l_(385894)
    freqs = []
    _l_(385895)
    for i in _c_(385900, _n_(385896, "range", lambda: range), 0, _c_(385899, _n_(385897, "len", lambda: len), _n_(385898, "scale", lambda: scale))):
        _l_(385922)

        if _n_(385901, "i", lambda: i) == _c_(385904, _n_(385902, "len", lambda: len), _n_(385903, "scale", lambda: scale))-1:
            _l_(385921)

            freqs += [_c_(385910, _a_(385906, _n_(385905, "np", lambda: np), "mean"), _n_(385907, "allfreqs", lambda: allfreqs)[_n_(385908, "scale", lambda: scale)[_n_(385909, "i", lambda: i)]:])]
            _l_(385911)
        else:
            freqs += [_c_(385919, _a_(385913, _n_(385912, "np", lambda: np), "mean"), _n_(385914, "allfreqs", lambda: allfreqs)[_n_(385915, "scale", lambda: scale)[_n_(385916, "i", lambda: i)]:_n_(385917, "scale", lambda: scale)[_n_(385918, "i", lambda: i)+1]])]
            _l_(385920)
    aux = _n_(385923, "newspec", lambda: newspec), _n_(385924, "freqs", lambda: freqs)
    _l_(385925)

    return aux

""" plot spectrogram"""
def plotstft(audiopath, binsize=2**10, plotpath=None, colormap="jet"):
    _l_(386045)

    samplerate, samples = _c_(385930, _a_(385928, _n_(385927, "wav", lambda: wav), "read"), _n_(385929, "audiopath", lambda: audiopath))
    _l_(385931)
    s = _c_(385935, _n_(385932, "stft", lambda: stft), _n_(385933, "samples", lambda: samples), _n_(385934, "binsize", lambda: binsize))
    _l_(385936)

    sshow, freq = _c_(385940, _n_(385937, "logscale_spec", lambda: logscale_spec), _n_(385938, "s", lambda: s), factor=1.0, sr=_n_(385939, "samplerate", lambda: samplerate))
    _l_(385941)
    ims = 20.*_c_(385948, _a_(385943, _n_(385942, "np", lambda: np), "log10"), _c_(385947, _a_(385945, _n_(385944, "np", lambda: np), "abs"), _n_(385946, "sshow", lambda: sshow))/10e-6) # amplitude to decibel
    _l_(385949) # amplitude to decibel

    timebins, freqbins = _c_(385953, _a_(385951, _n_(385950, "np", lambda: np), "shape"), _n_(385952, "ims", lambda: ims))
    _l_(385954)

    _c_(385957, _a_(385956, _n_(385955, "plt", lambda: plt), "figure"), figsize=(15, 7.5))
    _l_(385958)
    _c_(385966, _a_(385960, _n_(385959, "plt", lambda: plt), "imshow"), _c_(385964, _a_(385962, _n_(385961, "np", lambda: np), "transpose"), _n_(385963, "ims", lambda: ims)), origin="lower", aspect="auto", cmap=_n_(385965, "colormap", lambda: colormap), interpolation="none")
    _l_(385967)
    _c_(385970, _a_(385969, _n_(385968, "plt", lambda: plt), "colorbar"))
    _l_(385971)

    _c_(385974, _a_(385973, _n_(385972, "plt", lambda: plt), "xlabel"), "time (s)")
    _l_(385975)
    _c_(385978, _a_(385977, _n_(385976, "plt", lambda: plt), "ylabel"), "frequency (hz)")
    _l_(385979)
    _c_(385983, _a_(385981, _n_(385980, "plt", lambda: plt), "xlim"), [0, _n_(385982, "timebins", lambda: timebins)-1])
    _l_(385984)
    _c_(385988, _a_(385986, _n_(385985, "plt", lambda: plt), "ylim"), [0, _n_(385987, "freqbins", lambda: freqbins)])
    _l_(385989)

    xlocs = _c_(385996, _a_(385991, _n_(385990, "np", lambda: np), "float32"), _c_(385995, _a_(385993, _n_(385992, "np", lambda: np), "linspace"), 0, _n_(385994, "timebins", lambda: timebins)-1, 5))
    _l_(385997)
    _c_(386009, _a_(385999, _n_(385998, "plt", lambda: plt), "xticks"), _n_(386000, "xlocs", lambda: xlocs), ["%.02f" % _n_(386001, "l", lambda: l) for l in ((_n_(386002, "xlocs", lambda: xlocs)*_c_(386005, _n_(386003, "len", lambda: len), _n_(386004, "samples", lambda: samples))/_n_(386006, "timebins", lambda: timebins))+(0.5*_n_(386007, "binsize", lambda: binsize)))/_n_(386008, "samplerate", lambda: samplerate)])
    _l_(386010)
    ylocs = _c_(386020, _a_(386012, _n_(386011, "np", lambda: np), "int16"), _c_(386019, _a_(386014, _n_(386013, "np", lambda: np), "round"), _c_(386018, _a_(386016, _n_(386015, "np", lambda: np), "linspace"), 0, _n_(386017, "freqbins", lambda: freqbins)-1, 10)))
    _l_(386021)
    _c_(386028, _a_(386023, _n_(386022, "plt", lambda: plt), "yticks"), _n_(386024, "ylocs", lambda: ylocs), ["%.02f" % _n_(386025, "freq", lambda: freq)[_n_(386026, "i", lambda: i)] for i in _n_(386027, "ylocs", lambda: ylocs)])
    _l_(386029)

    if _n_(386030, "plotpath", lambda: plotpath):
        _l_(386040)

        _c_(386034, _a_(386032, _n_(386031, "plt", lambda: plt), "savefig"), _n_(386033, "plotpath", lambda: plotpath), bbox_inches="tight")
        _l_(386035)
    else:
        _c_(386038, _a_(386037, _n_(386036, "plt", lambda: plt), "show"))
        _l_(386039)

    _c_(386043, _a_(386042, _n_(386041, "plt", lambda: plt), "clf"))
    _l_(386044)


if _n_(386046, "__name__", lambda: __name__) == '__main__':
    _l_(386078)

    path='../tf_files/data_audio/'
    _l_(386047)

    folders=_c_(386051, _a_(386049, _n_(386048, "glob", lambda: glob), "glob"), _n_(386050, "path", lambda: path)+'*')
    _l_(386052)
    for folder in _n_(386053, "folders", lambda: folders):
        _l_(386077)

        waves = _c_(386057, _a_(386055, _n_(386054, "glob", lambda: glob), "glob"), _n_(386056, "folder", lambda: folder)+'/' + '*.wav')
        _l_(386058)
        _c_(386061, _n_(386059, "print", lambda: print), _n_(386060, "waves", lambda: waves))
        _l_(386062)
        if _c_(386065, _n_(386063, "len", lambda: len), _n_(386064, "waves", lambda: waves)) == 0:
            _l_(386067)

            continue
            _l_(386066)
        for f in _n_(386068, "waves", lambda: waves):
            _l_(386076)

            #try:
            _c_(386070, _n_(386069, "print", lambda: print), "Generating spectrograms..")
            _l_(386071)
            _c_(386074, _n_(386072, "plotstft", lambda: plotstft), _n_(386073, "f", lambda: f))
            _l_(386075)