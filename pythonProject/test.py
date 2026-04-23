import torch

X = torch.arange(12, dtype=torch.float32).reshape(3, 4)
Y = torch.tensor([[2, 0, 1, 4], [2, 0, 1, 4], [2, 0, 1, 4]])  # 改成 (3, 4)

before = id(Y)
# Y = Y + X  # 这个操作会创建一个新的张量，Y 的地址会改变
Y = Y.float()  # 将 Y 转为 float32
Y += X  # 原地修改，地址不变
after = id(Y)

print("操作前 Y 的地址:", before)
print("操作后 Y 的地址:", after)
print("地址是否相同:", before == after)  # 输出 False，因为 Y 是新创建的


Z = torch.zeros_like(Y)
print(id(Z))
Z[:] = X + Y
print(id(Z))

