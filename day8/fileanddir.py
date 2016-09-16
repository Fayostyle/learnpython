import os
import os.path


def listfiles(path, ext='.py'):
    files = os.listdir(path)
    for x in files:
        if os.path.isdir(x):
            listfiles(x, ext)
        else:
            if os.path.splitext(x)[1] == ext:
                print(x)

listfiles('.', '.log')