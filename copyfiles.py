import shutil
import os

directorypath = "C:/Users/User/Desktop/test_coins/c/adshares-esc-archive-master/"

storagepath = "tempstorage/"

if __name__ == '__main__':
    for path, dirs, files in os.walk(directorypath):
        for f in files:
            fp = os.path.join(path, f)
            shutil.copy2(fp, storagepath)
            dst_file = os.path.join(storagepath, f)
            new_dst_file_name = os.path.join(storagepath, "1_" + f)
            os.rename(dst_file, new_dst_file_name)