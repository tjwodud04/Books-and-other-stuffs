from collections import OrderedDict

with open(r'C:\Users\korea\Desktop\save_3years.txt', 'w', encoding='utf-8') as fp:
    with open(r'C:\Users\korea\Desktop\FilesAll\RelatedPerson.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = f.readlines()
            for i in range(len(line)):
                if int(line[i][2:6]) > 2015 and (int(line[i-1][0:13]) != int(line[i][0:13])):
                    fp.write(line[i])
f.close()
fp.close()
