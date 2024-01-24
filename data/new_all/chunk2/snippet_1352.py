# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75261563/gym-0-21-stable-baseline3-typeerror-tuple-indices-must-be-integers-or-slices
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gym
    _l_(447848)

except ImportError:
    pass
try:
    from stable_baselines3 import PPO
    _l_(447850)

except ImportError:
    pass
try:
    from stable_baselines3.common.vec_env import DummyVecEnv
    _l_(447852)

except ImportError:
    pass

env = _c_(447857, _n_(447853, "DummyVecEnv", lambda: DummyVecEnv), [lambda: _c_(447856, _a_(447855, _n_(447854, "gym", lambda: gym), "make"), "gym_envs:gym_envs/GridWorld-v0")])
_l_(447858)

model = _c_(447861, _n_(447859, "PPO", lambda: PPO), "MultiInputPolicy", _n_(447860, "env", lambda: env), verbose=1)
_l_(447862)
_c_(447865, _a_(447864, _n_(447863, "model", lambda: model), "learn"), total_timesteps=1000)  # TypeError: tuple indices must be integers or slices, not str
_l_(447866)  # TypeError: tuple indices must be integers or slices, not str