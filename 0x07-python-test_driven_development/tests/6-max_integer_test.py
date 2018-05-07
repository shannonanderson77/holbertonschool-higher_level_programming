#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''do I need a docstring here'''
    def test_max_at_end(self):
        '''Test when max is at the end of list'''
        list = [1, 2, 3, 4]
        max = max_integer(list)
        self.assertEqual(max, 4)

    def test_max_at_beginning(self):
        '''Test when max is at the beginning of list'''
        list = [4, 3, 2, 1]
        max = max_integer(list)
        self.assertEqual(max, 4)

    def test_max_in_middle(self):
        '''Test when max is in the middle of list'''
        list = [1, 2, 9, 3, 6]
        max = max_integer(list)
        self.assertEqual(max, 9)

    def test_max_one_negative(self):
        '''Test when list has one negative number'''
        list = [1, 6, -4, 2, 3]
        max = max_integer(list)
        self.assertEqual(max, 6)

    def test_max_all_negative(self):
        '''Test when list has all negative numbers'''
        list = [-1, -7, -9, -4]
        max = max_integer(list)
        self.assertEqual(max, -1)

    def test_max_empty_list(self):
        '''Test when list is empty'''
        list = []
        max = max_integer(list)
        self.assertEqual(max, None)

    def test_max_one_element(self):
        '''Test when list has one number'''
        list = [5]
        max = max_integer(list)
        self.assertEqual(max, 5)
