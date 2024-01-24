# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71062211/filenotfounderror-despite-file-existing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def generate_dataset(agent_name: _n_(630527, "str", lambda: str), env_name: _n_(630528, "str", lambda: str), dataset_size: _n_(630529, "int", lambda: int), num_envs: _n_(630530, "int", lambda: int) = 20, epsilon: _n_(630531, "float", lambda: float) = 0.1,
                     network_root_folder: _n_(630532, "str", lambda: str) = 'jax-models') -> _n_(630533, "Tuple", lambda: Tuple)[_a_(630535, _n_(630534, "onp", lambda: onp), "ndarray"), _a_(630537, _n_(630536, "onp", lambda: onp), "ndarray"), _a_(630539, _n_(630538, "onp", lambda: onp), "ndarray"),
                                                                       _a_(630541, _n_(630540, "onp", lambda: onp), "ndarray"), _n_(630542, "int", lambda: int)]:
    _l_(630588)


    num_actions = _a_(630548, _a_(630547, _c_(630546, _a_(630544, _n_(630543, "gym", lambda: gym), "make"), f'{_n_(630545, "env_name", lambda: env_name)}NoFrameskip-v0'), 'action_space'), 'n')
    _l_(630549)

    images_obs_dataset = _c_(630553, _a_(630551, _n_(630550, 'onp', lambda: onp), 'zeros'), (_n_(630552, 'dataset_size', lambda: dataset_size), 84, 84, 4))
    _l_(630554)
    ram_obs_dataset = _c_(630558, _a_(630556, _n_(630555, 'onp', lambda: onp), 'zeros'), (_n_(630557, 'dataset_size', lambda: dataset_size), 128))
    _l_(630559)
    q_values_dataset = _c_(630564, _a_(630561, _n_(630560, 'onp', lambda: onp), 'zeros'), (_n_(630562, 'dataset_size', lambda: dataset_size), _n_(630563, 'num_actions', lambda: num_actions)))
    _l_(630565)
    action_dataset = _c_(630569, _a_(630567, _n_(630566, 'onp', lambda: onp), 'zeros'), _n_(630568, 'dataset_size', lambda: dataset_size))
    _l_(630570)

    network_def, network_args = _c_(630574, _n_(630571, 'get_network_def', lambda: get_network_def), _n_(630572, 'agent_name', lambda: agent_name), _n_(630573, 'num_actions', lambda: num_actions))
    _l_(630575)
    network_params = _c_(630580, _n_(630576, 'load_network_params', lambda: load_network_params), _n_(630577, 'agent_name', lambda: agent_name), _n_(630578, 'env_name', lambda: env_name), network_root_folder=_n_(630579, 'network_root_folder', lambda: network_root_folder))
    _l_(630581)
    aux = _n_(630582, 'images_obs_dataset', lambda: images_obs_dataset), _n_(630583, 'ram_obs_dataset', lambda: ram_obs_dataset), _n_(630584, 'q_values_dataset', lambda: q_values_dataset), _n_(630585, 'action_dataset', lambda: action_dataset), _n_(630586, 'episodes_run', lambda: episodes_run)
    _l_(630587)

    return aux