import os
from PIL import Image
# train = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\train'
train = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\test'
new_folder = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\test_jpg\\'
filename = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\test'

im = Image.open('C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\black_square.png')
im.convert('RGB').save('C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\black_square.jpg',"JPEG") #this converts png image as jpeg

size = 128, 128
im.thumbnail(size, Image.ANTIALIAS)
im.convert('RGB').save('C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\black_square_small.jpg', "JPEG")


print('done')