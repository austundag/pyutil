'''
Created on Jun 10, 2013

@author: austundag004
'''    

def analyze(lines):
    routineName = None
    result = {}
    for line in lines:
        if routineName is None:
            if line[:9] == 'Routine ^':
                rest = line[9:]
                routineName = rest.split()[0]
                inlines = False
                numLines = 0
                hitLines = 0
            continue
        if not inlines:
            inlines = line[0].isdigit()
            continue
        if not line[0].isdigit():
            result[routineName] = (hitLines, numLines)
            routineName = None
            continue
        routineLine = line[15:].strip()
        hittimess = line[5:15].strip()
        hittimes = int(hittimess)
        if len(routineLine) > 0 and routineLine[0] == ';': continue
        numLines = numLines + 1
        if hittimes == 0: continue
        hitLines = hitLines + 1
    keys = result.keys()
    keys.sort()
    print keys
    for key in keys:
        (hitLines, numLines) = result[key]
        if numLines == 0: p = 0
        else: p = int((10000.0 * hitLines) / numLines) / 100.0
        print "%s: %f (%d of %d)" % (key,p,hitLines,numLines) 

def analyzeFile(fileName): 
    f = open(fileName, 'r')
    lines = f.readlines()
    f.close()
    analyze(lines)

if __name__ == '__main__':
    analyzeFile('C:\\afsin\\Coverage\\GMPLdetail.log')
    analyzeFile('C:\\afsin\\Coverage\\SDdetail.log')
    analyzeFile('C:\\afsin\\Coverage\\DGdetail.log')
