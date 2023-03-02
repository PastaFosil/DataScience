from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

img= np.array(Image.open("//home//juancho//Downloads//Full_Moon_Luc_Viatour.jpg"))
img1 = np.array(Image.open("//home//juancho//Documents//Personalizadas//DataScience//OIP.jpg"))
oldColor = [0,0,0]
newColor = [255,0,255]

mask = img==oldColor
#img = np.where(mask,newColor,img)
#img[mask.all(axis=2)] = newColor

img[:,:,0] = 0

mn = np.round_(np.mean(img1,axis=2))
mn = np.reshape(mn, (mn.shape[0],mn.shape[1],1))
imgBW = (np.ones(img1.shape)*mn).astype("uint64")

imgN = (np.ones(imgBW.shape)*255-imgBW).astype("uint64")

gauss = gaussian_filter(img1, 20, order=0, mode='nearest')

f, (a,a1) = plt.subplots(2,1,figsize=(6,6))
a.imshow(img1)
a1.imshow(imgBW)
plt.show()