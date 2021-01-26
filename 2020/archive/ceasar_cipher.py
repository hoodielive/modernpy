alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in = input("Enter your cipher text: ")

for shift in range(26):
    n = len(str_in)
    str_out = ""

    for i in range(n):
        c = str_in[i]
        loc = alpha.find(c)
        new_loc = (loc + shift) % 26
        str_out += alpha[new_loc]

    print(shift, str_out)
