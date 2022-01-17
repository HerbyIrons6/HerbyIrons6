


print("Welcome to my calculator!")

while True:
    s = input("Please select the action you want to apply: +,-,*,/: ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input(""))
        y = float(input(""))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Division by zero!")
    else:
        print("Error!")
        break

print("Thanks for using.  ")
