# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62119988/attributeerror-type-object-fooenv-has-no-attribute-reset
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import json
  _l_(683594)

except ImportError:
  pass
try:
  import numpy as np
  _l_(683596)

except ImportError:
  pass
try:
  from keras.models import Sequential
  _l_(683598)

except ImportError:
  pass
try:
  from keras.layers.core import Dense
  _l_(683600)

except ImportError:
  pass
try:
  from keras.optimizers import sgd
  _l_(683602)

except ImportError:
  pass
try:
  from FooEnv import FooEnv
  _l_(683604)

except ImportError:
  pass
class ExperienceReplay(_n_(683605, "object", lambda: object)):
  _l_(683718)

  def __init__(self, max_memory=100, discount=.9):
    _l_(683616)

    _n_(683606, "self", lambda: self).max_memory = _n_(683607, "max_memory", lambda: max_memory)
    _l_(683608)
    _n_(683609, "self", lambda: self).memory = _c_(683611, _n_(683610, "list", lambda: list))
    _l_(683612)
    _n_(683613, "self", lambda: self).discount = _n_(683614, "discount", lambda: discount)
    _l_(683615)

  def remember(self, states, game_over):
    _l_(683632)

    # memory[i] = [[state_t, action_t, reward_t, state_t+1], game_over?]
    _c_(683622, _a_(683619, _a_(683618, _n_(683617, "self", lambda: self), "memory"), "append"), [_n_(683620, "states", lambda: states), _n_(683621, "game_over", lambda: game_over)])
    _l_(683623)
    if _c_(683627, _n_(683624, "len", lambda: len), _a_(683626, _n_(683625, "self", lambda: self), "memory")) > _a_(683629, _n_(683628, "self", lambda: self), "max_memory"):
      _l_(683631)

      del self.memory[0]
      _l_(683630)

  def get_batch(self, model, batch_size=10):
    _l_(683717)

    len_memory = _c_(683636, _n_(683633, "len", lambda: len), _a_(683635, _n_(683634, "self", lambda: self), "memory"))
    _l_(683637)
    num_actions = _a_(683639, _n_(683638, "model", lambda: model), "output_shape")[-1]
    _l_(683640)
    # env_dim = self.memory[0][0][0].shape[1]
    env_dim = _a_(683643, _a_(683642, _n_(683641, "self", lambda: self), "memory")[0][0][0], "shape")[1]
    _l_(683644)
    inputs = _c_(683652, _a_(683646, _n_(683645, "np", lambda: np), "zeros"), (_c_(683650, _n_(683647, "min", lambda: min), _n_(683648, "len_memory", lambda: len_memory), _n_(683649, "batch_size", lambda: batch_size)), _n_(683651, "env_dim", lambda: env_dim)))
    _l_(683653)
    targets = _c_(683659, _a_(683655, _n_(683654, "np", lambda: np), "zeros"), (_a_(683657, _n_(683656, "inputs", lambda: inputs), "shape")[0], _n_(683658, "num_actions", lambda: num_actions)))
    _l_(683660)
    for i, idx in _c_(683669, _n_(683661, "enumerate", lambda: enumerate), _c_(683668, _a_(683664, _a_(683663, _n_(683662, "np", lambda: np), "random"), "randint"), 0, _n_(683665, "len_memory", lambda: len_memory),
                                              size=_a_(683667, _n_(683666, "inputs", lambda: inputs), "shape")[0])):
      _l_(683713)

      state_t, action_t, reward_t, state_tp1 = _a_(683671, _n_(683670, "self", lambda: self), "memory")[_n_(683672, "idx", lambda: idx)][0]
      _l_(683673)
      game_over = _a_(683675, _n_(683674, "self", lambda: self), "memory")[_n_(683676, "idx", lambda: idx)][1]
      _l_(683677)

      _n_(683678, "inputs", lambda: inputs)[_n_(683679, "i", lambda: i):_n_(683680, "i", lambda: i)+1] = _n_(683681, "state_t", lambda: state_t)
      _l_(683682)
      # There should be no target values for actions not taken.
      # Thou shalt not correct actions not taken #deep
      _n_(683683, "targets", lambda: targets)[_n_(683684, "i", lambda: i)] = _c_(683688, _a_(683686, _n_(683685, "model", lambda: model), "predict"), _n_(683687, "state_t", lambda: state_t))[0]
      _l_(683689)
      Q_sa = _c_(683696, _a_(683691, _n_(683690, "np", lambda: np), "max"), _c_(683695, _a_(683693, _n_(683692, "model", lambda: model), "predict"), _n_(683694, "state_tp1", lambda: state_tp1))[0])
      _l_(683697)
      if _n_(683698, "game_over", lambda: game_over):
        _l_(683712)

        _n_(683699, "targets", lambda: targets)[_n_(683700, "i", lambda: i), _n_(683701, "action_t", lambda: action_t)] = _n_(683702, "reward_t", lambda: reward_t)
        _l_(683703)
      else:
          # reward_t + gamma * max_a' Q(s', a')
          _n_(683704, "targets", lambda: targets)[_n_(683705, "i", lambda: i), _n_(683706, "action_t", lambda: action_t)] = _n_(683707, "reward_t", lambda: reward_t) + _a_(683709, _n_(683708, "self", lambda: self), "discount") * _n_(683710, "Q_sa", lambda: Q_sa)
          _l_(683711)
    aux = _n_(683714, "inputs", lambda: inputs), _n_(683715, "targets", lambda: targets)
    _l_(683716)
    return aux
