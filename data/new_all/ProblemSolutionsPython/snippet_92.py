import pandas as pd
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
print("Original array:")
print(df)
print("\nDataframe - Gradient color:")
df.style.background_gradient(subset=['C'])