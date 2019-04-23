x = 1
while x <=3:
    print(x)
    x = x +1
    print(x)

input("Please input a number: ")

passcode = 0

while passcode != 123:
    passcode = int(input("Please provide a passcode."))

    if passcode != 123:
        print("Wrong passcode.")