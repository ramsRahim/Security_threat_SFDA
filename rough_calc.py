import torch
from torch import nn
from matplotlib import pyplot as plt
# %matplotlib inline

class MinSvd(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        
    def forward(self, w):
        w = w.flatten(2)
        # print(w.shape)
        vals = torch.linalg.svdvals(w)
        return vals.norm(2)
    
    
def func(**kwargs):
    print(kwargs)
    
kwargs = {'a': 1, 'b': True, 'c': 'first'}

# func(a=1, b=True)
a = torch.rand(1,3)

print(a)
print(a.abs().sum())
print(a.norm(1))