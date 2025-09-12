a = [1, 2, 3, 4, 5]
b = [2, 3, 4]
print(f'数据{a},地址{id(a)}')
print(a * 2)
a += b  # 等价于a.extend(b),a的地址不变
print(f'操作后，数据{a},地址{id(a)}')

# a = a + b  # 相当于对a重新赋值，a的地址改变
# print(f'操作后，数据{a},地址{id(a)}')

print(a[2:6])
