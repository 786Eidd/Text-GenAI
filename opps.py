# # Creating a class Name as mycls and which will give the statement
# class mycls:
#     print("Hello I am Class")

# # Calling the Class name as mycls
# mycls()


# # Create a class name as Car whos attributes are brend and model. Then create an instance of the class

# class Car:
#     # Intializing the attributes
#     def __init__(self,CarBrend, CarModel):
#         self.__brend = CarBrend
#         self.model = CarModel
#     # Creating Method to the full name of the Car
#     def fullName(self):
#         return f"{self.brend} {self.model}"
    
#     # Incapsulation of the Brend attribute
#     def get_brend(self):
#         return self.__brend + "This the Incapsulated Attribute"
# # creating the object of the Car by creating it's instence
# MyCar = Car("Toyota", "TS34")
# print(MyCar.brend)
# print(MyCar.model)

# # Accessing the fullname Method that display the full name of th Car
# print(MyCar.fullName())
# # Formating of output.
# print(f"The full name of the Car is: {MyCar.fullName()}")


# # Inheritence
# """Problem: Create an electricCar class that inherits from the Car Class and has an additional Attribute battery_size"""
# class ElectricCar(Car):
#     def __init__(self, Carbrend, CarModel, battery_siz):
#         super().__init__(Carbrend, CarModel)
#         self.battery_siz = battery_siz

# # Creating the object of the Electric which is inherited from the Car Class
# print("\n This the output of the inheritenc class")
# MyElectricCar = ElectricCar("Toyota", "TS34", "85kwh")
# print(MyElectricCar.model)
# print(MyElectricCar.brend)
# print(MyElectricCar.battery_siz)

# # Accessing the full name method by inheritence
# print(MyElectricCar.fullName())


"""# Incapsulation Output Goes here"""
class Car:
    # Intializing the attributes
    def __init__(self,CarBrend, CarModel):
        self.__brend = CarBrend
        self.model = CarModel
    # Creating Method to the full name of the Car
    def fullName(self):
        return f"{self.brend} {self.model}"
    
    # Incapsulation of the Brend attribute
    def get_brend(self):
        return self.__brend + "\tThis is Incapsulated Attribute"

MyCar = Car("Toyota", "TS34")
print("\nIncapsulation Output Goes here")
print(MyCar.get_brend())