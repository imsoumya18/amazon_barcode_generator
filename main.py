from barcode import Code39
from barcode.writer import ImageWriter

number = '123456789026'

code = Code39(number, writer=ImageWriter())

code.save('new')
