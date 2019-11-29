import pyqrcode
from pyqrcode import QRCode

# Staring which represent the QR code
s = "Md Musleh Uddin Khan Akil"

# Genereate QR code
url = pyqrcode.create(s)

# create and save the file naming "myqr.png"
url.png("myqr1.png",scale=8)
