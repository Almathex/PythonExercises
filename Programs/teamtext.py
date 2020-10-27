file = open("teams.txt", "w")

club = ('test', 'Chrome', 'Atlas', 'Whipsnakes', 'Archers', 'Chaos')
file.seek(0)
for i in range (1,6):
    newline = club[i] + " Lacrosse club \n"
    file.write(newline)

file.close()    

file = open("teams.txt", "r")

print(file.readline())
file.readline()
file.readline()
print(file.readline())

file.close()