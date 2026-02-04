# 1.编写一个函数 file_info(filepath)，接收一个文件路径，返回一个字典，
# 包含以下键值：'exists'（布尔，路径是否存在）、'size'（整数，文件大小，若不存在则为0）
# 、'is_file'（布尔，是否为文件）、'is_dir'（布尔，是否为目录）。要求使用 os.path 模块。
import  os
def file_info(filepath):
    exists = os.path.exists(filepath)
    if exists:
        size = os.path.getsize(filepath)
    else:
        size = 0
    is_file = os.path.isfile(filepath) if exists else False
    is_dir = os.path.isdir(filepath) if exists else False
    return{
        "exists":exists,
        "size":size,
        "is_file":is_file,
        "is_dir":is_dir
    }
print(file_info("./test20260203.txt"))

