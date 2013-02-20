'''
Created on Feb 20, 2013

@author: Afsin
'''

def readlines(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    result = []
    for line in lines:
        r = line.split(',')[0]
        if r[-2:] == '.m':
            result.append(r[:-2])
    return result

def compare(filename1, filename2):
    lines1 = readlines(filename1)
    lines2 = readlines(filename2)    
    result = list(set(lines1) & set(lines2))
    return result

def writeresult(filename, routines):
    of = open(filename, 'w')
    for r in routines:
        of.write(r)
        of.write('\n')
    of.close()

if __name__ == '__main__':
    filename1 = 'C:\\work\\sandbox\\mergecheck\\osehra2osehra.csv'
    filename2 = 'C:\\work\\sandbox\\mergecheck\\pwc2osehra.csv'
    outfilename = 'C:\\work\\sandbox\\mergecheck\\compare.txt'
    routines = compare(filename1, filename2)
    writeresult(outfilename, routines)
