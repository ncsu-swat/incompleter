# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75784792/typeerror-load-missing-1-required-positional-argument-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import torch
    _l_(355963)

except ImportError:
    pass
try:
    import torch.backends.cudnn as cudnn
    _l_(355965)

except ImportError:
    pass
try:
    import numpy as np
    _l_(355967)

except ImportError:
    pass
try:
    import os
    _l_(355969)

except ImportError:
    pass
try:
    import argparse
    _l_(355971)

except ImportError:
    pass
try:
    import time
    _l_(355973)

except ImportError:
    pass
try:
    from tqdm import tqdm
    _l_(355975)

except ImportError:
    pass
try:
    import joblib
    _l_(355977)

except ImportError:
    pass
try:
    from utils.setup import get_model,get_data_loader
    _l_(355979)

except ImportError:
    pass
try:
    from utils.defense import gen_mask_set,double_masking_precomputed,certify_precomputed
    _l_(355981)

except ImportError:
    pass


    

parser = _c_(355984, _a_(355983, _n_(355982, "argparse", lambda: argparse), "ArgumentParser"))
_l_(355985)
_c_(355989, _a_(355987, _n_(355986, "parser", lambda: parser), "add_argument"), "--model_dir",default='checkpoints',type=_n_(355988, "str", lambda: str),help="directory of checkpoints")
_l_(355990)
_c_(355994, _a_(355992, _n_(355991, "parser", lambda: parser), "add_argument"), '--data_dir', default='data', type=_n_(355993, "str", lambda: str),help="directory of data")
_l_(355995)
_c_(355999, _a_(355997, _n_(355996, "parser", lambda: parser), "add_argument"), '--dataset', default='imagenette',type=_n_(355998, "str", lambda: str),choices=('imagenette','imagenet','cifar','cifar100','svhn','flower102'),help="dataset")
_l_(356000)
_c_(356004, _a_(356002, _n_(356001, "parser", lambda: parser), "add_argument"), "--model",default='vit_base_patch16_224',type=_n_(356003, "str", lambda: str),help="model name")
_l_(356005)
_c_(356009, _a_(356007, _n_(356006, "parser", lambda: parser), "add_argument"), "--num_img",default=-1,type=_n_(356008, "int", lambda: int),help="number of randomly selected images for this experiment (-1: using the all images)")
_l_(356010)
_c_(356014, _a_(356012, _n_(356011, "parser", lambda: parser), "add_argument"), "--mask_stride",default=-1,type=_n_(356013, "int", lambda: int),help="mask stride s (square patch; conflict with num_mask)")
_l_(356015)
_c_(356019, _a_(356017, _n_(356016, "parser", lambda: parser), "add_argument"), "--num_mask",default=-1,type=_n_(356018, "int", lambda: int),help="number of mask in one dimension (square patch; conflict with mask_stride)")
_l_(356020)
_c_(356024, _a_(356022, _n_(356021, "parser", lambda: parser), "add_argument"), "--patch_size",default=32,type=_n_(356023, "int", lambda: int),help="size of the adversarial patch (square patch)")
_l_(356025)
_c_(356029, _a_(356027, _n_(356026, "parser", lambda: parser), "add_argument"), "--pa",default=-1,type=_n_(356028, "int", lambda: int),help="size of the adversarial patch (first axis; for rectangle patch)")
_l_(356030)
_c_(356034, _a_(356032, _n_(356031, "parser", lambda: parser), "add_argument"), "--pb",default=-1,type=_n_(356033, "int", lambda: int),help="size of the adversarial patch (second axis; for rectangle patch)")
_l_(356035)
_c_(356039, _a_(356037, _n_(356036, "parser", lambda: parser), "add_argument"), "--dump_dir",default='dump',type=_n_(356038, "str", lambda: str),help='directory to dump two-mask predictions')
_l_(356040)
_c_(356043, _a_(356042, _n_(356041, "parser", lambda: parser), "add_argument"), "--override",action='store_true',help='override dumped file')
_l_(356044)

