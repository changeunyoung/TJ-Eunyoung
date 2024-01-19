print("Welcome to Eunyonng's Calculator!\n")

while True:
    print(" ")
    print("Please select and enter an operation:")
    print("+\n-\n*\n/\n")
    selection = input()
    print("You selected " + selection + "\n")

    x = int(input("Please enter the first number: "))
    y = int(input("Please enter the second number: "))
    print("")

    if selection == '+':
        print(x, '+', y, '=', x + y)
    elif selection == '-':
        print(x, '-', y, '=', x - y)
    elif selection == '*':
        print(x, '*', y, '=', x * y)
    elif selection == '/':
        print(x, '/', y, '=', x / y)
    else:
        print('ERROR!')

    print("")

    another = input("Is there anything else you would like to do? Enter yes or no:")
    if another == 'yes':
        continue
    elif another == 'no':
        break

print("Thank you for using Eunyoung's Calculator!")