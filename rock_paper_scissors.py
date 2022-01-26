from random import randint

# Counting the number of different results for player1 in rock, paper, scissors

# List of options to play
t = ["stone", "paper", "scissors"]

# Assigning numbers to options
player1 = t[randint(0, 2)]
player2 = t[randint(0, 2)]

# Making the loop
i = 0
draw = 0
win = 0
loss = 0
while i < 10000:
    i = i + 1
    if player1 == player2:
        draw = draw + 1
    elif player1 == "paper":
        if player2 == "stone":
            win = win + 1
        else:
            loss = loss + 1
    elif player1 == "scissors":
        if player2 == "paper":
            win = win + 1
        else:
            loss = loss + 1
    elif player1 == "stone":
        if player2 == "scissors":
            win = win + 1
        else:
            loss = loss + 1

    player1 = t[randint(0, 2)]
    player2 = t[randint(0, 2)]

print("Draws: ", draw)
print("Wins: ", win)
print("Losses: ", loss)
