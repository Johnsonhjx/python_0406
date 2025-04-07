# 终于可以同步到 github 了

# 待办事项程序
tasks = []

# 显示操作菜单
def show_menu():
    print('\n操作动作')
    print('1. 添加任务')
    print('2. 查看任务')
    print('3. 删除任务')
    print('4. 退出任务')


# 添加任务函数
def add_task():
    task = input('请输入任务内容')
    tasks.append(task)
    print(f"已添加任务：{task}")

# 查看任务函数
def view_tasks():
    if not tasks:
        print('当前没有任务')
    else:
        print('当前任务列表')
        for index, task in enumerate(tasks, start = 1):
            print(f"{index}. {task}")

# 删除任务
def delete_task():
    view_tasks()
    if tasks:
       try:
           task_num = int(input('请输入要删除的任务编号'))
           if 1<= task_num <= len(tasks):
               removed_task = tasks.pop(task_num - 1)
               print(f"已删除的任务：{removed_task}")
           else:
               print('无效的任务编号')
       except ValueError:
           print('请输入有效的数字')

# 主循环
while True:
    show_menu()
    choice = input("请选择操作 1 - 4")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print('感谢使用待办事项程序，再见')
        break
    else:
        print("请输入有效的选择")

























