class SecurityForce:
    def plan(self):
        print("Parent Plan")
    def attack(self):
        print("Parent attack")
class Armyforce(SecurityForce):
    def plan(self):
        print("Army Force Plan")
    def attack(self):
        print("Army Force attack")
class Navyforce(SecurityForce):
    def plan(self):
        print("Navy Force Plan")
    def attack(self):
        print("Navy Force attack")
class Airforce(SecurityForce):
    def plan(self):
        print("Air Force Plan")
    def attack(self):
        print("Air Force attack")
af=Armyforce()
af.plan()
af.attack()
nf=Navyforce()
nf.plan()
nf.attack()
ai=Airforce()
ai.plan()
ai.attack()
        
              
