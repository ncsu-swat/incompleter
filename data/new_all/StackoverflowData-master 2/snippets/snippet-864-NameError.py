#Source: https://stackoverflow.com/questions/54424933/typeerror-conv2dlayer-object-is-not-subscriptable
deconv4 = Conv2d(deconv3_bn_relu, 3, [5, 5], act=tf.tanh, padding='SAME', 
W_init=w_init, name='deconv4')

flow = deconv4[:, :, :, 0:2] 