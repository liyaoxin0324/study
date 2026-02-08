# 3.使用assert语句编写一个函数validate_age(age)，验证年龄的合法性：
# oage必须是整数
# oage必须在0到150之间（包含）
# o使用assert进行校验，并提供清晰的错误信息
# 编写测试代码，分别测试合法年龄和非法年龄。


def validate_age(age: int) :
    assert age >= 0 and age <= 150,"年龄不合法，请重新输入"
    # assert 后面跟正常值范围
    return age

if __name__ == '__main__':

    a = validate_age(149)
    print(a)


