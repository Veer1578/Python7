print("Enter your marks of 5 subjects")
markOne = int(input("Enter 1st subject marks "))
markTwo = int(input("Enter 2nd subject marks "))
markThree = int(input("Enter 3rd subject marks "))
markFour = int(input("Enter 4th subject marks "))
markFive = int(input("Enter 5th subject marks "))

total = markOne + markTwo + markThree + markFour + markFive
avg = total/5

if avg >= 90 and avg <= 100:
    print("Your grade is A1")
elif avg >= 80 and avg <= 89:
    print("Your grade is A2")
elif avg >= 70 and avg <= 79:
    print("Your grade is B1")
elif avg >= 60 and avg <= 69:
    print("Your grade is B2")
elif avg >= 50 and avg <= 59:
    print("Your grade is C1")
elif avg >= 40 and avg <= 49:
    print("Your grade is C2")
elif avg >= 30 and avg <= 39:
    print("Your grade is D1")
elif avg >= 0 and avg <= 29:
    print("You failed")
else:
    print("Invalid input")
