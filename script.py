import os
rows = open("Listatdc.txt", "r").read().split("\n")

for row in rows:
    cols = row.split(";")


    os.system("python Untitled-1.py {} {}".format(cols[0], cols[1]))