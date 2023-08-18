# X = 1
# Y = 1
# print("{:>4}".format(" "), end=" ")
# for X in range(1, 11):
#     print("{:>4}".format(X), end=" ")
# print()
# for X in range(1, 11):
#     print("{:>4}".format(X), end=" ")
#     while Y <= 10:
#         print("{:>4}".format(X * Y), end=" ")
#         Y += 1
#     # print()
#     # Y = 1
def multiply():
    row_multiply = int(
        input("How many rows and columns of multiplication do you wish to produce? ")
    )
    X = 1
    Y = 1
    print(
        f"\nThe multiplication table for the {row_multiply} rows and columns is stated below: "
    )
    print("\n{:>4}".format(" "), end=" ")
    for X in range(1, row_multiply + 1):
        print("{:>4}".format(X), end=" ")
    print()
    for X in range(1, row_multiply + 1):
        print("{:>4}".format(X), end=" ")
        while Y <= row_multiply:
            print("{:>4}".format(X * Y), end=" ")
            Y += 1
        print()
        Y = 1


multiply()
