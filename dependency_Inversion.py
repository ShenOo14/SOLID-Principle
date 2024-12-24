
class KeyStatus:
    def __init__(self, device):
        self.device = device
       
    def turn_on(self):
        print(f"{self.device} is Switched on")
    def turn_off(self):
        print(f"{self.device} is Switched off")
        
        
device1 = KeyStatus("television")
device1.turn_on()
device1.turn_off()

print('-----------------')
device2 = KeyStatus("fan")
device2.turn_on()
device2.turn_off()
device2.turn_on()





