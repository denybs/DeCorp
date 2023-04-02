import cv2 as cv
import json
"""
detecte les visages
"""
def saveFace(pixels,name):#il faut peut-etre faire en sorte de remplacer les datas existantes quand on refait avec le meme nom, ou bien laisser, a voir avec les resultats
    data = {name:pixels}
    with open("data.json", "a+") as file:
        json.dump(data, file)
def detectFaces(frame,face_cascade,name): #name ce sera pour voir si l'utilisateur a mis un nom associer au visage
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #detecte tout les visages
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # dessine le rectangle
    for (x, y, w, h) in faces:
        #si la zone detecté n'est pas assez grande alors on considere pas comme un visage et on skip
        if w>100 and h > 100:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if name != None:
            face_section = cv.resize(frame[y:y+h,x:x+w],(100,100)) #il faut bien resize de sorte qu'il n'y ai que le visage
            face_section_grey = cv.cvtColor(face_section, cv.COLOR_BGR2GRAY) 
            rows,cols = face_section_grey.shape
            pixels = []
            for i in range(rows):
                for j in range(cols):
                    k = int(face_section_grey[i,j])
                    pixels.append(k)
            saveFace(pixels,name)
def show():
    # importe la detection faciale
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
    # output de la cam
    cap =cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur")
            break
        detectFaces(frame,face_cascade,name=True)
        frame = cv.flip(frame,1)
        cv.imshow('DeCorp', frame)
        if cv.waitKey(1) == ord('q'):
            break
show()