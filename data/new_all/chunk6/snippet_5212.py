# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59298082/opencv-image-processing-gui-typeerror-on-click-diff-per-button-takes-1-posit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(346238)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(346240)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(346242)

except ImportError:
    pass
try:
    import glob
    _l_(346244)

except ImportError:
    pass
try:
    import os
    _l_(346246)

except ImportError:
    pass
try:
    import cv2
    _l_(346248)

except ImportError:
    pass
try:
    import numpy as np
    _l_(346250)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(346252)

except ImportError:
    pass
try:
    from PIL import ImageTk
    _l_(346254)

except ImportError:
    pass
try:
    from skimage.metrics import structural_similarity
    _l_(346256)

except ImportError:
    pass
class Button:
    _l_(346535)


    def __init__(self, root, frame2):
        _l_(346276)

        _n_(346257, "self", lambda: self).root = _n_(346258, "root", lambda: root)
        _l_(346259)
        _n_(346260, "self", lambda: self).frame2 = _n_(346261, "frame2", lambda: frame2)
        _l_(346262)
        _n_(346263, "self", lambda: self).radio_var = _c_(346266, _a_(346265, _n_(346264, "tk", lambda: tk), "IntVar"))
        _l_(346267)
        _n_(346268, "self", lambda: self).path_selected = 'none'
        _l_(346269)
        _n_(346270, "self", lambda: self).paths = []
        _l_(346271)
        _n_(346272, "self", lambda: self).radio_handle = []
        _l_(346273)
        _n_(346274, "self", lambda: self).check_value = []
        _l_(346275)

    def on_click_select_button(self, fname_label):
        _l_(346295)

        _c_(346278, _n_(346277, "print", lambda: print), 'select button clicked')
        _l_(346279)
        fileType = [('jpg/png file', ('*.jpg', '*.png'))]
        _l_(346280)
        _n_(346281, "self", lambda: self).path_selected = _c_(346285, _a_(346283, _n_(346282, "filedialog", lambda: filedialog), "askopenfilename"), filetypes=_n_(346284, "fileType", lambda: fileType))
        _l_(346286)
        _n_(346287, "fname_label", lambda: fname_label)['text'] = _c_(346293, _a_(346290, _a_(346289, _n_(346288, "os", lambda: os), "path"), "basename"), _a_(346292, _n_(346291, "self", lambda: self), "path_selected"))
        _l_(346294)

    def on_click_upload_button(self, path='None', image='None'):
        _l_(346330)

        _c_(346297, _n_(346296, "print", lambda: print), 'upload button clicked')
        _l_(346298)

        if _n_(346299, "path", lambda: path) == 'None':
            _l_(346309)

            path = _a_(346301, _n_(346300, "self", lambda: self), "path_selected")
            _l_(346302)
        else:
            _c_(346307, _a_(346304, _n_(346303, "cv2", lambda: cv2), "imwrite"), _n_(346305, "path", lambda: path), _n_(346306, "image", lambda: image))
            _l_(346308)

        if _n_(346310, "path", lambda: path) in _a_(346312, _n_(346311, "self", lambda: self), "paths"):
            _l_(346329)

            _c_(346316, _a_(346314, _n_(346313, "messagebox", lambda: messagebox), "showerror"), 'Upload Error', '"'
                                 + _n_(346315, "path", lambda: path)
                                 + '"' + ' is already uploaded.')
            _l_(346317)
        else:
            _c_(346322, _a_(346320, _a_(346319, _n_(346318, "self", lambda: self), "paths"), "append"), _n_(346321, "path", lambda: path))
            _l_(346323)
            _c_(346327, _a_(346325, _n_(346324, "self", lambda: self), "create_radio_button"), _n_(346326, "path", lambda: path))
            _l_(346328)

    def on_click_show_button(self):
        _l_(346370)

        _c_(346332, _n_(346331, "print", lambda: print), 'showButton clicked')
        _l_(346333)
        image = _c_(346342, _a_(346335, _n_(346334, "cv2", lambda: cv2), "imread"), _a_(346337, _n_(346336, "self", lambda: self), "paths")[_c_(346341, _a_(346340, _a_(346339, _n_(346338, "self", lambda: self), "radio_var"), "get"))])
        _l_(346343)
        file_name = _c_(346353, _a_(346346, _a_(346345, _n_(346344, "os", lambda: os), "path"), "basename"), _a_(346348, _n_(346347, "self", lambda: self), "paths")[_c_(346352, _a_(346351, _a_(346350, _n_(346349, "self", lambda: self), "radio_var"), "get"))])
        _l_(346354)
        name, ext = _c_(346359, _a_(346357, _a_(346356, _n_(346355, "os", lambda: os), "path"), "splitext"), _n_(346358, "file_name", lambda: file_name))
        _l_(346360)
        path = 'images/' + _n_(346361, "name", lambda: name) + '_' + _n_(346362, "ext", lambda: ext)
        _l_(346363)

        # cv2.imwrite(path, image)
        _c_(346368, _a_(346365, _n_(346364, "self", lambda: self), "open_image_window"), _n_(346366, "path", lambda: path), _n_(346367, "image", lambda: image))
        _l_(346369)

    def create_radio_button(self, path):
        _l_(346434)


        image = _c_(346374, _a_(346372, _n_(346371, "cv2", lambda: cv2), "imread"), _n_(346373, "path", lambda: path))
        _l_(346375)
        # image = cv2.resize(image,(120,120))
        image = _c_(346379, _a_(346377, _n_(346376, "self", lambda: self), "scale_to_height"), _n_(346378, "image", lambda: image), 120)
        _l_(346380)
        image_tk = _c_(346384, _a_(346382, _n_(346381, "self", lambda: self), "to_tk_image"), _n_(346383, "image", lambda: image))
        _l_(346385)

        radio_button = _c_(346397, _a_(346387, _n_(346386, "tk", lambda: tk), "Radiobutton"), _a_(346389, _n_(346388, "self", lambda: self), "frame2"), image=_n_(346390, "image_tk", lambda: image_tk),
                                      value=_c_(346394, _n_(346391, "len", lambda: len), _a_(346393, _n_(346392, "self", lambda: self), "radio_handle")),
                                      variable=_a_(346396, _n_(346395, "self", lambda: self), "radio_var"))
        _l_(346398)
        _c_(346402, _a_(346401, _a_(346400, _n_(346399, "self", lambda: self), "radio_var"), "set"), 0)
        _l_(346403)
        _c_(346408, _a_(346406, _a_(346405, _n_(346404, "self", lambda: self), "radio_handle"), "append"), _n_(346407, "radio_button", lambda: radio_button))
        _l_(346409)
        _c_(346415, _a_(346412, _a_(346411, _n_(346410, "self", lambda: self), "check_value"), "append"), _a_(346414, _n_(346413, "self", lambda: self), "radio_var"))
        _l_(346416)

        _c_(346427, _a_(346418, _n_(346417, "radio_button", lambda: radio_button), "grid"), row=(_c_(346422, _n_(346419, "len", lambda: len), _a_(346421, _n_(346420, "self", lambda: self), "radio_handle")) - 1) // 3,
                          column=(_c_(346426, _n_(346423, "len", lambda: len), _a_(346425, _n_(346424, "self", lambda: self), "radio_handle")) - 1) % 3)
        _l_(346428)
        _c_(346432, _a_(346431, _a_(346430, _n_(346429, "self", lambda: self), "root"), "mainloop"))
        _l_(346433)

    def open_image_window(self, path, image):
        _l_(346502)


        if _a_(346436, _n_(346435, "image", lambda: image), "shape")[0] > 300:
            _l_(346442)

            image = _c_(346440, _a_(346438, _n_(346437, "self", lambda: self), "scale_to_height"), _n_(346439, "image", lambda: image), 300)
            _l_(346441)

        img_win = _c_(346447, _a_(346444, _n_(346443, "tk", lambda: tk), "Toplevel"), _a_(346446, _n_(346445, "self", lambda: self), "root"))
        _l_(346448)
        fname = _c_(346453, _a_(346451, _a_(346450, _n_(346449, "os", lambda: os), "path"), "basename"), _n_(346452, "path", lambda: path))
        _l_(346454)
        _c_(346458, _a_(346456, _n_(346455, "img_win", lambda: img_win), "title"), _n_(346457, "fname", lambda: fname))
        _l_(346459)
        img_canvas = _c_(346467, _a_(346461, _n_(346460, "tk", lambda: tk), "Canvas"), _n_(346462, "img_win", lambda: img_win), width=_a_(346464, _n_(346463, "image", lambda: image), "shape")[1],
                               height=_a_(346466, _n_(346465, "image", lambda: image), "shape")[0])
        _l_(346468)
        _c_(346471, _a_(346470, _n_(346469, "img_canvas", lambda: img_canvas), "pack"))
        _l_(346472)
        image_tk = _c_(346476, _a_(346474, _n_(346473, "self", lambda: self), "to_tk_image"), _n_(346475, "image", lambda: image))
        _l_(346477)
        _c_(346481, _a_(346479, _n_(346478, "img_canvas", lambda: img_canvas), "create_image"), 0, 0, image=_n_(346480, "image_tk", lambda: image_tk), anchor='nw')
        _l_(346482)

        uploadButton2 = _c_(346491, _a_(346484, _n_(346483, "tk", lambda: tk), "Button"), _n_(346485, "img_win", lambda: img_win), text='upload',
                                  command=lambda: _c_(346490, _a_(346487, _n_(346486, "self", lambda: self), "on_click_upload_button"), _n_(346488, "path", lambda: path), _n_(346489, "image", lambda: image)))
        _l_(346492)
        _c_(346495, _a_(346494, _n_(346493, "uploadButton2", lambda: uploadButton2), "pack"))
        _l_(346496)
        _c_(346500, _a_(346499, _a_(346498, _n_(346497, "self", lambda: self), "root"), "mainloop"))
        _l_(346501)
    def to_tk_image(self, image_bgr):
        _l_(346522)

        image_rgb = _c_(346508, _a_(346504, _n_(346503, "cv2", lambda: cv2), "cvtColor"), _n_(346505, "image_bgr", lambda: image_bgr), _a_(346507, _n_(346506, "cv2", lambda: cv2), "COLOR_BGR2RGB"))
        _l_(346509)
        image_pil = _c_(346513, _a_(346511, _n_(346510, "Image", lambda: Image), "fromarray"), _n_(346512, "image_rgb", lambda: image_rgb))
        _l_(346514)
        image_tk = _c_(346518, _a_(346516, _n_(346515, "ImageTk", lambda: ImageTk), "PhotoImage"), _n_(346517, "image_pil", lambda: image_pil))
        _l_(346519)
        aux = _n_(346520, "image_tk", lambda: image_tk)
        _l_(346521)
        return aux
    def scale_to_height(self, img, height):
        _l_(346534)

        scale = _n_(346523, "height", lambda: height) / _a_(346525, _n_(346524, "img", lambda: img), "shape")[0]
        _l_(346526)
        aux = _c_(346532, _a_(346528, _n_(346527, "cv2", lambda: cv2), "resize"), _n_(346529, "img", lambda: img), dsize=None, fx=_n_(346530, "scale", lambda: scale), fy=_n_(346531, "scale", lambda: scale))
        _l_(346533)
        return aux
