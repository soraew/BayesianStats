import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys

print(sys.platform)

FontPath = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'

jpfont = FontProperties(fname=FontPath)
    
fig1 = plt.figure(num=1, facecolor='w')
q = np.linspace(0, 1, 250)
plt.plot(q, st.uniform.pdf(q), 'k')
plt.plot(q, st.beta.pdf(q, 0.5, 0.5), 'c--')
plt.xlim(0, 1)
plt.ylim(0, 2.8)
plt.legend(['一様分布', 'ベータ分布'], prop=jpfont)
plt.savefig('./2020_7/uni_beta.png', dpi=300)
plt.show()