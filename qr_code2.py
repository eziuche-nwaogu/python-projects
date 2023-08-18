import qrcode

data = input("Enter the data you wish to encode: ")
dest = input("Enter the full path of where you want your file to be saved: ")
name = input("Enter the name of the file to be saved: ")
dest = dest.replace("\\", "/")
dest = dest + "/" + name + ".png"
qr = qrcode.QRCode(version=1, box_size=50)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="yellow")
img.save(dest)
print("Success! You can check your folder for the image")
