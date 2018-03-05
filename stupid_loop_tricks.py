#Time a process Library

import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# >>>0.3018611848820001
# Command line: python -m timeit [-n N] [-r N] [-u U] [-s S] [-t] [-c] [-h] [statement ...]

from itertools import chain, islice

def chunks(iterable, size, format=iter):
    it = iter(iterable)
    while True:
        yield format(chain((it.next(),), islice(it, size - 1)))

l = ["a", "b", "c", "d", "e", "f", "g"]
for chunk in chunks(l, 3, tuple):
    print (chunk)
