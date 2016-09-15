import cv2
import numpy as np
import matplotlib.pyplot as plt
def click_and_crop(event, x, y, flags, param):
    #grab refrences to the global variables
    global refPt, cropping

    #if the left mouse button was clicked, record the starting
    #(x,y) coordinates and indicate that cropping is being performed

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt=[(x,y)]
        cropping = True

    #check to see if the left-mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        #record the ending(x,y) coordinates and indicate that
        #the cropping oeration has finished
        refPt.append((x,y))
        cropping = False

        #draw a rectangle arounf the region of interest
        cv2.rectangle(image,refPt[0],refPt[1],(0,0,200),)
        cv2.imshow("image",image)

image = cv2.imread('messi.jpg')
clone = image.copy()
cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback("image", click_and_crop)
bgModel = np.zeros((1,65), np.float64)
fgModel = np.zeros((1,65),np.float64)
 
# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
		
 
	# if the 'c' key is pressed, break from the loop
	if key == ord("c"):
		break
 
# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
    
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.imshow("ROI", roi)
    
    rect = (refPt[0][1],refPt[1][1], refPt[0][0],refPt[1][0])
    cv2.grabCut(image,mask,rect,bgModel,fgModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask ==0),0,1).astype('uint8')
    image = image*mask2[:,:,np.newaxis]
    cv2.imshow("Image",image)
    cv2.waitKey(0)
 
# close all open windows
cv2.destroyAllWindows()
