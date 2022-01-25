import random

dice1 = 0
dice2 = 0
dice3 = 0
dice4 = 0
dice5 = 0
dice6 = 0
i = 0

while i < 100000:
    dice = random.randint(1, 6)
    if dice == 1:
        dice1 += 1
    elif dice == 2:
        dice2 += 1
    elif dice == 3:
        dice3 += 1
    elif dice == 4:
        dice4 += 1
    elif dice == 5:
        dice5 += 1
    elif dice == 6:
        dice6 += 1
    i = i + 1

print("1:", dice1)
print("2:", dice2)
print("3:", dice3)
print("4:", dice4)
print("5:", dice5)
print("6:", dice6)
