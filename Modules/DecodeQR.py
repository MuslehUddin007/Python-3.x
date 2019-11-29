import qrtools

qr = qrtools.QR()
qr.decode("myqr1.png")
print(qr.data)