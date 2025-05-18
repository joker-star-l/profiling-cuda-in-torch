class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: "f32[10, 10]"):
         # File: /volumn/gpumode/profiling-cuda-in-torch/compile_square.py:7 in square, code: return x * x
        mul: "f32[10, 10]" = torch.ops.aten.mul.Tensor(arg0_1, arg0_1);  arg0_1 = None
        return (mul,)
        