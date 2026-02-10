#
# 8.实现登录注销方法：，在users列表中按current_login_user中存储的用户名找到对应的字典，将其中的isLogin设为False，
# 将current_login_user变量设为None。
# 9.实现退出方法，程序直接退出。注意：登录注销不能退出程序，主菜单可以继续选择功能。
# 10.编写主程序使用这个模块，提供简单的菜单界面。
import random

users = [
    {"username":"licc","passwd":111,"balance":50,"isLogin":False},
{"username":"fcc","passwd":222,"balance":502,"isLogin":False},
{"username":"lyx","passwd":333,"balance":5000,"isLogin":False},
{"username":"jc","passwd":444,"balance":5069,"isLogin":False},
{"username":"wyw","passwd":555,"balance":501111,"isLogin":False},
{"username":"lixin","passwd":666,"balance":10564,"isLogin":False},
{"username":"ok","passwd":777,"balance":33333,"isLogin":False},
]
# 1.先定义一个全局的列表对象users，列表中存储多个用户字典，每个用户字典有：用户名（username）、
# 密码（password）、余额（blance）、是否登录(isLogin，初始化为False)
# 并设置一个全局str变量“current_login_user”，默认值为None
current_login_user = None
# 实现一个注册方法，提示输入用户名和密码，然后检查用户名是否被注册，如果已注册则提示。如果没有注册，
# 则往列表对象添加一个用户，存储用户名、密码、余额(使用500-1000随机数)、是否登录(初始化为False)
def register():
    """注册新用户"""
    global user
    username_input =input("请输入您的用户名：").strip()
    username1 = str(username_input)
    password_input = int(input("请输入您的密码："))
    for user in users:
        if user["username"] == username1 :
            print(f"用户名{username1}已被注册")
        else:
            num_rand = random.randint(500,1000)
            new_user = {"username":username1,
                        "passwd":password_input,
                        "balance":num_rand,
                        "isLogin":False}
            users.append(new_user)
            print(f"{username1}注册成功，初始余额{num_rand}")
            return True


# 实现登录方法，判断用户是否在列表中，如果不在则提示，如果在则验证密码是否正确，如果正确，
# 将“是否登录”置为True。将登录的用户名写到current_login_user变量中
def log_in():
    """用户登陆"""
    global current_login_user

    username =input("请输入您的用户名：").strip()
    password = int(input("请输入您的密码："))
    for user in users:
        if user["username"] == username:
            if user["passwd"] == password:
                user["isLogin"] = True
                current_login_user = username
                print("登录成功")
                return  True
            else:
                print("您的密码输入错误")
                return False

    print("用户名错误或不存在")
    return False



# 实现登录检查方法，判断current_login_user存储的用户名，和对应的字典中的isLogin是否为True
def check_login():
    global current_login_user
    if current_login_user is None:
        return False
    for user in users:
        if user["username"] == current_login_user and user["isLogin"] :
            return True
    return False

# 实现方法：add_transaction(amount, category, description) 添加交易记录。
# 方法执行前要调用登录检查。实现方法：get_balance() 计算并返回当前余额。方法执行前要调用登录检查
def add_transaction():
    if not check_login():
        print("请先登录！")
        return
    try:
        amount = float(input("请输入交易金额（收入+，支出为-）："))
        category = input("请输入交易类型：").strip()
        description = input("描述或备注：").strip()
    except:
        print("金额输入错误")
        return
    for user in users:
        if user["username"] == current_login_user:
            user["balance"] += amount

            transaction = {
                "amount": amount,
                "category": category,
                "description": description,
            }
            if "transactions" not in user:
                user["transactions"] = []
            user["transactions"].append(transaction)
            print(f"交易添加成功! 当前余额: {user['balance']}")
            return

    # transaction = {
    #     "amount": amount,
    #     "category": category,
    #     "description": description,
    # }
    # if "transactions" not in user[current_login_user]:
    #     user[current_login_user]["transactions"] = []
    #
    # user[current_login_user]["transactions"].append(transaction)
    # print(f"交易添加成功！")
    # print(f"交易金额：{amount}")
    # print(f"交易类型：{category}")
    # print(f"交易描述：{description}")
    # print(f"当前余额：{user[current_login_user]['balance']:.2f}")


def get_balance():
    """
    获取当前余额
    需要在执行前检查登录状态
    """

    # 1. 检查是否登录
    if not check_login():
        print("请先登录！")
        return None

    # 2. 获取并返回余额
    for user in users:
        if user["username"] == current_login_user:
            balance = user["balance"]
            print(f"当前余额：{balance:.2f}")
            return balance
    return None

# 实现方法：get_summary_by_category() 按类别汇总交易金额。方法执行前要调用登录检查
def get_summary_by_category():

    if not check_login():
        print("请先登录！")
        return{}
    for user in users:
        if user["username"] == current_login_user:
            if "transactions" not in user or not user["transactions"]:
                print("暂无交易记录！")
                return {}

            summary = {}
            for transaction in user["transactions"]:
                category = transaction["category"]
                amount = transaction["amount"]

                if category not in summary:
                    summary[category] = 0
                    summary[category] += amount
            print("交易类别汇总：")
            for category, total in summary.items():
                print(f"{category}: {total:.2f}")
            return summary
    return {}

def logout():
    global current_login_user
    if current_login_user is None:
        print("当前没有用户登录")
        return
    for user in users:
        if user["username"] == current_login_user:
            user["isLogin"] = False
            print(f"用户{current_login_user}已注销")
    current_login_user = None

def exit_progrem():
    """退出程序"""
    print("程序退出")
    import  sys
    sys.exit(0)

def main_menu():
    while True:
        print("\n==============财务管理系统============")
        if current_login_user:
            print(f"当前用户: {current_login_user}")
            print("1. 添加交易记录")
            print("2. 查看余额")
            print("3. 交易类别汇总")
            print("4. 注销")
            print("5. 退出程序")
        else:
            print("1. 注册")
            print("2. 登录")
            print("3. 退出程序")

        choice = int(input("请选择操作: "))
        if current_login_user:
            match choice:
                case 1:
                    add_transaction()
                case 2:
                    get_balance()
                case 3:
                    get_summary_by_category()
                case 4:
                    logout()
                case 5:
                    exit_progrem()
                    break
        else:
            match choice:
                case 1:
                    register()
                case 2:
                    log_in()
                case 3:
                    exit_progrem()
                    continue
if __name__ == '__main__':
    main_menu()







