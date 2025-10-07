canFlyInput=int(input("¿Puede volar? --> 0.No 1.Si "))
canFly=bool(canFlyInput)
isHumanInput = bool(int(input("¿Es humano? --> 0.No 1.Si ")))
print(isHumanInput)
hasMaskInput = int(input("¿Tiene máscara? --> 0.No 1.Si "))
hasMask = bool(hasMaskInput)




if canFly:
    if isHumanInput:
        if hasMask:
            print("Eres Ironman")
        else:
            print("Eres Capitán América")
    elif hasMask:
        
            print("Eres Ronan el Acusador")
    else:
        print("Eres Visión")

else:

    if isHumanInput:

        if hasMask:
            print("Eres Spiderman")
        else:
            print("Hulk")
    elif hasMask:
        print("Eres Black Bolt")
    else:
        print("Eres Thanos")
            

