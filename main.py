import random

rock = "rock"
paper = "paper"
scissors = "scissors"
rsp = [rock, paper, scissors]

countD = 0
countPW = 0
countRW = 0
countSW = 0

n = 1000000
for i in range(n):
    a1 = random.choice(rsp)
    a2 = random.choice(rsp)

    if (a1 == rock and a2 == rock) or (a1 == paper and a2 == paper) or (a1 == scissors and a2 == scissors):
        #print("Draw!")
        countD += 1
    if (a1 == rock and a2 == paper) or (a1 == paper and a2 == rock):
        #print("Paper wins!")
        countPW += 1
    if (a1 == rock and a2 == scissors) or (a1 == scissors and a2 == rock):
        #print("Rock wins!")
        countRW += 1
    if (a1 == paper and a2 == scissors) or (a1 == scissors and a2 == paper):
        #print("Scissors win!")
        countSW += 1
print(f"Draw percentage: {countD / n * 100}%, paper win percentage: {countPW / n * 100}%,"
      f" rock win percentage: {countRW / n * 100}%, scissors win percentage: {countSW / n * 100}%, ")

