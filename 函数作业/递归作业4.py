# 题目4：灵活的统计学家（考察：参数与注解）
# 编写一个名为 smart_stats 的函数，要求：
# 参数设计：接受一个必选参数 data（列表类型），以及一个可选的命名关键字参数 mode（默认值为 "mean"）。
# 功能实现：
# 若 mode="mean"，返回列表数据的平均值。
# 若 mode="max"，返回最大值。
# 若 mode="min"，返回最小值。
# 要求：使用函数注解标明参数和返回值的预期类型。
def smart_stats(data: list,mode:str = "mean") -> float :
    """dhnfcxj"""
    mode = mode.lower()
    if mode == "mean":
        return sum(data)/len(data)
    elif mode == "min":
        return min(data)
    elif mode == "max":
        return max(data)

data = [1,2,3,4,5,6,7,8,9,10,11,12,80]

print(smart_stats(data, "mean"))  # 输出：5.5
print(smart_stats(data, "min"))   # 输出：1
print(smart_stats(data, "max"))   # 输出：10
print(smart_stats(data))









