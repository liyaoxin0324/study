num = int(input("请输入一个1到9的正整数："))
i = 1
while i <= num:
    row = ""
    j = 1
    while j <= i:
        row += str(j)
        j += 1
    spaces = " " * (num-i)
    i += 1
    print(f"{spaces}{row}")

num1 = []
for x in range (2,10000):
    num_sum = 0
    for i in range(1,x):
        if x % i == 0:
            num_sum += i
    if num_sum == x:
        num1.append(x)
        print(num1)

i_list = []
import math
for i in range(3,100):
        aqr_num = int(math.sqrt(i))
        number2 = True
        j = 2
        while j <= aqr_num:
            if i % j == 0:
                number2 = False
                break
            j += 1
        if number2:
            i_list.append(i)
print(i_list)

list_tmp = -1
for a in i_list:
    if (a - list_tmp) == 2:
        print(f"({list_tmp},{a})")
    list_tmp = a



while True:
    oder = input("输入：")
    parts = oder.split()

    if not parts :
        continue
    parts1 = parts[0]

    if parts1 == "takeoff":
        print("输出：“系统：正在启动动力系统，准备起飞。”")

    elif parts1 == "land":
        print("输出：“系统：正在自动循迹降落。”\n（程序结束）")
        break

    elif parts1 in ["up","down","speed"]:
        param = parts[1] if len(parts) > 1 else ""
        print(f"执行：{parts1} ，目标参数：{param}")

    elif parts1 == "move":
       if len(parts) < 3:
           print("警告，move需要两个参数")
       else:
           derection = parts[1]
           parts3 = parts[2]

           if derection not in ["forward","backward","left","right","north","south","east","west"]:
               print("警告，无法识别非法指令，请重新输入")
           elif not parts3.isdigit():
                print("距离必须为数字")
           elif parts3.isdigit():
                   print(f"航向修正：{derection}向 移动 {parts3}米")
    else:
        print("警告，无法识别的指令")


import random as rd
a = rd.randint(0,9)
passwd = 26583 + a
i = 0
j = 0
while i < 5 and j < 3:
  print(passwd)
  passed_input =int( input("请输入密码："))
  i += 1
  if passed_input == passwd :

    print("欢迎登录")
    break
  elif passed_input != passwd :
   j += 1
  print(f"登录失败，还剩{5-i}次机会")



