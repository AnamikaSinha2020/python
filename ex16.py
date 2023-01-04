
# taking two inputs at a time
a, b = input("Enter two values: ").split()
# print("First input is {} and second input is {}".format(a, b))
print("First enterd value is {} and second entered value is {}".format(a,b))
# print()
x=lambda a,b:int(a)+int(b)
print(x(a,b))