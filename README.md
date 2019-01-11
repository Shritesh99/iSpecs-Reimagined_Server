# iSpecs Reimagined 👓


iSpecs is the real time object detection specs based on YOLO with Raspberry pi.
It's like regular specs but with object detection

This is the server side repository of iSpecs in which detection occurs on each and every frame send by client side of iSpecs.
###### New Features!
  - separate client and server repos 
  -  better accuracy 

##### checkout the Client repo [here](https://github.com/Shritesh99/iSpecs-Reimagined_Client)
##### Checkout the manual version [here](https://github.com/Shritesh99/iSpecs)




![workflow diagram here](https://raw.githubusercontent.com/Shritesh99/iSpecs-Reimagined_Server/master/images/iSpecs-Arch.png)
In iSpecs the client raspberry pi sends the images obtain by picamera as a POST request and get the response of object detection in json format which will be spoken via tts engine in client.
### Tech
mainly uses YOLO system for object detection:
* [Yolo v3](https://pjreddie.com/darknet/yolo/) - real-time object detection system
* Django -  handling client request



### Installation

iSpecs requires Django to run.
Install the dependencies  and start the server.

```sh
$ python manage.py runserver
```



##### Contributors
  - [Shritesh](https://github.com/Shritesh99)

if you find any problem feel free to create issue.
 Suggestions and feedbacks are always welcomed!
### Todos

 - suppport better fps
 - add more features





