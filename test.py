import plotarchive as pa
import matplotlib.pyplot as plt
import numpy as np
import plotarchive.src.files as files
import os
import pickle
import dill


@pa.archiver(filename='test.plotarchive')
def plot(x, y, title='penis'):
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_title('asdf;j')
    fig.show()

fig = plot([1,2,3], np.array([1,2,3]), title='penis')


# pa.expand('test.plotarchive')

args = {'x':[1,2,3], 'y':[2,3,4]}
plot(**args)