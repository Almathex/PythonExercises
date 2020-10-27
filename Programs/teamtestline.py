file = open("teams.txt", "r")
outfile = ""
for line in range(1, 7):
    if line != 1:
        outfile += file.readline()
    else:
        outfile = 'This is a new line \n'
print(outfile)