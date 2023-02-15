import sys

args = sys.argv

file = args[1]
before_str="[ moleculetype ]"
after_str="#ifdef POSRES\n#include \"posre2.itp\"\n#endif\n\n[ moleculetype ]"

n = 0
with open(file) as f, open('cpx_solv_add-posre.top', 'w') as writer: 
    for line in f:
        if before_str in line:
            n += 1
        if n == 2:
            line = line.replace(before_str, after_str)
        writer.write(line)
        


