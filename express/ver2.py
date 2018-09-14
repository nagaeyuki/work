

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import cv2
import os
import numpy as np
from PIL import Image
import base64
# from io import StringIO
from io import BytesIO as StringIO

import scipy.misc


cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


def readb64(base64_string):
    sbuf = StringIO()
    sbuf.write(base64.b64decode(base64_string))

    im = Image.open(sbuf)
    return pimg
    #cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)


def detect():
    image_pil = readb64(sys.argv[1].replace("\\", "\\\\"))

    # image_pil = readb64(sys.argv[1].replace("\\", "\\\\")).convert('L')

    image = np.array(image_pil, 'uint8')

    faces = faceCascade.detectMultiScale(image, 1.1, 9, 0)

    scipy.misc.imsave('outfile.jpg', image)


    for (x, y, w, h) in faces:
        print (x, y, w, h)


detect()
