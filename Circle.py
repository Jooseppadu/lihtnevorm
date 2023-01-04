from math import pi  # impordi ja klassi vahel peab olema kaks rida


class Circle:

    def __init__(self, radius): # konstruktor
        """ Loo klass koos raadiusega """
       # print('Object created')
        self.radius = radius


    def get_radius(self):
       # print('Return radius')
        return self.radius

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        # pi * pow(self.radius, 2) # import pow
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius