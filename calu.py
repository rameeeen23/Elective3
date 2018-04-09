# menu() function prints the main menu, and prompts for a choice
def menu():
    #Operations
    print "Welcome to my Calculator in Python"
    print "Your options are:"
    print " "
    print "1.) Addition"
    print "2.) Subtraction"
    print "3.) Multiplication"
    print "4.) Division"
    print "5.) Quit calculator"
    print " "
    return input ("Please choose your option: ")

# Addition
def add(a,b):
    print a, "+", b, "=", a + b

# Subtraction
def sub(a,b):
    print a, "-", b, "=", a - b

# Multiplication
def mul(a,b):
    print a, "*", b, "=", a * b

# Division
def div(a,b):
    print a, "/", b, "=", a / b

# Run
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Enter first addend: "),input("Enter Second addend: "))
    elif choice == 2:
        sub(input("Enter the minuend: "),input("Enter the subtrahend: "))
    elif choice == 3:
        mul(input("Enter the multiplier: "),input("Enter the multiplicand: "))
    elif choice == 4:
        div(input("Enter the dividend: "),input("Enter the divisor: "))
    elif choice == 5:
        loop = 0

print "Thank you for using my calculator! \n Arigatou Gozaimasu"

# End
