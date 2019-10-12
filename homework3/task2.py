import task1
import warnings
import librosa
import numpy as np
import time
from multiprocessing import Pool

def main():
    start_time = time.time()
    task1.create_path()
    files = librosa.util.find_files(task1.AUDIO_PATH)
    files = np.asarray(files)
    pool = Pool(4)
    pool.map(task1.file_handle, files)
    print('Parallel program with multiprocessing run for {} minutes'.format((time.time() - start_time) / 60))

if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        task1.fxn()
        main()
