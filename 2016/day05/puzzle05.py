#!/usr/bin/python3

# --- Day 5: How About a Nice Game of Chess? ---

import hashlib
import re

k = 'reyedfim'
# k = 'abc'
i = 0
code = ''
# while True:
while False:
    bs = (k + str(i)).encode()
    h = hashlib.md5(bs).hexdigest()
    if h.startswith('00000'):
        code += h[5]
        print(i, code)
        if len(code) == 8:
            break
    i += 1

print("code = %s" % code)


# part 2
k = 'reyedfim'
# k = 'abc'
i = 0
code = {}
while True:
    bs = (k + str(i)).encode()
    h = hashlib.md5(bs).hexdigest()
    m = re.match('^00000([0-7])(.)', h)
    if m:
        pos, char = m.groups()
        if pos not in code:
            code[pos] = char
            print(i, pos, code)
            if len(code) == 8:
                break
    i += 1

codew = ''
for i in range(8):
    codew += code[str(i)]
print("code = %s" % codew)
