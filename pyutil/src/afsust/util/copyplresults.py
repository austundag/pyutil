'''
Created on Mar 8, 2013

@author: Afsin
'''

import os
import shutil

if __name__ == '__main__':
    srcDir = 'C:\\work\\automatedtesting\\osehra\\testbuild\\Testing\\Temporary\\'
    tgtDir = 'C:\\work\\sandbox\\osehraresult\\'
    srcNames = os.listdir(srcDir)
    for srcName in srcNames:
        index = srcName.find('pl_test')
        if index >= 0:
            tgtName = srcName[index:]
            srcFile = os.path.join(srcDir, srcName)
            tgtFile = os.path.join(tgtDir, tgtName)
            shutil.copy(srcFile, tgtFile)
