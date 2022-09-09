def calculate():
    print("********************************")
    print("         UNIT CHANGER           ")
    print("********************************\n\n")
    list1 = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    list2 = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    for i in range (0,7):
        print("{} - {} ".format(i+1,list1[i]))
    answer1=int(input("What is your unit?"))
    if 0<answer1<8:
        unit = int(input("Enter the value of your unit: "))
        for i in range(0, 7):
            print("{} - {} ".format(i + 1, list2[i]))
        answer2 = int(input("to which unit do you want to change?"))
        if 0<answer2<8:
            if answer2 - answer1 == 1:
                output = unit * 10
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == 2:
                output = unit * 100
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == 3:
                output = unit * 1000
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == 4:
                output = unit * 10000
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == 5:
                output = unit * 100
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == 6:
                output = unit * 1000000
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == -1:
                output = unit / 10
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == -2:
                output = unit / 100
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == -3:
                output = unit / 1000
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == -4:
                output = unit / 10000
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == -5:
                output = unit / 100000
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == 6:
                output = unit / 1000000
                print(str(output) + list2[answer2 - 1])
            elif answer2 - answer1 == 0:
                print(str(unit) + list2[answer2 - 1])
                return answer2
                return answer1
        else:
            print("Wrong value.Please try again!\n\n\n")
            calculate()
    else:
        print("Wrong value.Please try again!\n\n\n")
        calculate()

calculate()
