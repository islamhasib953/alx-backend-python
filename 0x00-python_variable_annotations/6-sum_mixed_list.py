#!/usr/bin/env python3
''' sum of list numbers of floats anf integrs '''

from typing import List
def sum_mixed_list(mxd_lst: List[int|float]) -> float:
    '''  function sum_mixed_list takes a list of integers and floats and returns sum as a float. '''
    return sum(mxd_lst)
