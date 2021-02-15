file = open("test.txt", 'w', encoding='utf-8')

for i in range(10):
    file.write("line " + str(i) + "\n")

file.close()
