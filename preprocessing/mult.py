import os
import multiprocessing
from multiprocessing import Process
import pandas as pd
import tqdm
import soundfile as sf
import math

def get_length(*args):
    files, bird, audios, lengths,birds, paths = args
    base = '/datasets/xeno_canto/491_all/'
    for file in files:
        if os.path.exists(file):
            f = sf.SoundFile(file)
            name = file.replace('/datasets/xeno_canto/491_all/', '')
            lengths.append(f.frames / f.samplerate)
            audios.append(name)
            birds.append(bird)
            paths.append(file)

if __name__ == '__main__':
    base = '/datasets/xeno_canto/wav_16khz_XC/'
    paths = os.listdir(base)
    paths = [p for p in paths if '_16.wav' not in p]
    print(paths)
    pbar = tqdm.tqdm(total=len(ls['audio'].tolist())) # Init pbar
    
    for i, row in ls.iterrows():
        f = row['audio']
        bird = row['bird']
        segments = math.ceil(row['length']/ float(60))
        ls = [(f.replace('.wav', '') + '_' + str(i) + '.wav') for i in range(segments)]
        ls = [base + l for l in ls]
        
        p = Process(target=get_length, args=(ls, bird, audios, lengths, birds, paths))
        p.start()
        processes.append(p)
        pbar.update(n=1)
        print(len(processes))

        
    for p in processes:
        p.join()

