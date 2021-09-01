"""Numeric Operators."""
lhs: str = input("Left-hand side: ")
rhs: str = input("Right-hand side: ")
print(lhs + " ** " + rhs + " is " + str(int(lhs) ** int(rhs)))
print(lhs + " / " + rhs + " is " + str(int(lhs) / int(rhs)))
print(lhs + " // " + rhs + " is " + str(int(lhs) // int(rhs)))
print(lhs + " % " + rhs + " is " + str(int(lhs) % int(rhs)))
