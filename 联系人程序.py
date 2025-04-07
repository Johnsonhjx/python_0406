
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
    print('6. 修改联系人手机号')
    print('7. 添加联系人的电子邮箱')

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

# 修改联系人手机号码
def modify_contact():
    name = input('请输入要修改的联系人姓名')
    if name in contacts:
        new_phone = input('请输入他的新号码')
        contacts[name] = new_phone
        print(f'已修改联系人{name} - 新号码为 {new_phone}')
    else:
        print('没有这号人哪')

# 添加联系人电子邮箱
def add_email():
    name = input('请输入联系人姓名')
    email = input('请输入联系人的电子邮箱')
    if '@' in email and '.com' in email:
        contacts[name] = {
            'email': email
        }

        print(f"已添加 {name} 的电子邮箱：{email}")
    else:
        print('请输入正确的邮箱格式！')


# 主循环

while True:
    show_menu()
    choice = input('请选择操作 1 - 7 ')

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
    elif choice == '6':
        modify_contact()
    elif choice == '7':
        add_email()
    else:
        print('你输入有误，重新输入 1-7 之间的数字')