#Source: https://stackoverflow.com/questions/42090620/typeerror-int-object-is-not-iterable-on-gresycale-image
from tkinter import*
import tkinter as Tkinter
from tkinter import filedialog, DISABLED, messagebox as tkMessageBox
import os
import ntpath
from PIL import Image, ImageTk, ImageFilter
import PIL
from collections import Counter
from random import randint
import random
import PIL.ImageOps


def EchelleDeGris():
    Ima2=Image.new("RGB",(z[0],z[1]))
    px=Ima1.load()
    px1=Ima2.load()
    for x in range(z[0]):
        for y in range(z[1]):
            p=px[x,y]
            if type(p)==int:
                p=(p,p,p)
            o=int((p[0]+p[1]+p[2])/3)
            px1[x,y]=(o,o,o)
    Ima2.save(""+dir_path+"\\Requirements\\ImageMod.png")
    im2 = ImageTk.PhotoImage(file=""+dir_path+"\\Requirements\\ImageMod.png")
    main.image = im2
    I2 = Tkinter.Label(main, image=im2)
    I2.grid(row=0, column=4, columnspan =4)

def SupprimerImage():
    I2 = Tkinter.Label(main, image=imt)
    I2.grid(row=0, column=4, columnspan =4)

def Luminosite():
    Ima2=Image.new("RGB",(z[0],z[1]))
    px=Ima1.load()
    px1=Ima2.load()
    for x in range(z[0]):
        for y in range(z[1]):
            p=px[x,y]
            if type(p)==int:
                p=(p,p,p)
            px1[x,y]=(p[0]+S1.get(),p[1]+S1.get(),p[2]+S1.get())
    Ima2.save(""+dir_path+"\\Requirements\\ImageMod.png")
    im2 = ImageTk.PhotoImage(file=""+dir_path+"\\Requirements\\ImageMod.png")
    main.image = im2
    I2 = Tkinter.Label(main, image=im2)
    I2.grid(row=0, column=4, columnspan =4)

def AnnulerModifications():
    I2 = Tkinter.Label(main, image=im1)
    I2.grid(row=0, column=4, columnspan =4)

def get_pixel(pixels, x, y):
    try:
        return pixels[x, y]
    except IndexError:
        return None


def get_neighbors(pixels, x, y):
    neighbors = list()
    neighbors.append(get_pixel(pixels, x, y - 1))
    neighbors.append(get_pixel(pixels, x, y + 1))
    neighbors.append(get_pixel(pixels, x - 1, y))
    neighbors.append(get_pixel(pixels, x + 1, y))
    neighbors.append(get_pixel(pixels, x - 1, y - 1))
    neighbors.append(get_pixel(pixels, x - 1, y + 1))
    neighbors.append(get_pixel(pixels, x + 1, y - 1))
    neighbors.append(get_pixel(pixels, x + 1, y + 1))
    return neighbors


def filter_art(pixels, size):
    indexes = dict()
    for x in range(size[0]):
        for y in range(size[1]):
            color = get_pixel(pixels, x, y)
            neighbors = get_neighbors(pixels, x, y)
            new_color = Counter(neighbors).most_common()[0][0]
            if new_color is not None:
                indexes[x, y] = new_color
    for x, y in indexes:
        pixels[x, y] = indexes[x, y]


