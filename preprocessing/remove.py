import os
import multiprocessing
from multiprocessing import Process
import pandas as pd
import tqdm
import sys

base = '/datasets/xeno_canto/wav_16khz_XC/'
def get_length(files):

    audios = os.listdir(files)
    audios = [f for f in audios if '_16.wav' not in f]
    if len(audios) == 0:
        print(files)
        print(audios)
            

if __name__ == '__main__':
    base = '/datasets/xeno_canto/wav_16khz_XC/'
    paths = os.listdir(base)
    
    pbar = tqdm.tqdm(total=len(os.listdir(base))) # Init pbar
    processes = []
    for folder in paths:

        file = base + folder
        p = Process(target=get_length, args=[file])
        
        p.start()
        processes.append(p)
        pbar.update(n=1)

    for p in processes:
        p.join()