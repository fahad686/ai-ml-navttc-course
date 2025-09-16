from  operations import addition
from  operations import multiplication
from  operations import division
from  operations import  subtraction

def calculator():
    while True:
        num_1=input('Enter first number: ')
        num_2=input('Enter second number: ')
        #now check coming numbers are digits are not if not then restart
        # Validate numbers
        if not num_1.replace('.', '', 1).isdigit() or not num_2.replace('.', '', 1).isdigit():
            print("Error: Please enter valid numbers.\n")
            continue  # Restart loop
        print(f"you putt correct numbers,{num_1} and {num_2}")
        ##convert string to float
        operand_1=float(num_1)
        operand_2=float(num_2)

        ##ask for expression like operator
        operator=input('Enter operation (+, /, *, -):')

        match operator:
            case '+':
                print(f'Addition: {addition.adding(operand_1,operand_2)}')
            case '-':
                print(f'Subtract: {subtraction.subtract_func(operand_1,operand_2)}')
            case '/':
                print(f'Division: {division.dividing(operand_1,operand_2)}')
            case '*':
                print(f'Multiplication: {multiplication.multiple(operand_1,operand_2)}')
            case _:
                print(f'Unsupported operation provided: {operator}')
                continue

        ### Here we define our yes/ no condition
        choice=input("Do you want to quit? (yes/no)")
        if choice =='yes' or choice=='YES' or choice =='y':
            print('Thanks for using . Good bey!')
            continue
        elif choice == 'no' or choice =='n' or choice =='No':
            print('Calculator Restarting....')




