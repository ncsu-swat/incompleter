# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49377109/typeerror-missing-1-required-positional-argument-value
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os,time,pexpect,re, subprocess, smtplib
    _l_(691033)

except ImportError:
    pass
try:
    from email import encoders
    _l_(691035)

except ImportError:
    pass
try:
    from email.header import Header
    _l_(691037)

except ImportError:
    pass
try:
    from email.mime.text import MIMEText
    _l_(691039)

except ImportError:
    pass

#-----------------------------------------

dir = _a_(691041, _n_(691040, "os", lambda: os), "environ")['HOME']
_l_(691042)
ouser = 'x02d726'
_l_(691043)
opasw = 'qwe12'
_l_(691044)
nLocalport = 7000
_l_(691045)
lookip = '127.0.0.1'
_l_(691046)
rsg_target = "rpahost0"
_l_(691047)
command = "ls -ltrh | grep tunnel | tail"
_l_(691048)
nstage = 0
_l_(691049)
mail_addr = 'cheng.huang@qq.com'
_l_(691050)
otp_file = _n_(691051, "dir", lambda: dir) + '/otplist/C591260'
_l_(691052)
otp_list = []
_l_(691053)
rsg_file = _n_(691054, "dir", lambda: dir) + '/.rsg_hosts'
_l_(691055)
known_hosts = _n_(691056, "dir", lambda: dir) + '/.ssh/known_hosts'
_l_(691057)
rsg_port = "auto"
_l_(691058)

#-----------------------------------------

def printlog(prompt):
    _l_(691073)

    year, mon, mday, hour, min, sec, wday, yday, isdst = _c_(691061, _a_(691060, _n_(691059, "time", lambda: time), "localtime"))
    _l_(691062)
    _c_(691071, _n_(691063, "print", lambda: print), "%04d-%02d-%02d %02d:%02d:%02d %s" % (_n_(691064, "year", lambda: year), _n_(691065, "mon", lambda: mon) , _n_(691066, "mday", lambda: mday), _n_(691067, "hour", lambda: hour), _n_(691068, "min", lambda: min), 
_n_(691069, "sec", lambda: sec), _n_(691070, "prompt", lambda: prompt)))
    _l_(691072)

def get_egw_name(ref_arr, key):
    _l_(691101)

    for oneline in _n_(691074, "ref_arr", lambda: ref_arr):
        _l_(691100)

        if _c_(691079, _a_(691076, _n_(691075, "re", lambda: re), "search"), _n_(691077, "key", lambda: key), _n_(691078, "oneline", lambda: oneline)):
            _l_(691099)

            templine = _n_(691080, "oneline", lambda: oneline)
            _l_(691081)
            oneline = _c_(691085, _a_(691083, _n_(691082, "re", lambda: re), "sub"), '^\s+|\s+$','',_n_(691084, "oneline", lambda: oneline))
            _l_(691086)
            egw_ssg = _c_(691090, _a_(691088, _n_(691087, "re", lambda: re), "split"), '\s+',_n_(691089, "oneline", lambda: oneline))[2]
            _l_(691091)
            result = _c_(691095, _a_(691093, _n_(691092, "re", lambda: re), "split"), ':',_n_(691094, "egw_ssg", lambda: egw_ssg))[0]
            _l_(691096)
            aux = _n_(691097, "result", lambda: result)
            _l_(691098)
            return aux

def sendworker(to_addr):
    _l_(691135)

    from_addr = 'itk-bj.ericsson.se'
    _l_(691102)
    smtp_server = 'smtp.eamcs.ericsson.se'
    _l_(691103)

    msg = _c_(691105, _n_(691104, "MIMEText", lambda: MIMEText), 'There is no otp left ,please input new OTP list', 
'plain', 'utf-8')
    _l_(691106)
    _n_(691107, "msg", lambda: msg)['From'] = _n_(691108, "from_addr", lambda: from_addr)
    _l_(691109)
    _n_(691110, "msg", lambda: msg)['To'] = _n_(691111, "to_addr", lambda: to_addr)
    _l_(691112)
    _n_(691113, "msg", lambda: msg)['Subject'] = _c_(691115, _n_(691114, "Header", lambda: Header), u'OTP List is Blank', 'utf-8')
    _l_(691116)

    server = _c_(691120, _a_(691118, _n_(691117, "smtplib", lambda: smtplib), "SMTP"), _n_(691119, "smtp_server", lambda: smtp_server), 25)
    _l_(691121)
    #server.set_debuglevel(1)
    _c_(691129, _a_(691123, _n_(691122, "server", lambda: server), "sendmail"), _n_(691124, "from_addr", lambda: from_addr), _n_(691125, "to_addr", lambda: to_addr), _c_(691128, _a_(691127, _n_(691126, "msg", lambda: msg), "as_string")))
    _l_(691130)
    _c_(691133, _a_(691132, _n_(691131, "server", lambda: server), "quit"))
    _l_(691134)

