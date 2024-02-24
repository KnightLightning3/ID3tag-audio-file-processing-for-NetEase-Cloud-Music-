import  os

path = r"path2mp3\\"
filenames = os.listdir(path)
for filename in filenames:
    if filename.startswith('#'):
        print(filename)
        os.rename(path  + filename, path + filename.replace('#', ''))
