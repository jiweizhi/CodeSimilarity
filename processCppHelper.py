def checkbbx(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
            index = code.find("\\x")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 3):])
    return 

def checkbbbn(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
            index = code.find("\\\n")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 4):])
    return

def checkmicro(filepath):
    micro = u'\u00b5'
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
            index = code.find(micro.encode("utf8"))
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return

# the strange symbol
def checksymbol(filepath):
    somesymbol = u'\u2318'
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
            index = code.find(somesymbol.encode("utf8"))
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 2):])
    return     

def checkqzz(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#         print("in a while loop")
            index = code.find("\'00")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return      

def checkqzt(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#         print("in a while loop")
            index = code.find("\'03")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return

def checkbd(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#         print("in a while loop")
            index = code.find("\\d")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return

def checkbc(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#         print("in a while loop")
            index = code.find("\\c")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return

def checkrightarrow(filepath):
    somesymbol = u'\u2192'
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#             print("arrow symbol = " + somesymbol.encode("utf16"))
            index = code.find(somesymbol.encode("utf8"))
            if index == -1:
                break
            else:
                print("found arrow symbol")
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return  

def checkat(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#         print("in a while loop")
            index = code.find("@")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return


def checkqq(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#         print("in a while loop")
            index = code.find("\'\'")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return

def checkbs(filepath):
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#         print("in a while loop")
            index = code.find("\\ ")
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return

def checkdollar(filepath):
    somesymbol = u'\u0024'
    while(1):
        with open(filepath, "r+") as f:
            code = f.read()
#             print("arrow symbol = " + somesymbol.encode("utf16"))
            index = code.find(somesymbol.encode("utf8"))
            if index == -1:
                break
            else:
                with open(filepath, "r+") as f:
                    f.write(code[:index])
                    f.write(code[(index + 1):])
    return  

def process(filepath):
    checkbbx(filepath)
    checkbbbn(filepath)
    checkmicro(filepath)
    checksymbol(filepath)
    checkqzz(filepath)
    checkqzt(filepath)
    checkbd(filepath)
    checkbc(filepath)
    checkrightarrow(filepath)
    checkat(filepath)
    checkdollar(filepath)
    #checkqq(filepath)
    #checkbs(filepath)            
