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
        rect = Rectangle(1, 2, 0, 0, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 5)

    def test_rectangle_c_one_attribute(self):
        '''Test instantiation of a Rectangle class with one attribute'''
        with self.assertRaises(TypeError):
            rect = Rectangle(1)

    def test_rectangle_d_missing_attributes(self):
        '''Test instantiation of a Rectangle class missing arguments'''
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_rectangle_e_neg_width(self):
        '''Test instantiation of a Rectangle class with negative width'''
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 2)
            self.assertIn("width must be > 0", message)

    def test_rectangle_f_neg_height(self):
        '''Test instantiation of a Rectangle class with negative height'''
        with self.assertRaises(ValueError):
            rect = Rectangle(1, -2)
            self.assertIn("height must be > 0", message)

    def test_rectangle_g_neg_x(self):
        '''Test instantiation of a Rectangle class with negative x'''
        with self.assertRaises(ValueError) as message:
            rect = Rectangle(1, 2, -3, 4)
            self.assertIn("x must be >= 0", message)

    def test_rectangle_h_neg_y(self):
        '''Test instantiation of a Rectangle class with negative y'''
        with self.assertRaises(ValueError) as message:
            rect = Rectangle(-1, 2, 3, -4)
            self.assertIn("y must be >= 0", message)

    def test_rectangle_i_zero_width(self):
        '''Test instantiation of a Rectangle class with zero width'''
        with self.assertRaises(ValueError) as message:
            rect = Rectangle(0, 2)
            self.assertIn("width must be > 0", message)

    def test_rectangle_j_zero_height(self):
        '''Test instantiation of a Rectangle class with zero height'''
        with self.assertRaises(ValueError) as message:
            rect = Rectangle(1, 0)
            self.assertIn("height must be > 0", message)

    def test_rectangle_k_string_width(self):
        '''Test instantiation of a Rectangle class with string width'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle("1", 2)
            self.assertIn("width must be an integer", message)

    def test_rectangle_l_string_x(self):
        '''Test instantiation of a Rectangle class with string x'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, "3", 4)
            self.assertIn("x must be an integer", message)

    def test_rectangle_m_string_y(self):
        '''Test instantiation of a Rectangle class with string y'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, 3, "4")
            self.assertIn("y must be an integer", message)

    def test_rectangle_n_string_height(self):
        '''Test instantiation of a Rectangle class with string height'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, "2")
            self.assertIn("height must be an integer", message)

    def test_rectangle_o_float_width(self):
        '''Test instantiation of a Rectangle class with float width'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1.5, 2)
            self.assertIn("width must be an integer", message)

    def test_rectangle_p_float_x(self):
        '''Test instantiation of a Rectangle class with float x'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, 3.5, 4)
            self.assertIn("x must be an integer", message)

    def test_rectangle_q_float_y(self):
        '''Test instantiation of a Rectangle class with float y'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, 3, 4.5)
            self.assertIn("y must be an integer", message)

    def test_rectangle_r_float_height(self):
        '''Test instantiation of a Rectangle class with float height'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2.5)
            self.assertIn("height must be an integer", message)

    def test_rectangle_s_none_width(self):
        '''Test instantiation of a Rectangle class with None width'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(None, 2)
            self.assertIn("width must be an integer", message)

    def test_rectangle_t_none_x(self):
        '''Test instantiation of a Rectangle class with None x'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, None, 4)
            self.assertIn("x must be an integer", message)

    def test_rectangle_u_none_y(self):
        '''Test instantiation of a Rectangle class with None y'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, 3, None)
            self.assertIn("y must be an integer", message)

    def test_rectangle_v_none_height(self):
        '''Test instantiation of a Rectangle class with None height'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, None)
            self.assertIn("height must be an integer", message)

    def test_rectangle_w_list_width(self):
        '''Test instantiation of a Rectangle class with list width'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle([1], 2)
            self.assertIn("width must be an integer", message)

    def test_rectangle_x_list_x(self):
        '''Test instantiation of a Rectangle class with list x'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, [3], 4)
            self.assertIn("x must be an integer", message)

    def test_rectangle_y_list_y(self):
        '''Test instantiation of a Rectangle class with list y'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, 3, [4])
            self.assertIn("y must be an integer", message)

    def test_rectangle_z_list_height(self):
        '''Test instantiation of a Rectangle class with list height'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, [2])
            self.assertIn("height must be an integer", message)

    def test_rectangle_aa_tuple_width(self):
        '''Test instantiation of a Rectangle class with tuple width'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle((1,), 2)
            self.assertIn("width must be an integer", message)

    def test_rectangle_bb_tuple_x(self):
        '''Test instantiation of a Rectangle class with tuple x'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, (3,), 4)
            self.assertIn("x must be an integer", message)

    def test_rectangle_cc_tuple_y(self):
        '''Test instantiation of a Rectangle class with tuple y'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, 3, (4,))
            self.assertIn("y must be an integer", message)

    def test_rectangle_dd_tuple_height(self):
        '''Test instantiation of a Rectangle class with tuple height'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, (2,))
            self.assertIn("height must be an integer", message)

    def test_rectangle_ee_nan_width(self):
        '''Test instantiation of a Rectangle class with NaN width'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(float('nan'), 2)
            self.assertIn("width must be an integer", message)

    def test_rectangle_ff_nan_x(self):
        '''Test instantiation of a Rectangle class with NaN x'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, float('nan'), 4)
            self.assertIn("x must be an integer", message)

    def test_rectangle_gg_nan_y(self):
        '''Test instantiation of a Rectangle class with NaN y'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, 3, float('nan'))
            self.assertIn("y must be an integer", message)

    def test_rectangle_hh_nan_height(self):
        '''Test instantiation of a Rectangle class with NaN height'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, float('nan'))
            self.assertIn("height must be an integer", message)

    def test_rectangle_ii_inf_width(self):
        '''Test instantiation of a Rectangle class with Inf width'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(float('inf'), 2)
            self.assertIn("width must be an integer", message)

    def test_rectangle_jj_inf_x(self):
        '''Test instantiation of a Rectangle class with Inf x'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, float('inf'), 4)
            self.assertIn("x must be an integer", message)

    def test_rectangle_kk_inf_y(self):
        '''Test instantiation of a Rectangle class with Inf y'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, 2, 3, float('inf'))
            self.assertIn("y must be an integer", message)

    def test_rectangle_ll_inf_height(self):
        '''Test instantiation of a Rectangle class with Inf height'''
        with self.assertRaises(TypeError) as message:
            rect = Rectangle(1, float('inf'))
            self.assertIn("height must be an integer", message)

    def test_rectangle_mm_area(self):
        '''Test area of rectangle'''
        rect = Rectangle(2, 2)
        self.assertEqual(rect.area(), 4)
