# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75198725/unable-to-solve-typeerror-invalid-shape-512-256-2-for-image-data-for-vgg1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(579506)

except ImportError:
    pass
try:
    import cv2
    _l_(579508)

except ImportError:
    pass
try:
    import numpy as np
    _l_(579510)

except ImportError:
    pass
try:
    import torch
    _l_(579512)

except ImportError:
    pass
try:
    import torch.nn as nn
    _l_(579514)

except ImportError:
    pass
try:
    import torch.nn.functional as F
    _l_(579516)

except ImportError:
    pass
try:
    from torchvision.models.vgg import vgg19
    _l_(579518)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(579520)

except ImportError:
    pass
try:
    import pywt
    _l_(579522)

except ImportError:
    pass
try:
    import pywt.data
    _l_(579524)

except ImportError:
    pass

# Defining a custom pre-trained model (VGG19)
class VGG19(_a_(579527, _a_(579526, _n_(579525, "torch", lambda: torch), "nn"), "Module")):
    _l_(579581)


    def __init__(self, device='cpu'):
        _l_(579560)

        _c_(579532, _a_(579531, _n_(579528, "super", lambda: super)(_n_(579529, "VGG19", lambda: VGG19), _n_(579530, "self", lambda: self)), "__init__"))
        _l_(579533)
        modelFeatures = _c_(579538, _n_(579534, "list", lambda: list), _a_(579537, _c_(579536, _n_(579535, "vgg19", lambda: vgg19), pretrained=True), "features")) # Extracting the feature of the model
        _l_(579539) # Extracting the feature of the model
        if _n_(579540, "device", lambda: device) == "cuda":
            _l_(579559)

            _n_(579541, "self", lambda: self).features = _c_(579549, _a_(579548, _c_(579547, _a_(579546, _c_(579545, _a_(579543, _n_(579542, "nn", lambda: nn), "ModuleList"), _n_(579544, "modelFeatures", lambda: modelFeatures)), "cuda")), "eval"))
            _l_(579550)
        else:
            _n_(579551, "self", lambda: self).features = _c_(579557, _a_(579556, _c_(579555, _a_(579553, _n_(579552, "nn", lambda: nn), "ModuleList"), _n_(579554, "modelFeatures", lambda: modelFeatures)), "eval"))
            _l_(579558)

    def forward(self, image):
        _l_(579580)

        featureMaps = [] # List used to store the output of the each layer of the VGG19 model
        _l_(579561) # List used to store the output of the each layer of the VGG19 model
        for index, layer in _c_(579565, _n_(579562, "enumerate", lambda: enumerate), _a_(579564, _n_(579563, "self", lambda: self), "features")):
            _l_(579577)

            image = _c_(579568, _n_(579566, "layer", lambda: layer), _n_(579567, "image", lambda: image))
            _l_(579569)
            if _n_(579570, "index", lambda: index) == 3:
                _l_(579576)

                _c_(579574, _a_(579572, _n_(579571, "featureMaps", lambda: featureMaps), "append"), _n_(579573, "image", lambda: image))
                _l_(579575)
        aux = _n_(579578, "featureMaps", lambda: featureMaps)
        _l_(579579)
        return aux