class Sample_Button:
    _l_(346740)

    def __init__(self, root, frame4):
        _l_(346555)

        _n_(346536, "self", lambda: self).Sample_root = _n_(346537, "root", lambda: root)
        _l_(346538)
        _n_(346539, "self", lambda: self).frame4 = _n_(346540, "frame4", lambda: frame4)
        _l_(346541)
        _n_(346542, "self", lambda: self).Sample_radio_var = _c_(346545, _a_(346544, _n_(346543, "tk", lambda: tk), "IntVar"))
        _l_(346546)
        _n_(346547, "self", lambda: self).Sample_path_selected = 'none'
        _l_(346548)
        _n_(346549, "self", lambda: self).Sample_paths = []
        _l_(346550)
        _n_(346551, "self", lambda: self).Sample_radio_handle = []
        _l_(346552)
        _n_(346553, "self", lambda: self).Sample_check_value = []
        _l_(346554)

    def on_click_select_button_Sample(self, Sample_fname_label):
        _l_(346574)

        _c_(346557, _n_(346556, "print", lambda: print), 'select Sample button clicked')
        _l_(346558)
        Sample_fileType = [('jpg/png file', ('*.jpg', '*.png'))]
        _l_(346559)
        _n_(346560, "self", lambda: self).Sample_path_selected = _c_(346564, _a_(346562, _n_(346561, "filedialog", lambda: filedialog), "askopenfilename"), filetypes=_n_(346563, "Sample_fileType", lambda: Sample_fileType))
        _l_(346565)
        _n_(346566, "Sample_fname_label", lambda: Sample_fname_label)['text'] = _c_(346572, _a_(346569, _a_(346568, _n_(346567, "os", lambda: os), "path"), "basename"), _a_(346571, _n_(346570, "self", lambda: self), "Sample_path_selected"))
        _l_(346573)

    def on_click_upload_button_Sample(self, Sample_path='None', Sample_image='None'):
        _l_(346609)

        _c_(346576, _n_(346575, "print", lambda: print), 'upload Sample button clicked')
        _l_(346577)

        if _n_(346578, "Sample_path", lambda: Sample_path) == 'None':
            _l_(346588)

            Sample_path = _a_(346580, _n_(346579, "self", lambda: self), "Sample_path_selected")
            _l_(346581)
        else:
            _c_(346586, _a_(346583, _n_(346582, "cv2", lambda: cv2), "imwrite"), _n_(346584, "Sample_path", lambda: Sample_path), _n_(346585, "Sample_image", lambda: Sample_image))
            _l_(346587)

        if _n_(346589, "Sample_path", lambda: Sample_path) in _a_(346591, _n_(346590, "self", lambda: self), "Sample_paths"):
            _l_(346608)

            _c_(346595, _a_(346593, _n_(346592, "messagebox", lambda: messagebox), "showerror"), 'Upload Error', '"'
                                 + _n_(346594, "Sample_path", lambda: Sample_path)
                                 + '"' + ' Sample is already uploaded.')
            _l_(346596)
        else:
            _c_(346601, _a_(346599, _a_(346598, _n_(346597, "self", lambda: self), "Sample_paths"), "append"), _n_(346600, "Sample_path", lambda: Sample_path))
            _l_(346602)
            _c_(346606, _a_(346604, _n_(346603, "self", lambda: self), "create_Sample_radio_button"), _n_(346605, "Sample_path", lambda: Sample_path))
            _l_(346607)

    def on_click_show_button_Sample(self):
        _l_(346643)

        _c_(346611, _n_(346610, "print", lambda: print), 'show Sample Button clicked')
        _l_(346612)
        Sample_image = _c_(346621, _a_(346614, _n_(346613, "cv2", lambda: cv2), "imread"), _a_(346616, _n_(346615, "self", lambda: self), "Sample_paths")[_c_(346620, _a_(346619, _a_(346618, _n_(346617, "self", lambda: self), "Sample_radio_var"), "get"))])
        _l_(346622)
        Sample_file_name = _c_(346632, _a_(346625, _a_(346624, _n_(346623, "os", lambda: os), "path"), "basename"), _a_(346627, _n_(346626, "self", lambda: self), "Sample_paths")[_c_(346631, _a_(346630, _a_(346629, _n_(346628, "self", lambda: self), "Sample_radio_var"), "get"))])
        _l_(346633)
        Sample_name, ext = _c_(346638, _a_(346636, _a_(346635, _n_(346634, "os", lambda: os), "path"), "splitext"), _n_(346637, "Sample_file_name", lambda: Sample_file_name))
        _l_(346639)
        Sample_path = 'Sample_images/' + _n_(346640, "Sample_name", lambda: Sample_name) + '_' + _n_(346641, "ext", lambda: ext)
        _l_(346642)


    def create_Sample_radio_button(self, Sample_path):
        _l_(346707)

        Sample_image = _c_(346647, _a_(346645, _n_(346644, "cv2", lambda: cv2), "imread"), _n_(346646, "Sample_path", lambda: Sample_path))
        _l_(346648)
        Sample_image = _c_(346652, _a_(346650, _n_(346649, "self", lambda: self), "scale_to_height_Sample"), _n_(346651, "Sample_image", lambda: Sample_image), 120)
        _l_(346653)
        Sample_image_tk = _c_(346657, _a_(346655, _n_(346654, "self", lambda: self), "Sample_to_tk_image"), _n_(346656, "Sample_image", lambda: Sample_image))
        _l_(346658)

        Sample_radio_button = _c_(346670, _a_(346660, _n_(346659, "tk", lambda: tk), "Radiobutton"), _a_(346662, _n_(346661, "self", lambda: self), "frame4"), image=_n_(346663, "Sample_image_tk", lambda: Sample_image_tk),
                                      value=_c_(346667, _n_(346664, "len", lambda: len), _a_(346666, _n_(346665, "self", lambda: self), "Sample_radio_handle")),
                                      variable=_a_(346669, _n_(346668, "self", lambda: self), "Sample_radio_var"))
        _l_(346671)
        _c_(346675, _a_(346674, _a_(346673, _n_(346672, "self", lambda: self), "Sample_radio_var"), "set"), 0)
        _l_(346676)
        _c_(346681, _a_(346679, _a_(346678, _n_(346677, "self", lambda: self), "Sample_radio_handle"), "append"), _n_(346680, "Sample_radio_button", lambda: Sample_radio_button))
        _l_(346682)
        _c_(346688, _a_(346685, _a_(346684, _n_(346683, "self", lambda: self), "Sample_check_value"), "append"), _a_(346687, _n_(346686, "self", lambda: self), "Sample_radio_var"))
        _l_(346689)

        _c_(346700, _a_(346691, _n_(346690, "Sample_radio_button", lambda: Sample_radio_button), "grid"), row=(_c_(346695, _n_(346692, "len", lambda: len), _a_(346694, _n_(346693, "self", lambda: self), "Sample_radio_handle")) - 1) // 3,
                          column=(_c_(346699, _n_(346696, "len", lambda: len), _a_(346698, _n_(346697, "self", lambda: self), "Sample_radio_handle")) - 1) % 3)
        _l_(346701)
        _c_(346705, _a_(346704, _a_(346703, _n_(346702, "self", lambda: self), "Sample_root"), "mainloop"))
        _l_(346706)

    def Sample_to_tk_image(self, Sample_image_bgr):
        _l_(346727)

        Sample_image_rgb = _c_(346713, _a_(346709, _n_(346708, "cv2", lambda: cv2), "cvtColor"), _n_(346710, "Sample_image_bgr", lambda: Sample_image_bgr), _a_(346712, _n_(346711, "cv2", lambda: cv2), "COLOR_BGR2RGB"))
        _l_(346714)
        Sample_image_pil = _c_(346718, _a_(346716, _n_(346715, "Image", lambda: Image), "fromarray"), _n_(346717, "Sample_image_rgb", lambda: Sample_image_rgb))
        _l_(346719)
        Sample_image_tk = _c_(346723, _a_(346721, _n_(346720, "ImageTk", lambda: ImageTk), "PhotoImage"), _n_(346722, "Sample_image_pil", lambda: Sample_image_pil))
        _l_(346724)
        aux = _n_(346725, "Sample_image_tk", lambda: Sample_image_tk)
        _l_(346726)
        return aux

    def scale_to_height_Sample(self, Sample_img, height):
        _l_(346739)

        scale = _n_(346728, "height", lambda: height) / _a_(346730, _n_(346729, "Sample_img", lambda: Sample_img), "shape")[0]
        _l_(346731)
        aux = _c_(346737, _a_(346733, _n_(346732, "cv2", lambda: cv2), "resize"), _n_(346734, "Sample_img", lambda: Sample_img), dsize=None, fx=_n_(346735, "scale", lambda: scale), fy=_n_(346736, "scale", lambda: scale))
        _l_(346738)
        return aux