args = _c_(356047, _a_(356046, _n_(356045, "parser", lambda: parser), "parse_args"))
_l_(356048)
DATASET = _a_(356050, _n_(356049, "args", lambda: args), "dataset")
_l_(356051)
MODEL_DIR = _c_(356057, _a_(356054, _a_(356053, _n_(356052, "os", lambda: os), "path"), "join"), '.',_a_(356056, _n_(356055, "args", lambda: args), "model_dir"))
_l_(356058)
DATA_DIR = _c_(356065, _a_(356061, _a_(356060, _n_(356059, "os", lambda: os), "path"), "join"), _a_(356063, _n_(356062, "args", lambda: args), "data_dir"),_n_(356064, "DATASET", lambda: DATASET))
_l_(356066)
DUMP_DIR = _c_(356072, _a_(356069, _a_(356068, _n_(356067, "os", lambda: os), "path"), "join"), '.',_a_(356071, _n_(356070, "args", lambda: args), "dump_dir"))
_l_(356073)
if not _c_(356078, _a_(356076, _a_(356075, _n_(356074, "os", lambda: os), "path"), "exists"), _n_(356077, "DUMP_DIR", lambda: DUMP_DIR)):
    _l_(356084)

    _c_(356082, _a_(356080, _n_(356079, "os", lambda: os), "mkdir"), _n_(356081, "DUMP_DIR", lambda: DUMP_DIR))
    _l_(356083)

MODEL_NAME = _a_(356086, _n_(356085, "args", lambda: args), "model")
_l_(356087)
NUM_IMG = _a_(356089, _n_(356088, "args", lambda: args), "num_img")
_l_(356090)

#get model and data loader
model = _c_(356095, _n_(356091, "get_model", lambda: get_model), _n_(356092, "MODEL_NAME", lambda: MODEL_NAME),_n_(356093, "DATASET", lambda: DATASET),_n_(356094, "MODEL_DIR", lambda: MODEL_DIR))
_l_(356096)
val_loader,NUM_IMG,ds_config = _c_(356102, _n_(356097, "get_data_loader", lambda: get_data_loader), _n_(356098, "DATASET", lambda: DATASET),_n_(356099, "DATA_DIR", lambda: DATA_DIR),_n_(356100, "model", lambda: model),batch_size=16,num_img=_n_(356101, "NUM_IMG", lambda: NUM_IMG),train=False)
_l_(356103)

device = 'cuda' 
_l_(356104) 
model = _c_(356108, _a_(356106, _n_(356105, "model", lambda: model), "to"), _n_(356107, "device", lambda: device))
_l_(356109)
_c_(356112, _a_(356111, _n_(356110, "model", lambda: model), "eval"))
_l_(356113)
_n_(356114, "cudnn", lambda: cudnn).benchmark = True
_l_(356115)

# generate the mask set
mask_list,MASK_SIZE,MASK_STRIDE = _c_(356119, _n_(356116, "gen_mask_set", lambda: gen_mask_set), _n_(356117, "args", lambda: args),_n_(356118, "ds_config", lambda: ds_config))
_l_(356120)

