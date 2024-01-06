import cv2

cascade_face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Cascade_smile=cv2.CascadeClassifier('haarcascade_smile.xml')

cap=cv2.VideoCapture(0)

while True:
    ret, img=cap.read()
    print(ret)
    g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    f=cascade_face.detectMultiScale(g,1.3,5)
    y=0;x=0;h=0;w=0  
    for(x, y, w, h) in f:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0), 5)  
            
    cv2.imshow('img',img)
    k=cv2.waitKey(20) & 0xff

    if k==27:
        break

cap.release()

cv2.destroyAllWindows()