class Difference_Button(_n_(346741, "Button", lambda: Button), _n_(346742, "Sample_Button", lambda: Sample_Button)):
    _l_(346812)

    def on_click_diff_per_button(self):
        _l_(346810)

        _c_(346744, _n_(346743, "print", lambda: print), 'select Difference button clicked')
        _l_(346745)

        Sample_image = _c_(346754, _a_(346747, _n_(346746, "cv2", lambda: cv2), "imread"), _a_(346749, _n_(346748, "self", lambda: self), "Sample_paths")[_c_(346753, _a_(346752, _a_(346751, _n_(346750, "self", lambda: self), "Sample_radio_var"), "get"))])
        _l_(346755)
        _c_(346758, _n_(346756, "print", lambda: print), _n_(346757, "Sample_image", lambda: Sample_image))
        _l_(346759)
        image = _c_(346768, _a_(346761, _n_(346760, "cv2", lambda: cv2), "imread"), _a_(346763, _n_(346762, "self", lambda: self), "paths")[_c_(346767, _a_(346766, _a_(346765, _n_(346764, "self", lambda: self), "radio_var"), "get"))])
        _l_(346769)
        _c_(346772, _n_(346770, "print", lambda: print), _n_(346771, "image", lambda: image))
        _l_(346773)
        #for x in range(7):
        Greyscale_Sample_image = _c_(346779, _a_(346775, _n_(346774, "cv2", lambda: cv2), "cvtColor"), _n_(346776, "Sample_image", lambda: Sample_image), _a_(346778, _n_(346777, "cv2", lambda: cv2), "COLOR_RGB2GRAY"))
        _l_(346780)
        Greyscale_image = _c_(346786, _a_(346782, _n_(346781, "cv2", lambda: cv2), "cvtColor"), _n_(346783, "image", lambda: image), _a_(346785, _n_(346784, "cv2", lambda: cv2), "COLOR_RGB2GRAY"))
        _l_(346787)

        (score, diff) = _c_(346791, _n_(346788, "structural_similarity", lambda: structural_similarity), _n_(346789, "Greyscale_image", lambda: Greyscale_image), _n_(346790, "Greyscale_Sample_image", lambda: Greyscale_Sample_image), full=True)  # bw_
        _l_(346792)  # bw_
        _c_(346795, _n_(346793, "print", lambda: print), "Image similarity %ge =", _n_(346794, "score", lambda: score) * 100)
        _l_(346796)

        diff = _c_(346799, _a_(346798, (_n_(346797, "diff", lambda: diff) * 255), "astype"), "uint8")
        _l_(346800)

        _c_(346804, _a_(346802, _n_(346801, "cv2", lambda: cv2), "imshow"), 'diff', _n_(346803, "diff", lambda: diff))
        _l_(346805)
        _c_(346808, _a_(346807, _n_(346806, "cv2", lambda: cv2), "waitKey"))
        _l_(346809)

    pass
    _l_(346811)


