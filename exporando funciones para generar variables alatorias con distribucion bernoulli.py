import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
fig_01, ax_01 = plt.subplots(1, 1)
fig_02, ax_02 = plt.subplots(1, 1)
p = 0.3
mean, var, skew, kurt = bernoulli.stats(p, moments='mvsk')
print(mean, var, skew,kurt)

x = np.arange(bernoulli.ppf(0.01, p),
              bernoulli.ppf(0.99, p))
ax_01.plot(x, bernoulli.pmf(x, p), 'bo', ms=8, label='bernoulli pmf')
ax_01.vlines(x, 0, bernoulli.pmf(x, p), colors='b', lw=5, alpha=0.5)
r = bernoulli.rvs(p, size=1000)
ax_02.hist(r, bins=200)
plt.show()
