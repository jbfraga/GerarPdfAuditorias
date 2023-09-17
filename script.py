import os
rows = open("Listatdc.txt", "r").read().split("\n")

for row in rows:
    cols = row.split(";")


    os.system("python Eorder.py {} {} {}".format(cols[0], cols[1],cols[2]))