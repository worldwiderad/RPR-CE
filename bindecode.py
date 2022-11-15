from calendar import c


def decryptchar(c):

     if c == "00001":
        return "a"
     elif c == "00010":
        return "b"
     elif c == "00011":
        return "c"
     elif c == "00100":
        return "d"
     elif c == "00101":
          return "e"
     elif c == "00110":
       return "f"
     elif c == "00111":
       return "g"
     elif c == "01000":
         return "h"
     elif c == "01001":
         return "i"
     elif c == "01010":
         return "j"
     elif c == "01011":
         return "k"
     elif c == "01100":
         return "l"
     elif c == "01101":
          return "m"
     elif c == "01110":
         return "n"
     elif c == "01111":
         return "o"
     elif c == "10000":
         return "p"
     elif c == "10001":
         return "q"
     elif c == "10010":
         return "r"
     elif c == "10011":
         return "s"
     elif c == "10100":
         return "t"
     elif c == "10101":
         return "u"
     elif c == "10110":
         return "v"
     elif c == "10111":
         return "w"
     elif c == "11000":
         return "x"
     elif c == "11001":
         return "y"
     elif c == "11010":
         return "z"
     elif c == "11011":
         return "."
     elif c == "11100":
         return ","
     elif c == "11101":
            return "!"
     elif c == "11110":
         return "'"
     elif c == "11111":
         return "-"
     else:
         return " "


def decrypt (ciphertext):
  if len(ciphertext) % 5 != 0:
    return ""
  else:
    decoded = ""
    for i in range(0, len(ciphertext), 5):
      binletter = ciphertext[i] + ciphertext[i + 1] + ciphertext[i + 2] + ciphertext[i + 3] + ciphertext[i + 4]
      decodedletter = decryptchar(binletter)
      decoded = decoded + decodedletter
    return decoded
