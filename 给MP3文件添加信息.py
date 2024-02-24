import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TALB, TPE1

path = r"path2MP3\\"

pic_path = r""  # 封面路径
author = u""    # 作者
album = u""     # 专辑

pic_bool = (pic_path != "")
author_bool = (author != "")
album_bool = (album != "")

filenames = os.listdir(path)
for filename in filenames:
    if filename.endswith('.mp3'):
        audio = MP3(path+filename, ID3=ID3)
        # 修改作者，专辑，封面
        if author_bool:
            audio["TPE1"] = TPE1(encoding=3, text=author)
        if album_bool:
            audio["TALB"] = TALB(encoding=3, text=album)
        if pic_bool:
            audio.tags.add(APIC(
                encoding=3, mime='image/jpeg',type=3,desc=u'Cover',data=open(pic_path, 'rb').read()
            ))
        audio.save()
        print(filename,"done")
