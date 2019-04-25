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


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def perimeter(self):
        return 2 * self.radius * Circle.pi

    def report_something(self,name):
        return 'Report {}'.format(name)

mycircle = Circle()

mycircle.radius
print(mycircle.area())

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def report(self):
        print("I am {} {}".format(self.first_name, self.last_name))


# p.hello()

class Agent(Person):

    def __init__(self, first_name, last_name, code_name):

        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

x = Agent(first_name='Alan', last_name='Turing', code_name='Hero')

# x.hello()

# class NameOfClass():

#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2