# Object oriented programming(OOP)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Started engine")

    def stop_engine(self):
        print("Engine stopped")

my_car =Car("Tesla","modelxx","2019")
my_car.start_engine()
my_car.stop_engine()
print(my_car.make)
print(my_car.model)
print(my_car.year)

print("================================================================")

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
            self.account_number = account_number
            self.balance = initial_balance
    def deposit(self, amount):
         self.balance += amount
         print(self.balance)
    def withdraw(self, amount):
        if amount < self.balance:
           self.balance -= amount 
           print(self.balance)
        else:
             print("Insufficient funds")
       

bill_account= BankAccount("100" , 450)
bill_account.deposit(100)
bill_account.withdraw(50)


#Exercise1
#calculate the area and circumfrence of a circle
print("================================================================")
class Circle:
       
       def __init__(self, radius):
              self.radius = radius
       
       def calculate_area(self):
              return 3.14*self.radius
       def calculate_circumference(self):
              return 2*3.14*self.radius
my_circle= Circle(7)
print(my_circle.calculate_area())

#Exercise2
# calculate and display employee bonuses(15%) of salary (employee1: 150000, employee2: 230000)
print("================================================================")
class Employee:
       
       def __init__(self, name, salary):
              self.name = name
              self.salary=salary
       def display(self):
              return self.salary
       def calculate_bonuses(self):
              return 15/100*self.salary

employee1 = Employee("employee1", 15000)
employee2 = Employee("employee2", 20000)
employee1.calculate_bonuses()
print(employee1.name)
print(employee1.calculate_bonuses())
print(employee2.name)
print(employee2.calculate_bonuses())
      
#Exercise 3 convert temperature(37) from celcius to fahrenheit
print("================================================================")
class Temperature:
    def __init__(self, temperature):
        self._temperature = temperature

    def _convert_to_fahrenheit(self):
        temperature_fahrenheit = (9/5) * self._temperature + 32
        return temperature_fahrenheit

    def display_temperature(self):
        print(f"Temperature in degrees Celsius: {self._temperature}")
        print(f"Temperature in degrees Fahrenheit: {self._convert_to_fahrenheit()}")


my_temperature = Temperature(37)
my_temperature.display_temperature()

print("================================================================")

#Exercise 4
# Show encapsulation with employee information to give a pay increment(salary with employee information with new salary) e.g 850000 to 1000000

class Employeex:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def increment_pay(self, increment_amount):
        if increment_amount > 0:
            self._salary += increment_amount

employee = Employeex("Cheptoyek Bill", 850000)
print(f"Employee Name: {employee.get_name()}")
print(f"Salary: {employee.get_salary()}")

employee.increment_pay(150000)
print(f"New Salary: {employee.get_salary()}")
