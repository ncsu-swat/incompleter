# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76137318/attributeerror-no-librosa-attribute-match-events
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import librosa
    _l_(610223)

except ImportError:
    pass
try:
    import numpy as np
    _l_(610225)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(610227)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(610229)

except ImportError:
    pass
try:
    import sounddevice as sd
    _l_(610231)

except ImportError:
    pass
try:
    from scipy.spatial.distance import euclidean
    _l_(610233)

except ImportError:
    pass
try:
    from fastdtw import fastdtw
    _l_(610235)

except ImportError:
    pass
try:
    import os
    _l_(610237)

except ImportError:
    pass
try:
    from secventa import semnal_secventa
    _l_(610239)

except ImportError:
    pass
try:
    from secventa import sr
    _l_(610241)

except ImportError:
    pass
try:
    from secventa import mfcc_matrix_secventa
    _l_(610243)

except ImportError:
    pass
try:
    from cheie1 import semnal_key
    _l_(610245)

except ImportError:
    pass
try:
    from cheie1 import mfcc_matrix_key
    _l_(610247)

except ImportError:
    pass


audio_dir = 'C:/Users/Daniel/OneDrive - Technical University of Cluj-Napoca/Desktop/Proiect_PSV/fisier_secvente'
_l_(610248)
audio_dir_key = 'C:/Users/Daniel/OneDrive - Technical University of Cluj-Napoca/Desktop/Proiect_PSV/fisier_cuv_cheie'
_l_(610249)

audio_files = _c_(610253, _a_(610251, _n_(610250, "os", lambda: os), "listdir"), _n_(610252, "audio_dir", lambda: audio_dir))
_l_(610254)
audio_files_key = _c_(610258, _a_(610256, _n_(610255, "os", lambda: os), "listdir"), _n_(610257, "audio_dir_key", lambda: audio_dir_key))
_l_(610259)

def find_keyword_time(audio_file_path, keyword):
    _l_(610300)

    semnal, sr = _c_(610263, _a_(610261, _n_(610260, "librosa", lambda: librosa), "load"), _n_(610262, "audio_file_path", lambda: audio_file_path), sr=16000)
    _l_(610264)
    keyword_samples = _c_(610280, _a_(610266, _n_(610265, "librosa", lambda: librosa), "samples_to_frames"), _c_(610279, _a_(610268, _n_(610267, "librosa", lambda: librosa), "match_events"), _c_(610273, _a_(610271, _a_(610270, _n_(610269, "librosa", lambda: librosa), "onset"), "onset_detect"), _n_(610272, "semnal", lambda: semnal)), _c_(610278, _a_(610276, _a_(610275, _n_(610274, "librosa", lambda: librosa), "onset"), "onset_detect"), _n_(610277, "keyword", lambda: keyword))))
    _l_(610281)
    start_time = _c_(610286, _a_(610283, _n_(610282, "librosa", lambda: librosa), "frames_to_time"), _n_(610284, "keyword_samples", lambda: keyword_samples)[0], sr=_n_(610285, "sr", lambda: sr))
    _l_(610287)
    end_time = _c_(610292, _a_(610289, _n_(610288, "librosa", lambda: librosa), "frames_to_time"), _n_(610290, "keyword_samples", lambda: keyword_samples)[-1], sr=_n_(610291, "sr", lambda: sr))
    _l_(610293)
    _c_(610298, _n_(610294, "print", lambda: print), f'Cuvantul cheie "{_n_(610295, "keyword", lambda: keyword)}" se afla de la  {_n_(610296, "start_time", lambda: start_time)} secunde pana la {_n_(610297, "end_time", lambda: end_time)} secunde in secventa originala')
    _l_(610299)

