import plotarchive as pa
import matplotlib.pyplot as plt
import numpy as np
import plotarchive.src.files as files
import os
import pickle
import dill


@pa.archive()
def plot(x, y, title='my_plot'):
    plt.figure()
    plt.plot(x,y)
    plt.show()

fig = plot([1,2,3], np.array([1,2,3]), title='penis')


pa.expand('test.plotarchive')
