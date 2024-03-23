#Source: https://stackoverflow.com/questions/62981032/python-filenotfounderror-errno-2-no-such-file-or-directory-how-to-add-file
from PIL import Image, ImageFilter
import os

root_dir= os.path.dirname(os.path.abspath(r'C:\Users\User\eclipse-workspace\Practice Python CS50 2019\images\Mario.png'))
before = Image.open('Mario.png')
after=before.filter(ImageFilter.BLUR)
after.save("MarioBLUR.png")