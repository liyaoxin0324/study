# 初始化客户数据存储字典，key为客户ID（字符串），value为客户姓名

customer_data = {}


def is_valid_id(input_id):
    """
    校验输入的ID是否为纯数字
    :param input_id: 输入的ID字符串
    :return: 纯数字返回True，否则返回False
    """
    return input_id.isdigit()


def add_customer():
    """添加客户的核心逻辑"""
    max_attempts = 3  # 最多输入ID的次数
    attempt = 0

    while attempt < max_attempts:
        # 提示输入客户ID
        customer_id = input("请输入客户id:")

        # 第一次校验：是否为纯数字
        if not is_valid_id(customer_id):
            print("客户id必须为纯数字")
            attempt += 1

            # 第三次输入时的额外提醒
            if attempt == max_attempts - 1:
                print("最后一次机会，请输入客户id:")
            continue

        # 第二次校验：ID是否已存在
        if customer_id in customer_data:
            print("客户id已存在，终止添加客户")
            return

        # ID校验通过，开始输入姓名
        customer_name = input("请输入客户姓名:")
        customer_data[customer_id] = customer_name
        print(f"客户{customer_id}({customer_name})添加成功！")
        return

    # 三次输入失败，终止添加
    print("终止添加客户")


def main_menu():
    """系统主菜单"""
    while True:
        # 打印主菜单
        print("\n---------客户管理系统---------")
        print("1. 添加客户")
        print("2. 删除客户")
        print("3. 修改客户")
        print("4. 查询客户")
        print("5. 显示客户")
        print("6. 退出")

        # 获取用户选择
        choice = input("请选择操作（输入数字1-6）：")

        # 菜单功能分发
        if choice == "1":
            add_customer()
        elif choice == "2":
            print("删除客户功能暂未实现")  # 可根据需求扩展
        elif choice == "3":
            print("修改客户功能暂未实现")  # 可根据需求扩展
        elif choice == "4":
            print("查询客户功能暂未实现")  # 可根据需求扩展
        elif choice == "5":
            if customer_data:
                print("\n当前客户列表：")
                for cid, cname in customer_data.items():
                    print(f"ID: {cid}, 姓名: {cname}")
            else:
                print("暂无客户数据")
        elif choice == "6":
            print("退出系统，感谢使用！")
            break
        else:
            print("输入无效，请选择1-6之间的数字！")

# 程序入口
if __name__ == "__main__":
    main_menu()