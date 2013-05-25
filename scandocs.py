#!/usr/bin/python3

import sys
import os
import shutil
import subprocess
import docsys

alen = len(sys.argv)

if alen != 1 and alen != 2:
    print("Only allowed argument is page height in millimeters.  Default is 279, if not supplied.")
    exit()

if alen == 2 and not sys.argv[1].isdigit():
    print("Page height supplied must be a number (assumed to be in millimeters)")
    exit()

def FindImageNum(path):
    digitpart = os.path.splitext(path)[0][3:]
    if not digitpart.isdigit():
        return -1
    return int(digitpart)

def FindStartImageNum():
    highest = -1
    def IsCurHigher(root, f):
        nonlocal highest
        curNum = FindImageNum(f)
        if curNum > highest:
            highest = curNum

    docsys.WalkCurFolder(IsCurHigher)
    return highest + 1
            

def DoScan(startIndex):
    arguments = ['scanimage', '-b', '-d', 'fujitsu', '--format=tiff', '--resolution=300', '--batch-start=' + str(startIndex) ] 
    if len(sys.argv) > 1:
        heightargs = [ '-y', sys.argv[1], '--page-height', sys.argv[1] ]
        arguments += heightargs
    print()
    print("Calling scanimage as follows:")
    print(' '.join(str(arg) for arg in arguments))
    print()
    subprocess.call(arguments)

def DoConversion(minIndex):
    def ConvertFile(root, f):
        if FindImageNum(f) < minIndex:
            return

        filesplit = os.path.splitext(f)
        if filesplit[1].lower() == '.tif':
            origpath = os.path.join(root, f)
            subprocess.call( ['convert', origpath, os.path.join(root, filesplit[0]) + '.png' ])
            os.remove(origpath)
            print("Converting " + os.path.join(root, f) + " to png format")
    docsys.WalkCurFolder(ConvertFile)

startNum = FindStartImageNum()
DoScan(startNum)
DoConversion(startNum)