# the computation of two-mask predictions is expensive; will dump (or resue the dumped) two-mask predictions.
SUFFIX = _c_(356127, _a_(356121, '_two_mask_{}_{}_m{}_s{}_{}.z', "format"), _n_(356122, "DATASET", lambda: DATASET),_n_(356123, "MODEL_NAME", lambda: MODEL_NAME),_n_(356124, "MASK_SIZE", lambda: MASK_SIZE),_n_(356125, "MASK_STRIDE", lambda: MASK_STRIDE),_n_(356126, "NUM_IMG", lambda: NUM_IMG))
_l_(356128)
if not _a_(356130, _n_(356129, "args", lambda: args), "override") and _c_(356140, _a_(356133, _a_(356132, _n_(356131, "os", lambda: os), "path"), "exists"), _c_(356139, _a_(356136, _a_(356135, _n_(356134, "os", lambda: os), "path"), "join"), _n_(356137, "DUMP_DIR", lambda: DUMP_DIR),'prediction_map_list'+_n_(356138, "SUFFIX", lambda: SUFFIX))):
    _l_(356398)

    _c_(356142, _n_(356141, "print", lambda: print), 'loading two-mask predictions')
    _l_(356143)
    prediction_map_list = _c_(356152, _a_(356145, _n_(356144, "joblib", lambda: joblib), "load"), _c_(356151, _a_(356148, _a_(356147, _n_(356146, "os", lambda: os), "path"), "join"), _n_(356149, "DUMP_DIR", lambda: DUMP_DIR),'prediction_map_list'+_n_(356150, "SUFFIX", lambda: SUFFIX)))
    _l_(356153)
    orig_prediction_list = _c_(356166, _a_(356155, _n_(356154, "joblib", lambda: joblib), "load"), _c_(356165, _a_(356158, _a_(356157, _n_(356156, "os", lambda: os), "path"), "join"), _n_(356159, "DUMP_DIR", lambda: DUMP_DIR),_c_(356164, _a_(356160, 'orig_prediction_list_{}_{}_{}.z', "format"), _n_(356161, "DATASET", lambda: DATASET),_n_(356162, "MODEL_NAME", lambda: MODEL_NAME),_n_(356163, "NUM_IMG", lambda: NUM_IMG))))
    _l_(356167)
    label_list = _c_(356180, _a_(356169, _n_(356168, "joblib", lambda: joblib), "load"), _c_(356179, _a_(356172, _a_(356171, _n_(356170, "os", lambda: os), "path"), "join"), _n_(356173, "DUMP_DIR", lambda: DUMP_DIR),_c_(356178, _a_(356174, 'label_list_{}_{}_{}.z', "format"), _n_(356175, "DATASET", lambda: DATASET),_n_(356176, "MODEL_NAME", lambda: MODEL_NAME),_n_(356177, "NUM_IMG", lambda: NUM_IMG))))
    _l_(356181)
