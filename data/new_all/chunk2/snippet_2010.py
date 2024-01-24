# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70387003/tkinter-videoplayer-library-to-play-a-video-typeerror-init-got-multiple-valu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(432199)

except ImportError:
    pass
try:
    from tkVideoPlayer import TkinterVideo
    _l_(432201)

except ImportError:
    pass


HEIGHT = 700
_l_(432202)
WIDTH = 800
_l_(432203)



root = _c_(432206, _a_(432205, _n_(432204, "tk", lambda: tk), "Tk"))
_l_(432207)

#Canvas
canvas = _c_(432213, _a_(432209, _n_(432208, "tk", lambda: tk), "Canvas"), _n_(432210, "root", lambda: root), height = _n_(432211, "HEIGHT", lambda: HEIGHT), width=_n_(432212, "WIDTH", lambda: WIDTH))
_l_(432214)
_c_(432217, _a_(432216, _n_(432215, "canvas", lambda: canvas), "pack"))
_l_(432218)

#Background Picture
background_img = _c_(432221, _a_(432220, _n_(432219, "tk", lambda: tk), "PhotoImage"), file = "GundamNarrative2.png")
_l_(432222)
background_label = _c_(432227, _a_(432224, _n_(432223, "tk", lambda: tk), "Label"), _n_(432225, "root", lambda: root), image=_n_(432226, "background_img", lambda: background_img))
_l_(432228)
_c_(432231, _a_(432230, _n_(432229, "background_label", lambda: background_label), "place"), relwidth=1, relheight=1)
_l_(432232)

#Background
background = _c_(432236, _a_(432234, _n_(432233, "tk", lambda: tk), "Frame"), _n_(432235, "root", lambda: root), bg = "blue")
_l_(432237)
_c_(432240, _a_(432239, _n_(432238, "background", lambda: background), "place"), relx=.5, rely=.1, relwidth=0.75, relheight=0.1, anchor="n")
_l_(432241)

# Buttons
record_button = _c_(432245, _a_(432243, _n_(432242, "tk", lambda: tk), "Button"), _n_(432244, "background", lambda: background), text = "Record", bg = "green")
_l_(432246)
_c_(432249, _a_(432248, _n_(432247, "record_button", lambda: record_button), "place"), relx = 0, rely = .5, relwidth = 0.15, relheight = .5)
_l_(432250)

skeleton_button = _c_(432254, _a_(432252, _n_(432251, "tk", lambda: tk), "Button"), _n_(432253, "background", lambda: background), text = "Skeleton", bg = "red")
_l_(432255)
_c_(432258, _a_(432257, _n_(432256, "skeleton_button", lambda: skeleton_button), "place"), relx = .4, rely = .5, relwidth = 0.15, relheight = .5)
_l_(432259)

frame_button = _c_(432263, _a_(432261, _n_(432260, "tk", lambda: tk), "Button"), _n_(432262, "background", lambda: background), text = "Frame", bg = "yellow")
_l_(432264)
_c_(432267, _a_(432266, _n_(432265, "frame_button", lambda: frame_button), "place"), relx = .85, rely = .5, relwidth = 0.15, relheight = .5)
_l_(432268)

#Label
video_label = _c_(432272, _a_(432270, _n_(432269, "tk", lambda: tk), "Label"), _n_(432271, "background", lambda: background), text = "Enter video name below")
_l_(432273)
_c_(432276, _a_(432275, _n_(432274, "video_label", lambda: video_label), "place"), relx = 0.4, rely=0, relwidth=.25, relheight=.15)
_l_(432277)

#Entry Area
entry = _c_(432281, _a_(432279, _n_(432278, "tk", lambda: tk), "Entry"), _n_(432280, "background", lambda: background), bg = 'gray')
_l_(432282)
_c_(432285, _a_(432284, _n_(432283, "entry", lambda: entry), "place"), relx = 0.4, rely=.15, relwidth=.25, relheight=.35)
_l_(432286)

#Bottom Frame
bottom_frame = _c_(432290, _a_(432288, _n_(432287, "tk", lambda: tk), "Frame"), _n_(432289, "root", lambda: root), bg = "blue", bd=10)
_l_(432291)
_c_(432294, _a_(432293, _n_(432292, "bottom_frame", lambda: bottom_frame), "place"), relx = .5, rely=0.25, relwidth=.75, relheight=.65, anchor = "n")
_l_(432295)

#Screen
screen = _c_(432299, _a_(432297, _n_(432296, "tk", lambda: tk), "Label"), _n_(432298, "bottom_frame", lambda: bottom_frame), text = "I want video to play here", bg = "gray")
_l_(432300)
_c_(432303, _a_(432302, _n_(432301, "screen", lambda: screen), "place"), relx=0, rely=0, relwidth=1, relheight=1)
_l_(432304)

#Error in line below
videoplayer = _c_(432307, _n_(432305, "TkinterVideo", lambda: TkinterVideo), _n_(432306, "screen", lambda: screen), scaled=True, pre_load=False)
_l_(432308)
_c_(432311, _a_(432310, _n_(432309, "videoplayer", lambda: videoplayer), "load"), "C:\\Users\\jcoli\\PycharmProjects\\SwimCodeProject\\PoseVideos\\Jordan.mov")
_l_(432312)
_c_(432315, _a_(432314, _n_(432313, "videoplayer", lambda: videoplayer), "place"), relx=0, rely=0, relwidth=1, relheight=1)
_l_(432316)

_c_(432319, _a_(432318, _n_(432317, "videoplayer", lambda: videoplayer), "play"))
_l_(432320)


_c_(432323, _a_(432322, _n_(432321, "root", lambda: root), "mainloop"))
_l_(432324)