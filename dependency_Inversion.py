#acheiving dependency inversion principle
#we implement more devices on one switch
class Switch:  
    def __init__(self, device):
        self.device = device
        
class KeyStatus(Switch):

    def turn_on(self):
        print(f"{self.device} is Switched on")
    def turn_off(self):
        print(f"{self.device} is Switched off")
        
        
device1 = KeyStatus("television")
device1.turn_on()
device1.turn_off()
device1.turn_on()

print('-----------------')

device2 = KeyStatus("fan")
device2.turn_on()
device2.turn_off()
device2.turn_on()

print('-----------------')

device3 = KeyStatus("electric lamp")
device3.turn_on()
device3.turn_off()
device3.turn_on()






