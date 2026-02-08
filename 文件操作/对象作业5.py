# 5.实现一个FileHandler上下文管理器类（模拟）。
# 要求：
# 这个类不是使用with语句和__enter__， __exit__， 而是模拟资源管理。
# 类有__init__方法，接受一个filename参数。
# 有open方法，打印“打开文件 [filename]”， 并将一个标志_is_open设为True。
# 有close方法，打印“关闭文件 [filename]”， 并将_is_open设为False。
# 实现__del__方法。在__del__中，如果文件还未关闭（_is_open为True）， 则自动调用close方法并打印警告信息
# ：“警告：对象被销毁时文件未关闭，已自动关闭。”
# 编写代码测试：创建一个FileHandler对象，调用open但不调用close，然后删除对象或让对象离开作用域，观察__del__的行为。
# 再测试正常open和close的情况。


class FileHandler():
    def __init__(self, filename):
        self.filename = filename
        self._is_open = False

    def open(self):
        self._is_open = True
        print(f"打开文件{self.filename}")

    def close(self):
        self._is_open = False
        print(f"关闭文件{self.filename}")

    def __del__(self):
        if self._is_open :
            self.close()
            print("警告：对象被销毁时文件未关闭，已自动关闭。")

if __name__ == '__main__':

    FileHandler = FileHandler("test.txt")
    FileHandler.open()
    FileHandler.__del__()
    FileHandler.open()
    FileHandler.close()











