#Source: https://stackoverflow.com/questions/71832875/attributeerror-nonetype-object-has-no-attribute-read-python-tkinter
from cProfile import label
from doctest import master
from importlib.metadata import files
from pydoc import text
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from functools import partial

import numpy as np
from tkinter.filedialog import asksaveasfile
from tkinter import ttk
import wave
import math
import contextlib
import warnings
 
outname =  (r"filtered.wav")
 



def fileaudio():
    global fname1
    fname1 = filedialog.askopenfilename(filetypes=(("Audio files", "*.wav;*.mp3"),
                                               ("All files", "*.*") ))
    print(fname1)
    
    return fname1


    

      

    
        





    
  


warnings.simplefilter("ignore", DeprecationWarning)


      
    # Change label contents
    



root =Tk()
root.geometry("1280x800")
root.resizable(False,False)
root.title("Audio filter")
root.configure(background="white")


    

#icon
image_icon=PhotoImage(file="filter.png")
root.iconphoto(False,image_icon)

#logo
photo=PhotoImage(file="filter.png")
myimage=Label(image=photo,background="white")
myimage.pack(padx=5,pady=5)

#name
Label(text="Audio filter",font="ariel 30 bold",background="black",fg="white").pack()

#entry box
def runlow():
    cutOffFrequency = 400.0
    



# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean

    def running_mean(x, windowSize):

        cumsum = np.cumsum(np.insert(x, 0, 0)) 

        return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize



# from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174

    def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):



        if sample_width == 1:

            dtype = np.uint8 # unsigned char

        elif sample_width == 2:

            dtype = np.int16 # signed 2-byte short

        else:

            raise ValueError("Only supports 8 and 16 bit audio formats.")



        channels = np.fromstring(raw_bytes, dtype=dtype)



        if interleaved:

        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data

            channels.shape = (n_frames, n_channels)

            channels = channels.T

        else:

        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1

            channels.shape = (n_channels, n_frames)
            return channels



    



    with contextlib.closing(wave.open(fname1,'rb')) as spf:

        sampleRate = spf.getframerate()

        ampWidth = spf.getsampwidth()

        nChannels = spf.getnchannels()

        nFrames = spf.getnframes()



    # Extract Raw Audio from multi-channel Wav File

        signal = spf.readframes(nFrames*nChannels)

        spf.close()

        channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)



    # get window size

    # from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter

        freqRatio = (cutOffFrequency/sampleRate)

        N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)



    # Use moviung average (only on first channel)

        filtered = running_mean(channels[0], N).astype(channels.dtype)



        wav_file = wave.open(outname, "w")

        wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))

        wav_file.writeframes(filtered.tobytes('C'))

        wav_file.close()

#button
record=Button(root,font="ariel 20",text="Input",bg="black",fg="white",border=0,command=fileaudio).pack(pady=30)
record2=Button(root,font="ariel 20",text="Filter",bg="black",fg="white",border=0,command=runlow).pack(pady=30)

#functions to integrate





# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean









root.mainloop()