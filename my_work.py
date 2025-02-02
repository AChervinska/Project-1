import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbow
from gtts import gTTS
from playsound import playsound

video = cv2.VideoCapture

while True: 
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_object(frame)
    output_image = draw_bbow(frame)