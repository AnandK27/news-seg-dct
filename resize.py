import cv2 
import sys
import numpy as np
import os

for filename in os.listdir('input/'):
    img = cv2.imread('input/'+filename)
    x, y = img.shape[0], img.shape[1]
    img = cv2.resize(img, ((y//8)*8,(y//8)*8))
    cv2.imwrite("input_rs/" + filename[:-4] + ".png",img)
    print(sys.getsizeof(img))