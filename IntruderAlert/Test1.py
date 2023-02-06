import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
upbody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
full_body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
flag=False

cap=cv2.VideoCapture(0)
_,frame0=cap.read()
_,frame1=cap.read()
while True:
    diff=cv2.absdiff(frame0,frame1)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray, (5,5), 0)
    _,thresh=cv2.threshold(blur,20,255, cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh, None, iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame0,contours,-1,(0,255,0),2)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<5000:
            continue
        cv2.rectangle(frame0,(x,y),((x+w),(y+h)),(0,0,255),2)
        roi = frame0[y:y + h, x:x + w]
        faces = face_cascade.detectMultiScale(roi, 1.3, 4)
        for (x1,y1,w1,h1) in faces:
            cv2.rectangle(roi, (x1, y1), ((x1 + w1), (y1 + h1)), (0, 255, 0), 2)
        up_bodies = upbody_cascade.detectMultiScale(roi, 1.3, 5)
        for (x1, y1, w1, h1) in up_bodies:
            cv2.rectangle(roi, (x1, y1), ((x1 + w1), (y1 + h1)), (0, 255, 255), 2)
        bodies = full_body_cascade.detectMultiScale(roi, 1.3, 5)
        for (x1, y1, w1, h1) in bodies:
            cv2.rectangle(roi, (x1, y1), ((x1 + w1), (y1 + h1)), (255, 0, 0), 2)
        if len(faces) or len(up_bodies) or len(bodies):
            flag=True
    if flag:
        cv2.putText(frame0, 'DETECTED', (0,50), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow("name",frame0)
    frame0=frame1
    _,frame1=cap.read()
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()