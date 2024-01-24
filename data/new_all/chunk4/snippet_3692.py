# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69710537/why-does-this-happen-attributeerror-shape
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
video = _c_(593448, _n_(593447, "VideoFileClip", lambda: VideoFileClip), r'C:\Users\TheD4\OneDrive\Desktop\bac.mp4')
_l_(593449)
frames = []
_l_(593450)
video_duration = 3
_l_(593451)
for line in _n_(593452, "lines", lambda: lines):
    _l_(593504)

    if _n_(593453, "y_text", lambda: y_text) < 560:
        _l_(593503)

        _c_(593460, _a_(593455, _n_(593454, "draw", lambda: draw), "text"), ((40), 10 + _n_(593456, "y_text", lambda: y_text)), _n_(593457, "line", lambda: line), font=_n_(593458, "font_type1", lambda: font_type1), fill=_n_(593459, "color", lambda: color))
        _l_(593461)
        y_text += _n_(593462, "height", lambda: height)
        _l_(593463)
        cropped = _c_(593472, _a_(593465, _n_(593464, "image", lambda: image), "crop"), (0,0,_a_(593467, _n_(593466, "image", lambda: image), "width"),_n_(593468, "y_text", lambda: y_text)-4+_c_(593471, _n_(593469, "int", lambda: int), _n_(593470, "height", lambda: height)/2)))
        _l_(593473)
        _c_(593477, _a_(593475, _n_(593474, "frames", lambda: frames), "append"), _n_(593476, "cropped", lambda: cropped))
        _l_(593478)
    elif _n_(593479, "y_text2", lambda: y_text2) < 560:
        _l_(593502)

        _c_(593486, _a_(593481, _n_(593480, "draw2", lambda: draw2), "text"), ((40), _n_(593482, "y_text2", lambda: y_text2)), _n_(593483, "line", lambda: line), font=_n_(593484, "font_type1", lambda: font_type1), fill=_n_(593485, "color", lambda: color))
        _l_(593487)
        y_text2 += _n_(593488, "height", lambda: height)
        _l_(593489)
        cropped2 = _c_(593495, _a_(593491, _n_(593490, "image2", lambda: image2), "crop"), (0,0,_a_(593493, _n_(593492, "image", lambda: image), "width"),_n_(593494, "y_text2", lambda: y_text2)+4))
        _l_(593496)
        _c_(593500, _a_(593498, _n_(593497, "frames", lambda: frames), "append"), _n_(593499, "cropped2", lambda: cropped2))
        _l_(593501)


clips = []
_l_(593505)
for frame in _n_(593506, "frames", lambda: frames):
    _l_(593532)

    logo = _c_(593514, _a_(593513, _c_(593512, _a_(593510, _c_(593509, _n_(593507, "ImageClip", lambda: ImageClip), _n_(593508, "frame", lambda: frame)), "set_duration"), _n_(593511, "video_duration", lambda: video_duration)), "set_position"), (0,0.10), relative=True)
    _l_(593515)
    video = _c_(593520, _a_(593517, _n_(593516, "video", lambda: video), "subclip"), _n_(593518, "video_duration", lambda: video_duration), _n_(593519, "video_duration", lambda: video_duration)*2)  
    _l_(593521)  
    final = _c_(593525, _n_(593522, "CompositeVideoClip", lambda: CompositeVideoClip), [_n_(593523, "video", lambda: video), _n_(593524, "logo", lambda: logo)])
    _l_(593526)
    _c_(593530, _a_(593528, _n_(593527, "clips", lambda: clips), "append"), _n_(593529, "final", lambda: final))
    _l_(593531)


video_clip = _c_(593535, _n_(593533, "concatenate_videoclips", lambda: concatenate_videoclips), _n_(593534, "clips", lambda: clips), method='chain')
_l_(593536)
_c_(593539, _a_(593538, _n_(593537, "video_clip", lambda: video_clip), "write_videofile"), r'C:\Users\TheD4\OneDrive\Desktop\VideoFolder\video-output.mp4', fps=24, remove_temp=True, codec="libx264", audio_codec="aac")  
_l_(593540)  