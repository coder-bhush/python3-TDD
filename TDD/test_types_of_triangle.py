'''
1) Triangle is scalene 
2) Triangle is isosceles
3) Triangle is equilateral

'''


#Solution:
    # Equilateral -->   Length of all 3 sides are same 
    # Isosceles  -->   Length of any Two sides are Same 
    # Scalene    -->   Length of all 3 sides are different 
   

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
    assert  triangle_is(20,15,15) == 'isosceles'
    assert  triangle_is(15,15,20) == 'isosceles'
    assert  triangle_is(15,20,15) == 'isosceles'
    
def test_triangle_is_scalene():
    expected_res = triangle_is(10,15,20)
    assert expected_res == 'scalene'
    