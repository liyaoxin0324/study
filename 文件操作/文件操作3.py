# # 3.编写一个函数 find_largest_file(directory)，接收一个目录路径，
# # 递归查找该目录及其子目录中最大的文件（按字节数），返回该文件的绝对路径和大小。
# # 若目录为空或不存在，返回 (None, 0)。使用 os 和 os.path 模块。
#
import os
def find_largest_file(directory):
    largest_size = 0
    largest_file = None
    if not os.path.exists(directory) or not os.path.isdir(directory):
        return None, 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
    try:
        size = os.path.getsize(filepath)
        if size > largest_size:
            largest_size = size
            largest_file = filepath
    except OSError:
        continue
    return largest_file, largest_size



