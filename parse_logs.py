import parse_config
import os

configuration = parse_config.ConfPacket()
configs = configuration.load_config('FOLDERS')
logs_dir = configs['FOLDERS']['logs_folder']
music_dir = configs['FOLDERS']['musics_folder']
logs_filelist = []
not_in_log_filelist = []


for file in os.scandir(logs_dir):
    if file.name[-3:].upper() != 'LOG':
        continue

    f = open(os.path.join(logs_dir, file.name), "r")
    linhas = f.readlines()
    for linha in linhas:
        try:
            name = (linha.split(' - ')[2])[:-1]         
        except:
            continue
        
        if not name in logs_filelist: 
            logs_filelist.append(name)
    f.close()

if os.path.exists('resultado.txt'):
    os.remove('resultado.txt')

f = open('resultado.txt', "a")
for file in os.scandir(music_dir):
    if not file.name in logs_filelist:
        not_in_log_filelist.append(file.name)
        try:
            f.write(file.name+'\n')
        except Exception as err:
            print(err)
            print(file.name)

f.close()