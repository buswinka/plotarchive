import matplotlib.pyplot as plt
import numpy as np
import pickle
import inspect

from . import files


def archive(filename):
    if filename is None:
        filename = 'myplot.plotarchive'

    python_files = files.create_file_dict()
    data = {'ax': plt.gca(), 'fig': plt.gcf(), 'files': python_files}
    pickle.dump(data, open(filename, 'wb'))

    files.write_files_from_dict(data['files'])


class archiver(object):
    def __init__(self, filename=None):
        if filename is None:
            self.filename = 'myplot.plotarchive'
        else:
            self.filename = filename

    def __call__(self, func):
        def wrapper(*args, **kwargs):

            python_files = files.create_file_dict()

            args_name = inspect.getfullargspec(func)[0]
            args_dict = dict(zip(args_name, args))

            for i, arg in enumerate(args):
                if not isinstance(arg, (int, float, bool, bytes, str, list, tuple, dict, np.ndarray)):
                    raise TypeError(f'Unrecognized argument type for {args_name[i]}:{type(arg)}')

            data = {'ax': plt.gca(), 'fig': plt.gcf(), 'args': args_dict, 'files': python_files}

            pickle.dump(data, open(self.filename, 'wb'))

            return func(*args, **kwargs)
        return wrapper


