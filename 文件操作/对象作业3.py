# 3.实现一个LimitedInstances类。
# 要求：
# 这个类限制最多只能创建3个实例。
# 重写__new__方法，在创建新实例前进行检查。
# 使用一个类属性（例如_instances列表）来跟踪已创建的实例。
# 如果当前实例数量未达到上限（3个），则创建新实例并将其加入列表，然后返回。
# 如果已达到上限，则抛出RuntimeError异常，提示“已达到最大实例数量限制（3个）”。
# 注意：需要考虑实例被销毁（del）的情况，以释放名额。可以在__del__方法中将实例从列表中移除（注意：__del__的调用时机不确定，此题为简化逻辑，假设在del对象后立即调用）。
# 编写代码测试，尝试创建第4个实例，观察是否抛出异常。



class LimitedInstances:
    _instance = []
    _max_instances = 3
    def __new__(cls, *args, **kwargs):  #分配空间，返回实例对象
        if len(cls._instance) >= cls._max_instances:
            raise RuntimeError("已达最大实例数量限制（3个）")
        instance = super(LimitedInstances, cls).__new__(cls)
        cls._instance.append(instance)
        return instance
    def __del__(self):
        if self in LimitedInstances._instance:
            LimitedInstances._instance.remove(self)

if __name__ == '__main__':
    try:
        print("创建第一个实例")
        obj1 = LimitedInstances()
        print(f"当前实例数：{len(LimitedInstances._instance)}")
        print("创建第2个实例")
        obj2 = LimitedInstances()
        print(f"当前实例数：{len(LimitedInstances._instance)}")
        print("创建第3个实例")
        obj3 = LimitedInstances()
        print(f"当前实例数：{len(LimitedInstances._instance)}")
        print("创建第4个实例")
        obj4 = LimitedInstances()
    except RuntimeError as e:
        print(f"错误：{e}")
        print("\n删除obj1后")
        del obj1
        print(f"当前实例数：{len(LimitedInstances._instance)}")
        print("\n尝试再次创建实例...")
        try:
            obj4 = LimitedInstances()
            print(f"创建成功！当前实例数: {len(LimitedInstances._instances)}")
        except RuntimeError as e:
            print(f"错误: {e}")


