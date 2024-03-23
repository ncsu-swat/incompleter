#Source: https://stackoverflow.com/questions/50779554/nameerror-name-gate-op-is-not-defined-tensorflow
class GradientDescentOptimizer(Optimizer, tf.train.GradientDescentOptimizer):
    def compute_gradients(self, loss, var_list=None,
                        gate_gradients=GATE_OP,
                        aggregation_method=None,
                        colocate_gradients_with_ops=False,
                        grad_loss=None):
        if var_list is not None:
            for v in var_list:
                v = v + epsilon
        if var_list is None:
            var_list = utils.hyperparameters()
            for v in var_list:
                v = v + epsilon
        grads_and_vars = super(GradientOracle, self).compute_gradients(loss, var_list)
        return grads_and_vars

    def apply_gradients(self, grads_and_vars, global_step=None, name=None):
        ts = super(GradientOracle, self).apply_gradients(grads_and_vars, global_step, name)
        dynamics = OrderedDict()
        for g, w in grads_and_vars:
            wk = w - tf.cast(self._learning_rate_tensor, g.dtype) * g
            dynamics[w] = wk
        return ts, dynamics

    def __str__(self):
        return '{}_lr{}'.format(self._name, self._learning_rate)

    @property
    def learning_rate(self):
        return self._learning_rate

    @property
    def learning_rate_tensor(self):
        return self._learning_rate_tensor