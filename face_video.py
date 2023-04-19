import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')

# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read("models/face-trainner.yml")

cap = cv2.VideoCapture(0)


# labels = {"person_name": 1}
# with open("data/face-labels.pickle", 'rb') as f:
#     og_labels = pickle.load(f)
#     labels = {v: k for k, v in og_labels.items()}

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
        roi_color = frame[y:y + h, x:x + w]

        # id_, conf = recognizer.predict(roi_gray)
        # if conf > 45:
        #     print(labels[id_])
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     name = labels[id_]
        #     color = (255, 255, 255)
        #     stroke = 2
        #     cv2.putText(frame, name, (x, y+h+50), font, 1, color, stroke, cv2.LINE_AA)

        color = (255, 0, 0)  # BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        # cv2.imwrite("liad_image.jpg", roi_color)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
