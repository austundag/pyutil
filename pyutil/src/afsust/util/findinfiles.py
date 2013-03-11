'''
Created on Mar 10, 2013

@author: Afsin
'''

import os

if __name__ == '__main__':
    d = 'C:\\work\\sandbox\\osehraresult\\'
    names = os.listdir(d)
    for name in names:
        fullname = os.path.join(d, name)
        f = open(fullname)
        lines = f.readlines()
        i = 0
        for line in lines:
            index = line.find('Replace Removed')
            if index >= 0:
                #print "%s %s -> %s\n" % (name, i, line)
                j = i+1
                while (j < len(lines) or j < 40):
                    jindex = lines[j].find('Menu Option')
                    if jindex >= 0:
                        print "%s %s -> %s\n" % (name, i, line)
                        print lines[j]
                        break
                    j = j + 1                
            i = i + 1