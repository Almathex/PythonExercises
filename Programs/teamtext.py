file = open("teams.txt", "w")

club = ('test', 'Chrome', 'Atlas', 'Whipsnakes', 'Archers', 'Chaos')
for i in range (1,6):
    file.seek(0)
    newline = club[i] + " Lacrosse club /n "
    file.write(newline)

file.close()    