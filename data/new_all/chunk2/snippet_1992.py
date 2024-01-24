# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72084680/typeerror-keyword-argument-not-understood-query-shape-with-keras-and-te
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ShiftedPatchTokenization(_a_(461199, _n_(461198, "layers", lambda: layers), "Layer")):
    _l_(461405)

    def __init__(
      self,
      image_size=IMAGE_SIZE,
      patch_size=PATCH_SIZE,
      half_patch=PATCH_SIZE//2,
      num_patches=NUM_PATCHES,
      projection_dim=PROJECTION_DIM,
      flatten_patches=None,
      projection=None,
      layer_norm=None,
      vanilla=False,
      **kwargs,
    ):
        _l_(461237)

        _c_(461205, _a_(461203, _n_(461200, "super", lambda: super)(_n_(461201, "ShiftedPatchTokenization", lambda: ShiftedPatchTokenization),_n_(461202, "self", lambda: self)), "__init__"), **_n_(461204, "kwargs", lambda: kwargs))
        _l_(461206)
        _n_(461207, "self", lambda: self).vanilla = _n_(461208, "vanilla", lambda: vanilla)  # Flag to switch to vanilla patch extractor      
        _l_(461209)  # Flag to switch to vanilla patch extractor      
        _n_(461210, "self", lambda: self).image_size = _n_(461211, "image_size", lambda: image_size)
        _l_(461212)
        _n_(461213, "self", lambda: self).patch_size = _n_(461214, "patch_size", lambda: patch_size)
        _l_(461215)
        _n_(461216, "self", lambda: self).half_patch = _n_(461217, "patch_size", lambda: patch_size) // 2 # la divisione con // dà il numero in int()
        _l_(461218) # la divisione con // dà il numero in int()
        _n_(461219, "self", lambda: self).flatten_patches = _c_(461223, _a_(461221, _n_(461220, "layers", lambda: layers), "Reshape"), (_n_(461222, "num_patches", lambda: num_patches), -1))
        _l_(461224)
        _n_(461225, "self", lambda: self).projection = _c_(461229, _a_(461227, _n_(461226, "layers", lambda: layers), "Dense"), units=_n_(461228, "projection_dim", lambda: projection_dim))
        _l_(461230)
        _n_(461231, "self", lambda: self).layer_norm = _c_(461235, _a_(461233, _n_(461232, "layers", lambda: layers), "LayerNormalization"), epsilon=_n_(461234, "LAYER_NORM_EPS", lambda: LAYER_NORM_EPS))
        _l_(461236)

    # Override function to avoid error while saving model
    def get_config(self):
        _l_(461264)

        config = _c_(461242, _a_(461241, _c_(461240, _a_(461239, _n_(461238, "super", lambda: super)(), "get_config")), "copy"))
        _l_(461243)
        _c_(461260, _a_(461245, _n_(461244, "config", lambda: config), "update"), {
            "image_size": _a_(461247, _n_(461246, "self", lambda: self), "image_size"),
            "patch_size": _a_(461249, _n_(461248, "self", lambda: self), "patch_size"),
            "half_patch": _a_(461251, _n_(461250, "self", lambda: self), "half_patch"),
            "flatten_patches": _a_(461253, _n_(461252, "self", lambda: self), "flatten_patches"),
            "vanilla": _a_(461255, _n_(461254, "self", lambda: self), "vanilla"),
            "projection": _a_(461257, _n_(461256, "self", lambda: self), "projection"),
            "layer_norm": _a_(461259, _n_(461258, "self", lambda: self), "layer_norm"),
            }
        )
        _l_(461261)
        aux = _n_(461262, "config", lambda: config)
        _l_(461263)
        return aux
     


    @_n_(461265, "classmethod", lambda: classmethod)
    def from_config(cls, config):
        _l_(461270)

        aux = _c_(461268, _n_(461266, "cls", lambda: cls), **_n_(461267, "config", lambda: config))
        _l_(461269)
        return aux

    def crop_shift_pad(self, images, mode):
        _l_(461339)

        # Build the diagonally shifted images
        if _n_(461271, "mode", lambda: mode) == "left-up":
            _l_(461308)

            crop_height = _a_(461273, _n_(461272, "self", lambda: self), "half_patch")
            _l_(461274)
            crop_width = _a_(461276, _n_(461275, "self", lambda: self), "half_patch")
            _l_(461277)
            shift_height = 0
            _l_(461278)
            shift_width = 0
            _l_(461279)
        elif _n_(461280, "mode", lambda: mode) == "left-down":
            _l_(461307)

            crop_height = 0
            _l_(461281)
            crop_width = _a_(461283, _n_(461282, "self", lambda: self), "half_patch")
            _l_(461284)
            shift_height = _a_(461286, _n_(461285, "self", lambda: self), "half_patch")
            _l_(461287)
            shift_width = 0
            _l_(461288)
        elif _n_(461289, "mode", lambda: mode) == "right-up":
            _l_(461306)

            crop_height = _a_(461291, _n_(461290, "self", lambda: self), "half_patch")
            _l_(461292)
            crop_width = 0
            _l_(461293)
            shift_height = 0
            _l_(461294)
            shift_width = _a_(461296, _n_(461295, "self", lambda: self), "half_patch")
            _l_(461297)
        else:
            crop_height = 0
            _l_(461298)
            crop_width = 0
            _l_(461299)
            shift_height = _a_(461301, _n_(461300, "self", lambda: self), "half_patch")
            _l_(461302)
            shift_width = _a_(461304, _n_(461303, "self", lambda: self), "half_patch")
            _l_(461305)

        # Crop the shifted images and pad them
        crop = _c_(461323, _a_(461311, _a_(461310, _n_(461309, "tf", lambda: tf), "image"), "crop_to_bounding_box"), _n_(461312, "images", lambda: images),
            offset_height=_n_(461313, "crop_height", lambda: crop_height),
            offset_width=_n_(461314, "crop_width", lambda: crop_width),
            target_height=_a_(461316, _n_(461315, "self", lambda: self), "image_size") - _a_(461318, _n_(461317, "self", lambda: self), "half_patch"),
            target_width=_a_(461320, _n_(461319, "self", lambda: self), "image_size") - _a_(461322, _n_(461321, "self", lambda: self), "half_patch"),
        )
        _l_(461324)
        shift_pad = _c_(461335, _a_(461327, _a_(461326, _n_(461325, "tf", lambda: tf), "image"), "pad_to_bounding_box"), _n_(461328, "crop", lambda: crop),
            offset_height=_n_(461329, "shift_height", lambda: shift_height),
            offset_width=_n_(461330, "shift_width", lambda: shift_width),
            target_height=_a_(461332, _n_(461331, "self", lambda: self), "image_size"),
            target_width=_a_(461334, _n_(461333, "self", lambda: self), "image_size"),
        )
        _l_(461336)
        aux = _n_(461337, "shift_pad", lambda: shift_pad)
        _l_(461338)
        return aux

    def call(self, images):
        _l_(461404)

        if not _a_(461341, _n_(461340, "self", lambda: self), "vanilla"):
            _l_(461363)

            # Concat the shifted images with the original image
            images = _c_(461361, _a_(461343, _n_(461342, "tf", lambda: tf), "concat"), [
                    _n_(461344, "images", lambda: images),
                    _c_(461348, _a_(461346, _n_(461345, "self", lambda: self), "crop_shift_pad"), _n_(461347, "images", lambda: images), mode="left-up"),
                    _c_(461352, _a_(461350, _n_(461349, "self", lambda: self), "crop_shift_pad"), _n_(461351, "images", lambda: images), mode="left-down"),
                    _c_(461356, _a_(461354, _n_(461353, "self", lambda: self), "crop_shift_pad"), _n_(461355, "images", lambda: images), mode="right-up"),
                    _c_(461360, _a_(461358, _n_(461357, "self", lambda: self), "crop_shift_pad"), _n_(461359, "images", lambda: images), mode="right-down"),
                ],
                axis=-1,
            )
            _l_(461362)
        # Patchify the images and flatten it
        patches = _c_(461376, _a_(461366, _a_(461365, _n_(461364, "tf", lambda: tf), "image"), "extract_patches"), images=_n_(461367, "images", lambda: images),
            sizes=[1, _a_(461369, _n_(461368, "self", lambda: self), "patch_size"), _a_(461371, _n_(461370, "self", lambda: self), "patch_size"), 1],
            strides=[1, _a_(461373, _n_(461372, "self", lambda: self), "patch_size"), _a_(461375, _n_(461374, "self", lambda: self), "patch_size"), 1],
            rates=[1, 1, 1, 1],
            padding="VALID",
        )
        _l_(461377)
        flat_patches = _c_(461381, _a_(461379, _n_(461378, "self", lambda: self), "flatten_patches"), _n_(461380, "patches", lambda: patches))
        _l_(461382)
        if not _a_(461384, _n_(461383, "self", lambda: self), "vanilla"):
            _l_(461400)

            # Layer normalize the flat patches and linearly project it
            tokens = _c_(461388, _a_(461386, _n_(461385, "self", lambda: self), "layer_norm"), _n_(461387, "flat_patches", lambda: flat_patches))
            _l_(461389)
            tokens = _c_(461393, _a_(461391, _n_(461390, "self", lambda: self), "projection"), _n_(461392, "tokens", lambda: tokens))
            _l_(461394)
        else:
            # Linearly project the flat patches
            tokens = _c_(461398, _a_(461396, _n_(461395, "self", lambda: self), "projection"), _n_(461397, "flat_patches", lambda: flat_patches))
            _l_(461399)
        aux = (_n_(461401, "tokens", lambda: tokens), _n_(461402, "patches", lambda: patches))
        _l_(461403)
        return aux


