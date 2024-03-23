#Source: https://stackoverflow.com/questions/61714227/type-error-unsupported-operand-types-for-nonetype-and-int
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
from tkinter import*
import threading
import re

class Application:
    def __init__(self,root):
        self.root=root
        self.root.grid_rowconfigure(0,weight=2)
        self.root.grid_columnconfigure(0,weight=1)
        self.root.config(bg="#ffdddd")

        top_label=Label(self.root,text="YouTube download manager",fg="blue",font=("ALGERIAN",70))
        top_label.grid(pady=(0,10))

        link_label=Label(self.root,text="Please paste your YouTube video link",bg="black",fg="red",font=("Agency FB",30))
        link_label.grid(pady=(0,20))

        self.YoutubeEntryVar=StringVar()

        self.YoutubeEntry=Entry(self.root,width=70,textvariable=self.YoutubeEntryVar,font=("Lucida Console",25),fg="blue")
        self.YoutubeEntry.grid(pady=(0,20),ipady=5)

        self.YoutubeEntryError=Label(self.root,text="",font=("Colonna MT",20),fg="green")
        self.YoutubeEntryError.grid(pady=(0,8))

        self.YoutubeFileSave=Label(self.root,text="Choose Directory",font=("Agency FB",20),fg="black")
        self.YoutubeFileSave.grid(pady=(0,8))

        self.YoutubeButton=Button(self.root,text="Directory",font=("Colonna MT",20),command=self.FileDirectory)
        self.YoutubeButton.grid(pady=(10,3),ipady=5)

        self.FileLocation=Label(self.root,text="",font=("Harlow Solid Italic",20))
        self.FileLocation.grid()

        self.DownloadSelect=Label(self.root,text="Choose the format to download",font=("Century Gothic",20))
        self.DownloadSelect.grid()

        self.DownloadChoice=[("Audio MP3",1),("Video MP4",2)]

        self.Choice=StringVar()
        self.Choice.set(1)

        for text,mode in self.DownloadChoice:
            self.YoutubeChoice=Radiobutton(self.root,text=text,font=("Candara",10),variable=self.Choice,value=mode)
            self.YoutubeChoice.grid()

        self.DownloadButton=Button(self.root,text="Download",font=("Lucida Console",10),command=self.checkLink)
        self.DownloadButton.grid(pady=(5,5))

    def checkLink(self):
        self.youtubeMatch=re.match("https://www.youtube.com/",self.YoutubeEntryVar.get())
        if(not self.youtubeMatch):
            self.YoutubeEntryError.config(text="Please choose a valid YouTube link !!")

        elif(not self.FolderName):
            self.FileLocation.config(text="Please choose a directory !!",fg="red")

        elif(self.youtubeMatch and self.FolderName):
            self.downloadFile()

    def downloadFile(self):
        self.newWindow=Toplevel(self.root)
        self.root.withdraw()
        self.newWindow.state("zoomed")
        self.newWindow.grid_rowconfigure(0,weight=2)
        self.newWindow.grid_columnconfigure(0,weight=1)



        self.app=Second(self.newWindow,self.YoutubeEntryVar.get(),self.FolderName,self.Choice.get())


    def FileDirectory(self):
        self.FolderName=filedialog.askdirectory()

        if(len(self.FolderName)>0):
            self.FileLocation.config(text=self.FolderName,fg="green")
            return True
        else:
            self.FileLocation.config(text="Please choose a directory !!",fg="red")

class Second:
    def __init__(self,downloadWindow,youtubeLink,foldername,FileChoice):
        self.downloadWindow=downloadWindow
        self.youtubeLink=youtubeLink
        self.foldername=foldername
        self.FileChoice=FileChoice

        self.yt=YouTube(self.youtubeLink)
        if(FileChoice=='1'):
            self.videoType=self.yt.streams.filter(only_audio=True).first()
            self.MaxfileSize=self.videoType.filesize
        if(FileChoice=='2'):
            self.videoType=self.yt.streams.first()
            self.MaxfileSize=self.videoType.filesize

        self.Loading=Label(self.downloadWindow,text="Download in Progress.........",font=("Agency FB",40))
        self.Loading.grid()

        self.percent=Label(self.downloadWindow,text="0",font=("Agency FB",20))
        self.percent.grid()

        self.progressBar=ttk.Progressbar(self.downloadWindow,length=500,orient='horizontal',mode='indeterminate')
        self.progressBar.grid(pady=(50,0))
        self.progressBar.start()

        threading.Thread(target=self.yt.register_on_progress_callback(self.show_Pregress)).start()

        threading.Thread(target=self.downloadfile).start()

    def downloadfile(self):
        if(self.FileChoice=='1'):
            self.yt.streams.filter(only_audio=True).first().download(self.foldername)
        if(self.FileChoice=='2'):
            self.yt.streams.filter().first().download(self.foldername)

    def show_Pregress(self,streams=None,Chunks=None,filehandle=None,bytes_remaining=None):

        percentCount = float("%0.2f"% (100 - (100*(bytes_remaining/self.MaxfileSize))))

        if(percentCount<100):

                        self.percent.config(text=str(percentCount))

        else:
            self.progressBar.stop()
            self.Loading.forget()
            self.progressBar.forget()

        self.downloadfinished=Label(self.downloadWindow,text="Download Finished",font=("ALGERIAN",20))
        self.downloadfinished.grid(pady(150,0))

        self.downloadfile=Label(self.downloadWindow,text=self.yt.title,font=("ALGERIAN",20))
        self.downloadfile.grid(pady(50,0))









if __name__=="__main__":

    window=Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app=Application(window)

    mainloop()