import os
import glob

# 今いるディレクトリの直下にある、一括で変えたいディレクトリたちがまとまっているディレクトリを指定
path = "./webaward"
files = glob.glob(path + '/*')

for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    s = f.replace('./webaward/', '')
    os.rename(f, path + '/' + '{0:03d}'.format(i + 1) + '_' + s + fext)
    