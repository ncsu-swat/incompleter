# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75261563/gym-0-21-stable-baseline3-typeerror-tuple-indices-must-be-integers-or-slices
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gym
    _l_(438319)

except ImportError:
    pass
try:
    from stable_baselines3 import ppo
    _l_(438321)

except ImportError:
    pass

env = _c_(438324, _a_(438323, _n_(438322, "gym", lambda: gym), "make"), "gym_envs:gym_envs/GridWorld-v0")
_l_(438325)

model = _c_(438328, _n_(438326, "PPO", lambda: PPO), "MultiInputPolicy", _n_(438327, "env", lambda: env), tensorboard_log="./logs/", verbose=1)
_l_(438329)
_c_(438332, _a_(438331, _n_(438330, "model", lambda: model), "learn"), total_timesteps=1000)
_l_(438333)