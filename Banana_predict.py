import cv2
import os
import numpy as np

def averagecolor(image):
    return np.mean(image, axis=(0, 1))

path = "D:/AI Bootcamp/Banana predict/"
trainX = []
trainY = []

for label in ('Unriped','Riped', 'No Banana Found'):
    print ("Loading training images for the label: "+label)
    
    #Load all images inside the subfolder
    for filename in os.listdir(path+label+"/"): 
        img = cv2.imread(path+label+"/"+filename)
        img_re = cv2.resize(img, (640,480))
        img_features = averagecolor(img_re)
        trainX.append(img_features)
        trainY.append(label)
test = "D:/AI Bootcamp/Banana predict/Test/"

for img in os.listdir(test):
    test_img = cv2.imread(test+img)
    test_img_feat = averagecolor(test_img)
    calculated_distances = []
    for i in trainX:
        calculated_distances.append(np.linalg.norm(test_img_feat-i))
    prediction = trainY[np.argmin(calculated_distances)]
    print(f"{img}:{prediction}")
    