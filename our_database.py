from os import listdir
from os.path import isfile, join
import imageio
import numpy as np
import scipy

def get_letters(folder_name):
    files = [f for f in listdir(folder_name) if isfile(join(folder_name, f))]
    keys = []
    values = []
    for file in files:
        letter = file[0]
        l = ord(letter)
        indice = 0
        if (ord('a') <= l) and (ord('z') >= l):
            indice = l - ord('a')
        else:
            indice = l - ord('A')
        fname = (folder_name + "/" + file)
        img = scipy.ndimage.imread(fname,
                                   flatten=False,
                                   mode='L') / 255
        img = img.flatten()
        key = np.zeros(26)
        key[indice] = 1
        values.append(np.array(img))
        keys.append(key)

    keys_r = np.array(keys)
    values_r = np.array(values)

    return values_r, keys_r




