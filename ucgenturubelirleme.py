def ucgen_belirleme(side_1,side_2,side_3):
    if side_1 == side_2:
        if side_1 == side_3:
            print("This is an equilateral triangle.")
        else:
            print("This is an isosceles triangle.")

    elif side_1 == side_3 :
        if side_1 == side_2:
            print("This is an equilateral triangle.")
        else:
            print("This is an isosceles triangle.")

    elif side_2 == side_3:
        if side_2 == side_1:
            print("This is an equilateral triangle.")
        else:
            print("This is an isosceles triangle.")

    else:
        print("This is a scalene triangle.")


while True:
    decision = input("on/off?")
    if decision == "on":
        side_1 = int(input("Enter the first corner of the triangle you want to check= "))
        side_2 = int(input("Enter the second corner of the triangle you want to check= "))
        side_3 = int(input("Enter the third corner of the triangle you want to check= "))
        if abs(side_1-side_2)<= side_3 <=side_2+side_1:

            ucgen_belirleme(side_1,side_2,side_3)
        else:
            print("Given sides doesn't make up a traingle please try again! ")
    elif decision == "off":
        print("closing...")
        break
    else:
        print("Please enter a valid answer!")
