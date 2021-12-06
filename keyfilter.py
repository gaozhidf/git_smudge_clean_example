#!/usr/bin/env python

import sys

REPLACE_CONTENT = [
    ('USERNAME', 'github'),
    ('PASSWORD', '123456')
]

def usage():
    print("""usage:
        1. for git smudge
            python keyfilter.py smudge
        2. for git clean
            python keyfilter.py clean
        """)

def smudge():
    for line in sys.stdin:
        for a in REPLACE_CONTENT:
            line = line.replace(*a[::-1])
        sys.stdout.write(line)

def clean():
    for line in sys.stdin:
        for a in REPLACE_CONTENT:
            line = line.replace(*a)
        sys.stdout.write(line)

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'smudge':
            smudge()
        elif sys.argv[1] == 'clean':
            clean()
        else:
            usage()
    except Exception as e:
        print(e)
        usage()

