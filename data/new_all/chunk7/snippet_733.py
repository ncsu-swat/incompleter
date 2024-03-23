# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69032946/python-process-typeerror-no-default-reduce-due-to-non-trivial-cinit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from aiohttp import web
    _l_(389230)

except ImportError:
    pass
try:
    from aiortc.mediastreams import MediaStreamTrack
    _l_(389232)

except ImportError:
    pass
try:
    from aiortc import RTCPeerConnection, RTCSessionDescription
    _l_(389234)

except ImportError:
    pass
try:
    from aiortc.contrib.media import MediaPlayer
    _l_(389236)

except ImportError:
    pass
try:
    from pydub import AudioSegment
    _l_(389238)

except ImportError:
    pass
try:
    import av
    _l_(389240)

except ImportError:
    pass
try:
    from aiohttp import web
    _l_(389242)

except ImportError:
    pass
try:
    from aiortc.mediastreams import MediaStreamTrack
    _l_(389244)

except ImportError:
    pass
try:
    from aiortc import RTCPeerConnection, RTCSessionDescription
    _l_(389246)

except ImportError:
    pass
try:
    from aiortc.contrib.media import MediaPlayer
    _l_(389248)

except ImportError:
    pass
try:
    from pydub import AudioSegment
    _l_(389250)

except ImportError:
    pass
try:
    import av
    _l_(389252)

except ImportError:
    pass
try:
    import pyaudio
    _l_(389254)

except ImportError:
    pass
try:
    import asyncio
    _l_(389256)

except ImportError:
    pass
try:
    import json
    _l_(389258)

except ImportError:
    pass
try:
    import os
    _l_(389260)

except ImportError:
    pass
try:
    from multiprocessing import Process, freeze_support, Queue
    _l_(389262)

except ImportError:
    pass
try:
    import sys
    _l_(389264)

except ImportError:
    pass
try:
    import threading
    _l_(389266)

except ImportError:
    pass
try:
    from time import sleep
    _l_(389268)

except ImportError:
    pass
try:
    import fractions
    _l_(389270)

except ImportError:
    pass
try:
    import time
    _l_(389272)

except ImportError:
    pass

