class Animal:
    
    def __init__(self, legs, name="Animal"):
            self.name = name # self - reference to the object
            self.legs = legs
            
    def voice(self):
        print(f"{self.name} is doing a voice")
    
    def jump(self):
        if self.legs == 0:
            print(F'{self.name} jumps with {self.legs} legs')

obj1 = Animal(legs=4, name='Dog')
obj1.voice()

obj2 = Animal(legs=4, name='Zebra')
obj2.voice()

obj3 = Animal(legs=0, name='Snake')
obj3.jump()
            