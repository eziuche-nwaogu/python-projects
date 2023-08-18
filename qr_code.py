import qrcode

data = "Don't forget to subscribe"
img = qrcode.make(data)
img.save("C:/Users/EZIUCHE NWOGU/Desktop/python/myqrcode.png")
