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

storagepath = "tempstorage/"

# TODO
directorypath = "C:/Users/User/Desktop/test_coins/c/"

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
    coins = get_immediate_subdirectories(directorypath)

    combi = rSubset(coins, r)
    
    for thiscombi in combi:
        coin1 = thiscombi[0]
        coin2 = thiscombi[1]
        copyFiles(os.path.join(directorypath, coin1), 1)
        copyFiles(os.path.join(directorypath, coin2), 2)
        
        # TODO
#         call(["java", "-jar", "C:\Users\User\Desktop\jplag.jar", "-l", "c/c++", "-m", "0%", "-r", "C:/Users/User/Desktop/tempresults", "C:/Users/User/Desktop/nbvcxz2/jplagRunner/tempstorage"])
        proc = subprocess.Popen(["java", "-jar", "C:\Users\User\Desktop\jplag.jar", "-l", "c/c++", "-m", "0%", "-vq", "-r", "C:/Users/User/Desktop/tempresults", "C:/Users/User/Desktop/nbvcxz2/jplagRunner/tempstorage"], stdout=subprocess.PIPE)
        
        
        
#         #
#         #
#         poll_obj = select.poll()
#         poll_obj.register(proc.stdout, select.POLLIN) 
#         outputline =proc.stdout.readline()
#         while(outputline):
#             outputline =proc.stdout.readline()
#             print(outputline)
#         #
#         #
        
        
        
        
#         #
#         #
#         while True:
#             line = proc.stdout.readline()
#             print(line)
#             if not line: break
#         #
#         #
        
        
        
        
#         while True:
#             line = proc.stdout.readline()
#             if (" submissions" in line):
#                 break
#         
#         
#         while(True):
#             line = run_with_timeout(10, None, proc.stdout.readline)
#             if line is None:
#                 break
#             else:
#                 print(line)
        
        
        
        
        
        
         
        output = proc.stdout.read()
        index = output.find("Comparing ")
        output = output[index:]
        buf = StringIO.StringIO(output)
        
        # total sum of percetages , to be divided by count
        sumpercentage = 0
        count = 0
        firstfile = ""
        percentage = 0
        #max percentage encountered for this file
        maxpercentage = 0
        #get the first percentage and first firstfile
        for line in buf:
            firstfile = getFirstFile(line)
            percentage = getPercentage(line)
            count = count + 1
            break
        
        for line in buf:
#             print(line)
#             print(getFirstFile(line))
#             print(getPercentage(line))
            thisfile = getFirstFile(line)
            thispercentage = getPercentage(line)
            
            #new file, initialize the variables
            if (thisfile != firstfile):
                firstfile = thisfile
                sumpercentage = sumpercentage + maxpercentage
                maxpercentage = 0
                count = count + 1
            
            if (thispercentage > maxpercentage):
                maxpercentage = thispercentage
            
        if (count != 0):
#             fr.write("Similarity percentage between " + coin1 + " and " + coin2 + " = " + str(((sumPercentage1 / numFiles1) + (sumPercentage2 / numFiles2)) / 2) + "\n")
#             fr.flush()
            print("Similarity percentage between " + coin1 + " and " + coin2 + " = " + str((sumpercentage / count)) + "\n")
        else:
            print("Similarity percentage between " + coin1 + " and " + coin2 + " = " + "count was zero!!!!!!! no compared result \n")
        
            
            
             
            
            
            
            
#         print(output)
#         for line in output:
#             print(line)
#             print("printed line")
         
        
        
        emptyfolder(storagepath)
        emptyfolder("C:/Users/User/Desktop/tempresults/")
        break
        
        
        