import math


def quad_solv(a, b, c):
    # discriminant

    D = (b**2)-(4*a*c) 

    # Nature of the roots

    if D < 0:
        print('\nThis Eq has no real roots\n')
    elif D == 0 :
        x = (-1*b)/(2*a)
        print(f'\nThis Eq has two real and equal roots : {x}, {x}')
    else :
        x1 = ((-1*b)-math.sqrt(D))/(2*a)
        x2 = ((-1*b)+math.sqrt(D))/(2*a)

        print(f'\nThis Eq has two real and distinct roots : {x1}, {x2}')


#inputs

print('\nax² + bx + c = 0')


while True : 
    try:
        a = int(input("\nEnter the Value of 'a' : "))
        b = int(input("\nEnter the Value of 'b' : "))
        c = int(input("\nEnter the Value of 'c' : "))
    except ValueError:
        print('\nEnter Only Numbers !!!')
    else:
        break

if a == 0:
    print("\n'a' Cannot be Zero !!!")
else:
    quad_solv(a, b, c)





        