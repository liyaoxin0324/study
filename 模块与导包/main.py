# o在 shapelib 的 __init__.py 中，编写代码，使得当用户使用 from shapelib import * 时，
# 只能导入四个面积函数（即 circle.area 和 rectangle.area），并分别为它们起别名 circle_area 和 rect_area。
# 同时，允许用户通过 import shapelib 后使用 shapelib.circle.circumference 的方式访问周长函数。
# 编写一个测试脚本，演示这两种导入方式的使用。

# import 模块作业2.shapelib
# a1 = 模块作业2.shapelib.circle.circumference(4)
# print(f"{a1:.2f}")
# #  模块作业2 mian方法一使用
#
# from 模块作业2.shapelib import *
# circle_area = circle.area(2)
# rect_area = rectangle.area(9,8)
# print(f"{circle_area:.2f}, {rect_area:.2f}")
# 模块作业2 mian方法二使用

# o动态发现 plugins/ 目录下所有 .py 文件（排除 __init__.py 和以 _ 开头的文件）。
# o动态导入这些模块。
# o准备一个字典 data，例如 {‘input‘: ‘test‘}。
# o按顺序调用每个插件的 execute 函数，并将 data 字典传递给它们。
# （提示：使用 os.listdir, importlib.import_module）
"""
#模块作业3
import importlib
import os
#导包，importlib动态导入模块，os文件操作系统模块
data = {"input": "test"}
plugins_path = "plugins"
#包的相对路径
for file in os.listdir(plugins_path):
    if file.startswith('_') or file.startswith('__'):  #  排除 __init__.py 和以 _ 开头的文件
        continue
    module1 = file[:-3]  #将文件名.py去除
    print(module1)
    module_name = f"plugins.{module1}"   #构建完整模块路径
    module = importlib.import_module(module_name)   #动态导入模块
    if hasattr(module, "execute"):  #检查导入的模块是否有某方法或函数
        result = module.execute(data)    #调用execute函数，获取data返回值
        print(f"{module1}执行结果：{result}")
    else:
        print(f"{module1}中没有execute函数")
print("所有插件已执行完成")

"""
# o在主程序中导入 config 模块，调用 get_config() 并打印配置。修改 config.json 文件的内容，
# 尝试在程序中重新获取配置，观察行为（需要用到 importlib.reload）。

"""
模块作业4
import importlib
import time
from 模块作业4 import config
print("第一次获取配置")
print(config.getconfig())
print("程序每5秒刷新")
for round_num in range(1, 16):  # 从第 1 轮到第 15 轮
    print(f"第 {round_num} 轮倒计时：")

    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
        importlib.reload(config)
        # 重新加载模块
        print("\n重载模块后再次获取配置：")
        print(config.getconfig())
        
        
        """







