# WHILE LOOP

# %% 10 b
x = 5
max_loops = x
upper_part = x // 2 + 1
stars = 1
upper_spaces = x // 2
lower_spaces = 1

while x != 0:
    is_upper_part = x >= upper_part
    if (is_upper_part):
        print(upper_spaces * " ", end="")
        print(stars * "*")
        if max_loops != stars:
            stars += 2
        upper_spaces -= 1
    else:
        stars -= 2
        print(lower_spaces * " ", end="")
        print(stars * "*")
        lower_spaces += 1

    x -= 1


# %% c
binary = "1010101"
spaces = 0

while len(binary) > 0:
    print(spaces * " ", end="")
    print(binary)
    spaces += 1
    binary = binary[0:-2]

# %%
