import time
import cv2
import numpy as np
import json
from django.core.files.base import ContentFile
from rpi_server import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from PIL import Image


class Detect(APIView):

    def post(self, request, *args, **kwargs):
        stime = time.time()
        file = request.FILES.get('frame').read()
        file = ContentFile(file)
        image = Image.open(file)
        frame = np.array(image)
        results = settings.tfnet.return_predict(frame)
        res = []
        for color, result in zip(settings.colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            cv2.imwrite('img/temp{}.jpg'.format(settings.count), frame)
            settings.count += 1
            res.append(label)
        print(res)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        return HttpResponse(json.dumps(res))
