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
class BattleField:
    def safety(self,sf):
        sf.plan()
        sf.attack()
def main():
 b=BattleField()
 af=Armyforce()
 nf=Navyforce()
 ai=Airforce()
 b.safety(af)#b.safety(Armyforce())
 b.safety(nf)#b.safety(Navyforce())
 b.safety(ai)#b.safety(Airforce())
main()
        
              