def pop_art(path_orig, path_mod, coef):

    s=[]
    for i in range(9):

        r=(randint(0,255), randint(0,255), randint(0,255))
        g=(randint(0,255), randint(0,255), randint(0,255))
        b=(randint(0,255), randint(0,255), randint(0,255))

        image_orig = Image.open(path_orig)
        size = image_orig.size
        image_mod = Image.new("RGB",(size[0],size[1]))
        pixels_orig = image_orig.load()
        pixels_mod = image_mod.load()
        for x in range(size[0]):
            for y in range(size[1]):
                p = pixels_orig[x, y]
                if isinstance(p, int):
                    rgb = (p,p,p)
                elif isinstance(p, tuple) and len(p) in (3, 4):
                    rgb = p[:3]
                else:
                    raise TypeError('Unknown pallete')
                average_color = sum(rgb) / 3
                if average_color <= 85:
                    pixels_mod[x, y] = r
                elif 85 < average_color <= 170:
                    pixels_mod[x, y] = g
                elif average_color > 170:
                    pixels_mod[x, y] = b
        for _ in range(coef):
            filter_art(pixels_mod, size)
        image_mod.save(''+dir_path+'\\PopArt\\Modified Images\\result'+str(i)+'.png')
        Img=[None]*9
    for i in range(9):
        Img[i]=Image.open(""+dir_path+"\\PopArt\\Modified Images\\result"+str(i)+".png")
        basewidth = int(Img[i].size[1]/3)
        wpercent = (basewidth / float(Img[i].size[0]))
        hsize = int((float(Img[i].size[1]) * float(wpercent )))
        Img[i] = Img[i].resize((basewidth , hsize ), PIL.Image.ANTIALIAS)
        Img[i].save(''+dir_path+'\\PopArt\\Resized Images\\resized_image'+str(i)+'.png')


    Img1=[None]*9
    pixels1=[None]*9
    Imaz=Image.new("RGB",(basewidth*3,hsize*3))
    pixels=Imaz.load()
    for i in range(9):
        Img1[i]=Image.open(''+dir_path+'\\PopArt\\Resized Images\\resized_image'+str(i)+'.png')
        pixels1[i]=Img1[i].load()


    for x in range(0,basewidth):
        for y in range(0,hsize):
            pixels[x,y]=pixels1[0][x,y]
        for y in range(hsize,hsize*2):
            pixels[x,y]=pixels1[1][x,y-hsize]
        for y in range(hsize*2,hsize*3):
            pixels[x,y]=pixels1[2][x,y-hsize*2]

    for x in range(basewidth,basewidth*2):
        for y in range(0,hsize):
            pixels[x,y]=pixels1[3][x-basewidth,y]
        for y in range(hsize,hsize*2):
            pixels[x,y]=pixels1[4][x-basewidth,y-hsize]
        for y in range(hsize*2,hsize*3):
            pixels[x,y]=pixels1[5][x-basewidth,y-hsize*2]

    for x in range(basewidth*2,basewidth*3):
        for y in range(0,hsize):
            pixels[x,y]=pixels1[6][x-basewidth*2,y]
        for y in range(hsize,hsize*2):
            pixels[x,y]=pixels1[7][x-basewidth*2,y-hsize]
        for y in range(hsize*2,hsize*3):
            pixels[x,y]=pixels1[8][x-basewidth*2,y-hsize*2]
    Imaz = Imaz.resize((size[0] , size[1] ), PIL.Image.ANTIALIAS)
    Imaz.save(""+dir_path+"\\PopArt\\Result Image\\result.png")


def usepop():
    im2 = ImageTk.PhotoImage(file=""+dir_path+"\\Requirements\\traitement.png")
    main.image = im2
    I2 = Tkinter.Label(main, image=im2)
    I2.grid(row=0, column=4, columnspan =4)
    I2.update_idletasks()
    pop_art(a, None, coef=4)
    im2 = ImageTk.PhotoImage(file=""+dir_path+"\\PopArt\\Result Image\\result.png")
    main.image = im2
    I2 = Tkinter.Label(main, image=im2)
    I2.grid(row=0, column=4, columnspan =4)

def change_contrast(level):

    img = Image.open(a)
    img.load()

    factor = (259 * (level+255)) / (255 * (259-level))
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            color = img.getpixel((x, y))
            new_color = tuple(int(factor * (c-128) + 128) for c in color)
            img.putpixel((x, y), new_color)

    return img

def use_contrast():
    result = change_contrast(S2.get())
    result.save(""+dir_path+"\\Requirements\\ImageMod.png")
    im2 = ImageTk.PhotoImage(file=""+dir_path+"\\Requirements\\ImageMod.png")
    main.image = im2
    I2 = Tkinter.Label(main, image=im2)
    I2.grid(row=0, column=4, columnspan =4)

