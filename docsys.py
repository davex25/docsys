#!/usr/bin/python3

import os

def WalkCurFolder(operation):
    for root, ins, files in os.walk('./'):
        for f in files:
            operation(root, f)

