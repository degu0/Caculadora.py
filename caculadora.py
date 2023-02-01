import math
def calculator():
    def factorial(n):
        fat = 1
        while (n > 1):
            fat = fat * n
            n -= 1
        return fat

    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulo
    # for square root
    ! for factorial
    c for combinatorics
    ''')
    
    number_1 = int(input('Enter your first number: '))

    if operation != '!' and operation != '#':
        number_2 = int(input('Enter your second number: '))
   
    if operation == '+':
        #Addition
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        #Subtraction
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        #Multiplication
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        #Division
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '**':
        #Power
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 ** number_2)
    elif operation == '%':
        #Modulo
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 % number_2)
    elif operation == '#':
        #Square root
        print('#{} = '.format(number_1))
        print(math.sqrt(number_1))
    elif operation == '!':
        #Factorial
        print('{}! = '.format(number_1))
        print(factorial(number_1))
    elif operation.upper() == 'C':
        #Combinatorics
        print('{}! / {}! *'.format(number_1, number_2) + ' ({} - {})! = '.format(number_1, number_2))
        print (factorial(number_1) / (factorial(number_2) * factorial(number_1 - number_2)))
    else:
        print("You have not typed a valid operator, please run the  program again.")

    def again():
        cal_again = input ('''
    Do you want to calculate again?
    Please type Y for yes or N for No.
        ''')
        if cal_again.upper() == 'Y':
            calculator()
        elif cal_again.upper() == 'N':
            print('See you later.')

    again()
calculator()
