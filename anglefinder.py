import cv2 as cv 
import math 

path = 'angles.jpeg'
img = cv.imread(path)

points = []

def GetAngle(points):

    b,c,a = points[-3:]
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1],a[0]-b[0]))
    an = round(ang + 360 if ang < 0 else ang)
    print (ang)

def Click_event(event,x,y,flags,params):
        global points,img
        if event == cv.EVENT_LBUTTONDOWN:
           if len(points) != 0 and len(points) % 3 != 0 :
             cv.line(img,tuple(points[round((len(points)-1)/3)*3]), (x,y),(0,255,0),2)
           cv.circle(img,(x,y),4,(0,255,0),-1)
           points.append([x,y])
           cv.imshow('image',img)
           if len(points) %3 == 0 and len (points) != 0 :
               GetAngle(points)
               cv.imshow('image' ,img)
        if event == cv.EVENT_RBUTTONDOWN:
            points = []
            img = cv.imread(path)
            cv.imshow('image',img)

cv.imshow('image',img)
cv.setMouseCallback('image',Click_event)
cv.waitKey(0)