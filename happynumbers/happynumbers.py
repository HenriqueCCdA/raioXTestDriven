def happy_it(number):
    box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum(int(char)**2 for char in  str(n))
    return n == 1

def happy_rec(number):
    next_ = sum(int(char)**2 for char in  str(number))
    return number in (1, 7) if number < 10 else happy(next_)

happy = happy_rec

assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 8, 9))