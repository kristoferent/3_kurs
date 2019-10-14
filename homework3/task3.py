import task1
import warnings
import librosa
import numpy as np
import time
import os
from queue import Queue
from threading import Thread, Lock

path = os.getcwd()

def file_handle(q, lock, n):
    while True:
        lock.acquire()
        try:
            f = q.get()
            if f is None:
                break
            y, sr = librosa.load(f)
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            s = path + '/mfcc' + f[len(task1.AUDIO_PATH):-3] + 'npy'
        finally:
            lock.release()
        print('creating {}'.format(s))
        np.save(s, mfcc)


def main():
    start_time = time.time()
    task1.create_path()
    files = librosa.util.find_files(task1.AUDIO_PATH)
    files = np.asarray(files)
    q = Queue(5)
    lock = Lock()
    th1 = Thread(target=file_handle, args=(q,lock,1))
    th2 = Thread(target=file_handle, args=(q,lock,2))
    th1.start()
    th2.start()
    for f in files:
        q.put(f)
    q.put(None)
    q.put(None)
    th1.join()
    th2.join()
    print('Parallel program with threads run for {} minutes'.format((time.time() - start_time) / 60))

if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        task1.fxn()
        main()
