def check_ten_sum(n1, n2):
    if n1 + n2 == 10:
        return True
    else:
        print(n1 + n2)

check_ten_sum(1, 9)
check_ten_sum(8, 4)

def upper_case(x):
    answer = x[0].upper()
    print(answer)

upper_case("test")
upper_case("worked")

def last_two(y):
    answer = y[-1:-2]
    print(answer)

last_two("test")
last_two("worked")