if _n_(683719, "__name__", lambda: __name__) == "__main__":
  _l_(683775)

  # parameters
  epsilon = .1  
  _l_(683720)  
  num_actions = 2  
  _l_(683721)  
  epoch = 1000
  _l_(683722)
  max_memory = 500
  _l_(683723)
  hidden_size = 100
  _l_(683724)
  batch_size = 50
  _l_(683725)
  input_size = 2
  _l_(683726)
  f_c=[2.4*10**9]
  _l_(683727)
  eta_Los=[1]
  _l_(683728)
  eta_NLos=[2]
  _l_(683729)
  x_threshold = [5]
  _l_(683730)
  model = _c_(683732, _n_(683731, "Sequential", lambda: Sequential))
  _l_(683733)
  _c_(683739, _a_(683735, _n_(683734, "model", lambda: model), "add"), _c_(683738, _n_(683736, "Dense", lambda: Dense), _n_(683737, "hidden_size", lambda: hidden_size), input_shape=(2, ), activation='relu'))
  _l_(683740)
  _c_(683746, _a_(683742, _n_(683741, "model", lambda: model), "add"), _c_(683745, _n_(683743, "Dense", lambda: Dense), _n_(683744, "hidden_size", lambda: hidden_size), activation='relu'))
  _l_(683747)
  _c_(683753, _a_(683749, _n_(683748, "model", lambda: model), "add"), _c_(683752, _n_(683750, "Dense", lambda: Dense), _n_(683751, "num_actions", lambda: num_actions)))
  _l_(683754)
  _c_(683759, _a_(683756, _n_(683755, "model", lambda: model), "compile"), _c_(683758, _n_(683757, "sgd", lambda: sgd), lr=.2), "mse")
  _l_(683760)
  # Define environment/game
  env = _c_(683765, _n_(683761, "FooEnv", lambda: FooEnv), _n_(683762, "f_c", lambda: f_c), _n_(683763, "eta_Los", lambda: eta_Los), _n_(683764, "eta_NLos", lambda: eta_NLos))
  _l_(683766)
  # Initialize experience replay object
  exp_replay = _c_(683769, _n_(683767, "ExperienceReplay", lambda: ExperienceReplay), max_memory=_n_(683768, "max_memory", lambda: max_memory))
  _l_(683770)
  _c_(683773, _a_(683772, _n_(683771, "FooEnv", lambda: FooEnv), "reset"))
  _l_(683774)