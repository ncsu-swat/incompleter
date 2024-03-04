#Source: https://stackoverflow.com/questions/75463626/typeerror-only-integer-tensors-of-a-single-element-can-be-converted-to-an-index
n_inc = torch.tensor(1)
theta = torch.tensor(0.6109)
phi = torch.tensor(0)
k0 = torch.tensor(6.2832)


kinc = k0*n_inc*[torch.sin(theta)*torch.cos(phi),
                 torch.sin(theta)*torch.sin(phi), 
                 torch.cos(theta)]
print(kinc)