import qrcode
#HACER UNA IMAGEN QR CON PYTHON
def Qrcode():
    QR = str(input("Por favor escribe el contenido del QR: "))
    qr = qrcode.QRCode()
    qr.add_data(QR)
    img = qr.make_image()
    nombreQr = str(input("Escribe el nombre de la imagen QR, con extension .png: "))
    img.save(nombreQr)
Qrcode()