import re
hand =open("raj.txt")
for line in hand:
    line =line.rstrip()
    if re.search ("From ",line):
        print(line)
    