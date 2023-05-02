def take_guess():
    print("숫자 4개를 하나씩 차례대로 입력하세요.")
    i = 0
    new_guess = []
    while i < 4:
        gue_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1)))
        if gue_number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if gue_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요. ")

