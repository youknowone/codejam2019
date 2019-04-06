#!/usr/bin/env python
# working for sample but not working for attempts

def int_input():
    text = input()
    return int(text)

def list_input(size=None):
    text = input()
    str_values = text.split(' ')
    if size is not None:
        assert len(str_values) == size
    return str_values

def intlist_input(size=None):
    return [int(item) for item in list_input(size)]

def loop(count, func):
    for x in range(0, count):
        func(x)

def print_case(count, fmt, *args, **kw):
    prefix = 'Case #{}:'.format(count + 1)
    if len(args) or len(kw):
        print(prefix, fmt.format(*args, **kw))
    else:
        print(prefix, fmt)

from math import gcd

alphalits = [chr(ord('A') + n) for n in range(26)]

def solution(count):
    n, l = intlist_input()
    enc = intlist_input()
    assert len(enc) == l

    dec = [gcd(enc[i], enc[i+1]) for i in range(l-1)]
    dec.insert(0, enc[0] // dec[0])
    dec.append(enc[-1] // dec[-1])

    alphabets = sorted(frozenset(dec))
    # assert len(alphabets) == 26
    # print(dec, alphabets)
    alphamap = dict(zip(alphabets, alphalits))

    s = ''.join(alphamap[a] for a in dec)
    assert len(s) == l + 1

    print_case(count, s)

if __name__ == '__main__':
    count = int_input()
    loop(count, solution)