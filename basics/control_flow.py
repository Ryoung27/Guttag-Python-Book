if 1 < 2:
    print("This is true")
else:
    print("WHAT!")

if 1 == 2:
    print("Woah")
elif 1 == 1:
    print("One is equal to one.")
else:
    print("Everything is normal.")

if 2 == 0:
    print("first condition true")
elif 2 == 1:
    print("second condition true")
elif 2 == 2:
    print("third condition true")
else:
    print('nothing true')

access_code = 12345
access = False

if access_code == 12345:
    print("CODE RESET")
    print("Call a supervisor")
elif access_code == 231912:
    print("Welcome")
    access = True
else:
    print("Sorry no matching code.")

if access == True:
    print("Access Granted")
else:
    print("Access Denied")