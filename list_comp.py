# my_list = []

s = 'Some string'

for letter in s:
    my_list.append(letter)

my_list = [letter for letter in s]

squares = [x**2 for x in range(0,11)]