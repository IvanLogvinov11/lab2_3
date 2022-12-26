
#!/usr/bin/env python3
# -- coding: utf-8 --

import math

if __name__ == '__main__':
    st1 = input()
    st2 = input()
    st3 = input()
    l1 = []
    l2 = []
    l3 = []

    for i in st1:
        if i not in st2 and st3:
            l1 += i
    for i in st2:
        if i not in st1 and st3:
            l2 += i
    for i in st3:
        if i not in st1 and st2:
            l3 += i
    print(' '.join(l1), ' '.join(l2), ' '.join(l3))
    print