#Source: https://stackoverflow.com/questions/43713966/python-3-x-checkbutton-get-value-not-working-getting-an-attributeerror-chec
from tkinter import *
import subprocess
#from tkinter.filedialog import asksaveasfilename

#save file
#saveFile = asksaveasfilename()
#print("You can write data to " + saveFile)

startup = Tk()

names = ["about","accounts","admin","administrador","administrator","ads","adserver","adsl","agent","blog","channel","client","dmz","dns","dns0","dns1","dns2","dns3","external","file","forum","forums","ftp","ftpserver","host","http",
"https","ids","intern","intranet","irc","linux","log","mail","map","member","members","name","nc","ns","ntp","ntserver","office","pop","pptp","print","printer","pub","public","root","route","router","server","smtp","sql","ssh","telnet",
"voip","webaccess","webadmin","webserver","website","win","windows","www","xml"]
nslookup= IntVar()

def cmdnslookup():
        domain='microsoft.com'
        process = "dig "+domain+" ns > NameServerLookup.txt"
        subprocess.Popen(process, shell=True)

def cmdmxlookup():
        domain='microsoft.com'
        process = "dig "+domain+" mx > MailServerLookup.txt"
        subprocess.Popen(process, shell=True)

def cmdipForward():
        for name in names:
                domain='www.stcloudstate.edu'
                process = "host "+name+"."+domain+" | grep 'has address' >> ForwardIPLookup.txt"
                subprocess.Popen(process, shell=True)


##def cmdipReverse():
##        
##def cmdipAdditional():
##        
##def cmdzoneTransfer():
##        
##def cmdoneSixtyOne():
##        
##def cmdsnmp():
##        
##def cmdrpc():
##        
##def cmdip():
##        


def close():
        startup.destroy()

def menu():
        startup.title("Wilson Recon Tool")

        menubar = Menu(startup)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Close", command=close)
        menubar.add_cascade(label="file", menu=filemenu)
        startup.config(menu=menubar)

        topFrame = Frame(startup)
        topFrame.pack()

        bottomFrame = Frame(startup)
        bottomFrame.pack(side=BOTTOM)

        about = Label(topFrame, text="Application Description", font="ariel 10 bold").grid(row=0, column=0, sticky=W)
        description = StringVar()
        description.set("This is a network recon tool. It's designed to help make reconassiance easier for those not familar with terminal based tools." )
        message = Message(topFrame, textvariable=description, width=250)
        message.grid(row=1,column=0)


        recon = Label(bottomFrame, text="Recon Information", font="ariel 10 bold")
        recon.grid(row=0,column=0,pady=5,sticky=W)
        global nslookup
        nslookup = Checkbutton(bottomFrame, text="Name Server Lookup",variable=nslookup)
        nslookup.grid(row=1,column=0,sticky=W)
        mxlookup= IntVar()
        mxlookup = Checkbutton(bottomFrame, text="Mail Server Lookup",variable=mxlookup)
        mxlookup.grid(row=2,column=0,sticky=W)
        ipForward= IntVar()
        ipForward = Checkbutton(bottomFrame, text="Forward Domain Lookup",variable=ipForward)
        ipForward.grid(row=3,column=0,sticky=W)
        ipReverse= IntVar()
        ipReverse = Checkbutton(bottomFrame, text="Reverse Domain Lookup",variable=ipReverse)
        ipReverse.grid(row=4,column=0,sticky=W)
        ipAdditional= IntVar()
        ipAdditional = Checkbutton(bottomFrame, text="Additional IPs Check",variable=ipAdditional, state=DISABLED)
        ipAdditional.grid(row=5,column=0,sticky=W)
        zoneTransfer= IntVar()
        zoneTransfer = Checkbutton(bottomFrame, text="Zone Transfer Check",variable=zoneTransfer, state=DISABLED)
        zoneTransfer.grid(row=6,column=0,sticky=W)
        oneSixtyOne= IntVar()
        oneSixtyOne = Checkbutton(bottomFrame, text="Onesixtyone",variable=oneSixtyOne)
        oneSixtyOne.grid(row=7,column=0,sticky=W)
        snmp= IntVar()
        snmp = Checkbutton(bottomFrame, text="SNMPWalk",variable=snmp)
        snmp.grid(row=8,column=0,sticky=W)
        rpc= IntVar()
        rpc = Checkbutton(bottomFrame, text="RPC Client using NETBIOS",variable=rpc, state=DISABLED)
        rpc.grid(row=9,column=0,sticky=W)
        otherNetwork = Label(bottomFrame, text="Other Network Information", font="ariel 10 bold")
        otherNetwork.grid(row=10,column=0,pady=5,sticky=W)
        ip= IntVar()
        ip = Checkbutton(bottomFrame, text="Local Machine",variable=ip)
        ip.grid(row=11,column=0,sticky=W)

##        nslookup.pack()
##        mxlookup.pack()
##        ipForward.pack()
##        ipReverse.pack()
##        ipAdditional.pack()
##        zoneTransfer.pack()
##        oneSixtyOne.pack()
##        snmp.pack()
##        rpc.pack()
##        ip.pack()



        def cmdrunButton():
                global nslookup
                nslookup.get()
                mxlookup.get()
                ipForward.get()
                ipReverse.get()
                ipAdditional.get()
                zoneTransfer.get()
                oneSixtyOne.get()
                snmp.get()
                rpc.get()
                ip.get()
                print(nslookup)

        runButton = Button(bottomFrame, text="Run", command=cmdrunButton)
        runButton.grid(row=12, padx=3,pady=3,column=0,sticky=W)
        quitButton = Button(bottomFrame, text="Quit",command=close)
        quitButton.grid(row=12, padx=3,pady=3,column=1,sticky=E)

##        runButton.pack()
##        quitButton.pack()



        startup.mainloop()
menu()