import os
from PIL import Image
# train = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\train'
train = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\test'
new_folder = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\test_jpg\\'

for root, dirs, files, in os.walk(train):
    for file in files:
        name = os.path.join(root, file)
        im = Image.open(name)
        new_name = name.split('.')[0] + ".jpg"
        new_name = new_name.split('test\\')[1]
        new_name = new_folder + new_name
        im.convert('RGB').save(new_name,"JPEG") #this converts png image as jpeg

print('done')