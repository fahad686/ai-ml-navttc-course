from operator import contains
from random import choice

from calculator_package.addition import adding
from calculator_package.division import dividing
from calculator_package.modulus import modulusing
from calculator_package.multiplication import multiplying
from calculator_package.squareroot_of import square_rooting
from calculator_package.subtraction import subtract

print("----------- W E L C O M  A I --------------")


#taking user input
number_1=int(input('Enter your first number?'))
number_2=int(input('Enter your second number?'))

# taking operator
operator=input('Enter operator:(+,*,-,/,%,**)')
operator=operator.strip() #remove extra space from side of operator

while True:
    match operator:
        case '+':
            result = str(adding(number_1, number_2))
        case '-':
            result = subtract(number_1, number_2)
        case '*':
            result = multiplying(number_1, number_2)
        case '/':
            result = dividing(number_1, number_2)
        case '%':
            result = modulusing(number_1, number_2)
        case '**':
            result = square_rooting(number_1, number_2)
        case _:
            result = "Enter wrong operator"
    print( f'Result is {result}')

    choice=input('Do you want to quit? yes/no : ')
    if choice =='no' or choice =='n':
        continue
    elif choice=='yes' or choice =='y':
        break


