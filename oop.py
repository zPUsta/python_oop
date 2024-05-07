class HR():
    sinif = "people"
    
    def __init__(self, name, surname, id, position):
        self.name = name
        self.surname = surname
        self.id = id
        self.position = position
        
    def senior(self, senior=False):
        if senior == True:
            return f"{self.name} senior"
        else:
            return f"{self.name} junior"

person1 = HR("Püstə", "Zeynalova", 1001, "Full-stack developer")
person2 = HR("Sevinc", "Əsədova", 1002, "Full-stack developer")

print(f"{person1.name} adlı işçinin idsi {person1.id}-dir və soyadı {person1.surname}-dır")

print(person1.senior(senior=False))

