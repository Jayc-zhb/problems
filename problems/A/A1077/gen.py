from random import *
from cyaron import *

CASES = 20

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sample = ["A", "a", "C","c" ,"Aa" , "AC","Ac" ,"aC" ,'ac' ,'AaC' , "Aac", 'ACc','aCc' ,'AaCc']
OK = [True, False]

for _t in range(1, CASES + 1):
    io = IO(f"{_t}.in")
    # ==============================
    ok = choice(OK)
    a = 0
    if _t <= 5 :
        a = randrange(1, 100, 1)
    elif _t <= 10:
        a = randrange(100, 1000, 1)
    elif _t <=15 :
        a = randrange(1000, 10000, 1)
    else :
        a = randrange(100000, 1000000, 1)
    io.input_writeln(a)
    s = ''
    temp = ""
    if ok : 
        temp = choice(sample)
    for _ in range(1, a+1):
        char = ""
        char = choice(alphabet)
        while temp.__contains__(char):
            char = choice(alphabet)
        s = s + char
    io.input_write(f"{s}")
    # ==============================
    io.close()