class GetFusedImage:
    _l_(579982)


    def __init__(self, CTscanImage, MRIscanImage):
        _l_(579601)

        """
        Class Fusion constructor

        Instance Variables:
            self.images: input images
            self.model: CNN model, default=vgg19
            self.device: either 'cuda' or 'cpu'
        """
        _n_(579582, "self", lambda: self).inputImages = _n_(579583, "CTscanImage", lambda: CTscanImage), _n_(579584, "MRIscanImage", lambda: MRIscanImage)
        _l_(579585)
        _n_(579586, "self", lambda: self).device = _c_(579593, _a_(579588, _n_(579587, "torch", lambda: torch), "device"), "cuda" if _c_(579592, _a_(579591, _a_(579590, _n_(579589, "torch", lambda: torch), "cuda"), "is_available")) else "cpu")
        _l_(579594)
        _n_(579595, "self", lambda: self).model = _c_(579599, _n_(579596, "VGG19", lambda: VGG19), _a_(579598, _n_(579597, "self", lambda: self), "device"))
        _l_(579600)

    def _RGB_to_YCbCr(self, img_RGB):
        _l_(579615)

        """
            A private method which converts an RGB image to YCrCb format
            """
        img_RGB = _c_(579606, _a_(579603, _n_(579602, "img_RGB", lambda: img_RGB), "astype"), _a_(579605, _n_(579604, "np", lambda: np), "float32")) / 255.
        _l_(579607)
        aux = _c_(579613, _a_(579609, _n_(579608, "cv2", lambda: cv2), "cvtColor"), _n_(579610, "img_RGB", lambda: img_RGB), _a_(579612, _n_(579611, "cv2", lambda: cv2), "COLOR_RGB2YCrCb"))
        _l_(579614)
        return aux

    def _YCbCr_to_RGB(self, img_YCbCr):
        _l_(579629)

        """
            A private method which converts a YCrCb image to RGB format
            """
        img_YCbCr = _c_(579620, _a_(579617, _n_(579616, "img_YCbCr", lambda: img_YCbCr), "astype"), _a_(579619, _n_(579618, "np", lambda: np), "float32"))
        _l_(579621)
        aux = _c_(579627, _a_(579623, _n_(579622, "cv2", lambda: cv2), "cvtColor"), _n_(579624, "img_YCbCr", lambda: img_YCbCr), _a_(579626, _n_(579625, "cv2", lambda: cv2), "COLOR_YCrCb2RGB"))
        _l_(579628)
        return aux

    def _is_gray(self, img):
        _l_(579655)

        """
            A private method which returns True if image is gray, otherwise False
            """
        if _c_(579633, _n_(579630, "len", lambda: len), _a_(579632, _n_(579631, "img", lambda: img), "shape")) < 3:
            _l_(579635)

            aux = True
            _l_(579634)
            return aux
        if _a_(579637, _n_(579636, "img", lambda: img), "shape")[2] == 1:
            _l_(579639)

            aux = True
            _l_(579638)
            return aux
        b, g, r = _n_(579640, "img", lambda: img)[:,:,0], _n_(579641, "img", lambda: img)[:,:,1], _n_(579642, "img", lambda: img)[:,:,2]
        _l_(579643)
        if _c_(579647, _a_(579646, (_n_(579644, "b", lambda: b) == _n_(579645, "g", lambda: g)), "all")) and _c_(579651, _a_(579650, (_n_(579648, "b", lambda: b) == _n_(579649, "r", lambda: r)), "all")):
            _l_(579653)

            aux = True
            _l_(579652)
            return aux
        aux = False
        _l_(579654)
        return aux

    def _softmax(self, tensor):
        _l_(579668)

        """
            A private method which compute softmax ouput of a given tensor
            """
        tensor = _c_(579659, _a_(579657, _n_(579656, "torch", lambda: torch), "exp"), _n_(579658, "tensor", lambda: tensor))
        _l_(579660)
        tensor = _n_(579661, "tensor", lambda: tensor) / _c_(579664, _a_(579663, _n_(579662, "tensor", lambda: tensor), "sum"), dim=1, keepdim=True)
        _l_(579665)
        aux = _n_(579666, "tensor", lambda: tensor)
        _l_(579667)
        return aux

    def _tranfer_to_tensor(self):
        _l_(579716)

        """
            A private method to transfer all input images to PyTorch tensors
            """
        _n_(579669, "self", lambda: self).images_to_tensors = []
        _l_(579670)
        for image in _a_(579672, _n_(579671, "self", lambda: self), "normalized_images"):
            _l_(579715)

            np_input = _c_(579677, _a_(579674, _n_(579673, "image", lambda: image), "astype"), _a_(579676, _n_(579675, "np", lambda: np), "float32"))
            _l_(579678)
            if _a_(579680, _n_(579679, "np_input", lambda: np_input), "ndim") == 2:
                _l_(579691)

                np_input = _c_(579684, _a_(579682, _n_(579681, "np", lambda: np), "repeat"), _n_(579683, "np_input", lambda: np_input)[None, None], 3, axis=1)
                _l_(579685)
            else:
                np_input = _c_(579689, _a_(579687, _n_(579686, "np", lambda: np), "transpose"), _n_(579688, "np_input", lambda: np_input), (2, 0, 1))[None]
                _l_(579690)
            if _a_(579693, _n_(579692, "self", lambda: self), "device") == "cuda":
                _l_(579714)

                _c_(579703, _a_(579696, _a_(579695, _n_(579694, "self", lambda: self), "images_to_tensors"), "append"), _c_(579702, _a_(579701, _c_(579700, _a_(579698, _n_(579697, "torch", lambda: torch), "from_numpy"), _n_(579699, "np_input", lambda: np_input)), "cuda")))
                _l_(579704)
            else:
                _c_(579712, _a_(579707, _a_(579706, _n_(579705, "self", lambda: self), "images_to_tensors"), "append"), _c_(579711, _a_(579709, _n_(579708, "torch", lambda: torch), "from_numpy"), _n_(579710, "np_input", lambda: np_input)))
                _l_(579713)

    def fuseAlgorithm(self):
        _l_(579824)

        """
        Perform fusion algorithm
        """
        with _c_(579719, _a_(579718, _n_(579717, "torch", lambda: torch), "no_grad")):
            _l_(579823)


            imageSumMaps = [-1 for tensor_img in _a_(579721, _n_(579720, "self", lambda: self), "images_to_tensors")]
            _l_(579722)
            for idx, tensor_img in _c_(579726, _n_(579723, "enumerate", lambda: enumerate), _a_(579725, _n_(579724, "self", lambda: self), "images_to_tensors")):
                _l_(579748)

                _n_(579727, "imageSummaps", lambda: imageSummaps)[_n_(579728, "idx", lambda: idx)] = []
                _l_(579729)
                featureMaps = _c_(579733, _a_(579731, _n_(579730, "self", lambda: self), "model"), _n_(579732, "tensor_img", lambda: tensor_img))
                _l_(579734)
                for featureMap in _n_(579735, "featureMaps", lambda: featureMaps):
                    _l_(579747)

                    sumMap = _c_(579739, _a_(579737, _n_(579736, "torch", lambda: torch), "sum"), _n_(579738, "featureMap", lambda: featureMap), dim=1, keepdim=True)
                    _l_(579740)
                    _c_(579745, _a_(579743, _n_(579741, "imageSumMaps", lambda: imageSumMaps)[_n_(579742, "index", lambda: index)], "append"), _n_(579744, "sumMap", lambda: sumMap))
                    _l_(579746)

            maxFusion = None
            _l_(579749)

            for sumMaps in _c_(579752, _n_(579750, "zip", lambda: zip), *_n_(579751, "imageSumMaps", lambda: imageSumMaps)):
                _l_(579803)

            
                features = _c_(579756, _a_(579754, _n_(579753, "torch", lambda: torch), "cat"), _n_(579755, "sumMaps", lambda: sumMaps), dim=1)
                _l_(579757)
                weights = _c_(579767, _a_(579759, _n_(579758, "self", lambda: self), "_softmax"), _c_(579766, _a_(579761, _n_(579760, "F", lambda: F), "interpolate"), _n_(579762, "features", lambda: features),
                                        size=_a_(579765, _a_(579764, _n_(579763, "self", lambda: self), "images_to_tensors")[0], "shape")[2:]))
                _l_(579768)
                weights = _c_(579775, _a_(579770, _n_(579769, "F", lambda: F), "interpolate"), _n_(579771, "weights", lambda: weights),
                                        size=_a_(579774, _a_(579773, _n_(579772, "self", lambda: self), "images_to_tensors")[0], "shape")[2:])
                _l_(579776)
                currentFusion = _c_(579782, _a_(579778, _n_(579777, "torch", lambda: torch), "zeros"), _a_(579781, _a_(579780, _n_(579779, "self", lambda: self), "images_to_tensors")[0], "shape"))
                _l_(579783)
                for index, tensor_img in _c_(579787, _n_(579784, "enumerate", lambda: enumerate), _a_(579786, _n_(579785, "self", lambda: self), "images_to_tensors")):
                    _l_(579792)

                    currentFusion += _n_(579788, "tensor_img", lambda: tensor_img) * _n_(579789, "weights", lambda: weights)[:,_n_(579790, "index", lambda: index)]
                    _l_(579791)
                if _n_(579793, "maxFusion", lambda: maxFusion) is None:
                    _l_(579802)

                    maxFusion = _n_(579794, "currentFusion", lambda: currentFusion)
                    _l_(579795)
                else:
                    maxFusion = _c_(579800, _a_(579797, _n_(579796, "torch", lambda: torch), "max"), _n_(579798, "maxFusion", lambda: maxFusion), _n_(579799, "currentFusion", lambda: currentFusion))
                    _l_(579801)

            output = _c_(579811, _a_(579805, _n_(579804, "np", lambda: np), "squeeze"), _c_(579810, _a_(579809, _c_(579808, _a_(579807, _n_(579806, "maxFusion", lambda: maxFusion), "cpu")), "numpy")))
            _l_(579812)
            if _a_(579814, _n_(579813, "output", lambda: output), "ndim") == 3:
                _l_(579820)

                output = _c_(579818, _a_(579816, _n_(579815, "np", lambda: np), "transpose"), _n_(579817, "output", lambda: output), (1, 2, 0))
                _l_(579819)
            aux = _n_(579821, "output", lambda: output)
            _l_(579822)
            return aux

    def fuseImage(self):
        _l_(579904)

        """
        A top level method which fuse self.images
        """
        # Convert all images to YCbCr format
        _n_(579825, "self", lambda: self).normalizedImages = [-1 for img in _a_(579827, _n_(579826, "self", lambda: self), "inputImages")]
        _l_(579828)
        _n_(579829, "self", lambda: self).YCbCrImages = [-1 for img in _a_(579831, _n_(579830, "self", lambda: self), "inputImages")]
        _l_(579832)

        #checking if the image is grayscale or not
        for index, img in _c_(579836, _n_(579833, "enumerate", lambda: enumerate), _a_(579835, _n_(579834, "self", lambda: self), "inputImages")):
            _l_(579862)

            if not _c_(579840, _a_(579838, _n_(579837, "self", lambda: self), "_is_gray"), _n_(579839, "img", lambda: img)):
                _l_(579861)

                _a_(579842, _n_(579841, "self", lambda: self), "YCbCrImages")[_n_(579843, "index", lambda: index)] = _c_(579847, _a_(579845, _n_(579844, "self", lambda: self), "_RGB_to_YCbCr"), _n_(579846, "img", lambda: img))
                _l_(579848)
                _a_(579850, _n_(579849, "self", lambda: self), "normalizedImages")[_n_(579851, "index", lambda: index)] = _a_(579853, _n_(579852, "self", lambda: self), "YCbCrImages")[_n_(579854, "index", lambda: index)][:, :, 0] #storingthe first channel of YCbCr image
                _l_(579855) #storingthe first channel of YCbCr image
            else:
                _a_(579857, _n_(579856, "self", lambda: self), "normalizedImages")[_n_(579858, "index", lambda: index)] = _n_(579859, "img", lambda: img) / 255.
                _l_(579860)
       
        # Transfer all images to PyTorch tensors (arrays)
        _c_(579865, _a_(579864, _n_(579863, "self", lambda: self), "_tranfer_to_tensor"))
        _l_(579866)

        # Perform fuse strategy
        fusedImage = _c_(579869, _a_(579868, _n_(579867, "self", lambda: self), "fuseAlgorithm"))[:, :, 0]
        _l_(579870)

        # Reconstruct fused image given rgb input images
        for index, img in _c_(579874, _n_(579871, "enumerate", lambda: enumerate), _a_(579873, _n_(579872, "self", lambda: self), "inputImages")):
            _l_(579897)

            if not _c_(579878, _a_(579876, _n_(579875, "self", lambda: self), "_is_gray"), _n_(579877, "img", lambda: img)):
                _l_(579896)

                _a_(579880, _n_(579879, "self", lambda: self), "YCbCrImages")[_n_(579881, "index", lambda: index)][:, :, 0] = _n_(579882, "fusedImage", lambda: fusedImage)
                _l_(579883)
                fusedImage = _c_(579889, _a_(579885, _n_(579884, "self", lambda: self), "_YCbCr_to_RGB"), _a_(579887, _n_(579886, "self", lambda: self), "YCbCr_images")[_n_(579888, "idx", lambda: idx)])
                _l_(579890)
                fusedImage = _c_(579894, _a_(579892, _n_(579891, "np", lambda: np), "clip"), _n_(579893, "fusedImage", lambda: fusedImage), 0, 1)
                _l_(579895)
        aux = _c_(579902, _a_(579899, (_n_(579898, "fusedImage", lambda: fusedImage) * 255), "astype"), _a_(579901, _n_(579900, "np", lambda: np), "uint8"))
        _l_(579903)

        return aux

    def waveletTransformation(self, image, imageName):
        _l_(579981)


        titles = ['Approximation', ' Horizontal detail',
                  'Vertical detail', 'Diagonal detail']
        _l_(579905)
        coeffs2 = _c_(579909, _a_(579907, _n_(579906, "pywt", lambda: pywt), "dwt2"), _n_(579908, "image", lambda: image), 'haar')
        _l_(579910)

        LL, (LH, HL, HH) = _n_(579911, "coeffs2", lambda: coeffs2)
        _l_(579912)

        fig = _c_(579915, _a_(579914, _n_(579913, "plt", lambda: plt), "figure"), figsize=(12, 3))
        _l_(579916)
        for i, a in _c_(579922, _n_(579917, "enumerate", lambda: enumerate), [_n_(579918, "LL", lambda: LL), _n_(579919, "LH", lambda: LH), _n_(579920, "HL", lambda: HL), _n_(579921, "HH", lambda: HH)]):
            _l_(579972)

            ax = _c_(579926, _a_(579924, _n_(579923, "fig", lambda: fig), "add_subplot"), 1, 4, _n_(579925, "i", lambda: i) + 1)
            _l_(579927)
            _c_(579934, _a_(579929, _n_(579928, "ax", lambda: ax), "imshow"), _n_(579930, "a", lambda: a), interpolation="nearest", cmap=_a_(579933, _a_(579932, _n_(579931, "plt", lambda: plt), "cm"), "gray"))
            _l_(579935)

            if "CTscanImage" in _n_(579936, "imageName", lambda: imageName):
                _l_(579957)

                path='jpg/ct_'+_c_(579939, _n_(579937, "str", lambda: str), _n_(579938, "i", lambda: i))+'.jpg'
                _l_(579940)
                _c_(579945, _a_(579942, _n_(579941, "cv2", lambda: cv2), "imwrite"), _n_(579943, "path", lambda: path),_n_(579944, "a", lambda: a))
                _l_(579946)

            else:
                path='jpg/mri_'+_c_(579949, _n_(579947, "str", lambda: str), _n_(579948, "i", lambda: i))+'.jpg'
                _l_(579950)
                _c_(579955, _a_(579952, _n_(579951, "cv2", lambda: cv2), "imwrite"), _n_(579953, "path", lambda: path),_n_(579954, "a", lambda: a))
                _l_(579956)

            _c_(579962, _a_(579959, _n_(579958, "ax", lambda: ax), "set_title"), _n_(579960, "titles", lambda: titles)[_n_(579961, "i", lambda: i)], fontsize=10)
            _l_(579963)
            _c_(579966, _a_(579965, _n_(579964, "ax", lambda: ax), "set_xticks"), [])
            _l_(579967)
            _c_(579970, _a_(579969, _n_(579968, "ax", lambda: ax), "set_yticks"), [])
            _l_(579971)

        _c_(579975, _a_(579974, _n_(579973, "fig", lambda: fig), "tight_layout"))
        _l_(579976)
        _c_(579979, _a_(579978, _n_(579977, "plt", lambda: plt), "show"))
        _l_(579980)


