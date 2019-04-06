#!/usr/bin/env python

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

def run(db, ok, n):
    found = True
    qp = []
    i = 0
    w = 0
    while i < ok:
        dup, w0, w1 = db[i]

        count = w1 - w0
        if count > dup:
            found = False
        c0 = count // 2
        c1 = count - c0

        space = w0 - w
        if space > 0:
            qp.append('0' * space)
        qp.append('0' * c0 + '1' * c1)

        i += dup
        w = w1
    if w != n:
        qp.append('0' * (n-w))

    if found:
        return None

    q = ''.join(qp)
    print(q)
    r = input()

    i = 0
    while i < ok:
        dup, w0, w1 = db[i]

        if dup == w1 - w0:
            i += dup
            continue

        hcount = (w1 - w0) // 2
        rp = r[i:i+dup]
        pos = rp.find('1')
        if pos < 0:
            db[i] = dup, w0, w0 + hcount
        elif pos == 0:
            db[i] = dup, w0 + hcount, w1
        else:
            db[i] = pos, w0, w0 + hcount
            db[i + pos] = dup - pos, w0 + hcount, w1
        i += dup

    return True

def debug(db, n):
    s = ['x'] * n
    for r in db:
        if r is None: continue
        dup, w0, w1 = r
        c = chr(ord('0') + dup)
        s[w0:w1] = [c] * (w1-w0)
    return ''.join(s)

def broken(db, ok, n):
    bs = []
    w = 0
    for row in db:
        if row is None:
            continue
        dup, w0, w1 = row
        for b in range(w, w0):
            bs.append(b)
        w = w1
    if w < n:
        for b in range(w, n):
            bs.append(b)
    assert len(bs) == n - ok
    return ' '.join(map(str, bs))

def solution(count):
    n, b, f = intlist_input()
    ok = n - b

    db = [None] * ok
    db[0] = ok, 0, n  # count, range
    while run(db, ok, n):
        # print('db:', db)
        # print('debug:', debug(db, n))
        pass

    print(broken(db, ok, n))
    r = input()
    assert r == '1'

if __name__ == '__main__':
    count = int_input()
    loop(count, solution)