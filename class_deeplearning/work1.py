import torch
a = torch.arange(20).reshape(4, 5)
print("1. 初始张量 a:\n", a)
row_2 = a[1, :]
print("2. 第 2 行:\n", row_2)
sub_tensor = a[0:3, 1:4]
print("3. 子张量:\n", sub_tensor)
a[a > 10] = -1
print("4. 替换后的 a:\n", a)
a_reshaped = a.reshape(2, 2, 5)
print("5. 转换形状后的 a:\n", a_reshaped)