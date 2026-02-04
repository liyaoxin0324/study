# 使用函数重构学生成绩管理系统：
# 1. 使用字典存储学生信息，键为学号，值为包含姓名和成绩的字典
# 2. 实现添加、删除、修改、查询、统计、排序等功能函数
# 3. 每个函数职责单一，参数和返回值明确
# 4. 使用函数实现自定义排序（选做）
# 5. 主函数提供完整的用户交互界面


# 1. 使用字典存储学生信息，键为学号，值为包含姓名和成绩的字典
dict_student = {
    1:{"name":"mary","grade":84},
    2:{"name":"john","grade":64},
    3:{"name":"dong","grade":42},
    4:{"name":"张三","grade":99},
    5:{"name":"李四","grade":85},
    6:{"name":"孙悟空","grade":75},

}

# 添加学生信息
def add_student():
    """添加学生信息"""
    id_add = int(input("您要添加的Id为："))
    if id_add  in dict_student:
        print(f"错误，您要添加的Id{id_add}已存在，无法重复添加")
        return
    name_add = str(input("您要添加的姓名为："))
    grade_add = int(input("您要添加的成绩为："))
    dict_student[id_add] = {
    "name" : name_add,
    "grade" : grade_add
}
    print(f"学生Id{id_add}({name_add})添加成功")


def del_student():
    """删除学生信息"""
    id_del = int(input("您要删除的Id为："))
    if id_del not  in dict_student:
        print(f"错误，您要删除的Id{id_del}不存在，请先添加id")
        return
    del dict_student[id_del]
    print(f"学生Id{id_del}删除成功")



def alter_student():
    """修改学生信息"""
    id_input = int(input("您要修改的Id为："))
    if id_input  in dict_student:
        name_alter = str(input("您想要将姓名修改为："))
        grade_alter = int(input("您想要将成绩修改为："))
        dict_student[id_input] = {
        "name" : name_alter,
        "grade" : grade_alter
        }
        print(f"学生Id为：{id_input}学生姓名修改为：({name_alter})学生成绩修改为：({grade_alter})")


def inquire_student():
    """查询学生信息"""
    id_input = int(input("1.您要查询的Id为：\n"
                         "2.查询全部学生信息\n"
                         "3.退出查询\n"
                         "选择您的功能："))
    match id_input:
        case 1:
            id_input = int(input("请输入Id查询："))
            if id_input  in dict_student:
                print(f"您查询Id{id_input}的信息为：({dict_student[id_input]})")
        case 2:
            print("==========学生信息=============\n"
                  f"{dict_student}")
        case 3:
            return
        case _:
            print("您想要查询的学生Id不存在，请先添加")


def sta_student():
    """统计用户输入的学生成绩区间，找到符合区间的学生输出"""
    global dict_student
    grade_max_input = (input("您想要查询的成绩区间上限为，不输入默认为100："))
    grade_max = int(grade_max_input) if grade_max_input.strip() else 100
    grade_min_input = input("您想要查询的成绩区间下限为，不输入默认为0：")
    grade_min = int(grade_min_input) if grade_min_input.strip() else 0
    print(f"\n成绩在【{grade_min} - {grade_max}】区间的学生信息：")
    match_count = 0
    for id_stu in dict_student.values():
        student_name = id_stu.get("name")
        student_grade = id_stu.get("grade")
        if grade_min <= student_grade <= grade_max:
            print(f"学生姓名：{student_name},成绩为：{student_grade}")
            match_count += 1
        if match_count == 0:
            print("暂无符合成绩区间的学生信息")

def sort_student():
    """按成绩从小到大排序"""
    global dict_student
    student_sort = sorted(dict_student.items(), key=lambda item: item[1]["grade"], reverse=True)
    for student_id, student_info in student_sort:
        student_name = student_info["name"]
        student_grade = student_info["grade"]
        print(f"ID: {student_id :<2} | 姓名: {student_name :<10} | 成绩: {student_grade :<5}")


def main():
    while True:
        num_select = int(input("============学生管理系统============\n"
                           "1.添加学生\n"
                           "2.删除学生\n"
                           "3.修改学生信息\n"
                           "4.查询学生信息\n"
                           "5.查找成绩区间学生\n"
                           "6.成绩排序\n"
                           "7.退出\n"
                           "请选择功能"))
        match num_select:
            case 1:
                add_student()
            case 2:
                del_student()
            case 3:
                alter_student()
            case 4:
                inquire_student()
            case 5:
                sta_student()
            case 6:
                sort_student()
            case 7:
                break


if __name__ == '__main__':
    main()