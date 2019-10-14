import librosa
import numpy as np
import os
import warnings
import time

AUDIO_PATH = '/home/simon/voices'
path = os.getcwd()

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

def create_path():
    print('creating path...')
    if not os.path.exists(path + '/mfcc'):
        os.mkdir(path + '/mfcc')
    tree = []
    for i in os.walk(AUDIO_PATH):
        tree.append(i)
    cur_path = path + '/mfcc'
    for address, _, _ in tree:
        if not os.path.exists(cur_path + address[len(AUDIO_PATH):]):
            os.mkdir(cur_path + address[len(AUDIO_PATH):])

def file_handle(f):
    y, sr = librosa.load(f)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    s = path + '/mfcc' + f[len(AUDIO_PATH):-3] + 'npy'
    #with open(s, 'w+') as txt:
    print('creating {}'.format(s))
    np.save(s, mfcc)

def main():
    start_time = time.time()
    create_path()
    files = librosa.util.find_files(AUDIO_PATH)
    files = np.asarray(files)
    for f in files:
        file_handle(f)
    print('Consecutive program run for {} minutes'.format((time.time() - start_time) / 60))

if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fxn()
        main()
