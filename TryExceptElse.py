
#problem two
def ask():
    count = 0
    while count < 3:
        try:
            number = int(input("Input an integer:"))
        except:
            print("An error occured, please try again")
            count += 1
        else:
            print("Thank you, your number squared is: {}".format(number**2))
            count = 3

ask()
