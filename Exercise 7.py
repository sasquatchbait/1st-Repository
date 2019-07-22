Number = input("Type a number")
Number = int(Number)
Number2 = 0
my_list = [10, 20, 30, 40, 50]
for i in range(5):
    if Number > my_list[i]:
        Number2 = Number2 + 1
print(Number2)