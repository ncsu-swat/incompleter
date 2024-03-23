#Source: https://stackoverflow.com/questions/41939088/typeerror-when-using-moviepy
from moviepy.editor import *

x = int(input("When do you want the cut to start? "))
y = int(input("When do you want the cut to end? "))


video = VideoFileClip("D:\Videos\Gatlinburgh Drone River 2.MOV").subclip(x,y)

##video = VideoFileClip("D:\SF_ep\T_R_D.mov").subclip(x,y)  #Path is correct


txt_clip = ( TextClip("The Red Dot episode",fontsize=70,color='white')
             .set_position('center')
             .set_duration(10) )

result = CompositeVideoClip([video, txt_clip])

result.write_videofile("Text on Screen.webm",fps=25)