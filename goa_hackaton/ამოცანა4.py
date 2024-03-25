num1 = 6
num2 = 10

for i in range(1, 100):
    if i % num1 == 0 and i % num2 == 0:
        print(i)
        break
