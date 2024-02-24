import os

def vtt2lrc(vtt_file, lrc_file):
    with open(vtt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(lrc_file, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if lines[i].strip().isdigit():  # 行号
                i += 1
                if i < len(lines) and lines[i].strip()[0:2] == '00' and lines[i].strip()[2] == ':':  # 时间戳
                    time = lines[i].strip()[0:11]
                    time = '[' + time[3:6] +  time[6:] + ']'
                    i += 1
                    if i < len(lines):  # 歌词内容
                        content = lines[i].strip()
                        f.write(time + content + '\n')
            i += 1
    print('Convert successfully!')

path = r"path2vtt\\"
filenames = os.listdir(path)
for filename in filenames:
    if filename.endswith('.vtt'):
        vtt2lrc(path+filename, path+filename[:-8]+'.lrc')