class PatchEncoder(_a_(461407, _n_(461406, "layers", lambda: layers), "Layer")):
    _l_(461472)

    def __init__(
        self,
        num_patches=NUM_PATCHES,
        projection_dim=PROJECTION_DIM,
        position_embedding=None,
        positions=None,
        **kwargs
    ):
        _l_(461432)

        _c_(461413, _a_(461411, _n_(461408, "super", lambda: super)(_n_(461409, "PatchEncoder", lambda: PatchEncoder),_n_(461410, "self", lambda: self)), "__init__"), **_n_(461412, "kwargs", lambda: kwargs))
        _l_(461414)
        _n_(461415, "self", lambda: self).num_patches = _n_(461416, "num_patches", lambda: num_patches)
        _l_(461417)
        _n_(461418, "self", lambda: self).position_embedding = _c_(461423, _a_(461420, _n_(461419, "layers", lambda: layers), "Embedding"), input_dim=_n_(461421, "num_patches", lambda: num_patches), output_dim=_n_(461422, "projection_dim", lambda: projection_dim)
        )
        _l_(461424)
        _n_(461425, "self", lambda: self).positions = _c_(461430, _a_(461427, _n_(461426, "tf", lambda: tf), "range"), start=0, limit=_a_(461429, _n_(461428, "self", lambda: self), "num_patches"), delta=1)
        _l_(461431)

    def get_config(self):
        _l_(461453)

        config = _c_(461437, _a_(461436, _c_(461435, _a_(461434, _n_(461433, "super", lambda: super)(), "get_config")), "copy"))
        _l_(461438)
        _c_(461449, _a_(461440, _n_(461439, "config", lambda: config), "update"), {
            "num_patches": _a_(461442, _n_(461441, "self", lambda: self), "num_patches"),
            "position_embedding": _a_(461444, _n_(461443, "self", lambda: self), "position_embedding"),
            "positions": _c_(461448, _a_(461447, _a_(461446, _n_(461445, "self", lambda: self), "positions"), "numpy")),
        })
        _l_(461450)
        aux = _n_(461451, "config", lambda: config)
        _l_(461452)
        return aux

    @_n_(461454, "classmethod", lambda: classmethod)
    def from_config(cls, config):
        _l_(461459)

        aux = _c_(461457, _n_(461455, "cls", lambda: cls), **_n_(461456, "config", lambda: config))
        _l_(461458)
        return aux

    def call(self, encoded_patches):
        _l_(461471)

        encoded_positions = _c_(461464, _a_(461461, _n_(461460, "self", lambda: self), "position_embedding"), _a_(461463, _n_(461462, "self", lambda: self), "positions"))
        _l_(461465)
        encoded_patches = _n_(461466, "encoded_patches", lambda: encoded_patches) + _n_(461467, "encoded_positions", lambda: encoded_positions)
        _l_(461468)
        aux = _n_(461469, "encoded_patches", lambda: encoded_patches)
        _l_(461470)
        return aux

