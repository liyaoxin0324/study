# 4.创建一个Vector2D类表示二维向量(x， y)。
# 要求：
# 在__init__中初始化x和y。
# 实现__add__特殊方法，支持两个向量相加（x相加，y相加），返回一个新的Vector2D对象。
# 实现__sub__特殊方法，支持两个向量相减。
# 实现__mul__特殊方法，支持向量与标量（数字）相乘（x和y分别乘以标量），返回新向量。
# 实现__str__方法，返回如“(3.0， 4.0)”的字符串。
# 实现__repr__方法，返回如“Vector2D(3.0， 4.0)”的字符串，使得eval(repr(v))能创建一个相同的向量。
# 编写代码测试向量的加、减、标量乘法，并打印其str和repr表示


class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar.x, self.y * scalar.y)
    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"
    def __repr__(self):
        return f"Vector2D({self.x:.1f}, {self.y:.1f})"
    # def __repr__(self):



if __name__ == '__main__':
    V1 = Vector2D(2,3)
    V2 = Vector2D(4,5)
    print(f"V1.__str__():{V1}")
    print(f"V1.__str__():{V2}")
    V3 = V1.__add__(V2)
    print(f"V3.__str__():{V3}")
    V4 = V1.__sub__(V2)
    print(f"V4.__str__():{V4}")
    V5 = V1.__mul__(V2)
    print(f"V5.__str__():{V5}")
    print(V5.__repr__())
    v_recreated = eval(repr(V1))
    print(f"通过 eval(repr(v1)) 重建的向量: {v_recreated}")
    print(f"重建向量是否相等: {V1.x == v_recreated.x and V1.y == v_recreated.y}")
