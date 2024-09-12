from turtledemo.nim import COLOR

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
def korean(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)

img = np.full((500,500,3), 255, dtype=np.uint8)

# cv2.putText(img, "Plain", (50,30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
# cv2.putText(img, "Simplex", (50,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
# cv2.putText(img, "Duplex", (50, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))
# cv2.putText(img, "Simplex X 2", (200,110), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,250))
# cv2.putText(img, "Complex", (50,200), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0))
# cv2.putText(img, "Complex", (50,260), cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,0))
# cv2.putText(img, "Complex", (200,260), cv2.FONT_HERSHEY_TRIPLEX ,1,(0,0,0))
# cv2.putText(img, "Complex", (200,260), cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255))

COLOR = (0,0,0)
FONT_SIZE = 30

img = korean(img, "아름다운 강산 -이용희", (20,50), FONT_SIZE, COLOR)


cv2.imshow('letters', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
