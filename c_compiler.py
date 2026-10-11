#!/usr/bin/env -S python3

import sys
import subprocess
import re

def lexer():
    current = ""

    # OG regex
    regexes = [
        "[a-zA-Z_][a-zA-Z0-9_]*$",
        "\d+$",
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
            #if char == "":
            #    # Reached EOF
            #    print(f"char: {current}")
            #    break
            #else:
            if char.isspace():
                if current:
                    if re.match(combined, current):
                        print(f"WordMatch: {current}")
                        current = ""
            elif re.match(wBoundCombined, char):
                if current:
                    if re.match(combined, current):
                        print(f"WordMatch: {current}")
                        current = ""
                    else:
                        sys.exit(f"Error: {current}")   #print(f"Error: {current}")
                print(f"CharMatch: {char}")
            elif char == "":
                # Reached EOF
                if current:
                    #if re.match(combined, current):
                    #    print(f"WordMatch: {current}")
                    #    current = ""
                    #else:
                    # Must be an error if we didn't catch it earlier.
                    sys.exit(f"Error: {current}")
                break
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