# 5.编写一个函数 safe_rename(old, new)，接收旧文件名和新文件名。
# 函数实现重命名操作，但需满足以下条件：若新文件已存在，则在文件名后添加 "(1)"（若仍存在则递增数字）再重命名；
# 若旧文件不存在，引发 FileNotFoundError。使用 os.path 和 os 模块。

import os
import os.path
def safe_rename(old, new)->str:
    if not os.path.exists(old):
        raise FileNotFoundError (f"源文件‘{old}’不存在")
    if not os.path.exists(new):
        os.rename(old, new)
        return new
    base, ext = os.path.splitext(new)
    counter = 1
    while True:
        new_name = f"{base}({counter}) + {ext}"
        if not os.path.exists(new_name):
            return new_name
        counter += 1