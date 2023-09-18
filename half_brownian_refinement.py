import numpy as np
import matplotlib.pyplot as plt
import h_b_r as hbr

a, b, c, d = hbr.refined_brownian_2n(1, 100)

plt.plot(a, c, 'r-+')
plt.plot(
    b,
    d,
    'g*--',
    # alpha = transparecia
    )
plt.show()
 