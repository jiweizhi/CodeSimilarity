import os
import sys

if __name__ == '__main__':
  
    for root, subdirs, files in os.walk("C:\Users\User\Desktop\jplagexercise1"):
#         print('--\nroot = ' + root)
        #for subdir in subdirs:
            
            #print('\t- subdirectory ' + subdir)
            for filename in files:
                file_path = os.path.join(root, filename)
     
                # skip regression.h, for now
                if (file_path == "C:\Users\User\Desktop\jplagexercise1\rippled\src\ed25519-donna\regression.h"):
                    continue
                
                #print("processing " + file_path)
                
                #print('\t- file %s (full path: %s)' % (filename, file_path))
                temp = filename.split('.')
                extension = temp[(len(temp)-1)]
#                 print("extension = " + extension)
                #consider only cpp files
                if (extension == "cpp" or extension == "h"): 
                    while(1):
                        with open(file_path, "r+") as f:
                         old = f.read()  # read everything in the file
#                          print(old)
#                          if(filename == "gen.cpp"):
#                              print("found gen.cpp")
                            
                         index = old.find("\\x")
                        if index == -1:
                            index = old.find("\\\n")
                            if index == -1:
#                                 break;
                                micro = u'\u00b5'
                                index = old.find(micro.encode("utf8"))
#                                 print('\u00b5'.decode('unicode-escape'))
                                if index == -1:
                                    somesymbol = u'\u2318'
                                    index = old.find(somesymbol.encode("utf8"))
                                    if index == -1:
                                        break
                                    else:
                                        print("some special letter found")
                                        with open(file_path, "r+") as f:
                                            f.write(old[:index])
                                            f.write(old[(index + 2):])
                                else:
                                    print("micro letter found")
                                    with open(file_path, "r+") as f:
                                        f.write(old[:index])
                                        f.write(old[(index + 1):])
                            else:
#                                 print("\\\n")
                                with open(file_path, "r+") as f:
                                    f.write(old[:index])
                                    f.write(old[(index + 4):])
                        else:
                            with open(file_path, "r+") as f:
                             f.write(old[:index])
                             f.write(old[(index + 3):])
                 
    print("done")
