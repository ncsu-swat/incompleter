import numpy as np
import matplotlib.pyplot as plt
bins = np.array([0, 1, 2, 3])
print('nums: ', nums)
print('bins: ', bins)
print('Result:', np.histogram(nums, bins))
plt.hist(nums, bins=bins)
plt.show()