#Source: https://stackoverflow.com/questions/74029182/is-there-a-better-solution-for-matplotlib-attributeerror-module-backend-intera
import cv2
import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.get_backend())  # here prints "module://backend_interagg" on pycharm with "Show plots in tool window" ticked
matplotlib.use('TkAgg')
print(matplotlib.get_backend())  # here prints "TkAgg"

img = cv2.imread('IMG_9249.PNG', 0)

plt.imshow(img, cmap='gray')
plt.show()