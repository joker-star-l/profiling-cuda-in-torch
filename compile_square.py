import os
import torch

os.environ["TORCH_COMPILE_DEBUG"] = "1"

def square(x):
    return x * x

compiled_square = torch.compile(square)
x = torch.randn(10, 10, device='cuda')
print(compiled_square(x))
