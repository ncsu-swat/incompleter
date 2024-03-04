#Source: https://stackoverflow.com/questions/71629374/typeerror-init-missing-1-required-positional-argument-server
from operator import truediv
import socket
import threading 
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

class Client:

    def __init__(self, server):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(('localhost', 1234))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=msg)

        self.gui_done = False 
        self.running = True

        gui_thread = threading.Thread(targer=self.gui_loop)
        receive_thread = threading.Thread(targer=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")
        
        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.tkinter.scrolledtext.ScrolledText
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.win, text="Message:", bg="Lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.end_button.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def write(self):
        message =f"{self.nickname}: {self.input_area.get('1.0', 'end')}"


    def stop(self):
        self.running = False
        self.win.destroy()
        self.server.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == 'NICKNAME':
                    self.server.send(self.nickname.encode('utd-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.server.close()
                break

    
client = Client()