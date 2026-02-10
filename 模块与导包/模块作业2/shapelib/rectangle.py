# o在 rectangle.py 中定义函数 area(length, width) 和 perimeter(length, width)。
# o在 shapelib 的 __init__.py 中，编写代码，使得当用户使用 from shapelib import * 时，
# 只能导入四个面积函数（即 circle.area 和 rectangle.area），并分别为它们起别名 circle_area 和 rect_area。
# 同时，允许用户通过 import shapelib 后使用 shapelib.circle.circumference 的方式访问周长函数。
# 编写一个测试脚本，演示这两种导入方式的使用。

def area(length, width):
    area_q = length * width
    return area_q
def perimeter(length, width):
    perimeter_q = length * 2 + width * 2
    return perimeter_q

