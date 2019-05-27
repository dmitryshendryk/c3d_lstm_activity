import argparse
import os 
import sys 

import cv2
from PIL import Image
import numpy as np 
import time

from yolov3.yolo import YOLO, detect_video


def yoloVideo(vid_input, isOutput=False):
    print("Loading yolo")
    yolo = YOLO()
    cap = cv2.VideoCapture(vid_input)

    while True:
        ret, frame = cap.read()
        if ret:

            image = Image.fromarray(frame)
            image, box = yolo.detect_image(image)
            print(box)
            result = np.asarray(image)
            cv2.namedWindow("result", cv2.WINDOW_NORMAL)
            cv2.imshow("result", result)
            if isOutput:
                out.write(result)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__  == '__main__':

    parser = argparse.ArgumentParser(description="C3D LSTM bahavior recognition")
    parser.add_argument('command', metavar='<commnad>', help='after the file name specify the command')
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./path2your_video',
        help = "Video input path"
    )

    args = parser.parse_args()

    if args.command == 'yolo_detect':
        yoloVideo(args.input, isOutput=False)
       





