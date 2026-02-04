# 编写一个字符串处理工具集，包含以下函数：
# 1.统计字符串中各种字符类型的数量（字母、数字、空格、其他）
# 2.检查字符串是否为回文（正读反读都一样）
# 3.将字符串中的单词反转顺序
# 4.统计每个单词出现的频率
# 5.将字符串转换为标题格式（每个单词首字母大写）
# 6.主函数提供交互式菜单供用户选择功能


# 1.统计字符串中各种字符类型的数量（字母、数字、空格、其他）
def type_str_count():
    str_input = input("请输入您想要统计的文本：")
    str1 = str_input.strip(" ")
    str_split = str1.split(" ")
    count_digit = 0
    count_alpha = 0
    count_space = 0
    count_else = 0
    for char in str_split:
        if char.isdigit():
            count_digit += 1
        if char.isalpha():
            count_alpha += 1
        if char.isspace():
            count_space += 1
        else:
            count_else += 1
    print(f"您输入文本中存在的数字个数为：{count_digit}")
    print(f"您输入文本中存在的字母个数为：{count_alpha}")
    print(f"您输入文本中存在的空格个数为：{count_space}")
    print(f"您输入文本的其余字符数量为：{count_else}")

# 2.检查字符串是否为回文（正读反读都一样）
def str_palindrome():
    str_input = input("请输入您想要统计的文本：")
    str1 = str_input.strip(" ")
    str_split = str1.split(" ")
    palindrome_list = []
    reverse_1 = []
    for char in str_split:
        palindrome_list.append(char)
        reverse_1 = palindrome_list[::-1]
        if  reverse_1 == palindrome_list:
            print(f"您输入文本的类型属于回文{palindrome_list}\n{reverse_1}")

# 3. 将字符串中的单词反转顺序
def words_revers():
    str_input = input("请输入您想要统计的文本：")
    str1 = str_input.strip()
    str_split = list(str1)
    words_list = str_split.copy()
    words_list.reverse()
    for char in str_split:
        words_list.append(char)

    print(f"将您输入的单词反转顺序：{''.join(words_list)}")

# 4.统计每个单词出现的频率
def words_count():
    str_input = input("请输入您想要统计的文本：")
    str1 = str_input.strip()
    str_split = str1.split()
    words_dict = {}
    for char in str_split:
        words_dict[char] = words_dict.get(char, 0) + 1
    for words, count in words_dict.items():
        print(f"单词{words}出现次数统计{count}")

# 5.将字符串转换为标题格式（每个单词首字母大写）
def title_text():
    str_input = input("请输入您想要统计的文本：")
    str1 = str_input.strip()
    str_split = str1.split()
    filtered_text = ' '.join(char for char in str_split if char.isalpha() or char == ' ')
    print(f"将您输入的文本更改为标题模式：{filtered_text.title()}")

# 6.主函数提供交互式菜单供用户选择功能
def main():
 while True:
    num_select = int(input(
                           "1.统计字符串中各种字符类型的数量（字母、数字、空格、其他）\n"
                           "2.检查字符串是否为回文（正读反读都一样）\n"
                           "3.将字符串中的单词反转顺序\n"
                           "4.统计每个单词出现的频率\n"
                           "5.将字符串转换为标题格式（每个单词首字母大写）\n"
                           "6.退出程序\n"
                            "请选择你要处理的工具选项："))
    match num_select :
        case 1:
            type_str_count()
        case 2:
            str_palindrome()
        case 3:
            words_revers()
        case 4:
            words_count()
        case 5:
            title_text()
        case 6:
         break
print("代码运行成功")

if __name__ == '__main__':
    main()

