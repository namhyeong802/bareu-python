import random
게임수 = 0

while True:
    A의선택 = int(input("A(1~3)?"))
    for n in range(A의선택):
        print("A",게임수 + n + 1, "!")

    게임수 += A의선택
    if 게임수 >= 31:
        break

    B의선택 = random.randint(1,3)
    print("B(1~3)?{}".format(B의선택))
    for k in range(B의선택):
        print("B",게임수 + k + 1, "!")

    게임수 += B의선택
    if 게임수 >= 31:
        break
print("벌칙당첨")