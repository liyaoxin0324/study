"""
编写一个程序，实现以下功能：
1.已知两个列表：list1 = [1, 2, 3, 4, 5, 6], list2 = [4, 5, 6, 7, 8]。
2.找出 既在list1中也存在，又在list2中也存在 的元素，放入一个新列表 common_list。
3.找出 在list1中存在，但不在list2中存在 的元素，放入一个新列表 only_in_list1。
4.打印两个新列表。
示例输出：
共有的元素: [4, 5, 6]
仅在list1中的元素: [1, 2, 3]
"""
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]
only_in_lis1 = []
set1 = set(list1)
set2 = set(list2)
common_list = set1 & set2
for x in list1:
    if x not in list2:
        only_in_lis1.append(x)
print("common_list:", common_list)
print("only_in_lis1:",only_in_lis1)


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(f"并集为：{set1 | set2},\n交集为：{set1 & set2},\n差集为：{set1 - set2},\n对称差集为：{(set1 - set2) | (set2 - set1)}")
print(f"set1是否是set2的子集{set1.issubset(set2)}\n set2是否是set1的超集{set1.issubset(set2)}\n 两个集合没有交集:{set1.isdisjoint(set2)}")

list1 = []
text1 = "banana apple apple orange banana apple grape orange apple"
text3 = text1.split(" ")
dict1 ={ char:0 for char in text3}
for x in text3:
    dict1[x] += 1
fruit_num = dict1.values()
fruit_max = max(fruit_num)
appear_max = [k for k,v in dict1.items() if v == fruit_max]
appear_only = [k for k,v in dict1.items() if v == 1]
appear_sum = sum (fruit_num)
words_input = sorted(dict1.items(), key=lambda x :x[1], reverse=True)
for key,value in dict1.items():
   per = round((value / appear_sum) * 100 ,2)
   dict1[key] = f"{per:.2f}%"
print(f"出现次数最多的次数{fruit_max}次\n\t 出现次数最多的单词：{appear_max}\n\t 不重复的单词： {appear_only}\n\t 出现的总数： {appear_sum}\n\t 排序输出： {words_input}\n\t 单词占总数百分比：{dict1}\n\t")


contacts = {
    "张三": {"phone": "13800138000", "email": "zhangsan@email.com", "group": "朋友"},
    "李四": {"phone": "13900139000", "email": "lisi@email.com", "group": "同事"},
    "王五": {"phone": "13700137000", "email": "wangwu@email.com", "group": "家人"},
}
contacts["赵六"] = {"phone": "13600136000", "邮箱": "zhaoliu@email.com", "group": "同学"}
contacts["李四"]["phone"] = "13900139111"
print("张三所有信息为：",contacts["张三"])

people_dict = { }
for name in contacts:
    group = contacts[name]["group"]
    if group not in people_dict:
        people_dict[group] = 1
    else:
        people_dict[group] = people_dict[group] + 1

email_dict = { }
for name in contacts:
    email = contacts[name].get("email","")
    email_dict[name] = email
print(f"人员分组信息为：{people_dict}\n, 邮箱包含@email.com的信息为: {email_dict}")

print("=====所有联系人=====")
for name,info in contacts.items():
    print(f"姓名：{name}")
    print(f"电话：{info.get('phone','没填')}")
    print(f"邮箱：{info.get('email','没填')}")
    print(f"分组：{info.get('group','没填')}")
    print("-" * 30)

name1 = input("请输入您要查找的姓名：")
if name1 in contacts:
    print(contacts[name1])





