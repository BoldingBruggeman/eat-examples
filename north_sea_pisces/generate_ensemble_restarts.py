import eatpy
import numpy as np
N = 20    # ensemble size
my=0.0
sigma=0.1
with eatpy.models.gotm.RestartEnsemble("restart.nc", N) as f:
    for name, values in f.template.items():
        if name in ("temp", "salt"):
            # select of one of the methods for shape
            #shape = (N,) + values.shape  # scalar offset
            shape = (N,) + (1,)*values.ndim  # profile offset
            offset = np.random.normal(my, sigma, size=shape)
            f[name] = values + offset

