# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __eq__(self, other):
#         return self.radius == other.radius

#     def __lt__(self, other):
#         return self.circumference() < other.circumference()

#     def __le__(self, other):
#         return self.circumference() <= other.circumference()

#     def __gt__(self, other):
#         return self.circumference() > other.circumference()

#     def __ge__(self, other):
#         return self.circumference() >= other.circumference()

#     def __add__(self, value):
#         return Circle(self.radius + value)

#     def __sub__(self, value):
#         return Circle(self.radius - value)

#     def circumference(self):
#         return 2 * math.pi * self.radius

#     def __repr__(self):
#         return f"Circle(radius={self.radius})"



# circle1 = Circle(15)
# circle2 = Circle(10)

# print(circle1 == circle2)  
# print(circle1 < circle2)   
# print(circle1 > circle2)  







# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)

#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)

#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.real * other.imag + self.imag * other.real
#         return Complex(real_part, imag_part)

#     def __truediv__(self, other):
#         denom = other.real + other.imag
#         real_part = (self.real * other.real + self.imag * other.imag) / denom
#         imag_part = (self.imag * other.real - self.real * other.imag) / denom
#         return Complex(real_part, imag_part)

#     def __repr__(self):
#         return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"


# n1 = Complex(1, 2)
# n2 = Complex(1, 7)

# print(f"c1: {n1}")
# print(f"c2: {n2}")
# print(f"Сложение: {n1 + n2}")  
# print(f"Вычитание: {n1 - n2}") 
# print(f"Умножение: {n1 * n2}")    
# print(f"Деление: {n1 / n2}")   





# class Airplane:
#     def __init__(self, model, max_passengers, current_passengers=0):
#         self.model = model
#         self.max_passengers = max_passengers
#         self.current_passengers = current_passengers

#     def __eq__(self, other):
#         return self.model == other.model

#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers

#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers

#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers

#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers


#     def __add__(self, passengers):
#         if isinstance(passengers, int):
#             new_passengers = self.current_passengers + passengers
#             if new_passengers <= self.max_passengers:
#                 return Airplane(self.model, self.max_passengers, new_passengers)
#             else:
#                 raise ValueError("Слишком иного пассажмров")

#     def __sub__(self, passengers):
#         if isinstance(passengers, int):
#             new_passengers = self.current_passengers - passengers
#             if new_passengers >= 0:
#                 return Airplane(self.model, self.max_passengers, new_passengers)
#             else:
#                 raise ValueError("Число пасажиров не может быть отрицательным")

#     def __iadd__(self, passengers):
#         if isinstance(passengers, int):
#             if self.current_passengers + passengers <= self.max_passengers:
#                 self.current_passengers += passengers
#                 return self
#             else:
#                 raise ValueError("Too many passengers")

#     def __isub__(self, passengers):
#         if isinstance(passengers, int):
#             if self.current_passengers - passengers >= 0:
#                 self.current_passengers -= passengers
#                 return self
#             else:
#                 raise ValueError("Number of passengers cannot be negative")

#     def __repr__(self):
#         return (f"Airplane({self.model}, max_passengers={self.max_passengers}, "
#                 f"current_passengers={self.current_passengers})")



# plane1 = Airplane("Boeing 737", 200, 150)
# plane2 = Airplane("Airbus A320", 180, 100)

# print(plane1 == plane2) 
# plane3 = Airplane("Boeing 737", 200, 150)
# print(plane1 == plane3)
# print(plane1 > plane2)
# print(plane1 < plane2)  
# plane1 += 30
# print(plane1)
# plane2 -= 50
# print(plane2)            






# class Flat:
#     def __init__(self, square, price):
#         self.square = square
#         self.price = price

#     def __eq__(self, other):
#         return self.square == other.square
        
#     def __ne__(self, other):
#         return self.square != other.square

#     def __lt__(self, other):
#         return self.price < other.price

#     def __le__(self, other):
#         return self.price <= other.price

#     def __gt__(self, other):
#         return self.price > other.price

#     def __ge__(self, other):
#         return self.price >= other.price
        

# flat1 = Flat(20, 1000)
# flat2 = Flat(19, 1500)
# print(flat1 == flat2)
# print(flat1 != flat2)
# print(flat1 <= flat2)
# print(flat1 >= flat2)
# print(flat1 < flat2)
# print(flat1 > flat2)