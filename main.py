import os
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('../source/face_detect.xml') #取用已經做好的模型
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer.yml')


while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceRect = faceCascade.detectMultiScale(gray, 1.1, 10)

        for (x, y, w, h) in faceRect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
            face = gray[y:y+h, x:x+w]

            label, confidence = recognizer.predict(face) #預測是否為圖庫中的人臉。輸出標籤以及信心度，信心越低代表約有可能是圖庫中的人臉。
            print(label, confidence)

            if confidence < 40:
                cv2.putText(frame, 'This guy is {} confidence {}'.format(label, confidence), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            else:
               cv2.putText(frame, 'NO!!!!', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3) 
        
        cv2.imshow('frame', frame)

    else:
        break

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()