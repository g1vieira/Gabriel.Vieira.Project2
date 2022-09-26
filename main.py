my_file = open("project2.txt", 'r')

all_lines = my_file.readlines()

for lines in all_lines:
    lines = lines.split(':')
    print(f"Student ID: {lines[0]}, {lines[2]}")