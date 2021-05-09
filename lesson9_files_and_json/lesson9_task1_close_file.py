filename = "myfile.txt"

with open(filename, 'r') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
