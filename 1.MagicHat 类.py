'''1.MagicHat类
MagicHat 类：小慧是一位小魔术师，她有一顶神奇的魔法帽子，可以根据她的心情改变颜色。请使用描述符和 property 实现一个 MagicHat 类，使得小慧可以设置帽子的颜色，
并且每次获取帽子的颜色时，都会显示一个神奇的特效。

要求：
创建一个 MagicHat 类，其中包含 color 属性。
使用描述符和 property 实现对 color 属性的设置和获取。
每次获取帽子的颜色时，程序应该显示一个神奇的特效。
小慧可以通过属性设置帽子的颜色。
程序应该能够打印出帽子的颜色。'''

# 定义一个描述符类，用于管理帽子的颜色属性
class ColorDescriptor:
    def __init__(self):
        # 初始化颜色为None
        self._color = None

    # 获取属性时调用的方法
    def __get__(self, instance, owner):
        # 如果实例为空，则返回描述符本身
        if instance is None:
            return self
        # 打印颜色变化的消息
        print("当前帽子的颜色为",end="")
        # 返回当前颜色
        return self._color

    # 设置属性时调用的方法
    def __set__(self, instance, value):
        # 打印颜色变化前后的信息
        print(f"帽子颜色从 {self._color} 变为 {value}")
        # 更新颜色值
        self._color = value


# 定义一个魔术帽类，使用描述符管理颜色属性
class MagicHat:
    # 将ColorDescriptor实例作为类属性
    color = ColorDescriptor()

    # 构造方法，初始化魔术帽的颜色
    def __init__(self, color):
        # 使用描述符设置帽子的初始颜色
        self.color = color  # 这里调用了__set__方法


# 示例
hat = MagicHat('蓝色')  # 创建一个魔术帽对象，并初始化颜色为蓝色
print(hat.color)  # 调用 ColorDescriptor 的 __get__ 方法
                 
                
hat.color = '红色'   # 调用 ColorDescriptor 的 __set__ 方法
print(hat.color)  # 输出: 帽子颜色从 蓝色 变为 红色


                
