import matplotlib.pyplot as plt
import numpy as np
import pickle
import inspect

from . import files


def expand(filename, folder=None):

    data = pickle.load(open(filename, 'rb'))

    # data = {'ax': plt.gca(), 'fig': plt.gcf(), 'args': args_dict, 'files': python_files}
    fig = data['fig']
    ax = data['ax']
    file_dict = data['files']

    if 'args' in data:
        args = data['args']
    else:
        args = None

    fig.axes(ax)
    fig.show()

    if folder is not None:
        files.write_files_from_dict(file_dict, folder)
