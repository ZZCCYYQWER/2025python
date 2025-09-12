def use_sum():
    """
    学习算数运算符
    :return:
    """
    a = 5 / 2
    print(a)


def use_logic():
    """
    使用逻辑运算符
    :return:
    """
    # and是遇假则假，都真返回后一个
    # or是遇真则真，否则返回前一个
    print(3 and 5)
    print(0 or 8)
    3 and print('hello')  # 短路运算


def use_bit():
    """
    使用位运算
    :return:
    """
    # 整数以补码形式存储在内存中
    print(5 & 7)    # 按位与
    print(5 | 7)    # 按位或
    print(~5)       # 取反
    print(5 ^ 7)    # 异或
    # python中左移不存在丢位，永远是*2
    print(5<<1)

    # 右移正数高位补0，负数高位补1
    print(5>>1)
    
#use_sum()
#use_logic()
use_bit()
