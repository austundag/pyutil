'''
Created on Mar 11, 2013

@author: Afsin
'''

def remove(filename, today):
    f = open(filename)
    lines = f.readlines();
    f.close()
    f = open(filename, 'w')
    key = today + '.'
    for line in lines:
        index = line.find(key)
        if index >= 0:
            index = index + 7
            i = index + 1
            while i < len(line) and line[i].isdigit():
                i = i + 1
            if i > index + 1:
                newline = line[:index] + line[i:]
            else:
                newline = line
        else:
            newline = line
        f.write("%s" % newline)
    f.close()

if __name__ == '__main__':
    today = "3130311"
    filename = "C:\\work\\sandbox\\globalsrefactored\\405+PATIENT MOVEMENT.zwr"
    remove(filename,today)
    filename = "C:\\work\\sandbox\\globalsorig\\405+PATIENT MOVEMENT.zwr"
    remove(filename,today)
    