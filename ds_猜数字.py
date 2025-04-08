# 猜数字小游戏
import random

def guess_number_game():
    # 游戏初始化
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1-100之间的整数，你有7次机会猜它。")
    
    # 生成随机数字
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    # 游戏主循环
    while attempts < max_attempts:
        # 获取玩家输入
        guess = input(f"\n这是你的第{attempts + 1}次尝试，请输入你猜的数字: ")
        
        # 检查输入是否有效
        if not guess.isdigit():
            print("请输入一个有效的数字！")
            continue
            
        guess = int(guess)
        
        # 检查猜测结果
        if guess < secret_number:
            print("你猜的数字太小了！")
        elif guess > secret_number:
            print("你猜的数字太大了！")
        else:
            print(f"恭喜你！你用了{attempts + 1}次猜对了数字{secret_number}！")
            return
            
        attempts += 1
    
    # 如果用完所有机会
    print(f"\n很遗憾，你没有在7次内猜中。正确的数字是{secret_number}。")

# 启动游戏
guess_number_game()

# 询问是否再玩一次
while True:
    play_again = input("\n想再玩一次吗？(输入y继续，其他退出): ")
    if play_again.lower() == 'y':
        guess_number_game()
    else:
        print("谢谢游玩，再见！")
        break