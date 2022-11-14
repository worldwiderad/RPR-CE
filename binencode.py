def charencode(c):
    if c == "a":
        return "00001"
    elif c == "b":
        return "00010"
    elif c == "c":
        return "00011"
    elif c == "d":
        return "00100"
    elif c == "e":
        return "00101"
    elif c == "f":
        return "00110"
    elif c == "g":
        return "00111"
    elif c == "h":
        return "01000"
    elif c == "i":
        return "01001"
    elif c == "j":
        return "01010"
    elif c == "k":
        return "01011"
    elif c == "l":
        return "01100"
    elif c == "m":
        return "01101"
    elif c == "n":
        return "01110"
    elif c == "o":
        return "01111"
    elif c == "p":
        return "10000"
    elif c == "q":
        return "10001"
    elif c == "r":
        return "10010"
    elif c == "s":
        return "10011"
    elif c == "t":
        return "10100"
    elif c == "u":
        return "10101"
    elif c == "v":
        return "10110"
    elif c == "w":
        return "10111"
    elif c == "x":
        return "11000"
    elif c == "y":
        return "11001"
    elif c == "z":
        return "11010"
    elif c == ".":
        return "11011"
    elif c == ",":
        return "11100"
    elif c == "!":
        return "11101"
    elif c == "'":
        return "11110"
    elif c == "-":
        return "11111"
    else:
        return "00000"

  

def encode(plaintext):
    cipher = ""
    for letter in plaintext:
        encoded_char = charencode(letter)
        cipher = cipher + encoded_char
    return (cipher)

print(encode(input("enter text dodo")))
