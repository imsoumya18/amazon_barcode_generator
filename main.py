from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
import os

number = 'HSDWJDWBDJWBJD'

code = Code128(number, writer=ImageWriter())

code.save('new')

im = Image.open(r'new.png')
im.save(r'new.jpg')

os.remove('new.png')
