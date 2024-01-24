# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44150310/openai-gym-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gym
    _l_(414192)

except ImportError:
    pass
env = _c_(414195, _a_(414194, _n_(414193, "gym", lambda: gym), "make"), 'CartPole-v0')
_l_(414196)
for i_episode in _c_(414198, _n_(414197, "range", lambda: range), 20):
    _l_(414233)

    observation = _c_(414201, _a_(414200, _n_(414199, "env", lambda: env), "reset"))
    _l_(414202)
    for t in _c_(414204, _n_(414203, "range", lambda: range), 100):
        _l_(414232)

        _c_(414207, _a_(414206, _n_(414205, "env", lambda: env), "render"))
        _l_(414208)
        _c_(414211, _n_(414209, "print", lambda: print), _n_(414210, "observation", lambda: observation))
        _l_(414212)
        action = _c_(414216, _a_(414215, _a_(414214, _n_(414213, "env", lambda: env), "action_space"), "sample"))
        _l_(414217)
        observation, reward, done, info = _c_(414221, _a_(414219, _n_(414218, "env", lambda: env), "step"), _n_(414220, "action", lambda: action))
        _l_(414222)
        if _n_(414223, "done", lambda: done):
            _l_(414231)

            _c_(414228, _n_(414224, "print", lambda: print), _c_(414227, _a_(414225, "Episode finished after {} timesteps", "format"), _n_(414226, "t", lambda: t)+1))
            _l_(414229)
            break
            _l_(414230)