if _n_(346813, "__name__", lambda: __name__) == '__main__':
    _l_(347073)

    _c_(346816, _a_(346815, _n_(346814, "os", lambda: os), "makedirs"), 'images', exist_ok=True)
    _l_(346817)
    root = _c_(346820, _a_(346819, _n_(346818, "tk", lambda: tk), "Tk"))
    _l_(346821)
    _c_(346824, _a_(346823, _n_(346822, "root", lambda: root), "title"), 'Image GUI')
    _l_(346825)
    _c_(346828, _a_(346827, _n_(346826, "root", lambda: root), "geometry"), '1280x960')
    _l_(346829)
    pw_left = _c_(346833, _a_(346831, _n_(346830, "tk", lambda: tk), "Frame"), _n_(346832, "root", lambda: root), relief='ridge', borderwidth=4)
    _l_(346834)
    _c_(346837, _a_(346836, _n_(346835, "pw_left", lambda: pw_left), "pack"), side='left', anchor='nw')
    _l_(346838)
    pw_right = _c_(346842, _a_(346840, _n_(346839, "tk", lambda: tk), "Frame"), _n_(346841, "root", lambda: root), relief='ridge', borderwidth=4)
    _l_(346843)
    _c_(346846, _a_(346845, _n_(346844, "pw_right", lambda: pw_right), "pack"), side='left', anchor='nw')
    _l_(346847)
    frame1 = _c_(346851, _a_(346849, _n_(346848, "tk", lambda: tk), "Frame"), _n_(346850, "pw_left", lambda: pw_left), bd=2, relief="ridge")
    _l_(346852)
    _c_(346855, _a_(346854, _n_(346853, "frame1", lambda: frame1), "pack"))
    _l_(346856)
    frame2 = _c_(346860, _a_(346858, _n_(346857, "tk", lambda: tk), "LabelFrame"), _n_(346859, "pw_right", lambda: pw_right), bd=2, text='Uploaded images')
    _l_(346861)
    _c_(346864, _a_(346863, _n_(346862, "frame2", lambda: frame2), "pack"), side='left', anchor='nw')
    _l_(346865)
    button = _c_(346869, _n_(346866, "Button", lambda: Button), _n_(346867, "root", lambda: root), _n_(346868, "frame2", lambda: frame2))
    _l_(346870)
    label = _c_(346874, _a_(346872, _n_(346871, "tk", lambda: tk), "Label"), _n_(346873, "frame1", lambda: frame1), text='File:')
    _l_(346875)
    _c_(346878, _a_(346877, _n_(346876, "label", lambda: label), "grid"), row=0, column=0)
    _l_(346879)
    file_name_label = _c_(346883, _a_(346881, _n_(346880, "tk", lambda: tk), "Label"), _n_(346882, "frame1", lambda: frame1), text='-----not selected-----', width=20, bg='white')
    _l_(346884)
    _c_(346887, _a_(346886, _n_(346885, "file_name_label", lambda: file_name_label), "grid"), row=0, column=1)
    _l_(346888)
    select_button = _c_(346896, _a_(346890, _n_(346889, "tk", lambda: tk), "Button"), _n_(346891, "frame1", lambda: frame1), text='select', command=lambda: _c_(346895, _a_(346893, _n_(346892, "button", lambda: button), "on_click_select_button"), _n_(346894, "file_name_label", lambda: file_name_label)))
    _l_(346897)
    _c_(346900, _a_(346899, _n_(346898, "select_button", lambda: select_button), "grid"), row=0, column=2)
    _l_(346901)
    uploadButton = _c_(346908, _a_(346903, _n_(346902, "tk", lambda: tk), "Button"), _n_(346904, "frame1", lambda: frame1), text='Upload',
                             command=lambda: _c_(346907, _a_(346906, _n_(346905, "button", lambda: button), "on_click_upload_button")))
    _l_(346909)
    _c_(346912, _a_(346911, _n_(346910, "uploadButton", lambda: uploadButton), "grid"), row=0, column=3)
    _l_(346913)
    _c_(346916, _a_(346915, _n_(346914, "os", lambda: os), "makedirs"), 'Sample_images', exist_ok=True)
    _l_(346917)
    pw_left = _c_(346921, _a_(346919, _n_(346918, "tk", lambda: tk), "Frame"), _n_(346920, "root", lambda: root), relief='ridge', borderwidth=4)
    _l_(346922)
    _c_(346925, _a_(346924, _n_(346923, "pw_left", lambda: pw_left), "pack"), side='left', anchor='nw')
    _l_(346926)
    pw_right = _c_(346930, _a_(346928, _n_(346927, "tk", lambda: tk), "Frame"), _n_(346929, "root", lambda: root), relief='ridge', borderwidth=4)
    _l_(346931)
    _c_(346934, _a_(346933, _n_(346932, "pw_right", lambda: pw_right), "pack"), side='left', anchor='nw')
    _l_(346935)
    frame3 = _c_(346939, _a_(346937, _n_(346936, "tk", lambda: tk), "Frame"), _n_(346938, "pw_left", lambda: pw_left), bd=2, relief="ridge")
    _l_(346940)
    _c_(346943, _a_(346942, _n_(346941, "frame3", lambda: frame3), "pack"))
    _l_(346944)
    frame4 = _c_(346948, _a_(346946, _n_(346945, "tk", lambda: tk), "LabelFrame"), _n_(346947, "pw_right", lambda: pw_right), bd=2, text='Uploaded Sample images')
    _l_(346949)
    _c_(346952, _a_(346951, _n_(346950, "frame4", lambda: frame4), "pack"), side='right', anchor='nw')
    _l_(346953)


    Sample_button = _c_(346957, _n_(346954, "Sample_Button", lambda: Sample_Button), _n_(346955, "root", lambda: root), _n_(346956, "frame4", lambda: frame4))
    _l_(346958)
    Sample_label = _c_(346962, _a_(346960, _n_(346959, "tk", lambda: tk), "Label"), _n_(346961, "frame3", lambda: frame3), text='Sample File:')
    _l_(346963)
    _c_(346966, _a_(346965, _n_(346964, "Sample_label", lambda: Sample_label), "grid"), row=0, column=0)
    _l_(346967)
    Sample_file_name_label = _c_(346971, _a_(346969, _n_(346968, "tk", lambda: tk), "Label"), _n_(346970, "frame3", lambda: frame3), text='-----not selected-----', width=20, bg='white')
    _l_(346972)
    _c_(346975, _a_(346974, _n_(346973, "Sample_file_name_label", lambda: Sample_file_name_label), "grid"), row=0, column=1)
    _l_(346976)
    Sample_select_button = _c_(346984, _a_(346978, _n_(346977, "tk", lambda: tk), "Button"), _n_(346979, "frame3", lambda: frame3), text='select',
                                     command=lambda: _c_(346983, _a_(346981, _n_(346980, "Sample_button", lambda: Sample_button), "on_click_select_button_Sample"), _n_(346982, "Sample_file_name_label", lambda: Sample_file_name_label)))
    _l_(346985)
    _c_(346988, _a_(346987, _n_(346986, "Sample_select_button", lambda: Sample_select_button), "grid"), row=0, column=2)
    _l_(346989)
    Sample_uploadButton = _c_(346996, _a_(346991, _n_(346990, "tk", lambda: tk), "Button"), _n_(346992, "frame3", lambda: frame3), text='Upload',
                                    command=lambda: _c_(346995, _a_(346994, _n_(346993, "Sample_button", lambda: Sample_button), "on_click_upload_button_Sample")))
    _l_(346997)
    _c_(347000, _a_(346999, _n_(346998, "Sample_uploadButton", lambda: Sample_uploadButton), "grid"), row=0, column=3)
    _l_(347001)
    _c_(347004, _a_(347003, _n_(347002, "os", lambda: os), "makedirs"), 'Differece_images', exist_ok=True)
    _l_(347005)
    pw_left = _c_(347009, _a_(347007, _n_(347006, "tk", lambda: tk), "Frame"), _n_(347008, "root", lambda: root), relief='ridge', borderwidth=4)
    _l_(347010)
    _c_(347013, _a_(347012, _n_(347011, "pw_left", lambda: pw_left), "pack"), side='left', anchor='nw')
    _l_(347014)
    pw_right = _c_(347018, _a_(347016, _n_(347015, "tk", lambda: tk), "Frame"), _n_(347017, "root", lambda: root), relief='ridge', borderwidth=4)
    _l_(347019)
    _c_(347022, _a_(347021, _n_(347020, "pw_right", lambda: pw_right), "pack"), side='left', anchor='nw')
    _l_(347023)
    frame5 = _c_(347027, _a_(347025, _n_(347024, "tk", lambda: tk), "Frame"), _n_(347026, "pw_left", lambda: pw_left), bd=2, relief="ridge")
    _l_(347028)
    _c_(347031, _a_(347030, _n_(347029, "frame5", lambda: frame5), "pack"))
    _l_(347032)
    frame6 = _c_(347036, _a_(347034, _n_(347033, "tk", lambda: tk), "LabelFrame"), _n_(347035, "pw_right", lambda: pw_right), bd=2, text='Uploaded images')
    _l_(347037)
    _c_(347040, _a_(347039, _n_(347038, "frame6", lambda: frame6), "pack"), side='left', anchor='nw')
    _l_(347041)

    difference_button = _c_(347045, _n_(347042, "Difference_Button", lambda: Difference_Button), _n_(347043, "root", lambda: root), _n_(347044, "frame6", lambda: frame6))
    _l_(347046)
    Difference_per_label = _c_(347050, _a_(347048, _n_(347047, "tk", lambda: tk), "Label"), _n_(347049, "frame5", lambda: frame5), text='Show Image Difference', width=20, bg='white')
    _l_(347051)
    _c_(347054, _a_(347053, _n_(347052, "Difference_per_label", lambda: Difference_per_label), "grid"), row=0, column=1)
    _l_(347055)
    img_diff_button = _c_(347063, _a_(347057, _n_(347056, "tk", lambda: tk), "Button"), _n_(347058, "frame5", lambda: frame5), text='Difference', command=lambda: _c_(347062, _a_(347060, _n_(347059, "difference_button", lambda: difference_button), "on_click_diff_per_button"), _n_(347061, "Difference_per_label", lambda: Difference_per_label)))
    _l_(347064)
    _c_(347067, _a_(347066, _n_(347065, "img_diff_button", lambda: img_diff_button), "grid"), row=0, column=2)
    _l_(347068)


    _c_(347071, _a_(347070, _n_(347069, "root", lambda: root), "mainloop"))
    _l_(347072)