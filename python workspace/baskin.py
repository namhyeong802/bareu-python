import random
import time
게임수 = 0

while True:
    while True:
        try:
            A의선택 = int(input("A(1~3)?"))
            if A의선택 == 1 or A의선택==2 or A의선택 ==3:
                break
            else:
                print("[경고] 1,2,3 숫자만 입력하시오.")  
        except:
            print("[경고]숫자만 입력하시오.")
            # break
    for n in range(A의선택):
     print("A",게임수 + n + 1, "!")
    게임수 += A의선택
    if 게임수 >= 31:
        print("A벌칙당첨")
        break
    B의선택 = random.randint(1,3)
    time.sleep(random.randint(1,4))
    print("B(1~3)?{}".format(B의선택))
    for k in range(B의선택):
        print("B",게임수 + k + 1, "!")

    게임수 += B의선택
    if 게임수 >= 31:
        print("B벌칙당첨")
        break