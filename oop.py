myList = [1,2,3]
myList.append(4)
myList.count(2)

class Sample():
    pass

x = Sample()

print(type(x))

class Agent():
    planet = "Earth"
    def __init__(self, real_name, eye_color, height):
        self.real_name = real_name
        self.eye_color = eye_color
        self.height = height

x = Agent("Random", "Brown", "5'10")
print(x.real_name)
print(x.eye_color)
print(x.planet)

# class NameOfClass():

#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2