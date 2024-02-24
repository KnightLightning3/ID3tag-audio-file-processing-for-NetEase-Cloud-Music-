import os
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TALB, TPE1
AudioSegment.converter = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"

path = r"path2wav\\"
output_path = r"outputpath2mp3\\"
pic_path = r""  # 封面路径
author = u""    # 作者
album = u""     # 专辑

def wav2mp3(wav_file, mp3_file):
    AudioSegment.converter = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
    bit_rate = "320k"
    sound = AudioSegment.from_wav(wav_file)
    sound.export(mp3_file, format="mp3", bitrate=bit_rate)
def mp3_add_info(mp3_file, pic_path='', author='', album=''):
    audio = MP3(mp3_file, ID3=ID3)
    # 添加作者，专辑，封面
    audio["TALB"] = TALB(encoding=3, text=album)
    audio["TPE1"] = TPE1(encoding=3, text=author)
    audio.tags.add(APIC(
            encoding=3, # 3 is for utf-8
            mime='image/jpeg', # image/jpeg or image/png
            type=3, # 3 is for the cover image
            desc=u'Cover',
            data=open(pic_path, 'rb').read()
        ))
    audio.save()

kwargs = {
    'pic_path': pic_path,
    'author': author,
    'album': album
}

filenames = os.listdir(path)
for filename in filenames:
    if filename.endswith('.wav'):
        mp3_filename=filename[:-4]+'.mp3'
        if not os.path.exists(output_path+mp3_filename):
            wav2mp3(path+filename, output_path+mp3_filename) # wav转mp3
            mp3_add_info(output_path+mp3_filename,kwargs)# 给MP3文件添加信息
            print(mp3_filename,' Convert successfully!')