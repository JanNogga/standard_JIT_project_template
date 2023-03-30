import torch
from lib.module_name import custom_add

A = torch.ones(16).cuda()
B = 5*A

# custom add is now loaded just-in-time if necessary
# this is specified by load() in lib.module_name.py
# in turn, that points to the kernel defined in lib/cuda/dummy.{cpp,cu}
print(custom_add(A,B))