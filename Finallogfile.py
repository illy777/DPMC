from sys import path
path.append("Temp")
from log import *


def write(i):
    with open("Temp\\log2.py", "a") as f:
        f.write("Pumpe"+str(i)+" = "+str(P)+"\n")
P = {}

i=0
for keys in Pumpe0:
    value = Pumpe0[keys]
    for chars in str(keys):
        if chars.isdigit() is True:
            n = chars
            nstring= str(keys).replace(n,"")
    # print(keys+": KN:"+str(value[1])+" SZ:"+str(value[0]))
    P[str(value[1])] = [value[0], nstring]
write(i)
i = i+1





