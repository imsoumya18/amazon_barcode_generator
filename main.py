from barcode import Code39
from barcode.writer import ImageWriter
from PIL import Image
import os

number = '123456789026'

code = Code39(number, writer=ImageWriter())

code.save('new')

im = Image.open(r'new.png')
im.save(r'new.jpg')

os.remove('new.png')
