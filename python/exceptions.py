x = int(input("x: "))
y = int(input("y: "))

try:
    result = x/y
except ZeroDivisionError:
    print("Error cannot divide by zero")
    exit(1)
    
print(f"{x}/{y} = {result}")