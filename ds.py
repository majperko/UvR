from math import sqrt
from itertools import count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


T = set()
S = set()
P = set()

n = 100

for st in range(n+1):
    if st != 0:
        if st % 3 == 0:
            T.add(st)
        if st % 4 == 0:
            S.add(st)
        if is_prime(st):
            P.add(st)


# Tuki samo vstavs tisto formulo k jo dobis na vsaki strani skalarnega produkta.
# Unija =  T.union(P)
# Presek = P & T
# T brez P = T - P

pr = ((P.union(S)).union(T)) - (S & T)
dr = T-S

print(len(pr) * len(dr))