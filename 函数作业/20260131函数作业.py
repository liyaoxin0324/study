def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#    找到n的阶乘

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
        else:
            return True
#  判断n是否为素数

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)
# 找到a，b的最大公约数

def fibnacci(n):
    if n == 0:
        return 0
    else:
        return fibnacci(n - 1) + n
#     计算斐波那契数列

def main():
    while True:
        num_select = int(input("请选择您要计算的方式：\n"
                               "1 计算阶乘\n"
                               "2 查找质数\n"
                               "3 查找两个数字的公约数\n"
                               "4 计算斐波那契数列\n"
                               "5 退出\n")) #type : int
        match num_select :
            case 1:
                n = int(input("请输入一个整数："))
                print(f"您输入的整数的阶乘为：{factorial(n)}")
            case 2:
                n = int(input("请输入一个整数："))
                print(f"您输入的数字是否为质数:{is_prime(n)}")
            case 3:
                a = int(input("请输入您要计算公约数的第一个数字："))
                b =int( input("请输入您要计算公约数的第二个数字："))
                print(f"您输入两个数字的最大公约数为：{gcd(a, b)}")
            case 4:
                n = int(input("请输入一个整数："))
                print(f"您输入的数字的斐波那契结果为：{fibnacci(n)}")
            case 5:
                break


if __name__ == '__main__':
    main()

