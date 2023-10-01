def test():
    list(range(1000))
from timeit import Timer
t1=Timer('test()','from __main__ import test')
print(t1.timeit(number=1000))