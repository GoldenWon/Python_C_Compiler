#!/usr/bin/env -S python3

import sys
import subprocess

numArgs = len(sys.argv)

if (numArgs < 2):
    sys.exit('Must have at least a C source file argument.')

pathToProgram = sys.argv[1]

print(pathToProgram)

programName = pathToProgram.split('/')

numSplitProgramName = len(programName)

programName = programName[numSplitProgramName - 1]

programName = programName.split('.')

programName = programName[0]

programName = programName + '.i'

print(programName)

if (numArgs == 3):
    option = sys.argv[2]
    print('You chose option ' + option)

subprocess.run(["gcc", "-E", "-P", pathToProgram, "-o", programName])