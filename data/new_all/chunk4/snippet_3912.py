# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65431109/matplotlib-xlim-typeerror-not-supported-between-instances-of-int-and-lis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(587636)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(587638)

except ImportError:
    pass
try:
    import argparse
    _l_(587640)

except ImportError:
    pass
try:
    from attacker import check_attack_type
    _l_(587642)

except ImportError:
    pass

IMG_DIR = "./plots"
_l_(587643)

def read_lines(f, d):
    _l_(587688)

    lines = _c_(587646, _a_(587645, _n_(587644, "f", lambda: f), "readlines"))[:-1]
    _l_(587647)
    for line in _n_(587648, "lines", lambda: lines):
        _l_(587687)

        typ, time, num = _c_(587651, _a_(587650, _n_(587649, "line", lambda: line), "split"), ',')
        _l_(587652)
        if _n_(587653, "typ", lambda: typ) == 'seq':
            _l_(587686)

            _c_(587659, _a_(587655, _n_(587654, "d", lambda: d)['seq']['time'], "append"), _c_(587658, _n_(587656, "float", lambda: float), _n_(587657, "time", lambda: time)))
            _l_(587660)
            _c_(587666, _a_(587662, _n_(587661, "d", lambda: d)['seq']['num'], "append"), _c_(587665, _n_(587663, "float", lambda: float), _n_(587664, "num", lambda: num)))
            _l_(587667)
        elif _n_(587668, "typ", lambda: typ) == 'ack':
            _l_(587685)

            _c_(587674, _a_(587670, _n_(587669, "d", lambda: d)['ack']['time'], "append"), _c_(587673, _n_(587671, "float", lambda: float), _n_(587672, "time", lambda: time)))
            _l_(587675)
            _c_(587681, _a_(587677, _n_(587676, "d", lambda: d)['ack']['num'], "append"), _c_(587680, _n_(587678, "float", lambda: float), _n_(587679, "num", lambda: num)))
            _l_(587682)
        else:
            raise "Unknown type read while parsing log file: %s" % _n_(587683, "typ", lambda: typ)
            _l_(587684)

