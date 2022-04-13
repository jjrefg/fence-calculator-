def number_check(question):
    valid = False
    while not valid:
        error = "please enter a number more than 0:"
        try:
            width=float(input(" enter a number: "))
            if width > 0:
                return width
            else:
                print(error)
                print()

        except ValueError:
            print(error)


keep_going =""
while keep_going == "":

    width=number_check("width: ")
    height=number_check("height")

    area = width * height

    perimeter = 2 * (width + height)

    print("perimeter: {} units".format(perimeter))
    print("area:{} square units".format(area))

    keep_going = input("press <enter> to keep going or any key to quit")

print()
print("thanks for using the perimeter / area calculator")