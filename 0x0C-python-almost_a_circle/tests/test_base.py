#!/usr/bin/python3
"""
Unittest for Base([..])

"""
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Base class tests'''

    def test_base_a_instantiation(self):
        '''Test instantiation of a Base class'''
        bc = Base()
        self.assertIsInstance(bc, Base)
        self.assertEqual(bc.id, 1)

    def test_base_b_id_none(self):
        '''Test incrementation of Base class'''
        bc = Base()
        self.assertEqual(bc.id, 2)

    def test_base_c_id_not_none(self):
        '''Test instantiation of a Base class with id!=None'''
        bc = Base(5)
        self.assertEqual(bc.id, 5)

    def test_base_e_id_increment(self):
        '''Test incrementation of Base class id increment after none'''
        bc = Base()
        self.assertEqual(bc.id, 3)

    def test_base_e_id_negative(self):
        '''Test instantiation of a Base class with id negative number'''
        with self.assertRaises(ValueError):
            bc = Base(-10)

    def test_base_f_id_float(self):
        '''Test instantiation of a Base class with id float'''
        with self.assertRaises(ValueError):
            bc = Base(10.5)

    def test_base_g_id_list(self):
        '''Test instantiation of a Base class with id list'''
        with self.assertRaises(TypeError):
            bc = Base([1])

    def test_base_h_id_string(self):
        '''Test instantiation of a Base class with id string'''
        with self.assertRaises(TypeError):
            bc = Base("Betty")

    def test_base_i_id_tuple(self):
        '''Test instantiation of a Base class with id tuple'''
        with self.assertRaises(TypeError):
            bc = Base((1,))