def recherche_contours():
    Ima2=Image.new("RGB",(z[0],z[1]))
    px=Ima1.load()
    px1=Ima2.load()
    for x in range(z[0]):
        for y in range(z[1]):
            p=px[x,y]
            if type(p)==int:
                p=(p,p,p)
            o=int((p[0]+p[1]+p[2])/3)
            px1[x,y]=(o,o,o)
    Ima2 = Ima2.filter(ImageFilter.FIND_EDGES)
    image = Ima2
    if image.mode == 'RGBA':
        r,g,b,a = image.split()
        rgb_image = Image.merge('RGB', (r,g,b))

        inverted_image = PIL.ImageOps.invert(rgb_image)

        r2,g2,b2 = inverted_image.split()

        final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

        final_transparent_image.save(""+dir_path+"\\Requirements\\ImageMod.png")

    else:
        inverted_image = PIL.ImageOps.invert(image)
        inverted_image.save(""+dir_path+"\\Requirements\\ImageMod.png")
    im2 = ImageTk.PhotoImage(file=""+dir_path+"\\Requirements\\ImageMod.png")
    main.image = im2
    I2 = Tkinter.Label(main, image=im2)
    I2.grid(row=0, column=4, columnspan =4)

main=Tk()

main.withdraw()
a = filedialog.askopenfilename()
main.deiconify()

dir_path = os.path.dirname(os.path.realpath("Test2.py"))

main.configure(background="#a1dbcd")
main.title("Photoshop Version.Megzari")

Ima1=Image.open(a)
z=Ima1.size
nux=Image.new("RGB",(z[0],z[1]))
nuxy=nux.load()
for x in range(z[0]):
    for y in range(z[1]):
        nuxy[x,y]=(255,255,255)
nux.save(""+dir_path+"\\Requirements\\Blank.png")


if z>(400,400):
    main.withdraw()
    tkMessageBox.showinfo( "Resolution Error", "The image is too big, please select a smaller one.")
    sys.exit()


elif z<(400,400):
    im1 = ImageTk.PhotoImage(file=a)
    I1 = Tkinter.Label(main, image=im1)
    I1.grid(row=0, column=1, columnspan =3)
    imt = ImageTk.PhotoImage(file=""+dir_path+"\\Requirements\\Blank.png")
    T1 = Tkinter.Label(main, image=imt)
    T1.grid(row=0, column=4, columnspan =4)
    B1 = Tkinter.Button(main, text ="Echelle de gris", command = EchelleDeGris, fg="#a1dbcd", bg="#383a39", state=NORMAL)
    B1.grid(padx=20, pady=20, row=1, column=0)
    B3 = Tkinter.Button(main, text ="Appliquer Luminosité", command = Luminosite, fg="#a1dbcd", bg="#383a39")
    B3.grid(padx=20, pady=20, row=1, column=1)
    S1 = Scale(main, from_=0, to=254, orient=HORIZONTAL, fg="#a1dbcd", bg="#383a39", length = 200)
    S1.grid(row=2, column=1)
    B2 = Tkinter.Button(main, text ="Supprimer Image", command = SupprimerImage, fg="#a1dbcd", bg="#383a39")
    B2.grid(padx=20, pady=20, row=1, column=7)
    B3 = Tkinter.Button(main, text ="Annuler Modifications", command = AnnulerModifications, fg="#a1dbcd", bg="#383a39")
    B3.grid(padx=20, pady=20, row=1, column=6)
    B4 = Tkinter.Button(main, text ="Pop Art", command = usepop, fg="#a1dbcd", bg="#383a39")
    B4.grid(padx=20, pady=20, row=1, column=3)
    S2 = Scale(main, from_=-258, to=258, orient=HORIZONTAL, fg="#a1dbcd", bg="#383a39", length = 200)
    S2.grid(row=2, column=4)
    B4 = Tkinter.Button(main, text ="Appliquer Contraste", command = use_contrast, fg="#a1dbcd", bg="#383a39")
    B4.grid(padx=20, pady=20, row=1, column=4)
    B5 = Tkinter.Button(main, text ="Trouver Contours", command = recherche_contours, fg="#a1dbcd", bg="#383a39")
    B5.grid(padx=20, pady=20, row=1, column=5)

    s=S1.get()
    s2=S2.get()





main.mainloop()