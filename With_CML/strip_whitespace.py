import sys


afile = sys.argv[1]

buffer_string = ""

with open(afile, "r") as rf:
    for line in rf:
        temp = line.rstrip()
        temp.replace("\t", "    ")
        buffer_string += temp + "\n"

with open(afile, "w") as wf:
    wf.write(buffer_string)
