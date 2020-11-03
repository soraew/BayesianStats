import random as rand
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

length = 10000

def randy(num_randys):
    randy = np.mean(np.array([rand.random() for i in range(num_randys)]))
    return randy

num_randys = int(input("N(integer) : "))
rands = np.array([randy(num_randys) for i in range(length)])
    
g = sns.distplot(rands)
plt.show()
# for i in tqdm(range(1, 10)):
#     rands = np.array([randy(i) for i in range(length)])
#     sns.distplot(rands)
#     plt.show()