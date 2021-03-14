import cv2
import math

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size=len(pointsList)
        if size != 0 and size %3!=0:
            cv2.line(img,tuple(pointsList[round(((size-1)/3)*3)]),(x,y),(0,0,255),2)                    #this will draw the line first in 2 points and with 3rd point
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)  #whenever we clicked we want circle on img
        pointsList.append([x,y])
        
def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])                                      #pts1[x1,y1] pts2[x2,y2]# #here we are applying formula to calculate angle

def getAngle(pointsList):
    pt1,pt2,pt3=pointsList[-3:]
    m1=gradient(pt1,pt2)
    m2=gradient(pt1,pt3)
    angR=math.atan((m2-m1)/1+(m2*m1))
    angD=round(math.degrees(angR))
    cv2.putText(img,str(angD),((pt1[0]-40),pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),2)              #this will print reading on image

if __name__ == '__main__':
    path = "/Users/pratik/Downloads/323569.jpg"
    img = cv2.imread(path)
    pointsList = []                                                             # MAking List to store X,Y POints where the mouse are clicked.
    while True:

        if len(pointsList) % 3 == 0 and len(
                pointsList) != 0:                                               # When pointList is divisble by 3 and not equal to zero it will run
            getAngle(pointsList)

        cv2.imshow('Image', img)
        cv2.setMouseCallback('Image',
                             mousePoints)                                       # This function return the X,Y coordinate where the mouse is clicked in the image
        if cv2.waitKey(1) & 0xFF == ord(
                'q'):                                                           # by this whenever we press q the old points will be refreshed by making fresh list
            pointList = []
            img = cv2.imread(path)






