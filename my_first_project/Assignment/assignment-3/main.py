from  operations import addition,subtraction,multiplication,division

def calculator():
    while True:
        num_1=input('Enter first number: ')
        num_2=input('Enter second number: ')
        #now check coming numbers are digits are not if not then restart
        if not num_1.replace('.','',1).isdigit() and not num_2.replace('.','',1):
            print('Please Enter correct numbers')
            continue # Restart our program




