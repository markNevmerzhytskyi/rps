import random

rock = "rock"
paper = "paper"
scissors = "scissors"
rsp = [rock, paper, scissors]

countD = 0
countPW = 0
countRW = 0
countSW = 0
count_pc = 0
count_my = 0

n = 100
for i in range(n):
    a1 = input("Your choice: ")
    a2 = random.choice(rsp)
    # Your choice: rock
    # Rock x Paper
    # Paper wins!
    # 3 - 2
    print(a1, "vs", a2)
    if (a1 == rock and a2 == rock) or (a1 == paper and a2 == paper) or (a1 == scissors and a2 == scissors):
        print("Draw!")
        countD += 1
    if (a1 == rock and a2 == paper) or (a1 == paper and a2 == rock):
        print(a2)
        print("Paper wins!")
        countPW += 1
        if a1 == paper:
            count_my += 1
        else:
            count_pc += 1
    if (a1 == rock and a2 == scissors) or (a1 == scissors and a2 == rock):
        print(a2)
        print("Rock wins!")
        countRW += 1
        if a1 == rock:
            count_my += 1
        else:
            count_pc += 1
    if (a1 == paper and a2 == scissors) or (a1 == scissors and a2 == paper):
        print(a2)
        print("Scissors wins!")
        countSW += 1
        if a1 == scissors:
            count_my += 1
        else:
            count_pc += 1
    if count_my == 5:
        print(f"Player wins! Score: {count_my} - {count_pc}")
        break
    if count_pc == 5:
        print(f"Computer wins! Score: {count_pc} - {count_my}")
        break
    print(count_my, "-", count_pc)


# print(f"Draw percentage: {countD / n * 100}%, paper win percentage: {countPW / n * 100}%,"
# f" rock win percentage: {countRW / n * 100}%, scissors win percentage: {countSW / n * 100}%, ")
