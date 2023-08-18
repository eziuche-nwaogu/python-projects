import qrcode

data = input("Enter the data you want to encode: ")
dest = input(
    "Enter the full path destination of where you want your qrcode to be saved: "
)
qr_name = input("Enter the name to save the image: ")
dest = dest.replace("\\", "/")
dest = dest + "/" + qr_name + ".png"
img = qrcode.make(data)
img.save(dest)
print("Success! You can check the folder for the QR Code")
