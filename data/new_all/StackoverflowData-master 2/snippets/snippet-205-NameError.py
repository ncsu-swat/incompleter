#Source: https://stackoverflow.com/questions/64175246/keras-model-fit-giving-out-typeerror-nonetype-object-is-not-callable
class SiameseNet(tf.keras.layers.Layer):

  def __init__(self, model):
    self.model = model  # This is the image feature extraction model (similar to InceptionV3)
    super().__init__()

  def call(self, feat):
    feats = self.model(feat[0])
    nfeats = self.model(feat[1])

    return [feats, nfeats]