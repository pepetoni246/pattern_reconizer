__author__ = "KLSA"
__copyright__ = "Copyright 2023 to Infinity and Beyond, CEDES AG"

import cv2
from image_proc.image_proc import ImageProcessor
from visualizer.visualizer import Visualizer
from CSVmanager.csvManager import CSVmanager
from CameraReader.CameraReader import Camera

class App:
    def __init__(self):
        self.csv=CSVmanager()
        self.camera=Camera()
        self.image_processor = ImageProcessor()
        self.visualizer = Visualizer("MyVis")


    def run(self):
        try:
            while True:
                #frame = cv2.imread("assets/test_image.JPG", cv2.IMREAD_COLOR)
                frame=self.camera.getImage(self)
                pattern_list = self.image_processor.process(frame)
                for pattern in pattern_list:
                    print(f"Pattern name: {pattern.name}, Color: {pattern.color}")
                    CSVmanager.writeCSV(pattern.name, pattern.color)
                self.visualizer.visualize(frame, pattern_list)
                
                
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        except KeyboardInterrupt:
            pass
        finally:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    app = App()
    app.run()
    
