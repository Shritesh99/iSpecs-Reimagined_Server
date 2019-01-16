# iSpecs Reimagined 👓


iSpecs is the real time object detection specs based on YOLO with Raspberry pi.
It's like regular specs but with object detection

This is the server side repository of iSpecs in which detection occurs on each and every frame send by client side of iSpecs.

![workflow diagram here](https://raw.githubusercontent.com/Shritesh99/iSpecs-Reimagined_Server/master/images/iSpecs-Arch.png)

### New Features!
  - Real Time Object detection.
  - Better accuracy 

#### Checkout the Client repository [here](https://github.com/Shritesh99/iSpecs-Reimagined_Client)
#### Checkout the Manual version [here](https://github.com/Shritesh99/iSpecs)

In iSpecs the client raspberry pi sends the images obtain by picamera as a POST request and get the response of object detection in json format which will be spoken via tts engine in client.
### Tech
Mainly uses YOLO system for object detection:
* [Yolo v3](https://pjreddie.com/darknet/yolo/) - real-time object detection system
* Django -  handling client request

### Installation

iSpecs requires Django to run.
Install the dependencies  and start the server.

```sh
$ python manage.py runserver
```

#### Contributors
  - [Shritesh](https://github.com/Shritesh99)
  - [Siddharth](https://github.com/siddharthshah3030)

If you find any problem feel free to create issue.

Suggestions and feedbacks are always welcomed!




