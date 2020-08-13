import plotarchive as pa
import matplotlib.pyplot as plt
import numpy as np
import plotarchive.src.files as files
import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)

# plt.plot([1,2,3], [1,2,3], 'ko')
# files, ax, fig = pa.archive('yeet')
# fig.show()
# print(ax)


@pa.archiver(filename='test.plotarchive')
def plot(x,y):
    plt.plot(x,y)
    plt.show()
    return None


plot([1,2,3], np.array([1,2,3]), )

pa.archive('yeet.pa')
pa.expand('yeet.pa')