else:
    _c_(356183, _n_(356182, "print", lambda: print), 'computing two-mask predictions')
    _l_(356184)
    prediction_map_list = []
    _l_(356185)
    confidence_map_list = []
    _l_(356186)
    label_list = []
    _l_(356187)
    orig_prediction_list = []
    _l_(356188)
    for data,labels in _c_(356191, _n_(356189, "tqdm", lambda: tqdm), _n_(356190, "val_loader", lambda: val_loader)):
        _l_(356325)

        data=_c_(356195, _a_(356193, _n_(356192, "data", lambda: data), "to"), _n_(356194, "device", lambda: device))
        _l_(356196)
        labels = _c_(356199, _a_(356198, _n_(356197, "labels", lambda: labels), "numpy"))
        _l_(356200)
        num_img = _a_(356202, _n_(356201, "data", lambda: data), "shape")[0]
        _l_(356203)
        num_mask = _c_(356206, _n_(356204, "len", lambda: len), _n_(356205, "mask_list", lambda: mask_list))
        _l_(356207)

        #two-mask predictions
        prediction_map = _c_(356214, _a_(356209, _n_(356208, "np", lambda: np), "zeros"), [_n_(356210, "num_img", lambda: num_img),_n_(356211, "num_mask", lambda: num_mask),_n_(356212, "num_mask", lambda: num_mask)],dtype=_n_(356213, "int", lambda: int))
        _l_(356215)
        confidence_map = _c_(356221, _a_(356217, _n_(356216, "np", lambda: np), "zeros"), [_n_(356218, "num_img", lambda: num_img),_n_(356219, "num_mask", lambda: num_mask),_n_(356220, "num_mask", lambda: num_mask)])        
        _l_(356222)        
        for i,mask in _c_(356225, _n_(356223, "enumerate", lambda: enumerate), _n_(356224, "mask_list", lambda: mask_list)):
            _l_(356288)

            for j in _c_(356229, _n_(356226, "range", lambda: range), _n_(356227, "i", lambda: i),_n_(356228, "num_mask", lambda: num_mask)):
                _l_(356287)

                mask2 = _n_(356230, "mask_list", lambda: mask_list)[_n_(356231, "j", lambda: j)]
                _l_(356232)
                masked_output = _c_(356248, _n_(356233, "model", lambda: model), _c_(356247, _a_(356235, _n_(356234, "torch", lambda: torch), "where"), _c_(356240, _a_(356237, _n_(356236, "torch", lambda: torch), "logical_and"), _n_(356238, "mask", lambda: mask),_n_(356239, "mask2", lambda: mask2)),_n_(356241, "data", lambda: data),_c_(356246, _a_(356245, _c_(356244, _a_(356243, _n_(356242, "torch", lambda: torch), "tensor"), 0.), "cuda"))))
                _l_(356249)
                masked_output = _c_(356255, _a_(356253, _a_(356252, _a_(356251, _n_(356250, "torch", lambda: torch), "nn"), "functional"), "softmax"), _n_(356254, "masked_output", lambda: masked_output),dim=1)
                _l_(356256)
                masked_conf, masked_pred = _c_(356259, _a_(356258, _n_(356257, "masked_output", lambda: masked_output), "max"), 1)
                _l_(356260)
                masked_conf = _c_(356267, _a_(356266, _c_(356265, _a_(356264, _c_(356263, _a_(356262, _n_(356261, "masked_conf", lambda: masked_conf), "detach")), "cpu")), "numpy"))
                _l_(356268)
                _n_(356269, "confidence_map", lambda: confidence_map)[:,_n_(356270, "i", lambda: i),_n_(356271, "j", lambda: j)] = _n_(356272, "masked_conf", lambda: masked_conf)
                _l_(356273)
                masked_pred = _c_(356280, _a_(356279, _c_(356278, _a_(356277, _c_(356276, _a_(356275, _n_(356274, "masked_pred", lambda: masked_pred), "detach")), "cpu")), "numpy"))
                _l_(356281)
                _n_(356282, "prediction_map", lambda: prediction_map)[:,_n_(356283, "i", lambda: i),_n_(356284, "j", lambda: j)] = _n_(356285, "masked_pred", lambda: masked_pred)
                _l_(356286)
        #vanilla predictions
        clean_output = _c_(356291, _n_(356289, "model", lambda: model), _n_(356290, "data", lambda: data))
        _l_(356292)
        clean_conf, clean_pred = _c_(356295, _a_(356294, _n_(356293, "clean_output", lambda: clean_output), "max"), 1)  
        _l_(356296)  
        clean_pred = _c_(356303, _a_(356302, _c_(356301, _a_(356300, _c_(356299, _a_(356298, _n_(356297, "clean_pred", lambda: clean_pred), "detach")), "cpu")), "numpy"))
        _l_(356304)
        _c_(356308, _a_(356306, _n_(356305, "orig_prediction_list", lambda: orig_prediction_list), "append"), _n_(356307, "clean_pred", lambda: clean_pred))
        _l_(356309)
        _c_(356313, _a_(356311, _n_(356310, "prediction_map_list", lambda: prediction_map_list), "append"), _n_(356312, "prediction_map", lambda: prediction_map))
        _l_(356314)
        _c_(356318, _a_(356316, _n_(356315, "confidence_map_list", lambda: confidence_map_list), "append"), _n_(356317, "confidence_map", lambda: confidence_map))
        _l_(356319)
        _c_(356323, _a_(356321, _n_(356320, "label_list", lambda: label_list), "append"), _n_(356322, "labels", lambda: labels))
        _l_(356324)
    
    prediction_map_list = _c_(356329, _a_(356327, _n_(356326, "np", lambda: np), "concatenate"), _n_(356328, "prediction_map_list", lambda: prediction_map_list))
    _l_(356330)
    confidence_map_list = _c_(356334, _a_(356332, _n_(356331, "np", lambda: np), "concatenate"), _n_(356333, "confidence_map_list", lambda: confidence_map_list))
    _l_(356335)
    orig_prediction_list = _c_(356339, _a_(356337, _n_(356336, "np", lambda: np), "concatenate"), _n_(356338, "orig_prediction_list", lambda: orig_prediction_list))
    _l_(356340)
    label_list = _c_(356344, _a_(356342, _n_(356341, "np", lambda: np), "concatenate"), _n_(356343, "label_list", lambda: label_list))
    _l_(356345)

    _c_(356355, _a_(356347, _n_(356346, "joblib", lambda: joblib), "dump"), _n_(356348, "confidence_map_list", lambda: confidence_map_list),_c_(356354, _a_(356351, _a_(356350, _n_(356349, "os", lambda: os), "path"), "join"), _n_(356352, "DUMP_DIR", lambda: DUMP_DIR),'confidence_map_list'+_n_(356353, "SUFFIX", lambda: SUFFIX)))
    _l_(356356)
    _c_(356366, _a_(356358, _n_(356357, "joblib", lambda: joblib), "dump"), _n_(356359, "prediction_map_list", lambda: prediction_map_list),_c_(356365, _a_(356362, _a_(356361, _n_(356360, "os", lambda: os), "path"), "join"), _n_(356363, "DUMP_DIR", lambda: DUMP_DIR),'prediction_map_list'+_n_(356364, "SUFFIX", lambda: SUFFIX)))
    _l_(356367)
    _c_(356381, _a_(356369, _n_(356368, "joblib", lambda: joblib), "dump"), _n_(356370, "orig_prediction_list", lambda: orig_prediction_list),_c_(356380, _a_(356373, _a_(356372, _n_(356371, "os", lambda: os), "path"), "join"), _n_(356374, "DUMP_DIR", lambda: DUMP_DIR),_c_(356379, _a_(356375, 'orig_prediction_list_{}_{}_{}.z', "format"), _n_(356376, "DATASET", lambda: DATASET),_n_(356377, "MODEL_NAME", lambda: MODEL_NAME),_n_(356378, "NUM_IMG", lambda: NUM_IMG))))
    _l_(356382)
    _c_(356396, _a_(356384, _n_(356383, "joblib", lambda: joblib), "dump"), _n_(356385, "label_list", lambda: label_list),_c_(356395, _a_(356388, _a_(356387, _n_(356386, "os", lambda: os), "path"), "join"), _n_(356389, "DUMP_DIR", lambda: DUMP_DIR),_c_(356394, _a_(356390, 'label_list_{}_{}_{}.z', "format"), _n_(356391, "DATASET", lambda: DATASET),_n_(356392, "MODEL_NAME", lambda: MODEL_NAME),_n_(356393, "NUM_IMG", lambda: NUM_IMG))))
    _l_(356397)


