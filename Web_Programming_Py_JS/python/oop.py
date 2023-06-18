import sys
try:
    x=int(input('Enter x: '))
    y=int(input('Enter y: '))
    result=x/y
except ValueError:
    print('You can`t enter non integer value!')
    sys.exit(1)
except ZeroDivisionError:
    print('You can`t divide to zero!')
    sys.exit(1)
print(f'x/y: {x/y}')