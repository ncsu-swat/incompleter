import os, signal

def process():
    try:
        for line in os.popen('ps ax | grep ' + name + ' | grep -v grep'):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)
        print('Process Successfully terminated')
    except:
        print('Error Encountered while running script')
process()