
number1 = float(input('enter first number: '))
sin = input('enter sin: ')
number2 = float(input('enter second number: '))

if sin == '+':
    print(number1+number2)
elif sin == '-':
    print(number1-number2)
elif sin == '*':
    print(number1*number2)
elif sin == '/':
    print(number1/number2)
else:
    print('invalit')
