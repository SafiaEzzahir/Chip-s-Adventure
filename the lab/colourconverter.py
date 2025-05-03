print("\n  ~~ let me convert those colours for you ~~\n\n")
hex = input("  ~~ hex code pls? ~~ \n\n")
print("")

letters = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

chars = list([*hex])
chars.pop(0)
digits = []

for index in range(0, 5, 2):
    digit = 0

    if chars[index].isnumeric():
        digit += int(chars[index])*16
    else:
        digit += letters.get(chars[index].upper())*16
    
    if chars[index+1].isnumeric():
        digit += int(chars[index+1])
    else:
        digit += letters.get(chars[index+1].upper())

    digit = int(digit)/255
    digits.append(str(round(digit, 3)))

print(", ".join(digits)+ ', 1\n')