def main():
    _l_(587870)

    parser = _c_(587691, _a_(587690, _n_(587689, "argparse", lambda: argparse), "ArgumentParser"), description="Plot script for plotting sequence numbers.")
    _l_(587692)
    _c_(587695, _a_(587694, _n_(587693, "parser", lambda: parser), "add_argument"), '--save', dest='save_imgs', action='store_true',
                        help="Set this to true to save images under specified output directory.")
    _l_(587696)
    _c_(587700, _a_(587698, _n_(587697, "parser", lambda: parser), "add_argument"), '--attack', dest='attack',
                        nargs='?', const="", type=_n_(587699, "check_attack_type", lambda: check_attack_type),
                        help="Attack name (used in plot names).")
    _l_(587701)
    _c_(587705, _a_(587703, _n_(587702, "parser", lambda: parser), "add_argument"), '--output', dest='output_dir', default=_n_(587704, "IMG_DIR", lambda: IMG_DIR),
                        help="Directory to store plots.")
    _l_(587706)
    args = _c_(587709, _a_(587708, _n_(587707, "parser", lambda: parser), "parse_args"))
    _l_(587710)
    save_imgs = _a_(587712, _n_(587711, "args", lambda: args), "save_imgs")
    _l_(587713)
    output_dir = _a_(587715, _n_(587714, "args", lambda: args), "output_dir")
    _l_(587716)
    attack_name = _a_(587718, _n_(587717, "args", lambda: args), "attack")
    _l_(587719)

    if _n_(587720, "save_imgs", lambda: save_imgs) and _n_(587721, "attack_name", lambda: attack_name) not in ['div', 'dup', 'opt'] :
        _l_(587726)

        _c_(587723, _n_(587722, "print", lambda: print), "Attack name needed for saving plot figures.")
        _l_(587724)
        aux = ""
        _l_(587725)
        return aux

    normal_log = {'seq':{'time':[], 'num':[]}, 'ack':{'time':[], 'num':[]}}
    _l_(587727)
    attack_log = {'seq':{'time':[], 'num':[]}, 'ack':{'time':[], 'num':[]}}
    _l_(587728)
    normal_f = _c_(587730, _n_(587729, "open", lambda: open), 'log.txt', 'r')
    _l_(587731)
    attack_f = _c_(587734, _n_(587732, "open", lambda: open), '%s_attack_log.txt' % _n_(587733, "attack_name", lambda: attack_name), 'r')
    _l_(587735)
    
    _c_(587739, _n_(587736, "read_lines", lambda: read_lines), _n_(587737, "normal_f", lambda: normal_f), _n_(587738, "normal_log", lambda: normal_log))
    _l_(587740)
    _c_(587744, _n_(587741, "read_lines", lambda: read_lines), _n_(587742, "attack_f", lambda: attack_f), _n_(587743, "attack_log", lambda: attack_log))
    _l_(587745)
   
    if _n_(587746, "attack_name", lambda: attack_name) == 'div':
        _l_(587756)

        attack_desc = 'ACK Division'
        _l_(587747)
    elif _n_(587748, "attack_name", lambda: attack_name) == 'dup':
        _l_(587755)

        attack_desc = 'DupACK Spoofing'
        _l_(587749)
    elif _n_(587750, "attack_name", lambda: attack_name) == 'opt':
        _l_(587754)

        attack_desc = 'Optimistic ACKing'
        _l_(587751)
    else:
        raise 'Unknown attack type: %s' % _n_(587752, "attack_name", lambda: attack_name)
        _l_(587753)
    norm_seq_time, norm_seq_num = _n_(587757, "normal_log", lambda: normal_log)['seq']['time'], _n_(587758, "normal_log", lambda: normal_log)['seq']['num']
    _l_(587759)
    norm_ack_time, norm_ack_num = _n_(587760, "normal_log", lambda: normal_log)['ack']['time'], _n_(587761, "normal_log", lambda: normal_log)['ack']['num']
    _l_(587762)
    atck_seq_time, atck_seq_num = _n_(587763, "attack_log", lambda: attack_log)['seq']['time'], _n_(587764, "attack_log", lambda: attack_log)['seq']['num']
    _l_(587765)
    atck_ack_time, atck_ack_num = _n_(587766, "attack_log", lambda: attack_log)['ack']['time'], _n_(587767, "attack_log", lambda: attack_log)['ack']['num']
    _l_(587768)
    _c_(587773, _a_(587770, _n_(587769, "plt", lambda: plt), "plot"), _n_(587771, "norm_seq_time", lambda: norm_seq_time), _n_(587772, "norm_seq_num", lambda: norm_seq_num), 'b^', label='Regular TCP Data Segments')
    _l_(587774)
    _c_(587779, _a_(587776, _n_(587775, "plt", lambda: plt), "plot"), _n_(587777, "norm_ack_time", lambda: norm_ack_time), _n_(587778, "norm_ack_num", lambda: norm_ack_num), 'bx', label='Regular TCP ACKs')
    _l_(587780)
    _c_(587786, _a_(587782, _n_(587781, "plt", lambda: plt), "plot"), _n_(587783, "atck_seq_time", lambda: atck_seq_time), _n_(587784, "atck_seq_num", lambda: atck_seq_num), 'rs', label='%s Attack Data Segments' % _n_(587785, "attack_desc", lambda: attack_desc))
    _l_(587787)
    _c_(587793, _a_(587789, _n_(587788, "plt", lambda: plt), "plot"), _n_(587790, "atck_ack_time", lambda: atck_ack_time), _n_(587791, "atck_ack_num", lambda: atck_ack_num), 'r+', label='%s Attack ACKs' % _n_(587792, "attack_desc", lambda: attack_desc))
    _l_(587794)
    _c_(587797, _a_(587796, _n_(587795, "plt", lambda: plt), "legend"), loc='upper left')
    _l_(587798)

    x = _c_(587808, _n_(587799, "max", lambda: max), _c_(587803, _n_(587800, "max", lambda: max), _n_(587801, "norm_seq_time", lambda: norm_seq_time), _n_(587802, "norm_ack_time", lambda: norm_ack_time)),_c_(587807, _n_(587804, "max", lambda: max), _n_(587805, "atck_seq_time", lambda: atck_seq_time), _n_(587806, "atck_ack_time", lambda: atck_ack_time)))
    _l_(587809)
    y = _c_(587819, _n_(587810, "max", lambda: max), _c_(587814, _n_(587811, "max", lambda: max), _n_(587812, "norm_seq_num", lambda: norm_seq_num), _n_(587813, "norm_ack_num", lambda: norm_ack_num)),_c_(587818, _n_(587815, "max", lambda: max), _n_(587816, "atck_seq_num", lambda: atck_seq_num), _n_(587817, "atck_ack_num", lambda: atck_ack_num)))
    _l_(587820)
    _c_(587824, _a_(587822, _n_(587821, "plt", lambda: plt), "xlim"), 0, _n_(587823, "x", lambda: x))
    _l_(587825)
    _c_(587829, _a_(587827, _n_(587826, "plt", lambda: plt), "ylim"), 0,_n_(587828, "y", lambda: y))
    _l_(587830)

    _c_(587833, _a_(587832, _n_(587831, "plt", lambda: plt), "xlabel"), 'Time (s)')
    _l_(587834)
    _c_(587837, _a_(587836, _n_(587835, "plt", lambda: plt), "ylabel"), 'Sequence Number (Bytes)')
    _l_(587838)

    if _n_(587839, "save_imgs", lambda: save_imgs):
        _l_(587861)

        # Save images to figure/
        if not _c_(587844, _a_(587842, _a_(587841, _n_(587840, "os", lambda: os), "path"), "exists"), _n_(587843, "output_dir", lambda: output_dir)):
            _l_(587850)

            _c_(587848, _a_(587846, _n_(587845, "os", lambda: os), "makedirs"), _n_(587847, "output_dir", lambda: output_dir))
            _l_(587849)
        _c_(587855, _a_(587852, _n_(587851, "plt", lambda: plt), "savefig"), _n_(587853, "output_dir", lambda: output_dir) + "/" + _n_(587854, "attack_name", lambda: attack_name))
        _l_(587856)
    else:
        _c_(587859, _a_(587858, _n_(587857, "plt", lambda: plt), "show"))
        _l_(587860)
    
    _c_(587864, _a_(587863, _n_(587862, "normal_f", lambda: normal_f), "close"))
    _l_(587865)
    _c_(587868, _a_(587867, _n_(587866, "attack_f", lambda: attack_f), "close"))
    _l_(587869)


if _n_(587871, "__name__", lambda: __name__) == "__main__":
    _l_(587875)

    _c_(587873, _n_(587872, "main", lambda: main))
    _l_(587874)