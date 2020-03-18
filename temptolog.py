import sys
sys.path.append("Temp")
from temp import *

dic = locals().copy()
list = ["__name__","__cached__","__doc__","__file__","__builtins__","__package__","__loader__","__spec__","__annotations__","__module__", "sys"]
list1 = ["Pumpe0", "Pumpe1", "Pumpe2", "Pumpe3", "Pumpe4", "Pumpe5", "Pumpe6"]


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
for x in range(6):
    if i == 0:
        for element in list1:
            try:
                if str("Pumpe"+str(x)) not in str(line):
                    with open("Temp\\log.py", "a") as f:
                        f.writelines(str("Pumpe"+str(x))+ ' = ' +str(dic)+ '\n' )
                        f.close
                    print("true")
                    i = i+1
                    break
                else:
                    pass
            except:
                if len(line) == 0:
                    with open("Temp\\log.py", "a") as f:
                        f.writelines(str("Pumpe"+str(x))+ ' = ' +str(dic)+ '\n' )
                        f.close
                    i = i+1
                    break
    else:
        break

with open("Temp\\temp.py", "w") as f:
    f.truncate(0)
    f.close()