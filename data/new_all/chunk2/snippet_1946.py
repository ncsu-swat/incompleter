# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76224141/what-does-it-mean-by-typeerror-argument-of-type-adam-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(428546)

except ImportError:
    pass
try:
    from tensorflow.keras.optimizers import Adam
    _l_(428548)

except ImportError:
    pass
try:
    from tensorflow.keras.models import Model
    _l_(428550)

except ImportError:
    pass
try:
    from ISR.models import RRDN, Discriminator
    _l_(428552)

except ImportError:
    pass
try:
    from ISR.models import Cut_VGG19
    _l_(428554)

except ImportError:
    pass
try:
    from ISR.train import Trainer
    _l_(428556)

except ImportError:
    pass

# Define paths for HR and LR input images
lr_train_dir = 'C:/data/lr_train_150/',
_l_(428557)
hr_train_dir = 'C:/data/hr_train_150/',
_l_(428558)
lr_valid_dir = 'C:/data/lr_test_150/',
_l_(428559)
hr_valid_dir = 'C:/data/hr_test_150/',
_l_(428560)

lr_train_patch_size = 22 #size of my LR image
_l_(428561) #size of my LR image
layers_to_extract = [5, 9]
_l_(428562)
scale = 10
_l_(428563)
hr_train_patch_size = _n_(428564, "lr_train_patch_size", lambda: lr_train_patch_size) * _n_(428565, "scale", lambda: scale) # 220 Size of my HR image
_l_(428566) # 220 Size of my HR image


# Instantiate models
rrdn = _c_(428570, _n_(428567, "RRDN", lambda: RRDN), arch_params={'C':4, 'D':3, 'G':64, 'G0':64, 'T':10, 'x':_n_(428568, "scale", lambda: scale)}, patch_size=_n_(428569, "lr_train_patch_size", lambda: lr_train_patch_size))
_l_(428571)
discriminator = _c_(428575, _n_(428572, "Cut_VGG19", lambda: Cut_VGG19), patch_size=_n_(428573, "hr_train_patch_size", lambda: hr_train_patch_size), layers_to_extract=_n_(428574, "layers_to_extract", lambda: layers_to_extract))
_l_(428576)
feature_extractor = _c_(428579, _n_(428577, "Discriminator", lambda: Discriminator), patch_size=_n_(428578, "hr_train_patch_size", lambda: hr_train_patch_size), kernel_size=3)
_l_(428580)


# Define optimizer and loss function
optimizer = _c_(428582, _n_(428581, "Adam", lambda: Adam), 1e-4, beta_1=0.9, beta_2=0.999)
_l_(428583)
#loss = 'mse'
loss_weights = {
  'generator': 0.0,
  'feature_extractor': 0.0833,
  'discriminator': 0.01
}
_l_(428584)
losses = {
  'generator': 'mae',
  'feature_extractor': 'mse',
  'discriminator': 'binary_crossentropy'
} 
_l_(428585) 
learning_rate = {'initial_value': 0.0004, 'decay_factor': 0.5, 'decay_frequency': 30}
_l_(428586)
log_dirs = {'logs': './logs', 'weights': './weights'}
_l_(428587)
flatness = {'min': 0.0, 'max': 0.15, 'increase': 0.01, 'increase_frequency': 5}
_l_(428588)


# Define trainer
trainer = _c_(428599, _n_(428589, "Trainer", lambda: Trainer), generator=_n_(428590, "rrdn", lambda: rrdn), 
                  discriminator=_n_(428591, "discriminator", lambda: discriminator),
                  feature_extractor=_n_(428592, "feature_extractor", lambda: feature_extractor), 
                  #name='srgan', 
                  log_dirs=_n_(428593, "log_dirs", lambda: log_dirs),
                  #checkpoint_dir='./models', 
                  learning_rate=_n_(428594, "learning_rate", lambda: learning_rate), 
                  losses=_n_(428595, "losses", lambda: losses), 
                  flatness = _n_(428596, "flatness", lambda: flatness),
                  loss_weights = _n_(428597, "loss_weights", lambda: loss_weights),
                  adam_optimizer=_n_(428598, "optimizer", lambda: optimizer),
                  lr_train_dir = 'C:/data/lr_train_150/',
                  hr_train_dir = 'C:/data/hr_train_150/',
                  lr_valid_dir = 'C:/data/lr_test_150/',
                  hr_valid_dir = 'C:/data/hr_test_150/'
                 )
_l_(428600)

# Train the model
_c_(428603, _a_(428602, _n_(428601, "trainer", lambda: trainer), "train"), batch_size=16, 
              steps_per_epoch=20, 
              #validation_steps=10, 
              epochs=1, 
              #print_frequency=100
              monitored_metrics={'val_generator_PSNR_Y': 'max'}
             )
_l_(428604)