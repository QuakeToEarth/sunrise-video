from turtle import width
import cv2 
import os
os.system('clear')
path = 'Images'
images = []
allImages = sorted(os.listdir(path))

for image in allImages:
    imageName= path+'/'+image
    images.append(imageName)



frame = cv2.imread(images[0])

height,width,channels = frame.shape
size = (width,height)
newVideo = cv2.VideoWriter('sunset.mp4', cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for i in range(len(images)-1,0,-1):
    frame = cv2.imread(images[i])
    newVideo.write(frame)

newVideo.release()
cv2.destroyAllWindows()