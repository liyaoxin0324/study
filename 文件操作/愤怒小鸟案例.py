# 1.2.1Birds 基类
# 1）设计目的
# 作为所有小鸟类的基类，它定义了小鸟的通用属性和行为，为后续具体小鸟类的扩展提供基础框架，体现了面向对象编程中的抽象和封装思想。
# 2）属性设计
# name：用于标识每只小鸟的名称，方便区分不同个体。
# color：代表小鸟的颜色，这是小鸟的一个显著特征，在游戏中可以对应不同类型的小鸟。
# skill_description：描述小鸟所具备的独特技能，让玩家了解每只小鸟的特殊能力。
# 3）方法设计
# fly()：描述小鸟飞行的基本动作，是小鸟在游戏中的常见行为，所有子类都可以重写该方法来展示不同的飞行特点。
# call()：模拟小鸟发出叫声的行为，同样可以被子类重写以体现不同小鸟的叫声差异。
# use_skill()：用于触发小鸟的特殊技能，展示小鸟使用技能的情况，子类可以根据自身技能特点进行相应实现。


class Birds():
    def __init__(self, name, color, skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description
    def __fly__(self):
        print(f"{self.name}飞行中")
    def call(self):
        print(f"{self.name}正在叫")
    def use_skill(self):
        print(f"{self.name}使用了技能{self.skill_description}")


# 继承自Birds基类，每个子类代表一种特定颜色的小鸟，它们在继承基类属性和方法的基础上，重写部分方法以展示不同小鸟的独特行为和技能，体现了面向对象编程中的继承和多态思想。
# 2）属性设计
# 通过调用基类的__init__方法，初始化各自的name、color和skill_description属性，确保每只小鸟都有自己的独特标识和技能。
# 3）方法设计
# fly()：重写基类的fly()方法，展示不同小鸟的飞行特点，如红鸟以稳定速度飞行，黄鸟快速飞行，蓝鸟优雅飞行。
# call()：重写基类的call()方法，模拟不同小鸟的叫声，增加游戏的趣味性。


class RedBird(Birds):
    def __init__(self, name):
        super().__init__(name,"red","单倍伤害，单倍飞行速度，目标命中率100%")
        self.name = name

    def fly(self):
        print("飞行稳定，单倍飞行速度,100%命中率")
    def call(self):
        print("叫一声，呱")


class BlueBird(Birds):
    def __init__(self, name):
        super().__init__(name,"blue","2倍伤害，2倍飞行速度，目标命中率80%")
        self.name = name
    def fly(self):
        print("2倍飞行速度，飞行不稳定，80%命中率")
    def call(self):
        print("叫2声，咕")


class GreenBird(Birds):
    def __init__(self, name):
        super().__init__(name,"green","4倍伤害，4倍飞行速度，目标命中率50%")
        self.name = name
    def fly(self):
        print("4倍飞行速度，飞行不稳定，50%命中率")
    def call(self):
        print("叫4声，哇")

# 代表游戏中的障碍物，如木头堡垒、石头塔楼等，负责处理障碍物被小鸟攻击的逻辑，与小鸟类进行交互，体现了面向对象编程中的对象交互和封装思想。
# 2）属性设计
# name：标识障碍物的名称，方便区分不同类型的障碍物。
# strength：表示障碍物的强度，即它能够承受的伤害值，当强度降为 0 时，障碍物被摧毁。
# 3）方法设计
# be_attacked(bird)：模拟障碍物被小鸟攻击的过程，根据小鸟的类型计算伤害，并更新障碍物的强度，同时输出攻击和受损信息，让玩家了解游戏进展。


class Obstacle:
    def __init__(self, name,strength):
        self.strength = strength
        self.name = name

    def be_attacked(self,bird):
        if self.strength <= 0:
            return
        print(f"{bird.name}飞向{self.name}")
        bird.use_skill()
        if isinstance(bird,RedBird):
            damage = 20 * 1
        elif isinstance(bird,BlueBird):
            damage = 20 * 2 * 0.8
        elif isinstance(bird,GreenBird):
            damage = 20 * 4 * 0.5
        self.strength -= damage
        if self.strength <= 0:
            print(f"{self.strength}已摧毁建筑物")
        else:
            print(f"{self.name}还剩余{self.strength}")


if __name__ == '__main__':
    red_bird = RedBird("红鸟")
    blue_bird = BlueBird("蓝鸟")
    green_bird = GreenBird("绿鸟")
    obstacle1 = Obstacle("土堡",20)
    obstacle2 = Obstacle("tower",1000)
    print("=== 小鸟能力测试 ===")
    red_bird.fly()
    red_bird.call()
    red_bird.use_skill()
    print()
    blue_bird.fly()
    blue_bird.call()
    blue_bird.use_skill()
    print()
    green_bird.fly()
    green_bird.call()
    green_bird.use_skill()
    print()
    print("=== 攻击障碍物测试 ===")
    obstacle1.be_attacked(red_bird)
    obstacle1.be_attacked(blue_bird)
    obstacle1.be_attacked(green_bird)
    print()

    obstacle2.be_attacked(red_bird)
    obstacle2.be_attacked(blue_bird)
    obstacle2.be_attacked(green_bird)
    print()

    print("\n=== 多态性测试 ===")
    birds = [red_bird, blue_bird, green_bird]
    for bird in birds:
        bird.fly()






