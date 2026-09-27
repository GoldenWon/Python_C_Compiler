#!/usr/bin/env -S python3

import sys
import subprocess
import re

def lexer():
    current = ""

    # OG regex
    regexes = [
        "[a-zA-Z_]\w*",
        "[0-9]+",
        "int",
        "void",
        "return",
        "\(",
        "\)",
        "{",
        "}",
        ";"
    ]
    combined = "(" + ")|(".join(regexes) + ")"

    wordBoundaries = [
        "\(",
        "\)",
        "{",
        "}",
        ";"
    ]
    wBoundCombined = "(" + ")|(".join(wordBoundaries) + ")"

    with open(cPreProcFile) as f:
        while True:
            char = f.read(1)
            if char == "":
                # Reached EOF
                break
            else:
                if char.isspace():
                    if current:
                        if re.match(combined, current):
                            print(f"Match: {current}")
                            current = ""
                elif re.match(wBoundCombined, char):
                    if re.match(combined, current):
                        print(f"Match: {current}")
                        current = ""
                    print(f"Match: {char}")
                else:
                    current += char

numArgs = len(sys.argv)

if (numArgs < 2):
    sys.exit('Must have at least a C source file argument.')

cSourceFile = sys.argv[1]

cPreProcFile = cSourceFile.removesuffix('c')

cPreProcFile = cPreProcFile + 'i'

subprocess.run(["gcc", "-E", "-P", cSourceFile, "-o", cPreProcFile])

if (numArgs == 3):
    option = sys.argv[2]

    match option:
        case '--lex':
            print('TODO: Run the lexer, but stop before parsing.')
        case '--parse':
            print('TODO: Run the lexer and parser, but stop before assembly generation.')
        case '--codegen':
            print('TODO: Perform lexing, parsing, and assembly generation, but stop before code emission.')
        case '-S':
            print('TODO: Emit an assembly file, but do not assemble or link it.')
        case _:
            sys.exit('There is no such option.')

lexer()