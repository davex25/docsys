#!/usr/bin/python3

import sys
import os
import shutil
import docsys

class Interleaver:
    startIndex = -1
    count = 0
    curIndex = 0

    def __init__(self, startIndex, count):
        self.startIndex = startIndex
        self.count = count
        self.curIndex = 0

    def GetFileName(self, index):
        return './out' + str(index + self.startIndex) + '.png'

    def TempFile(self, index):
        return './temp' + str(index + self.startIndex) + '.png'

    def CheckFilesExist(self):
        for i in range(0, self.count):
            filename = self.GetFileName(i)
            if not os.path.exists(filename):
                print("Cannot find file in specified range, " + filename + " is missing.")
                return

    def FinalizeCollate(self):
        self.curIndex = 0
        for self.curIndex in range(0, self.count):
            print("Moving " + self.TempFile(self.curIndex) + " to " + self.GetFileName(self.curIndex))
            shutil.move(self.TempFile(self.curIndex), self.GetFileName(self.curIndex))

    def CopyIndexToTemp(self, index):
        firstFile = self.GetFileName(index)
        tempFile = self.TempFile(self.curIndex)
        print("Copying " + firstFile + " to " + tempFile)
        shutil.copy(firstFile, tempFile)
        self.curIndex += 1

    def CopyToTemp(self):
        for i in range(0, int(self.count/2)):
            self.CopyIndexToTemp(i)
            self.CopyIndexToTemp(self.count - 1 - i)

        if self.count % 2 == 1:
            self.CopyIndexToTemp(int(self.count / 2))



def DoInterleave():
    if len(sys.argv) != 3:
        print("Need to specify start index of files to collate, and number of subsequent files.")
        exit()

    for i in range(1, 2):
        if not sys.argv[i].isdigit():
            print("File index and count must both be numbers")
            exit()

    inter = Interleaver(int(sys.argv[1]), int(sys.argv[2]))
    inter.CheckFilesExist()
    inter.CopyToTemp()
    inter.FinalizeCollate()

DoInterleave()

