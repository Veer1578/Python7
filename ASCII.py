char = input("Enter any character ")
asciiValue = ord(char)
if len(char) == 1:
    print(f"The Ascii value of {char} is {asciiValue}")
else:
    print("Enter one character only.")
