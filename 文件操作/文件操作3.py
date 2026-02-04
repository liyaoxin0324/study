# 3.编写一个函数 find_largest_file(directory)，接收一个目录路径，
# 递归查找该目录及其子目录中最大的文件（按字节数），返回该文件的绝对路径和大小。
# 若目录为空或不存在，返回 (None, 0)。使用 os 和 os.path 模块。

import os
def find_largest_file(directory):

