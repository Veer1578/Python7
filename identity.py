x = 5
if type(x) is int:
    print("True")
else:
    print("False")


x = 5.0
if type(x) is not float:
    print("True")
else: 
    print("False")


x = 20
y = 20
if x is y:
    print("X and Y have the same identity.")
y = 30
if x is not y:
    print("X and Y do not have the same identtity.")