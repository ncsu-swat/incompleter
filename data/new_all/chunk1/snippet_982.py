# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59338360/how-do-i-resolve-typeerror-not-supported-between-instances-of-int-and-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(392118, _a_(392116, _n_(392115, "model", lambda: model), "compile"), loss = 'categorical_crossentropy', optimizer = _n_(392117, "optim", lambda: optim), metrics = ['accuracy'])
_l_(392119)

model_checkpoint = _c_(392123, _n_(392120, "CustomModelCheckpoint", lambda: CustomModelCheckpoint), _n_(392121, "model", lambda: model), './weights_'+_n_(392122, "model_name", lambda: model_name)+'/epoch_')    
_l_(392124)    

train_generator = _c_(392128, _n_(392125, "DataLoader_video_train", lambda: DataLoader_video_train), '/train_CS.txt',_n_(392126, "version", lambda: version), batch_size = _n_(392127, "batch_size", lambda: batch_size))
_l_(392129)
test_generator = _c_(392133, _n_(392130, "DataLoader_video_test", lambda: DataLoader_video_test), '/test_CS.txt', _n_(392131, "version", lambda: version), batch_size = _n_(392132, "batch_size", lambda: batch_size))
_l_(392134)