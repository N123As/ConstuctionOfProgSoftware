class animal:   
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age
    def __str__(self):
        return f"{self.species} {self.name},{self.age} років"


class env:  
    def __init__(self,env_type,size):
        self.env_type = env_type
        self.size = size
        self.animals = []
    def add_animal(self,animal):
        self.animals.append(animal)
    def __str__(self):
        return f"{self.env_type}(Розмір: {self.size} м^2,Тварини: {len(self.animals)})"


class food: 
    def __init__(self,food_type,quantity):
        self.food_type = food_type
        self.quantity = quantity
    def __str__(self):
        return f"{self.food_type} -{self.quantity} кг"


class worker:   
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def __str__(self):
        return f"{self.position}: {self.name}"


class Zoo:  
    def __init__(self):
        self.envs = []
        self.food_inventory = []
        self.workers = []
    def add_env(self,env):
        self.envs.append(env)
    def add_food(self,food):
        self.food_inventory.append(food)
    def add_worker(self,worker):
        self.workers.append(worker)
    
    
    
    def inventory(self):    
        print("--| Інвентаризація Зоопарку |--")
        print("Вольєри:")
        for env in self.envs:
            print(f" - {env}")
            for animal in env.animals:
                print(f"   * {animal}")
        print("\nЗапаси їжі:")
        
        for food in self.food_inventory:
            print(f" - {food}")
        print("\nПрацівники:")
        
        for worker in self.workers:
            print(f" - {worker}")


def main():#завдання 2 ( щоб при запуску програми виводилась інфа на екрасн)
    zoo =Zoo()  
    
    env1 = env("Савана", 200)
    env1.add_animal(animal("Лео"," Лев", 5))
    env1.add_animal(animal("Житомир"," Жираф",  7))
    
    zoo.add_env(env1)
    zoo.add_food(food("М'ясо", 50))
    zoo.add_food(food("Сіно", 100))
    zoo.add_worker(worker("Іван", "Доглядач"))
    zoo.add_worker(worker("Марія", "Ветеринар"))
    
    zoo.inventory()



#перевірка (завадання 2)
if __name__ == "__main__":
    main()


