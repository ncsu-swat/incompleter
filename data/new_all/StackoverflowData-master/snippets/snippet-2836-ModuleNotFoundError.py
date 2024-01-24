#Source: https://stackoverflow.com/questions/61565222/generating-video-using-moviepy-using-image-and-text-but-getting-error-like-size
import glob
import os
from natsort import natsorted
from moviepy.editor import *

base_dir = os.path.realpath("./images/")
print(base_dir)

gif_name = 'pic'
fps = 24

file_list = glob.glob('./images/*.jpg')  # Get all the pngs in the current directory
file_list_sorted = natsorted(file_list,reverse=False)  # Sort the images

clips = [ImageClip(m).set_duration(5)
         for m in file_list_sorted]
print (clips)



text_list = ["Piggy", "Kermit", "Gonzo", "Fozzie"]
clip_list = []

for text in text_list:
    try:
        txt_clip = ( TextClip(text, fontsize = 70, color = 'white').set_duration(2))
        clip_list.append(txt_clip)
    except UnicodeEncodeError:
        txt_clip = TextClip("Issue with text", fontsize = 70, color = 'white').set_duration(2)
        clip_list.append(txt_clip)
print(clip_list)


final_clip = CompositeVideoClip([clips, clip_list])
final_clip.write_videofile("./video/export.mp4", fps = 24, codec = 'mpeg4')