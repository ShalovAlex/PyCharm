tickets = int(input("Enter the number of tickets, if the number of tickets is from 4, then the discount is 10%: "))
age = list(map(int, input("Enter the age of the visitors, separated by a space: ").split()))
while tickets != len(age):
    age = list(map(int, input("The number of visitors does not match the number of tickets.\n"
                              "Enter the age of the visitors separated by a space: ").split()))
price = []
for i in age:
    if i in range(0, 18):
        price.append(0)
    elif i in range(18, 25):
        price.append(990)
    else:
        price.append(1390)

if tickets > 3:
    print("The amount to be paid including the discount: ", sum(price) - ((sum(price) / 100) * 10), "rubles")
else:
    print("The amount to be paid: ", sum(price), "rubles")
