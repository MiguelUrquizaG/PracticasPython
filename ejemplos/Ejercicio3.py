print("Hello! ")

'''
number = int(input("Please enter a number: "))

remainder =  number %2 

if remainder != 0:
    print("Your number is odd")
elif remainder ==0 and remainder%4 ==0:
    print("Your number is even and multiple of 4")
else:
    print("Your number is even")
'''
num = int(input("Introduzca el dividendo: "))
check = int(input("Introduzca el divisor: "))

if num%check == 0:
    print("División sin resto.")
else:
    print("División con resto.")