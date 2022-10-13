
import cv2


cv2.aruco.detectMarkers

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
profile_cascade=cv2.CascadeClassifier("haarcascade_profileface.xml")
camera = cv2.VideoCapture(0)



while True:
    success, frame = camera.read()
    tickmark = cv2.getTickCount() #mesure de temps
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #passage au noir et blanc

    face = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3) #renvoie une liste de coordonées d'un rectangle
    for x,y,w,h in face: #a chaque quadruplet, on construit un rectangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    face = profile_cascade.detectMultiScale(gray, scaleFactor=1.2,minNeighbors=3)  # renvoie une liste de coordonées d'un rectangle
    for x, y, w, h in face:  # a chaque quadruplet, on construit un rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    gray2=cv2.flip(gray,1)
    face = profile_cascade.detectMultiScale(gray, scaleFactor=1.2,minNeighbors=3)  # renvoie une liste de coordonées d'un rectangle
    for x, y, w, h in face:  # a chaque quadruplet, on construit un rectangle
        cv2.rectangle(frame, (-x, y), (-x - w, y + h), (255, 0, 0), 2)

    if cv2.waitKey(1)&0xFF==ord(' '):
        break

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark) #deuxième mesure et on fait la dif pour voir le temps d'exec
    cv2.putText(frame,"FPS: {:05.2f}".format(fps),(10,30),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2) #affichage
    cv2.imshow('video',frame)

camera.release() #libère tout
cv2.destroyAllWindows()
