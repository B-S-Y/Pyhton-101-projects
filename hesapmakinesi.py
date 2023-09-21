#SORU ÇÖZÜMÜNDE SOR!
#OPERASYON SEMBOLÜNÜ DİREKT LİSTENİN İÇİNDEN SEÇİP İŞLEMİ YAPABİLİYOR MUYUZ?

def calculator():
    while True:
        decision = input("Write 'yes' to use the calculator or write 'no' to stop the calculator: ")
        calc_list = []

        if decision.lower() == "yes":
            first_num = int(input("Please enter the first number= "))
            second_num = int(input("Please enter the second number="))
            operation = input("Please enter the operation you want to do= (You must enter the operation by their symbol)")
            calc_list.append(first_num)
            calc_list.append(second_num)
            calc_list.append(operation)

            if calc_list[2] == "+" :
                result = calc_list[0] + calc_list[1]
                print(result)
            elif calc_list[2] == "-" :
                result = calc_list[0] - calc_list[1]
                print(result)
            elif calc_list[2] == "/" :
                result = calc_list[0] / calc_list[1]
                print(result)
            elif calc_list[2] == "*":
                result = calc_list[0] * calc_list[1]
                print(result)
            elif calc_list[2] == "**":
                result = calc_list[0] ** calc_list[1]
                print(result)
            else:
                print("This calculator is only eligible of doing addition,extraction,multiplication,divison and "
                      "exponentiation please be careful entering one of these symbols")

        elif decision.lower() == "no" :
            print("Closing the calculator...")
            break

        else:
            print("Please enter a valid answer")

calculator()