def ssh_cmd(port, target, user, ip, pasw, cmd ):
    _l_(691256)

    _c_(691137, _n_(691136, "printlog", lambda: printlog), "=== Script Start ===")
    _l_(691138)
    _c_(691140, _n_(691139, "printlog", lambda: printlog), "Monitoring via remote logon")
    _l_(691141)
    _c_(691144, _a_(691143, _n_(691142, "time", lambda: time), "sleep"), 1)
    _l_(691145)
    ssh = _c_(691153, _a_(691147, _n_(691146, "pexpect", lambda: pexpect), "spawn"), '/usr/bin/ssh -p %s -o HostKeyAlias=%s %s@%s %s' % 
(_n_(691148, "port", lambda: port), _n_(691149, "target", lambda: target), _n_(691150, "user", lambda: user), _n_(691151, "ip", lambda: ip), _n_(691152, "cmd", lambda: cmd) ),timeout=6000)
    _l_(691154)
    try:
        _l_(691251)

        i = _c_(691157, _a_(691156, _n_(691155, "ssh", lambda: ssh), "expect"), ['Password: ', 'continue connecting (yes/no)?'], 
timeout=15)
        _l_(691158)
        if _n_(691159, "i", lambda: i) == 0 :
            _l_(691213)

            _c_(691169, _n_(691160, "print", lambda: print), _c_(691164, _a_(691163, _a_(691162, _n_(691161, "ssh", lambda: ssh), "before"), "decode")),_c_(691168, _a_(691167, _a_(691166, _n_(691165, "ssh", lambda: ssh), "after"), "decode")))
            _l_(691170)
            _c_(691174, _a_(691172, _n_(691171, "ssh", lambda: ssh), "sendline"), _n_(691173, "pasw", lambda: pasw))
            _l_(691175)
        elif _n_(691176, "i", lambda: i) == 1:
            _l_(691212)

            _c_(691186, _n_(691177, "print", lambda: print), _c_(691181, _a_(691180, _a_(691179, _n_(691178, "ssh", lambda: ssh), "before"), "decode")),_c_(691185, _a_(691184, _a_(691183, _n_(691182, "ssh", lambda: ssh), "after"), "decode")))
            _l_(691187)
            _c_(691190, _a_(691189, _n_(691188, "ssh", lambda: ssh), "sendline"), 'yes')
            _l_(691191)
            _c_(691194, _a_(691193, _n_(691192, "ssh", lambda: ssh), "expect"), 'Password: ')
            _l_(691195)
            _c_(691205, _n_(691196, "print", lambda: print), _c_(691200, _a_(691199, _a_(691198, _n_(691197, "ssh", lambda: ssh), "before"), "decode")),_c_(691204, _a_(691203, _a_(691202, _n_(691201, "ssh", lambda: ssh), "after"), "decode")))
            _l_(691206)
            _c_(691210, _a_(691208, _n_(691207, "ssh", lambda: ssh), "sendline"), _n_(691209, "pasw", lambda: pasw))
            _l_(691211)
    except _a_(691215, _n_(691214, "pexpect", lambda: pexpect), "EOF"):
        _l_(691219)

        _c_(691217, _n_(691216, "print", lambda: print), "no connection EOF,please check RSG tunnel")
        _l_(691218)
    except _a_(691221, _n_(691220, "pexpect", lambda: pexpect), "TIMEOUT"):
        _l_(691225)

        _c_(691223, _n_(691222, "print", lambda: print), "your pexpect has TIMEOUT")
        _l_(691224)
    else:
        _c_(691230, _a_(691227, _n_(691226, "ssh", lambda: ssh), "expect"), _a_(691229, _n_(691228, "pexpect", lambda: pexpect), "EOF"))
        _l_(691231)
        _c_(691242, _n_(691232, "print", lambda: print), _c_(691236, _a_(691235, _a_(691234, _n_(691233, "ssh", lambda: ssh), "before"), "decode")),_c_(691241, _a_(691240, _c_(691239, _a_(691238, _n_(691237, "ssh", lambda: ssh), "after")), "decode"))) # if I disable this line, there will be no error.
        _l_(691243) # if I disable this line, there will be no error.
        flag = _c_(691247, _a_(691246, _a_(691245, _n_(691244, "ssh", lambda: ssh), "before"), "decode"))
        _l_(691248)
        aux = _n_(691249, "flag", lambda: flag)
        _l_(691250)
        return aux
    _c_(691254, _a_(691253, _n_(691252, "ssh", lambda: ssh), "close"))
    _l_(691255)

