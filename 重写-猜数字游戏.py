import random

def guess_number_game():
    # 生成一个随机数
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    # 游戏主循环
    while attempts < max_attempts:
        # 获取用户输入
        guess = int(f'这是你的第 {attempts+1} 次猜测，请输入一个数字')
        # 检查猜测是否正确
        if not guess.isdigit():
            print('请输入一个有效的数字')
            continue

        guess = int(guess)

        # 检查猜测结果
        if guess < secret_number:
            print('数字小了')
        elif guess > secret_number:
            print('数字打了')
        else:
            print(f'恭喜，你只用了 {attempts+1} 次就猜对了！')
            return

        attempts += 1

    # 尝试次数用完了，则结束游戏
    print('很遗憾，你没有在规定的次数内才对，正确数字是 {secret_number}}') 

# 启动游戏
guess_number_game()

while True:
    play_again = input('是否再玩一次？输入 “yes” 继续，输入“no” 退出游戏')
    if play_again.lower() == 'yes':
        guess_number_game()
    else:
        print('感谢参与，再见')
        break