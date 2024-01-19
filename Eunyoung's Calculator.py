print("Welcome to Eunyonng's Calculator!\n")
print("Please slect and enter an operation:")
print("+\n""-\n""*\n" "/\n")
selection = input()
print("You selected " + selection + "\n")
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
print("")
if (selection == '+'):
  print (x, '+', y, '=', x+y)
elif (selection == '-'):
  print(x, '-', y, '=', x-y)
elif (selection == '*'):
  print(x, '*', y, '=', x*y)
elif (selection == '/'):
  print(x, '/', y, '=', x/y)
else:
  print('ERROR!')
print("")
print("Thank you for using Eunyoung's Calculator!")