# 5.编写一个函数process_list(lst, index)，处理列表元素访问：
# o使用try-except处理可能的IndexError和TypeError
# o如果索引有效，返回对应元素
# o如果索引超出范围，返回"索引超出范围"
# o如果lst不是列表或index不是整数，返回"参数类型错误"
# 编写测试代码，验证各种情况。


def process_list(lst, index):
    try:
        value = lst[index]
        return value
    except IndexError:
        return "索引不是有效值"
    except TypeError:
        return "参数类型错误"

if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5]
    lst2 = ([5, 6, 7, 8, 9],"a")
    dict1 = {"1":"1", "2":"2", "3":"3", "4":"4", "5":"5"}
    a = process_list(dict1, 2)
    print(a)











