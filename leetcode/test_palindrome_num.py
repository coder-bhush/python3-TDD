# Palindrome Number :

"""Cases : 
1) Number == reverse number
2) Num is not palindrome --> return false
3) Negative num not be palindrome       """


def is_palindrome(n):
    str_n = str(n)
    rev_n = str_n[::-1]
    if str_n == rev_n:
        return True
    else:
        return False


# Test Cases :
def test_num_is_palindrome():
    expected_res = is_palindrome(121)
    assert expected_res == True


def test_num_is_not_palindrome():
    expected_res = is_palindrome(122)
    assert expected_res == False


def test_negative_num_is_palindrome():
    expected_res = is_palindrome(-121)
    assert expected_res == False
