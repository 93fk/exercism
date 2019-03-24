import numpy as np

coefs = [i for i in range(10,0,-1)]
legal_characters = [str(i) for i in range(10)]+['X']

def verify(isbn):
    isbn = isbn.replace('-', '')
    cond_1 = len(isbn) == 10
    cond_2 = 'X' not in isbn[:-1]
    cond_3 = set(isbn).issubset(set(legal_characters))
    if cond_1 and cond_2 and cond_3:
        last = 10 if isbn[-1] == 'X' else int(isbn[-1])
        isbn = [int(i) for i in isbn[:-1]]
        isbn.append(last)
        test_val = sum(isbn*np.array(coefs))
        if test_val % 11 == 0:
            return True
        else:
            return False
    else:
        return False


verify('3-598-21507-X')
