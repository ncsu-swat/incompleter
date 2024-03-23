#Source: https://stackoverflow.com/questions/36809972/socket-attributeerror-str-object-has-no-attribute-send
#---Import statments---#
import socket, os, multiprocessing
import tkinter as tk

#---global variables---#
setup = ''
cleintsocket = ''

#---Defs---#
def setup():
    global host, port, user
    host = setup_host_box.get()
    port = setup_port_box.get()
    user = setup_user_box.get()

def connect(self, hostname, connectingport):
    self.connect((hostname, int(connectingport)))
    print('connected')
    multiprocessing.Process(target = resv()).start()

def create_sock(nhost, nport):
    global cleintsocket
    cleintsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect(cleintsocket, nhost, nport)

def send(username, cleintsock):
    '''to send a message'''
    usrmsg = (username + ' - ' + chat_msg_box.get()).encode()
    cleintsock.send(usrmsg)

def resv(sock):
    '''resive subscript, run through mutiprosses module'''
    while True:
        rmsg = sock.recv(1024).decode()
        chat_msg_display_text.insert('end.0.', rmsg)

def chat():
    '''loads chat page'''
    setup_host_text.pack_forget()
    setup_host_box.pack_forget()
    setup_port_text.pack_forget()
    setup_port_box.pack_forget()
    setup_user_text.pack_forget()
    setup_user_box.pack_forget()
    setup_confirm_button.pack_forget()
    chat_msg_desplay_text.pack()
    chat_msg_box.pack()
    chat_msg_send_button.pack()

def start():
    '''starts the setup page'''
    setup_host_text.pack()
    setup_host_box.pack()
    setup_port_text.pack()
    setup_port_box.pack()
    setup_user_text.pack()
    setup_user_box.pack()
    setup_confirm_button.pack()

#---TK Setup---#
#--window setup--#
window = tk.Tk()
window.title('Chat')
window.geometry('600x600')
window.configure(background='#ffffff')
#--connection setup page--#
setup_host_text = tk.Label(window, text = 'Host')
setup_host_box = tk.Entry(window, bg = '#ffffff')
setup_port_text = tk.Label(window, text = 'Port')
setup_port_box = tk.Entry(window, bg = '#ffffff')
setup_user_text = tk.Label(window, text = 'Username')
setup_user_box = tk.Entry(window, bg = '#ffffff')
setup_confirm_button = tk.Button(window,text = 'Connect', command = setup())
#--chat page--#
chat_msg_box = tk.Entry(window, bg='#ffffff')
chat_msg_send_button = tk.Button(window, text = 'send', command = send(user, cleintsocket))
chat_msg_display_text = tk.Text(window, width=600, height=500, wrap = 'word')
#--------------#

start()