clean_corr = 0
_l_(356399)
robust = 0
_l_(356400)
orig_corr = 0
_l_(356401)
for i,(prediction_map,label,orig_pred) in _c_(356408, _n_(356402, "enumerate", lambda: enumerate), _c_(356407, _n_(356403, "zip", lambda: zip), _n_(356404, "prediction_map_list", lambda: prediction_map_list),_n_(356405, "label_list", lambda: label_list),_n_(356406, "orig_prediction_list", lambda: orig_prediction_list))):
    _l_(356433)

    prediction_map = _n_(356409, "prediction_map", lambda: prediction_map) + _a_(356411, _n_(356410, "prediction_map", lambda: prediction_map), "T") - _c_(356418, _a_(356413, _n_(356412, "np", lambda: np), "diag"), _c_(356417, _a_(356415, _n_(356414, "np", lambda: np), "diag"), _n_(356416, "prediction_map", lambda: prediction_map))) #generate a symmetric matrix from a triangle matrix
    _l_(356419) #generate a symmetric matrix from a triangle matrix
    robust += _c_(356423, _n_(356420, "certify_precomputed", lambda: certify_precomputed), _n_(356421, "prediction_map", lambda: prediction_map),_n_(356422, "label", lambda: label))
    _l_(356424)
    clean_corr += _c_(356427, _n_(356425, "double_masking_precomputed", lambda: double_masking_precomputed), _n_(356426, "prediction_map", lambda: prediction_map)) == _n_(356428, "label", lambda: label)
    _l_(356429)
    orig_corr += _n_(356430, "orig_pred", lambda: orig_pred) == _n_(356431, "label", lambda: label)
    _l_(356432)

_c_(356435, _n_(356434, "print", lambda: print), "------------------------------")
_l_(356436)
_c_(356440, _n_(356437, "print", lambda: print), "Certified robust accuracy:",_n_(356438, "robust", lambda: robust)/_n_(356439, "NUM_IMG", lambda: NUM_IMG))
_l_(356441)
_c_(356445, _n_(356442, "print", lambda: print), "Clean accuracy with defense:",_n_(356443, "clean_corr", lambda: clean_corr)/_n_(356444, "NUM_IMG", lambda: NUM_IMG))
_l_(356446)
_c_(356450, _n_(356447, "print", lambda: print), "Clean accuracy without defense:",_n_(356448, "orig_corr", lambda: orig_corr)/_n_(356449, "NUM_IMG", lambda: NUM_IMG))
_l_(356451)