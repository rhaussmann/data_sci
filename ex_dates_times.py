import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# >>>0.3018611848820001
# Command line: python -m timeit [-n N] [-r N] [-u U] [-s S] [-t] [-c] [-h] [statement ...]

