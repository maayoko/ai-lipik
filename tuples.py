# %% 1
tuple1 = ("Ivan", 33, True, None, [1, 2, 3])
tuple2 = tuple("Ivan")
tuple3 = tuple([1, 2, 3])
print(tuple2)
print(tuple3)
tuple4 = ("Ivan",)
print(tuple4)

# %% 2
tuple1 = (10, 20, 30, 40, 50, 60)
a, b, c, d, e, f = tuple1
print(a, b, c, d, e, f)

# %% 3
tuple1 = (10, 20, 30, 40, 50, 60)
a, b, *c = tuple1
print(a, b, c)

a, *b = tuple1
print(a, b)

a, *b, c = tuple1
print(a, b, c)

# %% 4
tuple1 = (10, 20, 30, 40, 50, 60)
tuple2 = (*tuple1, 70, 80, 90)
print(tuple2)

tuple3 = tuple1 + (70, 80, 90)
print(tuple3)
# %% 5
tuple1 = (10, 20, 30, 40, 50, 60)
print(tuple1[0])
print(tuple1[-1])
print(tuple1[2:-2])

for number in tuple1:
    print(number, end=" ")
print()
print(len(tuple1))
# %% 6
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
tuple1[1][1] = 333
print(tuple1)
# %% 7
names = ("marko", "ivan", "pero", "marko", "marko",
         "marko", "nikola", "ivan", "ivan")

input_name = input("Unesite ime: ")
matched_names = [name for name in names if name == input_name.lower()]
print(f"{input_name} se ponavlja u tuple-u {len(matched_names)} puta")

# %% 8
names = ("marko", "ivan", "pero", "marko", "marko",
         "marko", "nikola", "ivan", "ivan")
print(tuple(set(names)))

# %% 9
numbers = (1, 5, 3, 4, 2)
quadratic_numbers = [i ** 2 for i in numbers]
sorted_quadratic_numbers = sorted(quadratic_numbers)
print(sorted_quadratic_numbers)
print(sorted_quadratic_numbers[::-1])
# %% 10
brojevi = [17, 27, 37]
slova = ['d', 'f', 'g']

for num, letter in zip(brojevi, slova):
    print(num, letter)

# %%
