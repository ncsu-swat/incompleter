#Source: https://stackoverflow.com/questions/69710537/why-does-this-happen-attributeerror-shape
video = VideoFileClip(r'C:\Users\TheD4\OneDrive\Desktop\bac.mp4')
frames = []
video_duration = 3
for line in lines:
    if y_text < 560:
        draw.text(((40), 10 + y_text), line, font=font_type1, fill=color)
        y_text += height
        cropped = image.crop((0,0,image.width,y_text-4+(int(height/2))))
        frames.append(cropped)
    elif y_text2 < 560:
        draw2.text(((40), y_text2), line, font=font_type1, fill=color)
        y_text2 += height
        cropped2 = image2.crop((0,0,image.width,y_text2+4))
        frames.append(cropped2)


clips = []
for frame in frames:
    logo = (ImageClip(frame)
          .set_duration(video_duration)
          .set_position((0,0.10), relative=True))
    video = video.subclip(video_duration, video_duration*2)  
    final = CompositeVideoClip([video, logo])
    clips.append(final)


video_clip = concatenate_videoclips(clips, method='chain')
video_clip.write_videofile(r'C:\Users\TheD4\OneDrive\Desktop\VideoFolder\video-output.mp4', fps=24, remove_temp=True, codec="libx264", audio_codec="aac")  