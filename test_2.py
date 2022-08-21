from PIL import Image
import cv2
from sewar.full_ref import uqi
score_reached = 0
q = 10
image_path = "D:\\Prerana\\Techsurf\\koniq10k_512x384\\512x384\\826373.jpg"
image_file = Image.open(image_path)
while(not score_reached):
    image_file.save("test_2.jpg", quality=q)
    img_1 = cv2.imread(image_path)
    img_2 = cv2.imread("D:\\Prerana\\Techsurf\\test_2.jpg")
    print("Entered")
    score = uqi(img_1, img_2)
    if(score >= 0.95):
        score_reached = 1
    print(q, score)
    q += 2
print("DONE with q= "+str(q-2))
