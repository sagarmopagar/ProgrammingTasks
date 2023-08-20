a = int(input("Number 1: "))
b = int(input("Number 2: "))

lcm = 0

big = a if a > b else b

for i in range(big, a*b+1, 1):
    if i%a == 0 and i%b == 0:
        lcm = i
        break

print(f'LCM of {a} and {b} is: {lcm}')
