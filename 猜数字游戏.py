import random

def guess_number():
    # 游戏初始化
    print('欢迎来到猜数字游戏')
    print('我已经想好了一个1-100之间的整数，你有7次机会才到它')

    # 生成随机数字
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    # 游戏主循环
    while attempts < max_attempts:
        # 获取玩家输入
        guess = input(f'\n这是你第 {attempts+1} 次尝试，请输入一个1-100之间的整数')

        # 检查输入是否有效
        if not guess.isdigit():
            print('请输入一个有效的数字')
            continue

        guess = int(guess)

        # 检查猜测是否正确
        if guess < secret_number:
            print('你猜的数字小了')
        elif guess > secret_number:
            print('你猜的数字大了')
        else:
            print(f'恭喜你猜对了，这个数字是 {secret_number}')
            return

        attempts += 1

    # 游戏结束
    print(f'很遗憾，你没有在 {max_attempts} 次内猜中这个数字，正确的数字是 {secret_number}')

# 运行游戏

guess_number()

while True:
    play_again = input('\n是否再玩一次？输入 y 继续，输入 n 退出游戏')
    if play_again.lower() == 'y':
        guess_number()
    else:
        print('谢谢参与，再见')
        break