# inheritance
class Animal:
    def __init__(self, name):
        self.name = name


    def eat(self):
        print(f"{self.name} +  is eating..")


class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def miow(self):
        print("Cat meows")

my_Dog =Dog("Tyson")
my_Dog.bark()

my_Cat =Cat("Siri")
my_Cat.miow()


# Demonstrate using inheritance to calculate area and perimeter of circle and rectangle
# circle
class Circle:
  def __init__(self, radius):
    self.radius = radius  
  def area(self):
        return 3.14*self.radius*self.radius
  def perimeter(self):
        return 2*3.14*self.radius*self.radius
    
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
      
my_circle = Circle(12)
print(my_circle.area())
print(my_circle.perimeter())

my_rectangle= rectangle(3,2)
print(my_rectangle.area())
print(my_rectangle.perimeter())


# multiple inheritence
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")

class Flyable:
    def fly(self):
        print("Flying.")

class Bird(Animal, Flyable):
    def __init__(self, name):
        super().__init__(name)

bird = Bird("Sparrow")
bird.eat()  # Output: Sparrow is eating.
bird.fly()  # Output: Flying.



# polymorphism

# method over loading
class MyClass:
    def my_method(self, *args):
        if len(args) == 1:
            # Handle case with one argument
            print(f"Received one argument: {args[0]}")
        elif len(args) == 2:
            # Handle case with two arguments
            print(f"Received two arguments: {args[0]}, {args[1]}")

obj = MyClass()
obj.my_method(10)           # Output: Received one argument: 10
obj.my_method(20, 30)       # Output: Received two arguments: 20, 30


# abstraction

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Sedan(Car):
    def start(self):
        print(f"{self.brand} {self.model} started.")

    def stop(self):
        print(f"{self.brand} {self.model} stopped.")

class SUV(Car):
    def start(self):
        print(f"{self.brand} {self.model} started.")

    def stop(self):
        print(f"{self.brand} {self.model} stopped.")

sedan = Sedan("Toyota", "Camry")
sedan.start()  # Output: Toyota Camry started.
sedan.stop()   # Output: Toyota Camry stopped.

suv = SUV("Ford", "Explorer")
suv.start()    # Output: Ford Explorer started.
suv.stop()     # Output: Ford Explorer stopped.


import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and print the areas
print("Area of the circle:", circle.calculate_area())         # Output: Area of the circle: 78.53981633974483
print("Area of the rectangle:", rectangle.calculate_area())   # Output: Area of the rectangle: 24



#Assignement 1
# create a reciept printing program with GUI interface
#a more advanced earns you more points
import tkinter as tk

class ReceiptApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Receipt Printing Program")

        # Create input fields
        self.label_item = tk.Label(self, text="Item:")
        self.label_item.pack()
        self.entry_item = tk.Entry(self)
        self.entry_item.pack()

        self.label_price = tk.Label(self, text="Price:")
        self.label_price.pack()
        self.entry_price = tk.Entry(self)
        self.entry_price.pack()

        # Create button for adding items
        self.add_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_button.pack()

        # Create text widget for displaying the receipt
        self.receipt_text = tk.Text(self, height=10, width=50)
        self.receipt_text.pack()

    def add_item(self):
        item = self.entry_item.get()
        price = self.entry_price.get()

        if item and price:
            self.receipt_text.insert(tk.END, f"Item: {item}, Price: {price}\n")
            self.entry_item.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)

# Create an instance of the ReceiptApp and run the main event loop
app = ReceiptApp()
app.mainloop()
