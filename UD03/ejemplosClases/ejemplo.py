class StarWarsDroud:
    def switch_on(self):
        self.power_on = True
        print("Hi! I'm a droid.")
    def switch_off(self):
        self.power_on = False
        print("I'm turned off.")

c3po = StarWarsDroud()

c3po.switch_on()
print(c3po.power_on)

#print(type(c3po))

class Droid:
 def __init__(self,name:str):
    self.name =name
 

prueba = Droid()

#print(prueba.name)