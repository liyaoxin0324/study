# 其中定义了一个全局变量 count = 0 和一个函数 increment()，
# 该函数将 count 加1并打印当前值。
# 编写主程序 reload_test.py：

count = 0
def increment():
    global count
    count += 1
    return count


