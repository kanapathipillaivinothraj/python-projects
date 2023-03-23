import qrcode
# install QR Code Generator module
data = input("Enter your data: ")
img = qrcode.make(data)

img.save(f'{data}.png')
