
class Animal(object):
    # weight
    # color

    def __init__(self,weight=None, color=None):
        print("Initializing...")
        self.weight = weight
        self.color = color

    def __str__(self):
        return "Animal( weight: {}, color: {})".format(self.weight, self.color)

class Mammal(Animal):
    def __init__(self, weight = None, color = None, furry = None):
        super().__init__(weight, color)
        self.furry = furry


    def __str__(self):
        return "Mammal({}, {})".format(self.weight,self.furry)


print("Creating animal")
a = Mammal(30,"red","full")
print(a, a.weight)
b = Animal(40)
print(b)
a.wheels = 24
print (a.wheels)
