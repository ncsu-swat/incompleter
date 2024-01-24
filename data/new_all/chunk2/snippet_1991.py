# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72084680/typeerror-keyword-argument-not-understood-query-shape-with-keras-and-te
# From PB to h5 -- then load from h5

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
checkpoint_filepath="drive/MyDrive/Tirocinio/ViT/Model/vit_"+ _n_(430852, "num_dataset", lambda: num_dataset)
_l_(430853)
try:
    import os
    _l_(430855)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(430857)

except ImportError:
    pass
try:
    from tensorflow.keras.preprocessing import image
    _l_(430859)

except ImportError:
    pass
try:
    from keras.models import load_model
    _l_(430861)

except ImportError:
    pass


# LOAD THE PB MODEL
New_Model = _c_(430867, _a_(430865, _a_(430864, _a_(430863, _n_(430862, "tf", lambda: tf), "keras"), "models"), "load_model"), _n_(430866, "checkpoint_filepath", lambda: checkpoint_filepath)) # Loading the Tensorflow Saved Model (PB)
_l_(430868) # Loading the Tensorflow Saved Model (PB)
#print(New_Model.summary())

# Saving the Model in H5 Format and Loading it (to check if it is same as PB Format)
_c_(430875, _a_(430872, _a_(430871, _a_(430870, _n_(430869, "tf", lambda: tf), "keras"), "models"), "save_model"), _n_(430873, "New_Model", lambda: New_Model), _n_(430874, "checkpoint_filepath", lambda: checkpoint_filepath)+'/vit_1_model.h5') # Saving the Model in H5 Format
_l_(430876) # Saving the Model in H5 Format

# LOAD h5
loaded_model_from_h5 = _c_(430882, _n_(430877, "load_model", lambda: load_model), _n_(430878, "checkpoint_filepath", lambda: checkpoint_filepath)+'/vit_1_model.h5', custom_objects ={'ShiftedPatchTokenization': _n_(430879, "ShiftedPatchTokenization", lambda: ShiftedPatchTokenization), 'PatchEncoder':_n_(430880, "PatchEncoder", lambda: PatchEncoder), 'MultiHeadAttentionLSA':_n_(430881, "MultiHeadAttentionLSA", lambda: MultiHeadAttentionLSA)}) # Loading the H5 Saved Model
_l_(430883) # Loading the H5 Saved Model
_c_(430888, _n_(430884, "print", lambda: print), _c_(430887, _a_(430886, _n_(430885, "loaded_model_from_h5", lambda: loaded_model_from_h5), "summary")))
_l_(430889)