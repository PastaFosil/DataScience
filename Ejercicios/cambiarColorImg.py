from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open("//home//juancho//Downloads//Full_Moon_Luc_Viatour.jpg"))

oldColor = [0,0,0]
newColor = [255,0,255]

img = np.where(img==oldColor,newColor,img)

f, a = plt.subplots(figsize=(6,6))
a.imshow(img)
plt.show()