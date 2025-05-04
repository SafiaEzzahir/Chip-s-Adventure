print("\n  ~~ let me convert those colours for you ~~\n\n")
hex = input("  ~~ hex code pls? ~~ \n\n")
print("")

#letters = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

chars = list([*hex])
chars.pop(0)
digits = []

for index in range(0, 5, 2):
    digit = chars[index] + chars[index+1]

    digit = int(digit, 16)
    print(digit)

    digit = int(digit)/255
    digits.append(str(round(digit, 3)))

print(", ".join(digits)+ ', 1\n')