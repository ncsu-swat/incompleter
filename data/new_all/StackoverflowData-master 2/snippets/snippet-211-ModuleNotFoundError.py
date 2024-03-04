#Source: https://stackoverflow.com/questions/48847515/typeerror-image-data-cannot-be-converted-to-float
import cv2 
import matplotlib.pyplot as plt

img1 = cv2.imread('images\colombia_city.jpg')
img2 = cv2.imread('images\colombia_city_2.jpg')

#img = img1 + img2
#img = cv2.add(img1,img2)
abc = cv2.addWeighted(img1,0.7,img2,0.3,55)

plt.imshow(abc)
plt.show()
plt.title("Weighted"); plt.axes()
plt.waitforbuttonpress()