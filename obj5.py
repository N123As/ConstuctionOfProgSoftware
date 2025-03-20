class Character:
    def __init__(self, name):
        self.name = name
        self.height = None
        self.body = None
        self.hair = None
        self.eyes = None
        self.clothes = None
        self.inventory = []
        self.actions = []
        self.intelligence = None
        self.army_size = None
        self.army_description = None
        self.faction = None
        self.allies = []
    
    def __str__(self):
        return (f"{self.name}\n"
                f"Height: {self.height}\n"
                f"Body: {self.body}\n"
                f"Hair: {self.hair}\n"
                f"Eyes: {self.eyes}\n"
                f"Clothes: {self.clothes}\n"
                f"Inventory: {', '.join(self.inventory)}\n"
                f"Actions: {', '.join(self.actions)}\n"
                f"Intelligence: {self.intelligence}\n"
                f"Faction: {self.faction}\n"
                f"Allies: {', '.join(self.allies)}\n"
                f"Army: {self.army_size} ({self.army_description})\n")

class Builder:
    def set_height(self,h): pass
    def set_body(self,b): pass
    def set_hair(self,h): pass
    def set_eyes(self,e): pass
    def set_clothes(self,c): pass
    def add_item(self,item): pass
    def add_action(self,act): pass
    def set_intelligence(self,iq): pass
    def set_army(self,size,desc): pass
    def set_faction(self,f): pass
    def add_ally(self,ally): pass
    def build(self): pass
#####################################################
class HeroBuilder(Builder):
    def __init__(self,name):
        self.character = Character(name)
    
    def set_height(self,h):
        self.character.height = h
        return self
    
    def set_body(self,b):
        self.character.body = b
        return self
    
    def set_hair(self,h):
        self.character.hair = h
        return self
    
    def set_eyes(self,e):
        self.character.eyes = e
        return self
    
    def set_clothes(self,c):
        self.character.clothes = c
        return self
    
    def add_item(self,item):
        self.character.inventory.append(item)
        return self
    
    def add_action(self,act):
        self.character.actions.append(act)
        return self
    
    def set_intelligence(self,iq):
        self.character.intelligence = iq
        return self
    
    def set_army(self,size, desc):
        self.character.army_size = size
        self.character.army_description = desc
        return self
    
    def set_faction(self,f):
        self.character.faction = f
        return self
    
    def add_ally(self,ally):
        self.character.allies.append(ally)
        return self
    
    def build(self):
        return self.character
#####################################################
class EnemyBuilder(HeroBuilder):
    def add_evil_action(self, act):
        self.character.actions.append("EVIL: " + act)
        return self

class GO:
    def create_hero(self,builder):
        return (builder.set_height("170cm")
                .set_body("Muscular")
                .set_hair("Black")
                .set_eyes("Brown")
                .set_clothes("Kind of military clothing")
                .add_item("Peace Aggrement, a Safety of Ukraine guarantee")
                .add_action("Saving Ukraine, finding new allies, peacemaking, plans of Belgorod occupation")
                .set_intelligence("High Intelligence")
                .set_army(300000, 
"Ukrainian Army are highly-trained units,they're capable of pulling off deadly sophisticated and synchronized battle tactics, which make ODKB look like a bunch of wimps in comparison.")
                .set_faction("UA")
                .add_ally("Poland")
                .add_ally("France")
                .add_ally("Germany")
                .add_ally("USA")
                .add_ally("GreatBritain")
                .build())
    
    def create_enemy(self,builder):
        return (builder.set_height("Less than 150cm")
                .set_body("Badly Damaged")
                .set_hair("Bald")
                .set_eyes("Blue")#actually idk, but who cares?
                .set_clothes("Terrible oversized suit")
                .add_item("Pills")
                .add_evil_action("Racketeering, extortion, fraud, money laundering, murder, robbery, war crime and occupation")
                .set_intelligence("Retard")
                .set_army(800000, 
"russian Army is a mentally disturbed gang, responsible for most of the wars that happen in the world. They're genuine, mentally unstable psychopaths, unclouded by remorse or delusions of morality, and will kill on a whim for fun or their own sick pleasure.")
                .set_faction("RU")
                .add_ally("Belarus")
                .add_ally("Iran")
                .add_ally("North Korea")
                .build())

if __name__ == "__main__":
    char = GO()
    hero = char.create_hero(HeroBuilder("Zelenskij"))
    enemy = char.create_enemy(EnemyBuilder("Putin"))#im sorry for capital leters here, i jsut must do it for design purposes
    
    print(hero)
    print(enemy)

