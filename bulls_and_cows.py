import random

# 4자리 숫자 생성
def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]

# 입력받은 숫자와 비교하여 결과 반환
def compare_numbers(answer, guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if answer[i] == guess[i]:
            bulls += 1
        elif answer[i] in guess:
            cows += 1
    return bulls, cows

# 게임 진행
def play_game():
    answer = generate_number()
    print("게임을 시작합니다!")
    while True:
        guess = input("숫자를 입력하세요 (4자리): ")
        guess = [int(d) for d in guess]
        bulls, cows = compare_numbers(answer, guess)
        print(f"{bulls} Bulls, {cows} Cows")
        if bulls == 4:
            print("정답입니다!")
            break

play_game()