class RadioServer(_n_(389273, "Process", lambda: Process)):
    _l_(389553)

    def __init__(self,q):
        _l_(389294)

        _c_(389276, _a_(389275, _n_(389274, "super", lambda: super)(), "__init__"))
        _l_(389277)
        _n_(389278, "self", lambda: self).q = _n_(389279, "q", lambda: q)
        _l_(389280)
        _n_(389281, "self", lambda: self).ROOT = _c_(389286, _a_(389284, _a_(389283, _n_(389282, "os", lambda: os), "path"), "dirname"), _n_(389285, "__file__", lambda: __file__))
        _l_(389287)
        _n_(389288, "self", lambda: self).pcs = []
        _l_(389289)
        _n_(389290, "self", lambda: self).channels = []
        _l_(389291)
        _n_(389292, "self", lambda: self).stream_offers = []
        _l_(389293)
    
    def run(self):
        _l_(389354)

        _n_(389295, "self", lambda: self).app = _c_(389298, _a_(389297, _n_(389296, "web", lambda: web), "Application"))
        _l_(389299)
        _c_(389306, _a_(389303, _a_(389302, _a_(389301, _n_(389300, "self", lambda: self), "app"), "on_shutdown"), "append"), _a_(389305, _n_(389304, "self", lambda: self), "on_shutdown"))
        _l_(389307)
        _c_(389314, _a_(389311, _a_(389310, _a_(389309, _n_(389308, "self", lambda: self), "app"), "router"), "add_get"), "/", _a_(389313, _n_(389312, "self", lambda: self), "index"))
        _l_(389315)
        _c_(389322, _a_(389319, _a_(389318, _a_(389317, _n_(389316, "self", lambda: self), "app"), "router"), "add_get"), "/telephone_calls.js", _a_(389321, _n_(389320, "self", lambda: self), "javascript"))
        _l_(389323)
        _c_(389330, _a_(389327, _a_(389326, _a_(389325, _n_(389324, "self", lambda: self), "app"), "router"), "add_get"), "/jquery-3.5.1.min.js", _a_(389329, _n_(389328, "self", lambda: self), "jquery"))
        _l_(389331)
        _c_(389338, _a_(389335, _a_(389334, _a_(389333, _n_(389332, "self", lambda: self), "app"), "router"), "add_post"), "/offer", _a_(389337, _n_(389336, "self", lambda: self), "offer"))
        _l_(389339)
        
        _c_(389346, _a_(389345, _c_(389344, _a_(389341, _n_(389340, "threading", lambda: threading), "Thread"), target=_a_(389343, _n_(389342, "self", lambda: self), "fill_the_queues")), "start"))
        _l_(389347)
        _c_(389352, _a_(389349, _n_(389348, "web", lambda: web), "run_app"), _a_(389351, _n_(389350, "self", lambda: self), "app"), access_log=None, host="192.168.1.20", port="8080", ssl_context=None)
        _l_(389353)

    def fill_the_queues(self):
        _l_(389370)

        while(True):
            _l_(389369)

            frame = _c_(389358, _a_(389357, _a_(389356, _n_(389355, "self", lambda: self), "q"), "get"))
            _l_(389359)
            for stream_offer in _a_(389361, _n_(389360, "self", lambda: self), "stream_offers"):
                _l_(389368)

                _c_(389366, _a_(389364, _a_(389363, _n_(389362, "stream_offer", lambda: stream_offer), "q"), "put"), _n_(389365, "frame", lambda: frame))
                _l_(389367)

    async def index(self,request):
        _l_(389387)

        content = _c_(389380, _a_(389379, _c_(389378, _n_(389371, "open", lambda: open), _c_(389377, _a_(389374, _a_(389373, _n_(389372, "os", lambda: os), "path"), "join"), _a_(389376, _n_(389375, "self", lambda: self), "ROOT"), "index.html"), encoding="utf8"), "read"))
        _l_(389381)
        aux = _c_(389385, _a_(389383, _n_(389382, "web", lambda: web), "Response"), content_type="text/html", text=_n_(389384, "content", lambda: content))
        _l_(389386)
        return aux


    async def javascript(self,request):
        _l_(389404)

        content = _c_(389397, _a_(389396, _c_(389395, _n_(389388, "open", lambda: open), _c_(389394, _a_(389391, _a_(389390, _n_(389389, "os", lambda: os), "path"), "join"), _a_(389393, _n_(389392, "self", lambda: self), "ROOT"), "telephone_calls.js"), encoding="utf8"), "read"))
        _l_(389398)
        aux = _c_(389402, _a_(389400, _n_(389399, "web", lambda: web), "Response"), content_type="application/javascript", text=_n_(389401, "content", lambda: content))
        _l_(389403)
        return aux

    async def jquery(self,request):
        _l_(389421)

        content = _c_(389414, _a_(389413, _c_(389412, _n_(389405, "open", lambda: open), _c_(389411, _a_(389408, _a_(389407, _n_(389406, "os", lambda: os), "path"), "join"), _a_(389410, _n_(389409, "self", lambda: self), "ROOT"), "jquery-3.5.1.min.js"), encoding="utf8"), "read"))
        _l_(389415)
        aux = _c_(389419, _a_(389417, _n_(389416, "web", lambda: web), "Response"), content_type="application/javascript", text=_n_(389418, "content", lambda: content))
        _l_(389420)
        return aux

    async def offer(self,request):
        _l_(389522)

        params = await _c_(389424, _a_(389423, _n_(389422, "request", lambda: request), "json"))
        _l_(389425)
        offer = _c_(389429, _n_(389426, "RTCSessionDescription", lambda: RTCSessionDescription), sdp=_n_(389427, "params", lambda: params)["sdp"], type=_n_(389428, "params", lambda: params)["type"])
        _l_(389430)

        pc = _c_(389432, _n_(389431, "RTCPeerConnection", lambda: RTCPeerConnection))
        _l_(389433)
        _c_(389438, _a_(389436, _a_(389435, _n_(389434, "self", lambda: self), "pcs"), "append"), _n_(389437, "pc", lambda: pc))
        _l_(389439)

        # prepare epalxeis media
        _c_(389445, _a_(389442, _a_(389441, _n_(389440, "self", lambda: self), "stream_offers"), "append"), _c_(389444, _n_(389443, "CustomRadioStream", lambda: CustomRadioStream)))
        _l_(389446)
        _c_(389451, _a_(389448, _n_(389447, "pc", lambda: pc), "addTrack"), _a_(389450, _n_(389449, "self", lambda: self), "stream_offers")[-1])
        _l_(389452)

        #player = MediaPlayer(os.path.join(self.ROOT, "ΑΓΙΑ ΚΥΡΙΑΚΗ.mp3"))
        #pc.addTrack(player.audio)

        @_c_(389455, _a_(389454, _n_(389453, "pc", lambda: pc), "on"), "datachannel")
        def on_datachannel(channel):
            _l_(389472)

            _c_(389460, _a_(389458, _a_(389457, _n_(389456, "self", lambda: self), "channels"), "append"), _n_(389459, "channel", lambda: channel))
            _l_(389461)
            _c_(389470, _a_(389463, _n_(389462, "self", lambda: self), "send_channel_message"), _c_(389469, _n_(389464, "str", lambda: str), _c_(389468, _n_(389465, "len", lambda: len), _a_(389467, _n_(389466, "self", lambda: self), "pcs"))))
            _l_(389471)


        @_c_(389475, _a_(389474, _n_(389473, "pc", lambda: pc), "on"), "iceconnectionstatechange")
        async def on_iceconnectionstatechange():
            _l_(389494)

            if _a_(389477, _n_(389476, "pc", lambda: pc), "iceConnectionState") == "failed":
                _l_(389493)

                _c_(389482, _a_(389480, _a_(389479, _n_(389478, "self", lambda: self), "pcs"), "remove"), _n_(389481, "pc", lambda: pc))
                _l_(389483)
                _c_(389491, _n_(389484, "print", lambda: print), "Current peer connections:"+_c_(389490, _n_(389485, "str", lambda: str), _c_(389489, _n_(389486, "len", lambda: len), _a_(389488, _n_(389487, "self", lambda: self), "pcs"))))
                _l_(389492)

        # handle offer
        await _c_(389498, _a_(389496, _n_(389495, "pc", lambda: pc), "setRemoteDescription"), _n_(389497, "offer", lambda: offer))
        _l_(389499)

        # send answer
        answer = await _c_(389502, _a_(389501, _n_(389500, "pc", lambda: pc), "createAnswer"))
        _l_(389503)
        await _c_(389507, _a_(389505, _n_(389504, "pc", lambda: pc), "setLocalDescription"), _n_(389506, "answer", lambda: answer))
        _l_(389508)
        aux = _c_(389520, _a_(389510, _n_(389509, "web", lambda: web), "Response"), content_type="application/json",text=_c_(389519, _a_(389512, _n_(389511, "json", lambda: json), "dumps"), {"sdp": _a_(389515, _a_(389514, _n_(389513, "pc", lambda: pc), "localDescription"), "sdp"), "type": _a_(389518, _a_(389517, _n_(389516, "pc", lambda: pc), "localDescription"), "type")}))
        _l_(389521)
        
            

        return aux

    async def on_shutdown(self,app):
        _l_(389543)

        # close peer connections
        if _a_(389524, _n_(389523, "self", lambda: self), "pcs"):
            _l_(389542)

            coros = [_c_(389527, _a_(389526, _n_(389525, "pc", lambda: pc), "close")) for pc in _a_(389529, _n_(389528, "self", lambda: self), "pcs")]
            _l_(389530)
            await _c_(389534, _a_(389532, _n_(389531, "asyncio", lambda: asyncio), "gather"), *_n_(389533, "coros", lambda: coros))
            _l_(389535)
            _n_(389536, "self", lambda: self).pcs = []
            _l_(389537)
            _n_(389538, "self", lambda: self).channels = []
            _l_(389539)
            _n_(389540, "self", lambda: self).stream_offers = []
            _l_(389541)
    def send_channel_message(self,message):
        _l_(389552)

        for channel in _a_(389545, _n_(389544, "self", lambda: self), "channels"):
            _l_(389551)

            _c_(389549, _a_(389547, _n_(389546, "channel", lambda: channel), "send"), _n_(389548, "message", lambda: message))
            _l_(389550)

