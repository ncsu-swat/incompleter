import numpy as np
x = np.array([1, 2, 3])
result = np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))])
print(result)