if _n_(579983, "__name__", lambda: __name__) == "__main__":
    _l_(580027)


    arg = _c_(579986, _a_(579985, _n_(579984, "argparse", lambda: argparse), "ArgumentParser"))
    _l_(579987)
    _c_(579990, _a_(579989, _n_(579988, "arg", lambda: arg), "add_argument"), "--pathInCTImage", help="Path to CT Scan Image")
    _l_(579991)
    _c_(579994, _a_(579993, _n_(579992, "arg", lambda: arg), "add_argument"), "--pathInMRIImage", help="Path to MRI Scan Image")
    _l_(579995)
    args = _c_(579998, _a_(579997, _n_(579996, "arg", lambda: arg), "parse_args"))
    _l_(579999)

    CTscanImage = _c_(580004, _a_(580001, _n_(580000, "cv2", lambda: cv2), "imread"), _a_(580003, _n_(580002, "args", lambda: args), "pathInCTImage"))
    _l_(580005)
    MRIscanImage = _c_(580010, _a_(580007, _n_(580006, "cv2", lambda: cv2), "imread"), _a_(580009, _n_(580008, "args", lambda: args), "pathInMRIImage")) #MRI Image will be registered
    _l_(580011) #MRI Image will be registered

    handler = _c_(580015, _n_(580012, "GetFusedImage", lambda: GetFusedImage), _n_(580013, "CTscanImage", lambda: CTscanImage), _n_(580014, "MRIscanImage", lambda: MRIscanImage))
    _l_(580016)

    _c_(580020, _a_(580018, _n_(580017, "handler", lambda: handler), "waveletTransformation"), _n_(580019, "CTscanImage", lambda: CTscanImage), "CTscanImage")
    _l_(580021)
    _c_(580025, _a_(580023, _n_(580022, "handler", lambda: handler), "waveletTransformation"), _n_(580024, "MRIscanImage", lambda: MRIscanImage), "MRIscanImage")
    _l_(580026)