#Source: https://stackoverflow.com/questions/59298082/opencv-image-processing-gui-typeerror-on-click-diff-per-button-takes-1-posit
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import glob
import os
import cv2
import numpy as np
from PIL import Image
from PIL import ImageTk
from skimage.metrics import structural_similarity
class Button:

    def __init__(self, root, frame2):
        self.root = root
        self.frame2 = frame2
        self.radio_var = tk.IntVar()
        self.path_selected = 'none'
        self.paths = []
        self.radio_handle = []
        self.check_value = []

    def on_click_select_button(self, fname_label):
        print('select button clicked')
        fileType = [('jpg/png file', ('*.jpg', '*.png'))]
        self.path_selected = filedialog.askopenfilename(filetypes=fileType)
        fname_label['text'] = os.path.basename(self.path_selected)

    def on_click_upload_button(self, path='None', image='None'):
        print('upload button clicked')

        if path == 'None':
            path = self.path_selected
        else:
            cv2.imwrite(path, image)

        if path in self.paths:
            messagebox.showerror('Upload Error', '"'
                                 + path
                                 + '"' + ' is already uploaded.')
        else:
            self.paths.append(path)
            self.create_radio_button(path)

    def on_click_show_button(self):
        print('showButton clicked')
        image = cv2.imread(self.paths[self.radio_var.get()])
        file_name = os.path.basename(self.paths[self.radio_var.get()])
        name, ext = os.path.splitext(file_name)
        path = 'images/' + name + '_' + ext

        # cv2.imwrite(path, image)
        self.open_image_window(path, image)

    def create_radio_button(self, path):

        image = cv2.imread(path)
        # image = cv2.resize(image,(120,120))
        image = self.scale_to_height(image, 120)
        image_tk = self.to_tk_image(image)

        radio_button = tk.Radiobutton(self.frame2, image=image_tk,
                                      value=len(self.radio_handle),
                                      variable=self.radio_var)
        self.radio_var.set(0)
        self.radio_handle.append(radio_button)
        self.check_value.append(self.radio_var)

        radio_button.grid(row=(len(self.radio_handle) - 1) // 3,
                          column=(len(self.radio_handle) - 1) % 3)
        self.root.mainloop()

    def open_image_window(self, path, image):

        if image.shape[0] > 300:
            image = self.scale_to_height(image, 300)

        img_win = tk.Toplevel(self.root)
        fname = os.path.basename(path)
        img_win.title(fname)
        img_canvas = tk.Canvas(img_win, width=image.shape[1],
                               height=image.shape[0])
        img_canvas.pack()
        image_tk = self.to_tk_image(image)
        img_canvas.create_image(0, 0, image=image_tk, anchor='nw')

        uploadButton2 = tk.Button(img_win, text='upload',
                                  command=lambda: self.on_click_upload_button(path, image))
        uploadButton2.pack()
        self.root.mainloop()
    def to_tk_image(self, image_bgr):
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        image_tk = ImageTk.PhotoImage(image_pil)
        return image_tk
    def scale_to_height(self, img, height):
        scale = height / img.shape[0]
        return cv2.resize(img, dsize=None, fx=scale, fy=scale)
class Sample_Button:
    def __init__(self, root, frame4):
        self.Sample_root = root
        self.frame4 = frame4
        self.Sample_radio_var = tk.IntVar()
        self.Sample_path_selected = 'none'
        self.Sample_paths = []
        self.Sample_radio_handle = []
        self.Sample_check_value = []

    def on_click_select_button_Sample(self, Sample_fname_label):
        print('select Sample button clicked')
        Sample_fileType = [('jpg/png file', ('*.jpg', '*.png'))]
        self.Sample_path_selected = filedialog.askopenfilename(filetypes=Sample_fileType)
        Sample_fname_label['text'] = os.path.basename(self.Sample_path_selected)

    def on_click_upload_button_Sample(self, Sample_path='None', Sample_image='None'):
        print('upload Sample button clicked')

        if Sample_path == 'None':
            Sample_path = self.Sample_path_selected
        else:
            cv2.imwrite(Sample_path, Sample_image)

        if Sample_path in self.Sample_paths:
            messagebox.showerror('Upload Error', '"'
                                 + Sample_path
                                 + '"' + ' Sample is already uploaded.')
        else:
            self.Sample_paths.append(Sample_path)
            self.create_Sample_radio_button(Sample_path)

    def on_click_show_button_Sample(self):
        print('show Sample Button clicked')
        Sample_image = cv2.imread(self.Sample_paths[self.Sample_radio_var.get()])
        Sample_file_name = os.path.basename(self.Sample_paths[self.Sample_radio_var.get()])
        Sample_name, ext = os.path.splitext(Sample_file_name)
        Sample_path = 'Sample_images/' + Sample_name + '_' + ext


    def create_Sample_radio_button(self, Sample_path):
        Sample_image = cv2.imread(Sample_path)
        Sample_image = self.scale_to_height_Sample(Sample_image, 120)
        Sample_image_tk = self.Sample_to_tk_image(Sample_image)

        Sample_radio_button = tk.Radiobutton(self.frame4, image=Sample_image_tk,
                                      value=len(self.Sample_radio_handle),
                                      variable=self.Sample_radio_var)
        self.Sample_radio_var.set(0)
        self.Sample_radio_handle.append(Sample_radio_button)
        self.Sample_check_value.append(self.Sample_radio_var)

        Sample_radio_button.grid(row=(len(self.Sample_radio_handle) - 1) // 3,
                          column=(len(self.Sample_radio_handle) - 1) % 3)
        self.Sample_root.mainloop()

    def Sample_to_tk_image(self, Sample_image_bgr):
        Sample_image_rgb = cv2.cvtColor(Sample_image_bgr, cv2.COLOR_BGR2RGB)
        Sample_image_pil = Image.fromarray(Sample_image_rgb)
        Sample_image_tk = ImageTk.PhotoImage(Sample_image_pil)
        return Sample_image_tk

    def scale_to_height_Sample(self, Sample_img, height):
        scale = height / Sample_img.shape[0]
        return cv2.resize(Sample_img, dsize=None, fx=scale, fy=scale)

