# list1 = []
# str1 = input("请输入您想添加的整数：")
# str2 = str1.strip(" ")
# str3 =str2.split(" ")
# for i in str3:
#     list1.append(int(i))
# list2 = sorted(list1)
# list3 = []
# for num in list2:
#     if num not in list3:
#        list3.append(num)
# list4 = sorted(list3)
# print(list4)

import re
list1 = []
list2 = []
str1 = input("请输入一段英文文本：")
str2 = str1.strip(" ")
str_lower = str2.lower()
str_title = str_lower.title()
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for char in str1:
    if char.isalpha():
        count1 += 1
    elif char.isdigit():
        count2 += 1
    elif char == " ":
        count3 += 1
    words = re.findall("[A-Za-z]+", str2)
    count4 = len(words)
    list2 = str1.split(" ")
str3 = str2.split(" ")

dict1 = {}
for char in str_lower:
    if char.isalnum():
        dict1[char] = dict1.get(char,0) + 1
sort_dict = sorted(dict1.items(), key=lambda x : x[1], reverse=True)
sort_top = sort_dict[:3]
for i in str3:
    list1.append(i)
    len(list1)
print(f"列表为{list1}\n总字符数为{len(str1)}")
print(f"字母数为{count1}")
print(f"数字个数是{count2}")
print(f"空格个数是{count3}")   #未完成
print(f"单词个数是{count4}")
print(f"首字母大写格式为：{str_title}")
print(f"出现频率最高的单词个数是：{sort_top}")




# str1 = input("请输入数字或汉字：")
# str2 = str1.strip(",")
# str3 =str2.split(",")
# if str1.isalpha :
#     print(str1[::-1])
#
#
#
#
# numbers = []
# num_avg = ""
# while True:
#     num1 =int( input("请输入整数："))
#     if num1 < 0:
#         break
#     else:
#         numbers.append(num1)
#         num_avg = sum(numbers) / len(numbers)
#     print(f"列表为：{numbers}\n 平均值为：{num_avg:.2f}")


