class Switch:
    def __init__(self, device):
        self.device = device


class KeyStatus(Switch):
    def turn_on(self, device):
      print(f" {device}  is Switched on")
    def turn_off(self, device):
        print(f" {device} Switched off")
        
        
obj=Switch("television")
obj.turn_on()