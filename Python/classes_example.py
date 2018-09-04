# class Dog():

#     spiecies = 'mammal'

#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name

# sam = Dog('Huskie', 'Sammy')
# new_dog = Dog('Golden', 'Cindy')

# print(sam.breed)
# print(sam.name)
# print(sam.spiecies)


class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

mycircle = Circle(10)
print(mycircle.radius)
print(mycircle.area())