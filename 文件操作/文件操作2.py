# 2.编写一个函数 copy_file_skip_lines(src, dst, skip_lines)，接收源文件路径 src、
# 目标文件路径 dst 和一个整数 skip_lines。函数将 src 文件内容复制到 dst 文件，
# 但跳过前 skip_lines 行。使用 with 语句确保文件正常关闭，注意处理文件不存在等异常。


import  os
def  copy_file_skip_lines(src, dst, skip_lines):
    if not os.path.exists(src):
        raise FileNotFoundError(f"源文件{src}不存在")
    try:
        with open(src, "r", encoding="utf-8") as source_file:
            lines = source_file.readlines()
        with open(dst, "w", encoding="utf-8") as target_file:
            target_file.writelines(lines[skip_lines:])
    except FileNotFoundError  as e:
        print(f"文件错误：{e}")
    except IOError as e:
        print(f"读写错误：{e}")
    except Exception as e:
        print(f"未知错误：{e}")
copy_file_skip_lines("./test2026", "wad", 1)




