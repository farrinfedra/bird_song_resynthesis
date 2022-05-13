import os
import pandas as pd
import subprocess
"""
This script gets the frequency of classes in wav_16khz_XC directory
Requirements: ffmpeg/4.4.0_x265 
"""
base_path = '/datasets/xeno_canto/audio/'


audio_dict = {}
bird_freq = {}
birds = []
audio_names = []
lengths = []
paths = []
dest = []
folder_birds = []
freq = [] 
#base_path2 = '/datasets/xeno_canto/491/'
for bird in sorted(os.listdir(base_path)):
    
    audios = os.listdir(base_path + bird)
    if(len(audios) == 0 ):
        continue
        
    freq.append(len(audios))
    folder_birds.append(bird)
    audio_names.extend(audios)
    #temp = audios
    #temp = [(base_path2 + a) for a in temp]
    #dest.extend(temp)
    audios = [(base_path + bird + '/' + a) for a in audios]
    

    for audio in audios:
        print(audio)
        command = 'ffprobe -i {audio} -show_entries format=duration -v quiet -of csv=p=0'.format(audio = audio)
        #print('processing {folder} and {audio}\n'.format(folder = bird, audio = audios))
        out = subprocess.Popen(command, 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT, shell = True)
        
        stdout,stderr = out.communicate()
        print(stdout)
        print(stderr)
        if len(stdout) == 0:
            os.system('rm {audio}'.format(audio = audio))
            continue
        out = stdout.split()[0].decode("utf-8")
        birds.append(bird)
        paths.append(audio)
        lengths.append(out)
        

#for class frequency calculation        
bird_freq['bird'] = folder_birds
bird_freq['freq'] = freq


#audio dict here
audio_dict['bird'] = birds
audio_dict['audio'] = audio_names
audio_dict['path'] = paths
audio_dict['length'] = lengths
#audio_dict['destination'] = dest

df = pd.DataFrame(audio_dict)
df2 = pd.DataFrame(bird_freq)

df2.to_csv('./audio_data_freq.csv' , index = False)
df.to_csv('./audio_meta.csv', index = False)