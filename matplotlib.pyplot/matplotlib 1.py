import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,2,3],[3,5,6],'ro')

t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()