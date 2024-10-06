from random import *
from cyaron import *

CASES = 20

for _t in range(1, CASES + 1):
    io = IO(f"{_t}.in")
    # ==============================
    n = 0
    m = 0
    if _t <= 1:
        n = randrange(2, 5, 1)
    elif _t <= 2:
        n = randrange(2, 10, 1)
    elif _t <= 5 :
        n = randrange(1, 101, 1)
    elif _t <= 10:
        n = randrange(101, 1001, 1)
    elif _t <=15 :
        n = randrange(1001, 100001, 1)
    else :
        n = randrange(100001, 1000001, 1)
    io.input_write(n)
    io.input_write(' ')
    m = randrange(0, n+1, 1)
    io.input_writeln(m)
    for i in range(1, n+1):
        b = 0
        v = 0
        if _t <= 5 :
            b = randrange(1, 21, 1)
            v = randrange(1, 21, 1)
        elif _t <= 10:
            b = randrange(20, 10001, 1)
            v = randrange(20, 10001, 1)
        elif _t <=15 :
            b = randrange(10001, 1000001, 1)
            v = randrange(10001, 1000001, 1)
        else :
            b = randrange(1000001, 10000001, 1)
            v = randrange(1000001, 10000001, 1)
        io.input_write(b)
        io.input_write(' ')
        io.input_writeln(v)
    # ==============================
    io.close()
