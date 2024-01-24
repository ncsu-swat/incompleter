#Source: https://stackoverflow.com/questions/64534019/typeerror-cant-pickle-weakref-objects
import tensorflow as tf
import pickle as pkl

class OBJ():
    def __init__(self):
        self.model = tf.keras.models.Sequential()

save_location = 'your save location here'
pkl.dump(OBJ(), save_location)