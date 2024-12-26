#violating liskov substitution principle
class Bird:
    def __init__(self, eat):
        self.eat = eat

    def fly(self):
        raise NotImplementedError("This bird can't fly")
    
    
#acchieving liskov substitution principle 
class Bird:
    def __init__(self,eat):
        self.eat = eat
       

class flyableBird(Bird):
    def __init__(self,eat):
        super().__init__(eat)
    def fly(self):
        print("I can fly")
        
pigeon = flyableBird("bread")
print(pigeon.eat)
pigeon.fly()

print("-" *30)

penguin = Bird("fish")
print(penguin.eat)
print("-" *30)
ta3er = flyableBird("akl")
print(ta3er.eat)
ta3er.fly()
