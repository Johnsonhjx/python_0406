
contacts = {}

# 功能： 0. 显示菜单  1. 查看联系人 2. 添加联系人 3. 查找联系人 4. 删除联系人 5. 退出程序


# 显示菜单
def show_menu():
    print('\n通讯录程序')
    print('1. 添加联系人')
    print('2. 查看联系人')
    print('3. 查找联系人')
    print('4. 删除联系人')
    print('5. 退出程序')

# 添加联系人
def add_contact():
    name = input('请输入联系人姓名')
    phone = input('请输入手机号码')
    contacts[name] = phone
    print(f"已添加：{name} - {phone}")

# 查看所有联系人
def view_all_contacts():
    if not contacts:
        print('你没朋友')
    else:
        print('\n所有联系人：')
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


# 查找联系人
def search_contact():
    name = input('请输入联系人姓名')
    if name in contacts:
        print(f'找到联系人：{name} - {contacts[name]}')
    else:
        print(f'没有{name}这号人')


# 删除联系人
def delete_contact():
    name = input('要删掉谁？')
    if name in contacts:
        del contacts[name]
        print(f'已删除{name}, 此生不复相见')
    else:
        print(f'没有{name}这号人')

# 主循环

while True:
    show_menu()
    choice = input('请选择操作 1 - 5 ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_all_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print('感谢使用，再见')
    else:
        print('你输入有误，重新输入 1-5 之间的数字')