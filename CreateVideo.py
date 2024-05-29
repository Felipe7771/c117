import os
import cv2

path = "C:/Users/User/Downloads/Projeto117/PRO_1-4_C117_TemplateDoProjeto-main/Images"

Images = []

for file in os.listdir(path):
    name, extation = os.path.splitext(file)

    if extation in ['.jpg','.gif','.jpeg','.jfif','.png']:
        file_name = path + "/"+ file
        Images.append(file_name)
        #print(file_name)

    count = len(Images)
    frame = cv2.imread(Images[0])

    width, height, channels = frame.shape
    size = (width, height)
    print(size)

    out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):
    frame = cv2.imread(Images[i])
    out.write(frame)

print("Concluido")