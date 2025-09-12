a=1
b=1
# 两个变量地址一致，本质上都是数据1的地址
print(id(a))
print(id(b))

# python的变量设计：一切皆引用
a = 2       # a相当于又挂在数据2上
print(id(a))

print(type(a))