class CustomRadioStream(_n_(389554, "MediaStreamTrack", lambda: MediaStreamTrack)):
    _l_(389599)

    kind = "audio"
    _l_(389555)
    
    def __init__(self):
        _l_(389566)

        _c_(389558, _a_(389557, _n_(389556, "super", lambda: super)(), "__init__"))  # don't forget this!
        _l_(389559)  # don't forget this!
        
        _n_(389560, "self", lambda: self).q = _c_(389562, _n_(389561, "Queue", lambda: Queue))
        _l_(389563)
        _n_(389564, "self", lambda: self)._start = None
        _l_(389565)
    async def recv(self):
        _l_(389598)

        frame = _c_(389570, _a_(389569, _a_(389568, _n_(389567, "self", lambda: self), "q"), "get"))
        _l_(389571)
        frame_time = _a_(389573, _n_(389572, "frame", lambda: frame), "time")
        _l_(389574)
        if _a_(389576, _n_(389575, "self", lambda: self), "_start") is None:
            _l_(389595)

            _n_(389577, "self", lambda: self)._start = _c_(389580, _a_(389579, _n_(389578, "time", lambda: time), "time")) - _n_(389581, "frame_time", lambda: frame_time)
            _l_(389582)
        else:
            wait = _a_(389584, _n_(389583, "self", lambda: self), "_start") + _n_(389585, "frame_time", lambda: frame_time) - _c_(389588, _a_(389587, _n_(389586, "time", lambda: time), "time"))
            _l_(389589)
            await _c_(389593, _a_(389591, _n_(389590, "asyncio", lambda: asyncio), "sleep"), _n_(389592, "wait", lambda: wait))
            _l_(389594)
        aux = _n_(389596, "frame", lambda: frame)
        _l_(389597)
        return aux

