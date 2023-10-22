# Triangle is equilateral
# Triangle is isosceles
# Triangle is scalene


#Solution:
# How can i solve it :
    # Equilateral -->   Length of all 3 sides are same 
    # Isosceles  -->   Length of any Two sides are Same 
    # Scalene     -->   Length of all 3 sides are different 
   

def triangle_is(side1,side2,side3):
    if side1 == side2 and side2 == side3 and side3 == side1:
        return 'equilateral'
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return 'isosceles'
    else:
        return 'scalene'
    
# Test cases : 


def test_triangle_is_equilateral():
    expected_res = triangle_is(15,15,15)
    assert expected_res == 'equilateral'


def test_triangle_is_isosceles():
    expected_res = triangle_is(20,15,15)
    assert expected_res == 'isosceles'
    
def test_triangle_is_scalene():
    expected_res = triangle_is(10,15,20)
    assert expected_res == 'scalene'
    