# 题目1：使用递归实现斐波那契数列 (Fibonacci)
# 使用递归函数完成斐波那契数列计算。
# 数列：1, 1, 2, 3, 5, 8, 13...（每一项等于前两项之和）。
# 逻辑：F(n) = F(n-1) + F(n-2)
# 出口：当 n 是 1 或 2 时，返回 1。


def fibonacci(n):
    n_list = []
    for i in range(n):
        n_list.append(i)
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("请输入一个数字："))
result = fibonacci(n)
print(f"第{n}项的斐波那契数是：{result}")