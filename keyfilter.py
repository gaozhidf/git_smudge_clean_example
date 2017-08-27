import sys

REPLACE_CONTENT = [
    ('USERNAME', 'github'),
    ('PASSWORD', '123456')
]

def usage():
    print """usage:
        1. for git smudge 
            python keyfilter.py --smudge
        2. for git clean
            python keyfilter.py --clean
        """

def smudge():
    for line in sys.stdin:
        '''
        replace keyword list in line
        https://stackoverflow.com/questions/2484156/is-str-replace-replace-ad-nauseam-a-standard-idiom-in-python
        '''
        line = reduce(lambda s, r: s.replace(*r), REPLACE_CONTENT, line)
        sys.stdout.write(line)

def clean():
    for line in sys.stdin:
        line = reduce(lambda s, r: s.replace(*r[::-1]), REPLACE_CONTENT, line)
        sys.stdout.write(line)

if __name__ == '__main__':
    try:
        if sys.argv[1] == '--smudge':
            smudge()
        elif sys.argv[1] == '--clean':
            clean()
        else:
            usage()
    except Exception, e:
        print e
        usage()
