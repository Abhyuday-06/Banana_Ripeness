import cv2
import os
import numpy as np

def averagecolor(image):
    return np.mean(image, axis=(0, 1))

path = "D:/Programming/Banana_Ripeness/Data/"
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

cam = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cam.read()
    test_img_feat = averagecolor(frame)
    calculated_distances = []
    for i in trainX:
        calculated_distances.append(np.linalg.norm(test_img_feat-i))
    prediction = trainY[np.argmin(calculated_distances)]
    cv2.putText(frame, prediction, (100,100), cv2.FONT_HERSHEY_DUPLEX,1, (0,0,0), 2)
    

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()