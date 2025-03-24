import PartA


class Pet:

    def set_name(self, name):
        self.name= name
    def set_age(self, age):
            self.age = age
    def set_sex(self,sex):
            self.sex= sex
    def set_petId(self,petId):
        self.petId = petId
    def set_ownerName(self,ownerName):
            self.ownerName = ownerName
    def __init__(self, name, age, sex, petId, ownersName):
        self.set_name(name)
        self.set_age(age)
        self.set_sex(sex)
        self.set_petId(petId)
        self.set_ownerName(ownersName)
    def pet_details(self):
        print("Name of pet is ", self.name)
        print("Age of pet is",self.age)
        print("sex of pet is ",self.sex)
        print("petId of pet is ",self.petId)
        print("ownerName of pet is ",self.ownerName)
#methods to print all initialisation attributes#
p1= Pet('Samantha', 3, 'Female', 1234, 'John')
p2= Pet( 'Tabatha',  6, 'Male',  5678, 'Jane')
p1.pet_details()
p2.pet_details()


def show_meow():
    print("Meow")


class Cat (Pet):
    def show_meow(self):
        print("Meow")

        c1 = Cat("Samantha", 3, "Female", 1234, "John")
        c1.show_meow()
        c2 = Cat("Tabatha", 6, "Male", 5678, "Jane")
        c2.show_meow()






# User-defined classes such as `Pet` can now use the overridden `__build_class__`
