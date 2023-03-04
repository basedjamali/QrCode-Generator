import qrcode

data = input("Enter data: ")
img = qrcode.make(data)
img.save(input("Name the Qr-Code file: "))