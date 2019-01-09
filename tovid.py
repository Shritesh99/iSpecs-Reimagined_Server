import os
import cv2
'''
File to convert images to video
'''
dir = os.path.dirname(os.path.realpath(__file__))
dir = os.path.join(dir, 'img')
files = len(os.listdir(dir))

img1 = cv2.imread('img/temp1.jpg')
height, width, channels = img1.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('video.mp4', fourcc, 10, (width, height))
for i in range(1,files):
    img = cv2.imread('img/temp{}.jpg'.format(i))
    video.write(img)

cv2.destroyAllWindows()
video.release()