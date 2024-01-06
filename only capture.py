import cv2


cap=cv2.VideoCapture(0)

while True:
    
    ret, img=cap.read()
    #print(ret)
    
    #gr=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gr=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        
    a=cv2.imshow("img",img)
    cv2.imwrite("C:\\Users\\HP\\Desktop\\img.jpeg",gr)
    
    if cv2.waitKey(30) & 0xff== ord("q"):
        break
    
cap.releas()
cv2.destroyAllWindows()