class MultiHeadAttentionLSA(_a_(461476, _a_(461475, _a_(461474, _n_(461473, "tf", lambda: tf), "keras"), "layers"), "MultiHeadAttention")):
    _l_(461559)

    def __init__(
        self,
        tau=None, #modificato, prima non c'era
        **kwargs
    ):
        _l_(461496)

        _c_(461482, _a_(461480, _n_(461477, "super", lambda: super)(_n_(461478, "MultiHeadAttentionLSA", lambda: MultiHeadAttentionLSA),_n_(461479, "self", lambda: self)), "__init__"), **_n_(461481, "kwargs", lambda: kwargs))
        _l_(461483)
        _n_(461484, "self", lambda: self).tau = _c_(461494, _a_(461486, _n_(461485, "tf", lambda: tf), "Variable"), _c_(461493, _a_(461488, _n_(461487, "math", lambda: math), "sqrt"), _c_(461492, _n_(461489, "float", lambda: float), _a_(461491, _n_(461490, "self", lambda: self), "_key_dim"))), trainable=True) # The trainable temperature term. The initial value is the square root of the key dimension.
        _l_(461495) # The trainable temperature term. The initial value is the square root of the key dimension.

    def get_config(self):
        _l_(461513)

        config = _c_(461501, _a_(461500, _c_(461499, _a_(461498, _n_(461497, "super", lambda: super)(), "get_config")), "copy"))
        _l_(461502)
        _c_(461509, _a_(461504, _n_(461503, "config", lambda: config), "update"), {
            "tau": _c_(461508, _a_(461507, _a_(461506, _n_(461505, "self", lambda: self), "tau"), "numpy")), #modificato, prima era solo self.tau
        })
        _l_(461510)
        aux = _n_(461511, "config", lambda: config)
        _l_(461512)
        return aux

    @_n_(461514, "classmethod", lambda: classmethod)
    def from_config(cls, config):
        _l_(461519)

        aux = _c_(461517, _n_(461515, "cls", lambda: cls), **_n_(461516, "config", lambda: config))
        _l_(461518)
        return aux

    def _compute_attention(self, query, key, value, attention_mask=None, training=None):
        _l_(461558)

        query = _c_(461525, _a_(461521, _n_(461520, "tf", lambda: tf), "multiply"), _n_(461522, "query", lambda: query), 1.0 / _a_(461524, _n_(461523, "self", lambda: self), "tau"))
        _l_(461526)
        attention_scores = _c_(461533, _a_(461528, _n_(461527, "tf", lambda: tf), "einsum"), _a_(461530, _n_(461529, "self", lambda: self), "_dot_product_equation"), _n_(461531, "key", lambda: key), _n_(461532, "query", lambda: query))
        _l_(461534)
        attention_scores = _c_(461539, _a_(461536, _n_(461535, "self", lambda: self), "_masked_softmax"), _n_(461537, "attention_scores", lambda: attention_scores), _n_(461538, "attention_mask", lambda: attention_mask)) 
        _l_(461540) 
        attention_scores_dropout = _c_(461545, _a_(461542, _n_(461541, "self", lambda: self), "_dropout_layer"), _n_(461543, "attention_scores", lambda: attention_scores), training=_n_(461544, "training", lambda: training)
        )
        _l_(461546)
        attention_output = _c_(461553, _a_(461548, _n_(461547, "tf", lambda: tf), "einsum"), _a_(461550, _n_(461549, "self", lambda: self), "_combine_equation"), _n_(461551, "attention_scores_dropout", lambda: attention_scores_dropout), _n_(461552, "value", lambda: value)
        )
        _l_(461554)
        aux = _n_(461555, "attention_output", lambda: attention_output), _n_(461556, "attention_scores", lambda: attention_scores)
        _l_(461557)
        return aux

