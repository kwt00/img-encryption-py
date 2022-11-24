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
for index, values in enumerate(image):
	image[index] = values ^ key
fin = open(path, 'wb')
fin.write(image)
toolbar_width = 10
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
for i in range(toolbar_width):
    time.sleep(0.1)
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()
sys.stdout.write("]\n")
fin.close()
print('Image modification completed')
