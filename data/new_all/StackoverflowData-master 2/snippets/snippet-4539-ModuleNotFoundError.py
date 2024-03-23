#Source: https://stackoverflow.com/questions/55910379/typeerror-not-supported-between-instances-of-int-and-label
import tkinter as tk
def animate(frame_number,last_frame,label,framelist):
    #if the frame number is bigger than the last frame
    if frame_number > last_frame:
        frame_number = 0
        #how long each frame should last
    label.config(image=framelist[frame_number]) 
    window.after(1500, animate, frame_number+1)
#make mainwindow
window = tk.Tk()
# List to hold all the frames
framelist = [] 
# Frame index
frame_index = 0    

while True:
    try:
        # Read a frame from GIF file
        part = 'gif -index {}'.format(frame_index,fr)
        frame = tk.PhotoImage(file='giphy.gif', format=part)
    except:
        # Save index for last frame
        last_frame = frame_index - 1 
         # Will break when GIF index is reached
        break              
    framelist.append(frame)
     # Next frame index
    frame_index += 1       


#put the gif into a label
label = tk.Label(window, bg='black')
label.grid(column = 1, row = 7)

animate(last_frame,label,framelist,0)  # Start animation
#window size
window.geometry("600x600")

#end of page
window.mainloop()