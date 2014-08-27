import csv
import sys

space_delim = sys.argv[1]
comma_delim = sys.argv[2]

buffer_strings = []

with open(space_delim, "r") as f:
    for line in f:
        buffer_strings.append(line.split())
        
with open(comma_delim, "wb") as f:
    my_writer = csv.writer(f)
    for buffer_string in buffer_strings:
        my_writer.writerow(buffer_string)
