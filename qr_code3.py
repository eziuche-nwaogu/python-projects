# """This is a QR generator that accepts a series of input from the user and performs some
#    error handling before producing the QR code. It accepts information such as the data
#    to be encoded, the destination path to save the file, the name by which the file will
#    be saved, the background color and the fill color."""

import qrcode

color1 = {1: "red", 2: "yellow", 3: "green", 4: "blue", 5: "indigo", 6: "white"}
color2 = {1: "red", 2: "yellow", 3: "green", 4: "blue", 5: "indigo", 6: "white"}

data = input("Enter the data you wish to encode: ")
dest = input("\nEnter the full path of where you want your file to be saved: ")
name = input("\nEnter the name of the file to be saved: ")
while True:
    while True:
        print("1. red")
        print("2. yellow")
        print("3. green")
        print("4. Blue")
        print("5. Indigo")
        print("6. white")
        back1_color = input("\nEnter your choice of color for the background: ")
        if not back1_color.isdigit() and back1_color.lower() not in color1.values():
            print("\nInvalid color. Please try again")
        elif back1_color.isdigit() and (int(back1_color) < 1 or int(back1_color) > 5):
            print("\nYou entered a wrong value. Please try again")
        else:
            break

    while True:
        print("1. red")
        print("2. yellow")
        print("3. green")
        print("4. Blue")
        print("5. Indigo")
        print("6. white")

        fill_col = input("\nEnter your choice of color for the fill color: ")
        if not fill_col.isdigit() and fill_col.lower() not in color2.values():
            print("\nInvalid color. Please try again")
        elif fill_col.isdigit() and (int(fill_col) < 1 or int(fill_col) > 5):
            print("\nYou entered a wrong value. Please try again")
        else:
            break

    backG_color = color1[int(back1_color)] if back1_color.isdigit() else back1_color
    fillcol = color2[int(fill_col)] if fill_col.isdigit() else fill_col
    if backG_color.lower() == fillcol.lower():
        print(
            "\nThe background color and the fill color cannot be the same! Choose different colors"
        )
    else:
        break
dest = dest.replace("\\", "/")
dest = dest + "/" + name + ".png"

qr = qrcode.QRCode(version=1, box_size=50)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color=fillcol, back_color=backG_color)
img.save(dest)

print("\nSuccess! You can check your folder for the image")
