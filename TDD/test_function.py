
#

def even_odd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def test_even_no():
    res = even_odd(22)
    assert res == 'Even' 

def test_even_no():
    res = even_odd(19)
    assert res == 'Odd'    

