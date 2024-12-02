import cv2
from deepface import DeepFace
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import time
import matplotlib.pyplot as plt

img_file = "./img/children.jpg"
image = cv2.imread(img_file)

# backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'fastmtcnn', 'retinaface', 'mediapipe', 'yolov8', 'yunet', 'centerface']

backends = ['opencv', 'ssd',  'mtcnn',  'retinaface', 'yunet', 'centerface']
timing = []


for engine in backends:
    start = time.time()
    detections = DeepFace.extract_faces(img_path=img_file,
                                        detector_backend=engine,
                                        enforce_detection=False)
    end = time.time()
    timing.append((end-start)*1000)

for face in detections:
    facial_area = face['facial_area']
    print(facial_area)
    cv2.rectangle(image, (facial_area['x'], facial_area['y']), (facial_area['x'] + facial_area['w'], facial_area['y'] + facial_area['h']), (255, 0, 0),2)
    cv2.putText(image, engine, (10, 10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))

plt.bar(backends, timing, color = 'skyblue', alpha=0.7)
plt.xlabel('Engines')
plt.ylabel('RunTime')
plt.show()

cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()