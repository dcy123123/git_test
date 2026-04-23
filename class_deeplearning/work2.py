import torch
a = torch.tensor([[1], [2], [3]])
b = torch.tensor([10, 20, 30])
print("1.张量 a:\n", a)
print("  张量 b:\n", b)
result = a + b
print("2.a + b 的结果:\n", result)
element = result[0, 2]
print("3.第1行第3列的元素:", element)
element_reshape = result.reshape(-1)
print("4.一维结果:\n", element_reshape)
reversed_tensor = element_reshape.flip(dims=[0])
print("5.逆序后:\n", reversed_tensor)