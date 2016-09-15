import cv2
import numpy as np
import matplotlib.pyplot as plt

class BackgroundSubtract:
    def __init__(self):
    	pass
refPt = []
cropping = False
img = cv2.imread('messi1.jpg')
#image = cv2.imread('messi.jpg')
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
        cv2.rectangle(img,refPt[0],refPt[1],(0,255,0),2)
        cv2.imshow("CropImage",img)


    


mask = np.zeros(img.shape[:2], np.uint8)
cv2.namedWindow("CropImage",cv2.WINDOW_AUTOSIZE)
#copy = img.clone
cv2.setMouseCallback("CropImage",click_and_crop)
bgModel = np.zeros((1,65), np.float64)
fgModel = np.zeros((1,65),np.float64)
cv2.imshow("image",img)
x = raw_input()
if len(refPt) ==2 and x ==1:
    rect = (refPt[0][1],refPt[1][1], refPt[0][0],refPt[1][0])
    cv2.grabCut(img,mask,rect,bgModel,fgModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask ==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    cv2.imshow("Image",img)
    
cv2.imshow("1Image",img)
plt.imshow(img),plt.colorbar(),plt.show()
cv2.DestroyAllWindows()