def mlp(x, hidden_units, dropout_rate):
    _l_(461581)

    for units in _n_(461560, "hidden_units", lambda: hidden_units):
        _l_(461578)

        x = _c_(461569, _c_(461567, _a_(461562, _n_(461561, "layers", lambda: layers), "Dense"), _n_(461563, "units", lambda: units), activation=_a_(461566, _a_(461565, _n_(461564, "tf", lambda: tf), "nn"), "gelu")), _n_(461568, "x", lambda: x)) 
        _l_(461570) 
        x = _c_(461576, _c_(461574, _a_(461572, _n_(461571, "layers", lambda: layers), "Dropout"), _n_(461573, "dropout_rate", lambda: dropout_rate)), _n_(461575, "x", lambda: x))
        _l_(461577)
    aux = _n_(461579, "x", lambda: x)
    _l_(461580)
    return aux

diag_attn_mask = 1 - _c_(461585, _a_(461583, _n_(461582, "tf", lambda: tf), "eye"), _n_(461584, "NUM_PATCHES", lambda: NUM_PATCHES))
_l_(461586)
diag_attn_mask = _c_(461592, _a_(461588, _n_(461587, "tf", lambda: tf), "cast"), [_n_(461589, "diag_attn_mask", lambda: diag_attn_mask)], dtype=_a_(461591, _n_(461590, "tf", lambda: tf), "int8"))
_l_(461593)