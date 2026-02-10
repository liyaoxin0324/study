# o在 circle.py 中定义函数 area(radius) 和 circumference(radius)。
# o在 rectangle.py 中定义函数 area(length, width) 和 perimeter(length, width)。
# o在 shapelib 的 __init__.py 中，编写代码，使得当用户使用 from shapelib import * 时，
# 只能导入四个面积函数（即 circle.area 和 rectangle.area），并分别为它们起别名 circle_area 和 rect_area。
# 同时，允许用户通过 import shapelib 后使用 shapelib.circle.circumference 的方式访问周长函数。
# 编写一个测试脚本，演示这两种导入方式的使用。

pi = 3.1415926

def area(radius):
    area_c = pi * radius * radius
    return area_c
def circumference(radius):
    circumference_c = pi * radius * 2
    return circumference_c






