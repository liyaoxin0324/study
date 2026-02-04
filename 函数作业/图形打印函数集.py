def right_triangle():
    """
    打印直角三角形
    :param height: 三角形高度
    :param char: 使用的字符
    """
    height = int(input("您想要输入直角三角形的高为："))
    char = str(input("您想要什么字符组成您的三角形："))
    for i in range(1, height + 1):
        print(char * i)
    print()  # 空行分隔

def isosceles():
    """
    打印等腰三角形
    :param height: 三角形高度
    :param char: 使用的字符
    """
    height = int(input("您想要输入等腰三角形的高为："))
    char = str(input("您想要什么字符组成您的三角形："))
    for i in range( height ):
        # 当前行的字符数
        char_count = 2 * i + 1
        # 计算空格（使用字符串的center方法）
        line = (char * char_count).center(2 * height - 1)
        print(line)
    print()


def diamond():
    """
    打印菱形
    :param height: 菱形高度（必须为奇数，如果不是会自动加1）
    :param char: 使用的字符
    """
    # 确保高度为奇数
    height = int(input("您想要输入菱形的高为："))
    char = str(input("您想要什么字符组成您的菱形："))
    # 上半部分（包括中间）
    for i in range( height ):
        char_count = 2 * i + 1
        # 计算空格（使用字符串的center方法）
        line = (char * char_count).center(2 * height - 1)
        print(line )

    # 下半部分
    for i in range(height - 1, 0, -1):
        char_count = 2 * i - 1
        # 计算空格（使用字符串的center方法）
        line = (char * char_count).center(2 * height - 1)
        print(line)
    print()  # 空行分隔

def hollow_square():
    """
    打印空心正方形
    :param side: 正方形边长
    :param char: 使用的字符
    """
    side= int(input("您想要输入正方形的边长为："))
    char = str(input("您想要什么字符组成您的正方形："))
    for i in range(side):
        if i == 0 or i == side - 1:
            print((char+'  ') * side)
        else:
            spaces = "   " * (side - 1)
            print(char + spaces + char)
    print()


def multiplication_table():
    """
    打印乘法表
    :param size: 乘法表大小（通常为9）
    """
    size = int(input("您想要输入乘法表的大小为："))
    print(f"乘法表（{size}×{size}）：")
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            # 使用f-string格式化，保持对齐
            print(f"{j}×{i}={i * j:2}", end="  ")
        print()  # 换行
    print()  # 空行分隔

def main():
    while True:
        num_select = int(input("========图形函数测试========\n"
                               "1.打印直角三角形\n"
                               "2.打印等腰三角形\n"
                               "3.打印菱形\n"
                               "4.打印正方形\n"
                               "5.打印乘法表\n"
                               "6.退出\n"
                               "选择数字对应的功能:"))
        match num_select:
            case 1:
                right_triangle()
            case 2:
                isosceles()
            case 3:
                diamond()
            case 4:
                hollow_square()
            case 5:
                multiplication_table()
            case 6:
                break

if __name__ == '__main__':
    main()