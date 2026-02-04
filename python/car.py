class Car:
  def __init__(self, make, model, year):
     self.make = make
     self.model = model
     self.year = year
     self.odometer_reading = 0
     
# when a methode s called by specific instance or object use self
  def get_descriptive_name(self):

     long_name =f"{self.year} {self.make} {self.model} "  
     return long_name.title()
  
  def update_odometer(self, mileage):
     self.odometer_reading = mileage
  

  def increment_odometer(self, miles):
       self.odometer_reading += miles


  def read_odometer(self):
     print(f"This car has {self.odometer_reading} miles on it.")



class ElectricCar(Car):


   def __init__(self, make, model, year):
      super().__init__(make, model, year)
      self.battery_size= 75
   

   def describe_battery(self):
      print(f"This car has a {self.battery_size}-KWH battery")


my_tesla = ElectricCar('tesla' , 'model' , 2019)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(34)
my_tesla.describe_battery()
