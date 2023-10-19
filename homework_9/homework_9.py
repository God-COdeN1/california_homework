text = "Hello world"
i = 0
while i < len(text):
    print(text[i])
    i += 1

for i in text:
    print(i)


i = 0
while i <= 5:
    if i == 6:
        break
    print(i)
    i += 1

num = int(input("Enter num: "))
power = int(input("Enter power: "))
result = 1
while power > 0:
    result *= num
    power -= 1
print("Result:", result)

list_1 = []
for i in range(0, 16):
    list_1.append(i)

print(list_1)

list_1 = []
for i in range(15, -1, -1):
    list_1.append(i)

print(list_1)


list_2 = ["a", "b", "c", "d", "e", "f", "g"]
for index, value in enumerate(list_2):
    print(f"Index: {index}, Value: {value}")
