# FizzBuzz

""" 
1) Div by 3              return      Fizz
2) Div by 5              return      Buzz
3) Div by both 3 & 5     return      FizzBuzz
4) Not Div by 3 and 5    return      Empty Str or \n

"""


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def fizzbuzz100():
    s = ""
    for i in range(1, 101):
        result = fizzbuzz(i)
        s += result + "\n"
    return s


# Test Cases :
def test_fizzbuzz_should_return_fizz_if_number_is_divisible_by_3():
    expected_result = fizzbuzz(6)
    assert expected_result == "Fizz"


def test_fizzbuzz_should_return_buzz_if_number_is_divisible_by_5():
    expected_result = fizzbuzz(25)
    assert expected_result == "Buzz"


def test_fizzbuzz_should_return_fizzbuzz_if_number_is_divisible_by_3_and_5():
    expected_result = fizzbuzz(15)
    assert expected_result == "Fizzbuzz"


def test_fizzbuzz_should_return_number_if_number_is_not_divisible_by_3_or_5():
    expected_result = fizzbuzz(4)
    assert expected_result == "4"


def test_fizzbuzz_100_should_return_100_lines():
    expected_result = fizzbuzz100()
    lines = expected_result.split("\n")
    assert len(lines) == 101
