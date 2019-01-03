import time
import cv2
import json
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rpi_server import settings
from django.http import HttpResponse
from rest_framework.views import APIView


class Detect(APIView):

    def post(self, request, *args, **kwargs):
        stime = time.time()
        if default_storage.exists('temp.jpg'):
            default_storage.delete('temp.jpg')
        file = request.FILES.get('frame')
        path = default_storage.save('temp.jpg', ContentFile(file.read()))
        frame = cv2.imread('temp.jpg')
        results = settings.tfnet.return_predict(frame)
        res = []
        for result in results:
            res.append(result['label'])
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        return HttpResponse(json.dumps(res))
