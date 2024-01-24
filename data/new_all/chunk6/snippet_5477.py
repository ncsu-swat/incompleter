# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65864101/python-deepspeech-typeerror-init-takes-2-positional-arguments-but-3-were
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import deepspeech
    _l_(338167)

except ImportError:
    pass
try:
    import numpy as np
    _l_(338169)

except ImportError:
    pass
try:
    import os
    _l_(338171)

except ImportError:
    pass
try:
    import pyaudio
    _l_(338173)

except ImportError:
    pass
try:
    import time
    _l_(338175)

except ImportError:
    pass

# DeepSpeech parameters
DEEPSPEECH_MODEL_DIR = 'deepspeech-0.9.3-models'
_l_(338176)
MODEL_FILE_PATH = _c_(338181, _a_(338179, _a_(338178, _n_(338177, "os", lambda: os), "path"), "join"), _n_(338180, "DEEPSPEECH_MODEL_DIR", lambda: DEEPSPEECH_MODEL_DIR), 'output_graph.pbmm')
_l_(338182)
BEAM_WIDTH = 500
_l_(338183)
LM_FILE_PATH = _c_(338188, _a_(338186, _a_(338185, _n_(338184, "os", lambda: os), "path"), "join"), _n_(338187, "DEEPSPEECH_MODEL_DIR", lambda: DEEPSPEECH_MODEL_DIR), 'lm.binary')
_l_(338189)
TRIE_FILE_PATH = _c_(338194, _a_(338192, _a_(338191, _n_(338190, "os", lambda: os), "path"), "join"), _n_(338193, "DEEPSPEECH_MODEL_DIR", lambda: DEEPSPEECH_MODEL_DIR), 'trie')
_l_(338195)
LM_ALPHA = 0.75
_l_(338196)
LM_BETA = 1.85
_l_(338197)

# Make DeepSpeech Model
model = _c_(338202, _a_(338199, _n_(338198, "deepspeech", lambda: deepspeech), "Model"), _n_(338200, "MODEL_FILE_PATH", lambda: MODEL_FILE_PATH), _n_(338201, "BEAM_WIDTH", lambda: BEAM_WIDTH))
_l_(338203)
_c_(338210, _a_(338205, _n_(338204, "model", lambda: model), "enableDecoderWithLM"), _n_(338206, "LM_FILE_PATH", lambda: LM_FILE_PATH), _n_(338207, "TRIE_FILE_PATH", lambda: TRIE_FILE_PATH), _n_(338208, "LM_ALPHA", lambda: LM_ALPHA), _n_(338209, "LM_BETA", lambda: LM_BETA))
_l_(338211)

# Create a Streaming session
context = _c_(338214, _a_(338213, _n_(338212, "model", lambda: model), "createStream"))
_l_(338215)

# Encapsulate DeepSpeech audio feeding into a callback for PyAudio
text_so_far = ''
_l_(338216)
def process_audio(in_data, frame_count, time_info, status):
    _l_(338251)

    global text_so_far
    _l_(338217)
    data16 = _c_(338223, _a_(338219, _n_(338218, "np", lambda: np), "frombuffer"), _n_(338220, "in_data", lambda: in_data), dtype=_a_(338222, _n_(338221, "np", lambda: np), "int16"))
    _l_(338224)
    _c_(338229, _a_(338226, _n_(338225, "model", lambda: model), "feedAudioContent"), _n_(338227, "context", lambda: context), _n_(338228, "data16", lambda: data16))
    _l_(338230)
    text = _c_(338234, _a_(338232, _n_(338231, "model", lambda: model), "intermediateDecode"), _n_(338233, "context", lambda: context))
    _l_(338235)
    if _n_(338236, "text", lambda: text) != _n_(338237, "text_so_far", lambda: text_so_far):
        _l_(338246)

        _c_(338242, _n_(338238, "print", lambda: print), _c_(338241, _a_(338239, 'Interim text = {}', "format"), _n_(338240, "text", lambda: text)))
        _l_(338243)
        text_so_far = _n_(338244, "text", lambda: text)
        _l_(338245)
    aux = (_n_(338247, "in_data", lambda: in_data), _a_(338249, _n_(338248, "pyaudio", lambda: pyaudio), "paContinue"))
    _l_(338250)
    return aux

# PyAudio parameters
FORMAT = _a_(338253, _n_(338252, "pyaudio", lambda: pyaudio), "paInt16")
_l_(338254)
CHANNELS = 1
_l_(338255)
RATE = 16000
_l_(338256)
CHUNK_SIZE = 1024
_l_(338257)

# Feed audio to deepspeech in a callback to PyAudio
audio = _c_(338260, _a_(338259, _n_(338258, "pyaudio", lambda: pyaudio), "PyAudio"))
_l_(338261)
stream = _c_(338269, _a_(338263, _n_(338262, "audio", lambda: audio), "open"), format=_n_(338264, "FORMAT", lambda: FORMAT),
    channels=_n_(338265, "CHANNELS", lambda: CHANNELS),
    rate=_n_(338266, "RATE", lambda: RATE),
    input=True,
    frames_per_buffer=_n_(338267, "CHUNK_SIZE", lambda: CHUNK_SIZE),
    stream_callback=_n_(338268, "process_audio", lambda: process_audio)
)
_l_(338270)

_c_(338272, _n_(338271, "print", lambda: print), 'Please start speaking, when done press Ctrl-C ...')
_l_(338273)
_c_(338276, _a_(338275, _n_(338274, "stream", lambda: stream), "start_stream"))
_l_(338277)

try:
    _l_(338314)

    while _c_(338280, _a_(338279, _n_(338278, "stream", lambda: stream), "is_active")):
        _l_(338285)

        _c_(338283, _a_(338282, _n_(338281, "time", lambda: time), "sleep"), 0.1)
        _l_(338284)
except _n_(338286, "KeyboardInterrupt", lambda: KeyboardInterrupt):
    _l_(338313)

    # PyAudio
    _c_(338289, _a_(338288, _n_(338287, "stream", lambda: stream), "stop_stream"))
    _l_(338290)
    _c_(338293, _a_(338292, _n_(338291, "stream", lambda: stream), "close"))
    _l_(338294)
    _c_(338297, _a_(338296, _n_(338295, "audio", lambda: audio), "terminate"))
    _l_(338298)
    _c_(338300, _n_(338299, "print", lambda: print), 'Finished recording.')
    _l_(338301)
    # DeepSpeech
    text = _c_(338305, _a_(338303, _n_(338302, "model", lambda: model), "finishStream"), _n_(338304, "context", lambda: context))
    _l_(338306)
    _c_(338311, _n_(338307, "print", lambda: print), _c_(338310, _a_(338308, 'Final text = {}', "format"), _n_(338309, "text", lambda: text)))
    _l_(338312)