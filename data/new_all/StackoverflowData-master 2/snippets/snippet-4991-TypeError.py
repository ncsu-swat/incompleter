#Source: https://stackoverflow.com/questions/30675805/python-3-x-error-with-methods-asking-for-input-error-is-typeerror-init-ta
# Create class for Pet

class Pet:
    __name = ""
    __species = ""
    __age = ""

    # Object constructor
    def __init__():
        self.__name = name
        self.__species = species
        self.__age = age

    #Methods    
    def setName(self):
        self.__name =input("What is your pet's name?\n")

    def setSpecies(self, species):
        self.__species=input("What type of pet is it?\n")

    def setAge(self, age):
        self.__age=input("How old is your pet?\n")

    def getName(self):
        return self.__name

    def getSpecies(self):
        return self.__species

    def getAge(self):
        return self.__age

    def get_type(self):
        print("Pet")

    def toString(self):
        return"{} is a {} and is {} years old".format(self.__name,self.__species,self.__age)

#name=input("What is your pet's name?\n")
#species=input("What type of pet is it?\n")
#age=input("How old is your pet?\n")

myPet=Pet()
myPet.setName()

#myPet=Pet(name,species,age)
print(myPet.toString())