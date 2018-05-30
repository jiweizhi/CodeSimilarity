import shutil
import os
from itertools import combinations
from twisted.conch.client import direct
import subprocess
from subprocess import call
import select
import StringIO
import thread
from threading import Timer
from collections import namedtuple
import multiprocessing
from main import compare

storagepath = "tempstorage/"

# TODO
directorypath = "C:/Users/User/Desktop/test_coins/c/"

finalresultpath = "finalresult2.txt"

r = 2

def rSubset(arr, r):
 
    # return list of all subsets of length r
    # to deal with duplicate subsets use 
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))

def copyFiles(coinpath, firstorsecond):
    for path, dirs, files in os.walk(coinpath):
        for f in files:
            fp = os.path.join(path, f)
            shutil.copy2(fp, storagepath)
            dst_file = os.path.join(storagepath, f)
            if (firstorsecond == 1):
                new_dst_file_name = os.path.join(storagepath, "1_" + f)
            else:
                new_dst_file_name = os.path.join(storagepath, "2_" + f)
            os.rename(dst_file, new_dst_file_name)
    
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
    
def emptyfolder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
            
def run_with_timeout(timeout, default, f, *args, **kwargs):
    if not timeout:
        return f(*args, **kwargs)
    try:
        timeout_timer = Timer(timeout, thread.interrupt_main)
        timeout_timer.start()
        result = f(*args, **kwargs)
        return result
    except KeyboardInterrupt:
        return default
    finally:
        timeout_timer.cancel()

# gets the first file
def getFirstFile(line):
    index = line.find("-1_")
    if (index == -1):
        index = line.find("-2_")
    return line[10:(index)]

# gets the first file
def getPercentage(line):
    index = line.find(":")
    if (index == -1):
        return "error: colon not found"
    return float(line[(index + 2):])

# # gets percentage given line, returns int type
# def getPercentage(line):
#     #index = thisline.find("for ")
#     #index = index
#     #split = thisline[index:]
# #     endindex = split.find("%")-1
# #     split = split[:endindex]
#     p = [int(s) for s in line.split() if s.isdigit()]
#     #print(split[:endindex])
#     #return int(split[:endindex])
#     return p[0]


PercentStruct = namedtuple("PercentStruct", "source dest percent")

if __name__ == '__main__':
    count = 0
    threads = []
    coins = get_immediate_subdirectories(directorypath)

    combi = rSubset(coins, r)

    satisfied = 0
    for thiscombi in combi:
        coin1 = thiscombi[0]
        coin2 = thiscombi[1]
        coin1path = os.path.join(directorypath, coin1)
        coin2path = os.path.join(directorypath, coin2)
        
        
        
        if (satisfied == 0):
            if(not((coin1 == "adshares-esc-archive-master") and (coin2 == "bitshares-bitshares-core-archive-master"))):
                continue
            else:
                satisfied = 1
                
        # get the size of directory
        total_size1 = 0
        for path, dirs, files in os.walk(coin1path):
            for f in files:
                fp = os.path.join(path, f)
                total_size1 += os.path.getsize(fp)
        
        if ((total_size1 == 0) or (total_size1 > 10000000 )):
            continue
        
        # get the size of directory
        total_size2 = 0
        for path, dirs, files in os.walk(coin2path):
            for f in files:
                fp = os.path.join(path, f)
                total_size2 += os.path.getsize(fp)
        
        if ((total_size2 == 0) or (total_size2 > 10000000 )):
            continue
        
        p = multiprocessing.Process(target=compare, args=(coin1,coin2))
        threads.append(p)
        count = count + 1
        if (count == 10):
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            count = 0
            threads = []
#    
            
            
        
        