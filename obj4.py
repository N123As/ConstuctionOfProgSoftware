import copy

class Virus:
    def __init__(self, name, typ, weight, age, children=None):
        self.name = name#Naming
        self.typ = typ#Variant
        self.wgt = weight#Weight
        self.age = age#Age
        self.children = children if children else[]
    
    def clone(self):
        return copy.deepcopy(self)
    def add_child(self, child):
        self.children.append(child)
    def __str__(self):
        return f"{self.name} ({self.typ}),age: {self.age},weight: {self.wgt} mg, {len(self.children)} children"

if __name__ == "__main__":
    v1 = Virus("CoronaVirus 2019 ALPHA","Alpha", 5, 1)
    v2 = Virus("CoronaVirus 2020","Beta", 4, 1)
    v3 = Virus("CoronaVirus 2022","Gamma", 6, 2, [v1,v2])
    v4 = Virus("CoronaVirus 2025 THE REMAKE","Zero", 7, 3,[v3])
    
    # клонування вірусу parent з усіма children
    v4_clone = v4.clone()
    
    print(v4)
    print(v4_clone)
