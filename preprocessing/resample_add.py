import os 

"""
This script resamples audio files to 16kHz and also moves the missing ones in the wav_16khz_XC folder
Requirements: ffmpeg/4.4.0_x265 and sox

"""

path = '/datasets/xeno_canto/audio/'
dest_scr = '/datasets/xeno_canto/wav_16khz_XC/'

if not os.path.exists(dest_scr):
    os.mkdir(dest_scr)
    
for bird in os.listdir(path):
    if bird == '.DS_Store':
        continue
    for audio in os.listdir(path + bird):
        folder = dest_scr + bird
        if not os.path.exists(folder):
            os.mkdir(folder)
            
        old = path + bird + '/' + audio
        temp = audio.replace('mp3', 'wav')
        new_audio = dest_scr + bird + '/' + temp
        
        if not os.path.exists(new_audio):
            os.system("ffmpeg -i {src} {dest}".format(src = old, dest = new_audio))
            print("converting mp3 to wav => {src} to {dest}".format(src = old, dest = new_audio))
            
            
        print("converting to 16khz {old} to {old} ".format(old = new_audio))    
        os.system("sox {old} -r 16000 {old}".format(old = new_audio))
        
        print("---------------------------------------------------------------------------    --------------------------")
        
        
    