class Difference_Button(Button, Sample_Button):
    def on_click_diff_per_button(self):
        print('select Difference button clicked')

        Sample_image = cv2.imread(self.Sample_paths[self.Sample_radio_var.get()])
        print(Sample_image)
        image = cv2.imread(self.paths[self.radio_var.get()])
        print(image)
        #for x in range(7):
        Greyscale_Sample_image = cv2.cvtColor(Sample_image, cv2.COLOR_RGB2GRAY)
        Greyscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        (score, diff) = structural_similarity(Greyscale_image, Greyscale_Sample_image, full=True)  # bw_
        print("Image similarity %ge =", score * 100)

        diff = (diff * 255).astype("uint8")

        cv2.imshow('diff', diff)
        cv2.waitKey()

    pass


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    root = tk.Tk()
    root.title('Image GUI')
    root.geometry('1280x960')
    pw_left = tk.Frame(root, relief='ridge', borderwidth=4)
    pw_left.pack(side='left', anchor='nw')
    pw_right = tk.Frame(root, relief='ridge', borderwidth=4)
    pw_right.pack(side='left', anchor='nw')
    frame1 = tk.Frame(pw_left, bd=2, relief="ridge")
    frame1.pack()
    frame2 = tk.LabelFrame(pw_right, bd=2, text='Uploaded images')
    frame2.pack(side='left', anchor='nw')
    button = Button(root, frame2)
    label = tk.Label(frame1, text='File:')
    label.grid(row=0, column=0)
    file_name_label = tk.Label(frame1, text='-----not selected-----', width=20, bg='white')
    file_name_label.grid(row=0, column=1)
    select_button = tk.Button(frame1, text='select', command=lambda: button.on_click_select_button(file_name_label))
    select_button.grid(row=0, column=2)
    uploadButton = tk.Button(frame1, text='Upload',
                             command=lambda: button.on_click_upload_button())
    uploadButton.grid(row=0, column=3)
    os.makedirs('Sample_images', exist_ok=True)
    pw_left = tk.Frame(root, relief='ridge', borderwidth=4)
    pw_left.pack(side='left', anchor='nw')
    pw_right = tk.Frame(root, relief='ridge', borderwidth=4)
    pw_right.pack(side='left', anchor='nw')
    frame3 = tk.Frame(pw_left, bd=2, relief="ridge")
    frame3.pack()
    frame4 = tk.LabelFrame(pw_right, bd=2, text='Uploaded Sample images')
    frame4.pack(side='right', anchor='nw')


    Sample_button = Sample_Button(root, frame4)
    Sample_label = tk.Label(frame3, text='Sample File:')
    Sample_label.grid(row=0, column=0)
    Sample_file_name_label = tk.Label(frame3, text='-----not selected-----', width=20, bg='white')
    Sample_file_name_label.grid(row=0, column=1)
    Sample_select_button = tk.Button(frame3, text='select',
                                     command=lambda: Sample_button.on_click_select_button_Sample(
                                         Sample_file_name_label))
    Sample_select_button.grid(row=0, column=2)
    Sample_uploadButton = tk.Button(frame3, text='Upload',
                                    command=lambda: Sample_button.on_click_upload_button_Sample())
    Sample_uploadButton.grid(row=0, column=3)
    os.makedirs('Differece_images', exist_ok=True)
    pw_left = tk.Frame(root, relief='ridge', borderwidth=4)
    pw_left.pack(side='left', anchor='nw')
    pw_right = tk.Frame(root, relief='ridge', borderwidth=4)
    pw_right.pack(side='left', anchor='nw')
    frame5 = tk.Frame(pw_left, bd=2, relief="ridge")
    frame5.pack()
    frame6 = tk.LabelFrame(pw_right, bd=2, text='Uploaded images')
    frame6.pack(side='left', anchor='nw')

    difference_button = Difference_Button(root, frame6)
    Difference_per_label = tk.Label(frame5, text='Show Image Difference', width=20, bg='white')
    Difference_per_label.grid(row=0, column=1)
    img_diff_button = tk.Button(frame5, text='Difference', command=lambda: difference_button.on_click_diff_per_button(Difference_per_label))
    img_diff_button.grid(row=0, column=2)


    root.mainloop()