import qrcode
import image
qr= qrcode.QRCode(
    version=1, #1 means the version of the qr code, higher the number the more complicated qr code will get. You can give it from 1-40
    box_size=10, #sizo of the box where qr code will be displayed
    border=5

)

data="https://github.com/HemanthReddyChappidi"

# i have given my github profile link , the same way you can give anything you want.

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",black_color="white")
img.save("test.png")