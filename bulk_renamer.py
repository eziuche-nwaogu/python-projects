import os


def renamer():
    path = input("Enter the file path you wish to rename: ")
    path = path.replace("\\", "/")
    path = path + "/"
    i = 0
    for filename in os.listdir(path):
        my_source = path + filename
        my_dest = "IMG" + str(i) + ".jpg"
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
    print("Success! You can now check your folder")


renamer()
