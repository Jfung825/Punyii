class NPC:
    def __init__(self,name ,hp,mana):
        self.name = name
        self.hp = hp
        self.mana = mana
    
    def describe(self):
        print(f"Name {self.name}",end=" ")
        print(f"HP {self.hp}",end=" ")
        print(f"Mana {self.mana}",end=" \n")

    def damage(self,damage):
        if self.mana <= 0:
            print("Not enough mana")
            return
        self.hp -= damage
        self.mana -= damage
        print(f"{self.name} HP got -{damage}")
    


n1 = NPC("A",100,100)
n2 = NPC("B",500,200)
n3 = NPC("C",1000,1000)

n1.describe()
n2.describe()
n3.describe()