if _n_(691257, "__name__", lambda: __name__) == '__main__':
    _l_(691495)

    if _c_(691263, _a_(691260, _a_(691259, _n_(691258, "os", lambda: os), "path"), "exists"), _a_(691262, _n_(691261, "os", lambda: os), "environ")['HOME'] + "/.ssh/known_hosts"):
        _l_(691270)

        _c_(691267, _a_(691265, _n_(691264, "os", lambda: os), "remove"), _n_(691266, "known_hosts", lambda: known_hosts))
        _l_(691268)
    else:
        pass
        _l_(691269)
    label = _c_(691278, _n_(691271, "ssh_cmd", lambda: ssh_cmd), _n_(691272, "nLocalport", lambda: nLocalport), _n_(691273, "rsg_target", lambda: rsg_target), _n_(691274, "ouser", lambda: ouser), _n_(691275, "lookip", lambda: lookip), _n_(691276, "opasw", lambda: opasw), _n_(691277, "command", lambda: command))
    _l_(691279)
    if _c_(691285, _a_(691281, _n_(691280, "re", lambda: re), "search"), 'tunnel_check', _c_(691284, _n_(691282, "str", lambda: str), _n_(691283, "label", lambda: label))):
        _l_(691287)

        nstage = 1
        _l_(691286)
    if (_n_(691288, "nstage", lambda: nstage) == 0):
        _l_(691494)

        _c_(691290, _n_(691289, "printlog", lambda: printlog), "Tunnel was down and  will re-establish now\n")
        _l_(691291)
        rsg = _c_(691294, _n_(691292, "open", lambda: open), _n_(691293, "rsg_file", lambda: rsg_file),'r')
        _l_(691295)
        rsg_in = _c_(691298, _a_(691297, _n_(691296, "rsg", lambda: rsg), "readlines"))
        _l_(691299)
        _c_(691302, _a_(691301, _n_(691300, "rsg", lambda: rsg), "close"))
        _l_(691303)
        egwname = _c_(691307, _n_(691304, "get_egw_name", lambda: get_egw_name), _n_(691305, "rsg_in", lambda: rsg_in), _n_(691306, "rsg_target", lambda: rsg_target))
        _l_(691308)
        try :
            _l_(691490)

            otp = _c_(691311, _n_(691309, "open", lambda: open), _n_(691310, "otp_file", lambda: otp_file), 'r')
            _l_(691312)
            otp_arrary = _c_(691315, _a_(691314, _n_(691313, "otp", lambda: otp), "readlines"))
            _l_(691316)
            _c_(691319, _a_(691318, _n_(691317, "otp", lambda: otp), "close"))
            _l_(691320)
            for ot in _n_(691321, "otp_arrary", lambda: otp_arrary):
                _l_(691335)

                ot = _c_(691324, _a_(691323, _n_(691322, "ot", lambda: ot), "strip"))
                _l_(691325)
                ot = _c_(691328, _a_(691327, _n_(691326, "ot", lambda: ot), "replace"), '^\s*|\s*$', '')
                _l_(691329)
                _c_(691333, _a_(691331, _n_(691330, "otp_list", lambda: otp_list), "append"), _n_(691332, "ot", lambda: ot))
                _l_(691334)
            otp_num = _c_(691338, _n_(691336, "len", lambda: len), _n_(691337, "otp_list", lambda: otp_list)) + 1
            _l_(691339)
            if (_n_(691340, "otp_num", lambda: otp_num) > 0):
                _l_(691484)

                _c_(691344, _a_(691342, _n_(691341, "os", lambda: os), "remove"), _n_(691343, "rsg_file", lambda: rsg_file))
                _l_(691345)
                try :
                    _l_(691479)

                    new_otp = _n_(691346, "otp_list", lambda: otp_list)[0]
                    _l_(691347)
                except _n_(691348, "IndexError", lambda: IndexError):
                    _l_(691360)

                    _c_(691350, _n_(691349, "printlog", lambda: printlog), 'There is no otp left ,please input new OTP list')
                    _l_(691351)
                    _c_(691354, _n_(691352, "sendworker", lambda: sendworker), _n_(691353, "mail_addr", lambda: mail_addr))
                    _l_(691355)
                    _c_(691358, _a_(691357, _n_(691356, "sys", lambda: sys), "exit"))
                    _l_(691359)
                else:
                    out = _c_(691363, _n_(691361, "open", lambda: open), _n_(691362, "rsg_file", lambda: rsg_file), 'w')
                    _l_(691364)
                    for line in _n_(691365, "rsg_in", lambda: rsg_in) :
                        _l_(691408)

                        line = _c_(691368, _a_(691367, _n_(691366, "line", lambda: line), "strip"))
                        _l_(691369)
                        line = _c_(691372, _a_(691371, _n_(691370, "line", lambda: line), "replace"), '^\s+|\s+$','')
                        _l_(691373)
                        if _c_(691378, _a_(691375, _n_(691374, "re", lambda: re), "match"), _n_(691376, "egwname", lambda: egwname), _n_(691377, "line", lambda: line)):
                            _l_(691402)

                            temp_line = _n_(691379, "line", lambda: line)
                            _l_(691380)
                            old_otp = _c_(691384, _a_(691382, _n_(691381, "re", lambda: re), "split"), '\s+',_n_(691383, "temp_line", lambda: temp_line))[5]
                            _l_(691385)
                            old_otp = _c_(691388, _a_(691387, _n_(691386, "old_otp", lambda: old_otp), "replace"), '^\s+|\s+$', '')
                            _l_(691389)
                            line = _c_(691396, _a_(691395, _c_(691394, _a_(691391, _n_(691390, "line", lambda: line), "replace"), _n_(691392, "old_otp", lambda: old_otp), _n_(691393, "new_otp", lambda: new_otp)), "replace"), '\\','')
                            _l_(691397)
                            _c_(691400, _n_(691398, "printlog", lambda: printlog), _n_(691399, "line", lambda: line) + "\n")
                            _l_(691401)
                        _c_(691406, _a_(691404, _n_(691403, "out", lambda: out), "write"), _n_(691405, "line", lambda: line) + "\n")
                        _l_(691407)
                    _c_(691411, _a_(691410, _n_(691409, "out", lambda: out), "close"))
                    _l_(691412)
                    _c_(691416, _a_(691414, _n_(691413, "os", lambda: os), "remove"), _n_(691415, "otp_file", lambda: otp_file))
                    _l_(691417)
                    _c_(691420, _a_(691419, _n_(691418, "time", lambda: time), "sleep"), 1)
                    _l_(691421)
                    outotp = _c_(691424, _n_(691422, "open", lambda: open), _n_(691423, "otp_file", lambda: otp_file) , 'w+')
                    _l_(691425)
                    i = 0
                    _l_(691426)
                    while (_n_(691427, "i", lambda: i) < _c_(691430, _n_(691428, "len", lambda: len), _n_(691429, "otp_list", lambda: otp_list))):
                        _l_(691438)

                        _c_(691435, _a_(691432, _n_(691431, "outotp", lambda: outotp), "write"), _n_(691433, "otp_list", lambda: otp_list)[_n_(691434, "i", lambda: i)] + "\n")
                        _l_(691436)
                        i += 1
                        _l_(691437)
                    _c_(691441, _a_(691440, _n_(691439, "outotp", lambda: outotp), "close"))
                    _l_(691442)
                    _c_(691448, _a_(691444, _n_(691443, "os", lambda: os), "system"), "pkill -9 -f \"ssh\.\*-L " + _c_(691447, _n_(691445, "str", lambda: str), _n_(691446, "nLocalport", lambda: nLocalport)) + "\"")
                    _l_(691449)
                    _c_(691452, _a_(691451, _n_(691450, "os", lambda: os), "system"), "sleep 10")
                    _l_(691453)
                    _c_(691459, _a_(691455, _n_(691454, "os", lambda: os), "system"), "pkill -9 -f \"rtunnel\.\*-p " + _c_(691458, _n_(691456, "str", lambda: str), _n_(691457, "nLocalport", lambda: nLocalport)) + "\"")
                    _l_(691460)
                    _c_(691467, _a_(691462, _n_(691461, "os", lambda: os), "system"), "nohup /opt/ericsson/itk/bin/rtunnel -d -q -g -p " + _c_(691465, _n_(691463, "str", lambda: str), _n_(691464, "nLocalport", lambda: nLocalport)) + "-rp auto " + _n_(691466, "rsg_target", lambda: rsg_target) + " &")
                    _l_(691468)
                    _c_(691471, _a_(691470, _n_(691469, "os", lambda: os), "system"), "sleep 10")
                    _l_(691472)
                    _c_(691474, _n_(691473, "printlog", lambda: printlog), "Kill the rtunnel process\n");
                    _l_(691475)
                    _c_(691477, _n_(691476, "printlog", lambda: printlog), "Tunnel is re-established again\n");
                    _l_(691478)
            else:
                _c_(691482, _n_(691480, "sendworker", lambda: sendworker), _n_(691481, "mail_addr", lambda: mail_addr))
                _l_(691483)
        except _n_(691485, "IOError", lambda: IOError):
            _l_(691489)

            _c_(691487, _n_(691486, "print", lambda: print), "File is not accessible.")
            _l_(691488)
    else:
        _c_(691492, _n_(691491, "printlog", lambda: printlog), "Tunnel OK")
        _l_(691493)