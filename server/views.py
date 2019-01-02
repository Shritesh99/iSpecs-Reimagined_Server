import numpy as np
import time
import cv2
import os
from rpi_server import settings
from django.http import JsonResponse
from rest_framework.views import APIView


class Detect(APIView):

    def post(self, request, *args, **kwargs):
        stime = time.time()
        res = {}
        frame = cv2.imread(request.POST.get('frame'), cv2.IMREAD_COLOR)
        results = settings.tfnet.return_predict(frame)
        for result in zip(results):
             res[result['label']] = result['confidence']
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        return JsonResponse(res)
