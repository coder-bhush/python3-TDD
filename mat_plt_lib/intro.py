# Introductio to matplotlib


# Checking Matplotlib Version
import matplotlib

print(matplotlib.__version__)

# Matplotlib Pyplot :

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
