import qrcode

myqr=qrcode.make("https://www.youtube.com/")
myqr.save("myqr.png")
