# 2.创建一个自定义异常类NegativeNumberError，用于表示负数错误。
# 编写函数check_positive(number)，检查输入的数字是否为正数。
# o如果number>0，返回True
# o如果number<=0，抛出NegativeNumberError，异常信息为"输入的数字必须为正数"
# 编写测试代码，捕获该异常并打印异常信息。


class NegativeNumberError(Exception):
    def __init__(self, value = "输入的数字必须为正数"):
        self.value = value
        super().__init__(self.value)

def check_positive(value):
    if value > 0:
        return True
    else:
        raise NegativeNumberError()

if __name__ == '__main__':
    try:
        result = check_positive(12)
        print(f"check_positive(12) 返回: {result}")
    except NegativeNumberError as e:
        print(f"异常: {e}")
    # b = check_positive(1)
    # a = check_positive(-1)
    #
    # print(b,a)