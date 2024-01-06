import cv2
cascade_face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

while True:
    
    ret, img=cap.read()

    
    gr=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    f=cascade_face.detectMultiScale(gr,1.3,5)
    
    y=0;x=0;h=0;w=0  
    for(x, y, w, h) in f:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0), 5)  
        
    a=cv2.imshow("img",img)
    cv2.imwrite("C:\\Users\\HP\\Desktop\\img.jpeg",gr)
    
    if cv2.waitKey(30) & 0xff== ord("q"):
        break
    
cap.releas()
cv2.destroyAllWindows()
