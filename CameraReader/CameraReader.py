import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)
        print("Kamera initialisiert")
        if not self.camera.isOpened():
            print("Kamera konnte nicht geöffnet werden.")
            exit()

    def getImage(self, app):
        ret, frame = self.camera.read()
        #cv2.imshow('Kamera', frame)
        app.image_processor.process(frame)
        return frame