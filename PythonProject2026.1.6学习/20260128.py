year1 =int( input("请输入年份："))
if year1 % 4 == 0 and not year1 % 100 == 0 or year1 % 400 == 0:
    print("闰年")
    print(year1)
else:
    print("平年")
    print(year1)


import math
number1 = int(input("请输入一个正整数："))
if number1 <= 1:
    print("1不是质数")
elif number1 == 2:
    print("2是最小的偶质数")
else:
    aqr_num = int(math.sqrt(number1))
    number2 = True
    i = 2
    while i <= aqr_num:
        if number1 % i == 0:
            print(f"{number1}不是质数且能被{i}整除")
            number2 = False
            break
        i += 1
    if number2:
        print(f"{number1}是质数")


import random as rd
num =rd.randint(1,100)
i = 0
while i < 7:
  i += 1
  num_guss = int(input("您猜测的数字是："))
  if num_guss < num :
    print("太小")
  elif num_guss > num :
    print("太大")
  else:
    print(f"{i}次就猜对了\n 正确数字是{num}")
if i >= 7 and num_guss != num :
  print(f"你用完了{i}次机会，正确数字是{num}")


length =int( input("您要生成的数列长度为："))
fib_seq = []
a,b = 0,1
i = 0
while i < length:
    fib_seq.append(a)
    a,b = b,a+b
    i += 1
print(f"生成长度为{length}的斐波那契数列为：{fib_seq}")


passwd_right = "Python123"
x = 0
while x < 3:
    passwd = input("Enter your password: ")
    if passwd == passwd_right:
        print("欢迎")
        break
    else:
        x += 1
        print(f"密码错误，密码输入剩余次数{3 - x}")
    if x > 3:
        print("您输入的密码已超过上限，账户已被锁定")

print("-------------------欢迎使用计算器-------------------------\t")
print("----------输入格式：数字 运算符 数字（例如：3 + 5）----------\t")
print("------------------输入quit可退出程序----------------------\t")
while True:
    user_input = input("请输入表达式或quit：").strip()
    if user_input.lower() == "quit":
        print("感谢使用，程序退出")
        break
    parts = user_input.split(" ")
    if len(parts) != 3:
        print("输入格式错误，请按【数字 运算符 数字】格式输入")
        continue
    num1_str = parts[0]
    num2_str = parts[1]
    num3_str = parts[2]
    try:
        num1 = float(num1_str)
        num3 = float(num3_str)
    except ValueError:
        print("您输入的不是有效数字，请重新输入")
        continue
    result = None
    if num2_str == "+":
        result = num1 + num3
    elif num2_str == "-":
        result = num1 - num3
    elif num2_str == "*":
        result = num1 * num3
    elif num2_str == "/":
        if num3 == 0:
            print("错误，除数不能为0")
            continue
        result = num1 / num3
    else:
        print(f"不支持运算符 {num2_str}仅支持+，-，*，/")
        continue
    print(f"计算结果{num1_str} {num2_str} {num3_str} = {result}\n")








