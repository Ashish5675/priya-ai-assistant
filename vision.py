import cv2

def detect_emotion():
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    ret, frame = cam.read()
    if not ret:
        cam.release()
        return "no camera"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    cam.release()

    if len(faces) > 0:
        return "neutral"
    else:
        return "no user"
