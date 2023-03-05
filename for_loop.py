#structure with: FOR


for x in range(0, 5):
    print(f"192.168.18.15.{x}")

print("="*60)

for c in "python":
    print(c)


print("="*60)

fruits = ["banana", "apple", "kiwi"]
for x in fruits:
    print(x)


print("="*60)

cars = ["volkswagen", "toyota", "audi", "mercedes", "volvo"]
for i in cars:
    print(i)
    if i == "mercedes":
        break
    