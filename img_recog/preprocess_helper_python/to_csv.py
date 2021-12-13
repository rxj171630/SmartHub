import os

# pics = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\toCsv\\train'
# csv_file = open('C:\\Users\\jackk\\Desktop\\IOT Final Project\\toCsv\\fingers_data.csv', 'a')
test = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\testjpg'
train = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\archive\\fingers\\trainjpg'
csv_file = open('C:\\Users\\jackk\\Desktop\\IOT Final Project\\toCsv\\fingers_data_colab.csv', 'a')

for root, dirs, files, in os.walk(train):
    for file in files:
        # line = "TRAIN," + os.path.join(root, file)
        line = "TRAIN,/content/drive/MyDrive/IOT/trainjpg/" + file 
        before, label = line.split('_')
        label = label.split('.')[0]
        csv_file.write(line + ',' + label +  ',0,0,1,0,1,1,0,1' + '\n')
        # csv_file.write(line + '\n')


for root, dirs, files, in os.walk(test):
    for file in files:
        # line = "TEST," + os.path.join(root, file)
        line = "TEST,/content/drive/MyDrive/IOT/testjpg/" + file 
        before, label = line.split('_')
        label = label.split('.')[0]
        csv_file.write(line + ',' + label +  ',0,0,1,0,1,1,0,1' + '\n')
        # csv_file.write(line + '\n')        

print("done")
csv_file.close()