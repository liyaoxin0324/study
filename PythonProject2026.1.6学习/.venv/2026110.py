
"""
name =str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height(meters): "))
number_like = int(input("your favorite number: "))
age_square = int(age ** 2)
height_cm = int(height * 100)
number_favor = hex(number_like)
print("------------------------------")
print(f"姓名： [{name}]")
print(f"年龄：[{age}]")
print(f"年龄的平方：[{age_square}]")
print(f"身高： [{height}]")
print(f"身高（厘米）：[{height_cm}]")
print(f"最喜欢的数字（十进制）：[{number_like}]")
print(f"最喜欢的数字（十六进制）：[{number_favor}]")
print("------------------------------")
"""

"""
while True:
    try:
        number1 = int(input("Enter a number from 0 to 65535: "))
        if 0 <= number1 <= 65535:
            break
        else:
            print("无效，请重新输入")
    except ValueError:
            print("输入无效，请重新输入一个整数")

number2 = bin(number1)
number8 = oct(number1)
number16 = hex(number1)
number_str = chr(number1)

utf8_bytes = number_str.encode('utf-8')
number_utf8_hex = utf8_bytes.hex()
lists = list(number_str.encode('utf-8'))
# number_utf8_10 = hex(number_str.encode('utf-8'))
print(f"十进制：{number1}")
print(f"二进制：{number2}")
print(f"八进制：{number8}")
print(f"十六进制：{number16}")
print(f"对应的UTF-8字符串：{repr(number_str)}\n UTF-8编码十六进制：{number_utf8_hex}\n 字节值列表：{lists}")
"""

#
# try:
#     price_unit = float(input("Enter your unit price: "))
# except ValueError:
#     print("抱歉，您输入的不是有效数字\n 程序结束")
#     exit()
# count_buy =int(input("Enter your count of buy: "))
#
# price_total = price_unit * count_buy
# if price_total > 100:
#     price_discount = price_total * 0.9
# print(f"原始总价：{price_total}元，折后价格：{price_discount} 元\n 程序结束")

# tem = input("输入温度值和单位（c/f）：")
# tem1 = tem.lower()
# tem2 =float(tem1.strip("cf"))
# tem_hua = None
# tem_she = None
# if "c" in tem1:
#     tem_hua = tem2 * 9/5 + 32
#     tem_she = tem2
# if "f" in tem1:
#     tem_she = (tem2 - 32) * 5/9
#     tem_hua = tem2
# print(f"{tem_she}摄氏度 = {tem_hua}华氏度")





