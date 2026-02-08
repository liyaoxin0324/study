# 1.编写一个函数safe_divide(a, b)，要求：
# o使用try-except处理除法运算
# o当b为0时，捕获ZeroDivisionError并返回None
# o当a或b不是数值类型时，捕获TypeError并返回"参数类型错误"
# o其他异常捕获并返回"未知错误"
# o无论是否发生异常，最后都打印"除法运算完成"


def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    except TypeError:
        return "参数类型错误"
    except Exception:
        return "未知错误"
    finally:
        print("除法运算完成")

if __name__ == '__main__':

    a = safe_divide(3, 4)
    print(a)

