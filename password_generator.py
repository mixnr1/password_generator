# -*- coding: utf-8 -*-
#!/usr/bin/env python
#from os import urandom
import os
import argparse
charsets={
"a":"abcdefghijklmnopqrstuvwxyz",\
"A":"ABCDEFGHIJKLMNOPQRSTUVWXYZ",\
"0":"0123456789",\
"$":"^!\"$%&/()=?{[]}+*~#'-_.:,;<>|\\ "\
}
def GeneratePassword(length=9,charset="aA0$"):
    password=""
    lc=""
    charset_string=""
    for c in charset:
        if c in charsets.keys():
            charset_string+=charsets[c]
    while len(password)<length:
        c=os.urandom(1).decode("utf-8", "replace")
        if c in charset_string and c!=lc:
            password+=c
            lc=c
    return password

def main(plen, pcount, charset):
    for _ in range(pcount):
        print(GeneratePassword(plen, charset))


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate Password")
    parser.add_argument('integers', metavar='N', type=int, help='length of password')
    parser.add_argument('pcount', metavar='p', type=int, help='how many passwords to generate')
    parser.add_argument('charset', help='determine character to be used from "aA0$"')
    args = parser.parse_args()
    main(args.integers, args.pcount, args.charset)
    