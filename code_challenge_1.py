# class CircularArray(object):
#     """An array that may be rotated, and items retrieved by index"""

#     def __init__(self):
#         """Instantiate CircularArray."""
#         self.list = []
#         self.head = None


#     def add_item(self, item):
#         """Add item to array, at the end of the current rotation."""
#         if self.head is None:
#             self.head = 0
#             self.list = [item]
#         else:
#             #insert it at END of array, which is right "before" the head
#             self.list.insert(self.head, item)
#             self.head += 1

#     def get_by_index(self, index):
#         """Return the data at a particular index."""
#         if index >= len(self.list):
#             return None
#         else:
#             if index + self.head < len(self.list):
#                 return self.list[index + self.head]
#             else:
#                 adjusted_index = self.head + index - len(self.list)
#                 return self.list[adjusted_index]

#     def rotate(self, increment):
#         """Rotate array, positive for right, negative for left.

#         If increment is greater than list length, keep going around.
#         """

#         if self.head is None:
#             return None
#         else:
#             adjusted = (self.head + increment) % len(self.list)
#             self.head = adjusted 

            

#     def print_array(self):
#         """Print the circular array items in order, one per line"""
        
#         print(self.list[self.head:] + self.list[:self.head])




# circ = CircularArray()
# circ.add_item('harry')
# circ.add_item('hermione')
# circ.add_item('ginny')
# circ.add_item('ron')
# circ.rotate(-2)
# circ.add_item('dobby')
# circ.print_array()


################################################################################
################################################################################



"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""







if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")