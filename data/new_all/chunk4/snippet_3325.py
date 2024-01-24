# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75659289/getting-typeerror-jpegimagefile-object-is-not-callable-while-asking-for-user
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(623829)

except ImportError:
    pass

input_path = 'seal.jpeg'
_l_(623830)
output_path = 'output.png'
_l_(623831)

# Open the input image
input_image = _c_(623835, _a_(623833, _n_(623832, "Image", lambda: Image), "open"), _n_(623834, "input_path", lambda: input_path))
_l_(623836)

if _a_(623838, _n_(623837, "input_image", lambda: input_image), "mode") == 'RGBA':
    _l_(623931)

    # If the image is already transparent, do nothing
    _c_(623840, _n_(623839, "print", lambda: print), "Image is already transparent")
    _l_(623841)
else:
    # Convert to RGBA mode to have alpha channel
    rgba = _c_(623844, _a_(623843, _n_(623842, "input_image", lambda: input_image), "convert"), 'RGBA')
    _l_(623845)

    # Create a new transparent image with same size
    output_image = _c_(623850, _a_(623847, _n_(623846, "Image", lambda: Image), "new"), 'RGBA', _a_(623849, _n_(623848, "rgba", lambda: rgba), "size"), (0,0,0,0))
    _l_(623851)

    # Loop through all the pixels
    for x in _c_(623855, _n_(623852, "range", lambda: range), _a_(623854, _n_(623853, "rgba", lambda: rgba), "size")[0]):
        _l_(623883)

        for y in _c_(623859, _n_(623856, "range", lambda: range), _a_(623858, _n_(623857, "rgba", lambda: rgba), "size")[1]):
            _l_(623882)

            # Get the RGBA values of the pixel
            r,g,b,a = _c_(623864, _a_(623861, _n_(623860, "rgba", lambda: rgba), "getpixel"), (_n_(623862, "x", lambda: x),_n_(623863, "y", lambda: y)))
            _l_(623865)
            # Check if the pixel is not too bright (not white or near white)
            if _c_(623870, _n_(623866, "sum", lambda: sum), (_n_(623867, "r", lambda: r),_n_(623868, "g", lambda: g),_n_(623869, "b", lambda: b))) < 600:
                _l_(623881)

                # Set the pixel in the output image with the same color and alpha value
                _c_(623879, _a_(623872, _n_(623871, "output_image", lambda: output_image), "putpixel"), (_n_(623873, "x", lambda: x),_n_(623874, "y", lambda: y)), (_n_(623875, "r", lambda: r),_n_(623876, "g", lambda: g),_n_(623877, "b", lambda: b),_n_(623878, "a", lambda: a)))
                _l_(623880)

    # Ask user if they want to resize the output image
    resize_str = _c_(623889, _a_(623884, "Output image is {}x{} pixels. Do you want to resize it? (y/n): ", "format"), _a_(623886, _n_(623885, "output_image", lambda: output_image), "size")[0], _a_(623888, _n_(623887, "output_image", lambda: output_image), "size")[1])
    _l_(623890)
    resize_choice = _c_(623895, _n_(623891, "input", lambda: input), _c_(623894, _a_(623892, "{}", "format"), _n_(623893, "resize_str", lambda: resize_str)))
    _l_(623896)
    if _c_(623899, _a_(623898, _n_(623897, "resize_choice", lambda: resize_choice), "lower")) == "y":
        _l_(623925)

        percent_str = "Enter desired resize percentage (e.g. 50 for 50%): "
        _l_(623900)
        resize_percent = _c_(623907, _n_(623901, "int", lambda: int), _c_(623906, _n_(623902, "input", lambda: input), _c_(623905, _a_(623903, "{}", "format"), _n_(623904, "percent_str", lambda: percent_str))))
        _l_(623908)
        resize = (_c_(623913, _n_(623909, "int", lambda: int), _a_(623911, _n_(623910, "output_image", lambda: output_image), "size")[0]*_n_(623912, "resize_percent", lambda: resize_percent)/100), _c_(623918, _n_(623914, "int", lambda: int), _a_(623916, _n_(623915, "output_image", lambda: output_image), "size")[1]*_n_(623917, "resize_percent", lambda: resize_percent)/100))
        _l_(623919)
        output_image = _c_(623923, _a_(623921, _n_(623920, "output_image", lambda: output_image), "resize"), _n_(623922, "resize", lambda: resize))
        _l_(623924)

    # Save the output image
    _c_(623929, _a_(623927, _n_(623926, "output_image", lambda: output_image), "save"), _n_(623928, "output_path", lambda: output_path))
    _l_(623930)