for file in _n_(610301, 'audio_files', lambda: audio_files):
    _l_(610493)

    semnal_secventa, sr = _c_(610310, _a_(610303, _n_(610302, 'librosa', lambda: librosa), 'load'), _c_(610309, _a_(610306, _a_(610305, _n_(610304, 'os', lambda: os), 'path'), 'join'), _n_(610307, 'audio_dir', lambda: audio_dir), _n_(610308, 'file', lambda: file)), sr=16000)
    _l_(610311)
    found_keywords = []
    _l_(610312)
    for file_key in _n_(610313, 'audio_files_key', lambda: audio_files_key):
        _l_(610401)

        semnal_key, sr = _c_(610322, _a_(610315, _n_(610314, 'librosa', lambda: librosa), 'load'), _c_(610321, _a_(610318, _a_(610317, _n_(610316, 'os', lambda: os), 'path'), 'join'), _n_(610319, 'audio_dir_key', lambda: audio_dir_key), _n_(610320, 'file_key', lambda: file_key)), sr=16000)
        _l_(610323)
        step = 100
        _l_(610324)
        nr_frames = _c_(610333, _n_(610325, 'int', lambda: int), (_c_(610328, _n_(610326, 'len', lambda: len), _n_(610327, 'semnal_secventa', lambda: semnal_secventa))-_c_(610331, _n_(610329, 'len', lambda: len), _n_(610330, 'semnal_key', lambda: semnal_key)))/_n_(610332, 'step', lambda: step))
        _l_(610334)
        D = _c_(610338, _a_(610336, _n_(610335, 'np', lambda: np), 'zeros'), _n_(610337, 'nr_frames', lambda: nr_frames)-1)
        _l_(610339)
        for k in _c_(610342, _n_(610340, 'range', lambda: range), 0, _n_(610341, 'nr_frames', lambda: nr_frames) - 1):
            _l_(610382)

            signal1 = _n_(610343, 'semnal_secventa', lambda: semnal_secventa)[_c_(610347, _n_(610344, 'int', lambda: int), _n_(610345, 'k', lambda: k)*_n_(610346, 'step', lambda: step)):_c_(610351, _n_(610348, 'int', lambda: int), _n_(610349, 'k', lambda: k)*_n_(610350, 'step', lambda: step)) + _c_(610354, _n_(610352, 'len', lambda: len), _n_(610353, 'semnal_key', lambda: semnal_key))-1]
            _l_(610355)
            mfcc1 = _c_(610361, _a_(610358, _a_(610357, _n_(610356, 'librosa', lambda: librosa), 'feature'), 'mfcc'), y=_n_(610359, 'signal1', lambda: signal1), sr=_n_(610360, 'sr', lambda: sr))
            _l_(610362)
            mfcc2 = _c_(610368, _a_(610365, _a_(610364, _n_(610363, 'librosa', lambda: librosa), 'feature'), 'mfcc'), y=_n_(610366, 'semnal_key', lambda: semnal_key), sr=_n_(610367, 'sr', lambda: sr))
            _l_(610369)
            val, path = _c_(610376, _n_(610370, 'fastdtw', lambda: fastdtw), _a_(610372, _n_(610371, 'mfcc1', lambda: mfcc1), 'T'), _a_(610374, _n_(610373, 'mfcc2', lambda: mfcc2), 'T'), dist=_n_(610375, 'euclidean', lambda: euclidean))
            _l_(610377)
            _n_(610378, 'D', lambda: D)[_n_(610379, 'k', lambda: k)] = _n_(610380, 'val', lambda: val)
            _l_(610381)

        dist_min=_c_(610386, _a_(610384, _n_(610383, 'np', lambda: np), 'amin'), _n_(610385, 'D', lambda: D))
        _l_(610387)
        if _n_(610388, 'dist_min', lambda: dist_min) < 300:
            _l_(610400)

            index = _c_(610393, _a_(610390, _n_(610389, 'np', lambda: np), 'where'), _n_(610391, 'D', lambda: D) == _n_(610392, 'dist_min', lambda: dist_min))[0][0]
            _l_(610394)
            _c_(610398, _a_(610396, _n_(610395, 'found_keywords', lambda: found_keywords), 'append'), _n_(610397, 'file_key', lambda: file_key))
            _l_(610399)

    if _c_(610404, _n_(610402, 'len', lambda: len), _n_(610403, 'found_keywords', lambda: found_keywords)) > 0:
        _l_(610492)

        _c_(610410, _n_(610405, 'print', lambda: print), f"In secventa audio {_n_(610406, 'file', lambda: file)} am gasit cuvantul cheie {_c_(610409, _a_(610407, ' si ', 'join'), _n_(610408, 'found_keywords', lambda: found_keywords))}")
        _l_(610411)

        for keyword in _n_(610412, "found_keywords", lambda: found_keywords):
            _l_(610487)

            semnal_key, sr = _c_(610421, _a_(610414, _n_(610413, "librosa", lambda: librosa), "load"), _c_(610420, _a_(610417, _a_(610416, _n_(610415, "os", lambda: os), "path"), "join"), _n_(610418, "audio_dir_key", lambda: audio_dir_key), _n_(610419, "keyword", lambda: keyword)), sr=16000)
            _l_(610422)
            # Creare figura cu 2 subplot-uri   
            fig, (ax1, ax2) = _c_(610425, _a_(610424, _n_(610423, "plt", lambda: plt), "subplots"), 2, 1)
            _l_(610426)

            # Plotare waveform in primul subplot
            _c_(610433, _a_(610429, _a_(610428, _n_(610427, "librosa", lambda: librosa), "display"), "waveshow"), _n_(610430, "semnal_key", lambda: semnal_key), sr=_n_(610431, "sr", lambda: sr), ax=_n_(610432, "ax1", lambda: ax1))
            _l_(610434)
            _c_(610438, _a_(610436, _n_(610435, "ax1", lambda: ax1), "set"), title=f'Waveform pentru {_n_(610437, "keyword", lambda: keyword)}', xlabel='Time', ylabel='Amplitude')
            _l_(610439)

            # Plotare spectrograma in al doilea subplot
            D = _c_(610446, _a_(610441, _n_(610440, 'np', lambda: np), 'abs'), _c_(610445, _a_(610443, _n_(610442, 'librosa', lambda: librosa), 'stft'), _n_(610444, 'semnal_key', lambda: semnal_key)))
            _l_(610447)
            img = _c_(610458, _a_(610450, _a_(610449, _n_(610448, 'librosa', lambda: librosa), 'display'), 'specshow'), _c_(610456, _a_(610452, _n_(610451, 'librosa', lambda: librosa), 'amplitude_to_db'), _n_(610453, 'D', lambda: D), ref=_a_(610455, _n_(610454, 'np', lambda: np), 'max')), y_axis='log', x_axis='time', ax=_n_(610457, 'ax2', lambda: ax2))
            _l_(610459)
            _c_(610462, _a_(610461, _n_(610460, 'ax2', lambda: ax2), 'set'), title='Spectrogram')
            _l_(610463)
            _c_(610468, _a_(610465, _n_(610464, 'fig', lambda: fig), 'colorbar'), _n_(610466, 'img', lambda: img), ax=_n_(610467, 'ax2', lambda: ax2), format='%+2.0f dB')
            _l_(610469)
            
            # Find start and end time of keyword
            _c_(610477, _n_(610470, 'find_keyword_time', lambda: find_keyword_time), _c_(610476, _a_(610473, _a_(610472, _n_(610471, 'os', lambda: os), 'path'), 'join'), _n_(610474, 'audio_dir_key', lambda: audio_dir_key), _n_(610475, 'keyword', lambda: keyword)), 'keyword')
            _l_(610478)
    
            _c_(610481, _a_(610480, _n_(610479, 'plt', lambda: plt), 'tight_layout'))
            _l_(610482)
            _c_(610485, _a_(610484, _n_(610483, 'plt', lambda: plt), 'show'))  
            _l_(610486)  
    else:
     _c_(610490, _n_(610488, 'print', lambda: print), f"In secventa audio {_n_(610489, 'file', lambda: file)} nu am gasit niciun cuvant cheie")
     _l_(610491)