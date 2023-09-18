import os
rows = open("Listatdc.txt", "r").read().split("\n")

for row in rows:
    cols = row.split(";")
    os.system("python Eorder.py {} {} {} {}".format(cols[0], cols[1],cols[2],cols[3]))
   
for row in rows:
    cols = row.split(";")
    
    os.system("python GPM.py {} {} {} {}".format(cols[0], cols[1],cols[2],cols[3]))

print("Terminou")