import numpy as np
from scipy.stats import norm
from matplotlib import pylab as plt
f = norm(loc=0, scale=1)
x = f.rvs(500)
xs = np.r_[-3:3:1024j]
ys = f.pdf(xs)
h = plt.hist(x, bins=30, normed=True, color=(0,.5,0,1), label='Histogram')
plt.plot(xs, ys, 'r--', linewidth=2, label='$\mathcal{N}(0,1)$')
plt.xlim(-3,3)
plt.xlabel('X')

from pyqt_fit import kde
est = kde.KDE1D(x)
plot(xs, est(xs), label='Estimate (bw={:.3g})'.format(est.bandwidth))
plt.legend(loc='best')