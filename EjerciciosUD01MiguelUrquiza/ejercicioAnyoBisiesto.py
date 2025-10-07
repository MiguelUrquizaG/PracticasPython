anyo = int(input("Introduzca el año: "))

if (anyo%4 ==0 and anyo%100!=0) or anyo%400==0:
    print("EL año es bisiesto.")
else:
    print("El año no es bisiesto.")