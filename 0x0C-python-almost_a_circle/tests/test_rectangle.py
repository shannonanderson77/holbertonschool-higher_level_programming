#!/usr/bin/python3
"""
Unittest for Rectangle([..])

"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Rectangle class tests'''

    def test_rectangle_a_instantiation(self):
        '''Test instantiation of a Rectangle class'''
        rect = Rectangle(1, 2)
        self.assertIsInstance(rect, Base)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_b_all_attributes(self):
        '''Test instantiation of Rectangle class with all attributes'''
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 5)

    def test_rectangle_c_one_attribute(self):
        '''Test instantiation of a Rectangle class with one attribute'''
        with self.assertRaises(TypeError):
            rect = Rectangle(1)

    def test_rectangle_d_missing_attributes(self):
        '''Test instantiation of a Rectangle class missing arguments'''
        with self.assertRaises(TypeError):
            rect = Rectangle()

#    def test_rectangle_id_not_none(self):
#        '''Test instantiation of a Rectangle class with id!=None'''
#        self.assertEqual(rect3.id, 5)
