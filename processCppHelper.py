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

def process(filepath):
    checkbbx(filepath)
    checkbbbn(filepath)
    checkmicro(filepath)
    checksymbol(filepath)
    checkqzz(filepath)
                
