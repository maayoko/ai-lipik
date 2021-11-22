# %% 1
import math
num1 = 3
num2 = 4

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 >= num2)

# %% 2
bool1 = True
bool2 = False

print(bool1 and bool2)
print(bool1 or bool2)
print(not bool2)

# %% 4
a = 23
b = 45

a_ = int(str(a)[0] + str(b)[-1])
b_ = int(str(b)[0] + str(a)[-1])
print(a_, b_)
# %% 5
numbers = [int(input("Unesite broj: ")) for x in range(8)]


def calculate_something(a, b, c, d, e, f, g, h):
    return a + b / c * d**e // f - g % h


print(calculate_something(*numbers))
# %% 6
random_number = int(input("Unesi broj: "))
if (random_number > 101):
    print("Unesite broj između 0 i 101")
else:
    numbers = [x for x in range(random_number)]
    average = sum(numbers) / len(numbers)
    radius = (2*math.pi) / random_number

    print(average)
    print(radius)

# %% 7
