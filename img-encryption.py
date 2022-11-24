import time
import sys
path = input(r'Enter path of image : ')
key= []
keyS = (input('Enter Key(int and string) : '))
keyS = list(keyS)
for i in keyS:
    if i=="": continue
    elif i.isnumeric():key.append(i)
    else:key.append(ord(i))
holder = key
key = 1
for e in range(len(holder)):
    key^=int(holder[e])
print('Filepath : ', path)
fin = open(path, 'rb')
image = fin.read()
fin.close()
image = bytearray(image)
counter=0
sys.stdout.write("[")
for index, values in enumerate(image):
	image[index] = values ^ key
	counter+=1
	if counter==len(image)//20:
	 counter=0
	 sys.stdout.write("#")
sys.stdout.write("]")
fin = open(path, 'wb')
fin.write(image)
fin.close()
print('\nImage modification completed')
