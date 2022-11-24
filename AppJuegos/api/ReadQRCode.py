# sudo dnf install zbar-libs
# sudo apt-get install libzbar0

from pyzbar import pyzbar
from PIL import Image

image = Image.open("qrcode.png")
qr_code = pyzbar.decode(image)[0]

data = qr_code.data.decode('utf8').encode('shift-jis').decode('utf-8')
print("The data is: ", data)