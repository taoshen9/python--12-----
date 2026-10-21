'''2.Calculator 类
编写一个 Calculator 类，其中包括公有属性 name（计算器名称）和私有属性 __result（计算结果）。
类还应该提供公有加法 add()、减法subtract()、乘法multiply() 和 除法divide()，用于执行相应的数学运算，并将结果存储到私有属性 __result 中。
还应提供公有方法 get_result()，用于获取计算结果。
'''

class Calculator:
    def __init__(self, name):
        self.name = name  # 公有属性，计算器名称
        self.__result = 0  # 私有属性，计算结果

    def add(self, a, b):
        """加法操作"""
        self.__result = a + b

    def subtract(self, a, b):
        """减法操作"""
        self.__result = a - b

    def multiply(self, a, b):
        """乘法操作"""
        self.__result = a * b

    def divide(self, a, b):
        """除法操作"""
        if b != 0:
            self.__result = a / b
        else:
            raise ValueError("除数不能为零")

    def get_result(self):
        """获取计算结果"""
        return self.__result

# 示例
calc = Calculator("简单计算器")
calc.add(5, 3)
print(calc.get_result())  # 输出: 8

calc.subtract(10, 4)
print(calc.get_result())  # 输出: 6

calc.multiply(7, 2)
print(calc.get_result())  # 输出: 14

calc.divide(14, 2)
print(calc.get_result())  # 输出: 7.0
