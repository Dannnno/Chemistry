import csv


buffer_strings = []

with open("ab.txt", "r") as f:
    for line in f:
        buffer_strings.append(line.split())
        
with open("ab.txt", "wb") as f:
    my_writer = csv.writer(f)
    for buffer_string in buffer_strings:
        my_writer.writerow(buffer_string)
