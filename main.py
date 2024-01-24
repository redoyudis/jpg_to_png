import sys
import os
from PIL import Image

old_path = sys.argv[1]
new_path = sys.argv[2]

try:
    os.mkdir(new_path)
except OSError as error:
    print(error)

for infile in os.listdir(old_path):
    f, e = os.path.splitext(infile)
    try:
        with Image.open(f'{old_path}/{infile}') as im:
            im.save(f'./{new_path}/{f}.png')
    except OSError as err:
        # print("cannot convert", infile)
        print(err)
print('process Complete')
