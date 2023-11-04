# Merge two lists and create new sorted list..
""" 
Cases :
 1) One list is empty
 2) Both lists having some containt
 3) Both two lists are empty Lists
                                        """


def merge_two_sorted_lists(list1, list2):
    list1.sort()
    list2.sort()
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

# Test Cases:
def test_merge_two_lists_one_is_empty():
    expected_res = merge_two_sorted_lists([], [1, 3, 15])
    assert expected_res == [1, 3, 15]

def test_merge_two_lists_having_some_content():
    expected_res = merge_two_sorted_lists([8, 10, 2], [1, 3, 15])
    assert expected_res == [1, 2, 3, 8, 10, 15]

def test_merge_two_empty_lists():
    expected_res = merge_two_sorted_lists([], [])
    assert expected_res == []
