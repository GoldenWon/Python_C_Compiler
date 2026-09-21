#!/usr/bin/env -S python3

import sys
import subprocess

numArgs = len(sys.argv)

if (numArgs < 2):
    sys.exit('Must have at least a C source file argument.')

cSourceFile = sys.argv[1]

cPreProcFile = cSourceFile.removesuffix('c')

cPreProcFile = cPreProcFile + 'i'

if (numArgs == 3):
    option = sys.argv[2]
    print('You chose option ' + option)

subprocess.run(["gcc", "-E", "-P", cSourceFile, "-o", cPreProcFile])