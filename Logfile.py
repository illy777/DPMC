import os
import sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
sys.path.append(resource_path("Temp"))
from temp import *
from log import*

dic = locals().copy()
list = ["__name__","__cached__","__doc__","__file__","__builtins__","__package__","__loader__","__spec__","__annotations__","__module__", "sys", "resource_path","os"]
list1 = ["Pumpe0", "Pumpe1", "Pumpe2", "Pumpe3", "Pumpe4", "Pumpe5", "Pumpe6", "Pumpe7", "Pumpe8","Pumpe9"]


for x in range(len(list)):
    try:
        dic.pop(list[x])
    except:
        pass

with open("Temp\\log.py", "r") as f:
    line = f.readlines()
    f.close

# print(line)

i = 0
for x in range(len(list1)):
    if i == 0:
        for element in list1:
            if str("Pumpe"+str(x)) not in str(line):
                with open("Temp\\log.py", "a") as f:
                    f.writelines(str("Pumpe"+str(x))+ ' = ' +str(dic)+ '\n' )
                    f.close
                print("true")
                i = i+1
                break
            elif len(line) == 0:
                with open("Temp\\log.py", "a") as f:
                    f.writelines(str("Pumpe"+str(x))+ ' = ' +str(dic)+ '\n' )
                    f.close
                i = i+1
                break
            else:
                pass
    else:
        break

with open("Temp\\temp.py", "w") as f:
    f.truncate(0)
    f.close()