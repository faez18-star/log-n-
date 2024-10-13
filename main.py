def computePower(x, y):
    result = 1
    while y > 0:
        if y % 2 == 0:  # If y is even
            x = x * x  # Square the base
            y >>= 1    # Divide the exponent by 2 (bitwise right shift)
        else:          # If y is odd
            result = result * x  # Multiply result by the base
            y = y - 1  # Subtract 1 from y
    return result

x = int(input("Enter x for x^y: "))
y = int(input("Enter y for x^y: "))
print("Total: ", computePower(x, y))