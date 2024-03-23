#Source: https://stackoverflow.com/questions/51720014/attributeerror-module-multiprocessing-has-no-attribute-event
import multiprocessing
import tkinter as tk
import cv2

e = multiprocessing.Event()
p = None

# -------begin capturing and saving video
def startrecording(e,width,height,fourcc,out):

    #width = 1920#window.winfo_screenwidth()
    #height = 500#window.winfo_screenheight()

    #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    #out = cv2.VideoWriter("output.avi", fourcc, 5.0, (width,height))


    while True:
        img = ImageGrab.grab(bbox=(0,0,width,height))
        img_np = np.array(img)

        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        #cv2.imshow('Screen', frame)

        out.write(frame)

        if cv2.waitKey(1) == 27:
            break

def start_recording_proc(width,height,fourcc,out):
    global p
    p = multiprocessing.Process(target=startrecording, args=(e,width,height,fourcc,out))
    p.start()

# -------end video capture and stop tk
def stoprecording(out):
    e.set()
    p.join()
    out.release()
    cv2.destroyAllWindows()


    root.quit()
    root.destroy()

if __name__ == "__main__":
    # -------configure window
    root = tk.Tk()
    root.geometry("%dx%d+0+0" % (100, 100))

    width = 1920#window.winfo_screenwidth()
    height = 500#window.winfo_screenheight()

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (width,height))


    startbutton=tk.Button(root,width=10,height=1,text='START',command= lambda: start_recording_proc(width,height,fourcc,out))
    stopbutton=tk.Button(root,width=10,height=1,text='STOP', command= lambda: stoprecording(out))
    startbutton.pack()
    stopbutton.pack()

    # -------begin
    root.mainloop()