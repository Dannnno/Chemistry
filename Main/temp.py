s = "foo123"

def f(s):
    n = ['1','2','3','4','5','6','7','8','9']
    for i in range(0,len(s)):
        if s[i] in n:
            return (s[:i],s[i:])

print f(s)

import re

print re.split('(\d+)',s)[:-1]
n = "foo123 bar456"
print re.split('(\d+)',n)[:-1]