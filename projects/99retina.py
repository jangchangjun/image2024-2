from retinaface import RetinaFace
import cv2
import time

start = time.time()

imgfile = './img/graduate.jpg'
resp = RetinaFace.detect_faces(imgfile)

image = cv2.imread(imgfile)

for key, face in resp.items():
    cv2.rectangle(image, (face['facial_area'][0], face['facial_area'][1]), (face['facial_area'][2],face['facial_area'][3]), (0, 255,0), 2)
    cv2.putText(image, f"{face['score']:.3f}", (face['facial_area'][0], face['facial_area'][1]), cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))

# face1 = resp['face_1']
# farea1 = face1['facial_area']
# cv2.rectangle(image, (farea1[0], farea1[1]), (farea1[2], farea1[3]), (0, 255,0), 2)

# face2 = resp['face_2']
# farea2 = face2['facial_area']
# cv2.rectangle(image, (farea2[0], farea2[1]), (farea2[2], farea2[3]), (0, 255,0), 2)

# cv2.putText(image, f"{face1['score']:.3f}", (face1['facial_area'][0], face1['facial_area'][1]), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255))
# cv2.putText(image, f"{face2['score']:.3f}", (face2['facial_area'][2], face2['facial_area'][3]), cv2.FONT_HERSHEY_PLAIN,2,(0,255,0))

cv2.imshow("face", image)
end = time.time()
print((end-start)*1000)
cv2.waitKey(0)
cv2.destroyAllWindows()
