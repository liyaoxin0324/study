# 4.实现一个简单的上下文管理器FileLogger，用于记录文件操作日志：
# o在enter方法中打开日志文件（追加模式），记录进入with块的时间
# o在exit方法中记录退出with块的时间，并关闭文件
# o如果with块中发生异常，在日志中记录异常信息
# 编写测试代码，演示正常情况和异常情况下的日志记录。


import datetime
class FileLogger:
    def __init__(self,filename):
        self.filename = filename
        self.file = None
    def __enter__(self):
        self.file = open(self.filename,"a",encoding="utf-8")
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.file.write(f"[{now_time}]进入with模块\n")
        self.file.flush()
        return self

    def __exit__(self,exc_type, exc_value, exc_tb):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if exc_type is None:
            self.file.write(f"[{now_time}]正常退出with模块\n")
        else:
            self.file.write(f"[{now_time}]发生异常：{exc_type.__name__}:{exc_value}\n")
        self.file.write(f"[{now_time}] 关闭日志文件\n")
        self.file.close()
        return False

if __name__ == '__main__':
    print("测试1：正常情况")
    with FileLogger("test.log") as logger:
        # 在with块中执行一些操作
        result = 10 + 20
        print(f"计算: 10 + 20 = {result}")
    print("\n测试2：异常情况 - 除零错误")

    try:
        with FileLogger("test.log") as logger:
            result = 10 / 0  # 这会引发除零错误
    except ZeroDivisionError as e:
        print(f"捕获到异常: {e}")

    print("\n测试3：异常情况 - 值错误")
    try:
        with FileLogger("test.log") as logger:
            num = int("不是数字")  # 这会引发值错误
    except ValueError as e:
        print(f"捕获到异常: {e}")

    print("\n日志文件内容：")
    with open("test.log", 'r', encoding='utf-8') as f:
        print(f.read())






