import cv2
import os
import easyocr

image_dir = "Images"
reader = easyocr.Reader(['en'], gpu = False)        # Creating a reader instance for easyOCR
for file in os.listdir(image_dir):
    img_path = file
    img = cv2.imread(os.path.join(image_dir,img_path))
    mod_dir = "mod_dir"
    ocr_dir = "Output"
    if not os.path.exists(ocr_dir):
        os.mkdir(ocr_dir)
    if not os.path.exists(mod_dir):
        os.mkdir(mod_dir)
    mod_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    mod_img = cv2.convertScaleAbs(mod_img, alpha=1.7, beta=0.7)        # increasing image contrast for better detections
    mod_img_path = f'mod_dir/mod_{img_path}'
    cv2.imwrite(mod_img_path, mod_img)        # saving modified images in 'mod_dir' directory
    result = reader.readtext(mod_img_path)
    for detections in result:
        top = tuple([int(val) for val in detections[0][0]])
        bottom = tuple([int(val) for val in detections[0][2]])
        text = detections[1]
        font = cv2.FONT_HERSHEY_PLAIN
        img = cv2.rectangle(img, top, bottom, (0,255,0), 3)        # making a rectangle label around detections
        img = cv2.putText(img, text, top, font, 2, (120,255,255), 3, cv2.LINE_AA)        # writing text over those labels
    ocr_img_path = f'Output/out_{img_path}'
    cv2.imwrite(ocr_img_path, img)        # saving output file in 'Output' directory




