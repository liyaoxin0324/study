# 2.设计一个Singleton类（单例模式）。
# 要求：
# 重写__new__方法，确保这个类在整个程序中最多只有一个实例。
# 提示：在__new__中，检查类是否已经有一个实例存储在类属性中（例如_instance），如果没有，则调用父类的__new__创建并存储；如果有，则直接返回存储的实例。
# 提供一个__init__方法用于初始化（注意：在单例模式中，__init__可能会被多次调用，需要小心处理，例如可以设置一个标志位_initialized来避免重复初始化）。
# 在__init__中接受一个value参数，并将其赋值给实例的data属性。
# 编写代码测试，创建两个Singleton对象，检查它们是否是同一个对象（id()是否相同），并打印它们的data属性。

class Singleton():
    _instance = None
    _initialized = False
    def __new__(cls, *args, **kwargs):   #
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    def __init__(self,value):
        if not self._initialized:
            self.data = value
            self._initialized = True
if __name__ == '__main__':
    s1 = Singleton(10)
    s2 = Singleton(20)
    print(f"s1id  =  {id(s1)}")
    print(f"s2id  =  {id(s2)}")
    print(f"s1和s2是否为同一对象：{s1 is s2}")
    print(f"s1属性为: {s1.data}")
    print(f"s2属性为: {s2.data}")





