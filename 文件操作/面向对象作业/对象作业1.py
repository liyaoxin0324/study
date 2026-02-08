# 1.定义一个Student类。
# 要求：
# 使用__init__方法初始化学生的name（姓名）和__score（私有属性，成绩）。
# 使用@property和@score.setter实现一个名为score的属性。
# ogetter返回成绩。
# osetter在设置成绩时进行验证：成绩必须在0到100之间（包含0和100），否则抛出ValueError异常，
# 并提示“成绩必须在0-100之间”。
# 实现__str__方法，返回字符串如：“学生张三，成绩：85”。
# 编写代码创建Student对象，尝试设置合法和非法的成绩，并打印学生信息。


# class Student():
#     """建立学生类，输入姓名，成绩"""
#     def __init__(self, name:str, score:int):
#         self.name = name
#         self.__score = score
#         return
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, value:int):
#         if value < 0 and value > 100 :
#             raise ValueError("成绩必须在0-100之间")
#         else:
#             self.__score = value
#
#     def __str__(self):
#         return f"学生{self.name}，成绩{self.score}"

class Student:

    def __init__(self,name,score:int):
        self.name = name
        if score < 0 or score > 100:
            raise ValueError("成绩必须在0-100之间")
        else:
            self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0 or value > 100:
            raise ValueError("参数类型错误")
        else:
            self.__score = value

    def __str__(self):
        return f"学生{self.name},成绩{self.__score}"


s3 = Student("张四",99)
s5 = Student("赵六", 64)
s6 = Student("迅七", 50)

if __name__ == '__main__':
    print(s3)
    s3.score = -1

    print(s5)
    print(s6)



