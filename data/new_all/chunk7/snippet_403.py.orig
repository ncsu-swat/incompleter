#Source: https://stackoverflow.com/questions/30099542/mmap-typeerror-str-does-not-support-the-buffer-interface-python
f = open('C:\Python33\File.doc')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if (s.find("blabla")) != -1:
    print("True")