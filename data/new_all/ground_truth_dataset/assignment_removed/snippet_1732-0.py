import numpy as np
print('Given array:')
print(n_arr)
print('\nRemove all columns containing non-numeric elements ')
print(n_arr[:, ~np.isnan(n_arr).any(axis=0)])