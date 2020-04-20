amount = int(input())
years = 0
while amount <= 700000:
    years += 1
    amount += amount * 7.1 / 100
print(years)