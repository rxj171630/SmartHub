
import shutil

source = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\nothing\\square.jpg'


for i in range(1501):
    name = "C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\nothing\\square" + str(i) + ".jpg"
    shutil.copy(source, name) 
   # print(name)
print("done")