class RadioOutputStream:
    _l_(389841)

    def __init__(self,q):
        _l_(389710)

        _n_(389600, "self", lambda: self).sample_rate = 44800
        _l_(389601)
        _n_(389602, "self", lambda: self).AUDIO_PTIME = 0.744
        _l_(389603)
        _n_(389604, "self", lambda: self).samples = _c_(389610, _n_(389605, "int", lambda: int), _a_(389607, _n_(389606, "self", lambda: self), "AUDIO_PTIME") * _a_(389609, _n_(389608, "self", lambda: self), "sample_rate"))
        _l_(389611)
        _n_(389612, "self", lambda: self).packet_time = 20
        _l_(389613)

        _n_(389614, "self", lambda: self).FORMAT = _a_(389616, _n_(389615, "pyaudio", lambda: pyaudio), "paInt16")
        _l_(389617)
        _n_(389618, "self", lambda: self).CHANNELS = 2
        _l_(389619)
        _n_(389620, "self", lambda: self).RATE = _a_(389622, _n_(389621, "self", lambda: self), "sample_rate")
        _l_(389623)
        _n_(389624, "self", lambda: self).CHUNK = _c_(389626, _n_(389625, "int", lambda: int), 44100*0.744)
        _l_(389627)

        
        _n_(389628, "self", lambda: self).files_directory = _c_(389632, _a_(389631, _a_(389630, _n_(389629, "os", lambda: os), "path"), "abspath"), r"C:\Users\Χρήστος\Music\Αναστάσιμα τροπάρια ή άλλα τροπάρια Δεσποτικών, Θεομητορικών ή άλλων εορτών Αγίων")
        _l_(389633)
        _n_(389634, "self", lambda: self).files_paths = _c_(389639, _a_(389636, _n_(389635, "os", lambda: os), "listdir"), _a_(389638, _n_(389637, "self", lambda: self), "files_directory"))
        _l_(389640)
        _n_(389641, "self", lambda: self).files_info = []
        _l_(389642)
        for song_file in _a_(389644, _n_(389643, "self", lambda: self), "files_paths"):
            _l_(389675)

            if ".mp3" in _c_(389647, _a_(389646, _n_(389645, "song_file", lambda: song_file), "lower")):
                _l_(389674)

                file_segment = _c_(389661, _a_(389658, _c_(389657, _a_(389649, _n_(389648, "AudioSegment", lambda: AudioSegment), "from_file"), _c_(389656, _a_(389652, _a_(389651, _n_(389650, "os", lambda: os), "path"), "join"), _a_(389654, _n_(389653, "self", lambda: self), "files_directory"), _n_(389655, "song_file", lambda: song_file))), "set_frame_rate"), _a_(389660, _n_(389659, "self", lambda: self), "sample_rate"))
                _l_(389662)
                duration_milliseconds = _c_(389665, _n_(389663, "len", lambda: len), _n_(389664, "file_segment", lambda: file_segment))
                _l_(389666)
                _c_(389672, _a_(389669, _a_(389668, _n_(389667, "self", lambda: self), "files_info"), "append"), {"file_segment":_n_(389670, "file_segment", lambda: file_segment),"duration_milliseconds":_n_(389671, "duration_milliseconds", lambda: duration_milliseconds)})
                _l_(389673)
        _n_(389676, "self", lambda: self).total_files = _c_(389680, _n_(389677, "len", lambda: len), _a_(389679, _n_(389678, "self", lambda: self), "files_info"))
        _l_(389681)
        _n_(389682, "self", lambda: self).current_file = 0
        _l_(389683)
        _n_(389684, "self", lambda: self).chunk_number = 0
        _l_(389685)

        _n_(389686, "self", lambda: self).silence = _c_(389691, _a_(389688, _n_(389687, "AudioSegment", lambda: AudioSegment), "silent"), duration=_a_(389690, _n_(389689, "self", lambda: self), "packet_time"))
        _l_(389692)

        _n_(389693, "self", lambda: self).q = _n_(389694, "q", lambda: q)
        _l_(389695)

        _n_(389696, "self", lambda: self).codec = _c_(389700, _a_(389699, _a_(389698, _n_(389697, "av", lambda: av), "CodecContext"), "create"), 'pcm_s16le', 'r')
        _l_(389701)
        _a_(389703, _n_(389702, "self", lambda: self), "codec").sample_rate = 44800
        _l_(389704)
        _a_(389706, _n_(389705, "self", lambda: self), "codec").channels = 2
        _l_(389707)

        _n_(389708, "self", lambda: self).audio_samples = 0
        _l_(389709)
    def run_stream(self):
        _l_(389840)

        while(True):
            _l_(389839)

            if((_a_(389712, _n_(389711, "self", lambda: self), "chunk_number")+1)*_a_(389714, _n_(389713, "self", lambda: self), "packet_time")<=_a_(389716, _n_(389715, "self", lambda: self), "files_info")[_a_(389718, _n_(389717, "self", lambda: self), "current_file")]["duration_milliseconds"]):
                _l_(389835)

                final_slice = _a_(389720, _n_(389719, "self", lambda: self), "files_info")[_a_(389722, _n_(389721, "self", lambda: self), "current_file")]["file_segment"][_a_(389724, _n_(389723, "self", lambda: self), "chunk_number")*_a_(389726, _n_(389725, "self", lambda: self), "packet_time"):(_a_(389728, _n_(389727, "self", lambda: self), "chunk_number")+1)*_a_(389730, _n_(389729, "self", lambda: self), "packet_time")]
                _l_(389731)
                #final_slice = final_slice + 100
                _n_(389732, "self", lambda: self).chunk_number += 1
                _l_(389733)

                packet = _c_(389738, _a_(389735, _n_(389734, "av", lambda: av), "Packet"), _a_(389737, _n_(389736, "final_slice", lambda: final_slice), "raw_data"))
                _l_(389739)
                frame = _c_(389744, _a_(389742, _a_(389741, _n_(389740, "self", lambda: self), "codec"), "decode"), _n_(389743, "packet", lambda: packet))[0]
                _l_(389745)
                _n_(389746, "frame", lambda: frame).pts = _a_(389748, _n_(389747, "self", lambda: self), "audio_samples")
                _l_(389749)
                _n_(389750, "frame", lambda: frame).time_base = _c_(389756, _a_(389752, _n_(389751, "fractions", lambda: fractions), "Fraction"), 1, _a_(389755, _a_(389754, _n_(389753, "self", lambda: self), "codec"), "sample_rate"))
                _l_(389757)
                _n_(389758, "self", lambda: self).audio_samples += _n_(389759, "frame", lambda: frame).samples
                _l_(389760)
                _c_(389765, _a_(389763, _a_(389762, _n_(389761, "self", lambda: self), "q"), "put"), _n_(389764, "frame", lambda: frame))
                _l_(389766)
            else:
                if(_a_(389768, _n_(389767, "self", lambda: self), "chunk_number")*_a_(389770, _n_(389769, "self", lambda: self), "packet_time")<_a_(389772, _n_(389771, "self", lambda: self), "files_info")[_a_(389774, _n_(389773, "self", lambda: self), "current_file")]["duration_milliseconds"]):
                    _l_(389834)

                    final_slice = _a_(389776, _n_(389775, "self", lambda: self), "files_info")[_a_(389778, _n_(389777, "self", lambda: self), "current_file")]["file_segment"][_a_(389780, _n_(389779, "self", lambda: self), "chunk_number")*_a_(389782, _n_(389781, "self", lambda: self), "packet_time"):]
                    _l_(389783)
                    final_slice = _n_(389784, "final_slice", lambda: final_slice) + _a_(389786, _n_(389785, "self", lambda: self), "silence")
                    _l_(389787)
                    #final_slice = final_slice + 100
                    _n_(389788, "self", lambda: self).chunk_number += 1
                    _l_(389789)


                    packet = _c_(389794, _a_(389791, _n_(389790, "av", lambda: av), "Packet"), _a_(389793, _n_(389792, "final_slice", lambda: final_slice), "raw_data"))
                    _l_(389795)
                    frame = _c_(389800, _a_(389798, _a_(389797, _n_(389796, "self", lambda: self), "codec"), "decode"), _n_(389799, "packet", lambda: packet))[0]
                    _l_(389801)
                    _n_(389802, "frame", lambda: frame).pts = _a_(389804, _n_(389803, "self", lambda: self), "audio_samples")
                    _l_(389805)
                    _n_(389806, "frame", lambda: frame).time_base = _c_(389812, _a_(389808, _n_(389807, "fractions", lambda: fractions), "Fraction"), 1, _a_(389811, _a_(389810, _n_(389809, "self", lambda: self), "codec"), "sample_rate"))
                    _l_(389813)
                    _n_(389814, "self", lambda: self).audio_samples += _n_(389815, "frame", lambda: frame).samples
                    _l_(389816)
                    _c_(389821, _a_(389819, _a_(389818, _n_(389817, "self", lambda: self), "q"), "put"), _n_(389820, "frame", lambda: frame))
                    _l_(389822)
                else:
                    #start song from begin
                    _n_(389823, "self", lambda: self).chunk_number=0
                    _l_(389824)
                    if _a_(389826, _n_(389825, "self", lambda: self), "current_file")==_a_(389828, _n_(389827, "self", lambda: self), "total_files")-1:
                        _l_(389833)

                        _n_(389829, "self", lambda: self).current_file = 0
                        _l_(389830)
                    else:
                        _n_(389831, "self", lambda: self).current_file += 1
                        _l_(389832)
                    
            _c_(389837, _n_(389836, "sleep", lambda: sleep), 0.01)
            _l_(389838)

if _n_(389842, "__name__", lambda: __name__) == "__main__":
    _l_(389872)

    _c_(389844, _n_(389843, "freeze_support", lambda: freeze_support))
    _l_(389845)

    q = _c_(389847, _n_(389846, "Queue", lambda: Queue))
    _l_(389848)
    radio_stream = _c_(389851, _n_(389849, "RadioOutputStream", lambda: RadioOutputStream), _n_(389850, "q", lambda: q))
    _l_(389852)
    _c_(389859, _a_(389858, _c_(389857, _a_(389854, _n_(389853, "threading", lambda: threading), "Thread"), target=_a_(389856, _n_(389855, "radio_stream", lambda: radio_stream), "run_stream")), "start"))
    _l_(389860)

    custom_server_child_process = _c_(389863, _n_(389861, "RadioServer", lambda: RadioServer), _n_(389862, "q", lambda: q))
    _l_(389864)
    _c_(389867, _a_(389866, _n_(389865, "custom_server_child_process", lambda: custom_server_child_process), "start"))
    _l_(389868)
    _c_(389870, _n_(389869, "print", lambda: print), "Thread and process started sucessfully.")
    _l_(389871)