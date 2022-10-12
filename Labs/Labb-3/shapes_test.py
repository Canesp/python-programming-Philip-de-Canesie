from __future__ import annotations
import sys, os
import unittest

from geometry_shapes import Cirkel
from geometry_shapes import Rektangel


class TestShapes(unittest.TestCase):
    
    def setUp(self):
        self.x, self.y = 1, 2
        self.width, self.height = 2, 1
        self.radius = 1

    def create_rektangle(self):
        return Rektangel(x= self.x, y= self.y, width=self.width, height= self.height)
    
    def test_equal_rektangle(self):
        r1 = self.create_rektangle()
        r2 = Rektangel(x= 1, y= 2, width=2, height=1)
        self.assertEqual(r1, r2)
    
    def test_not_equal_rektangle(self):
        r1 = self.create_rektangle()
        r2 = Rektangel(x= 1, y= 2, width=3, height=2)
        self.assertNotEqual(r1, r2)
    
    def test_greater_rektangle(self):
        r1 = self.create_rektangle()
        r2 = Rektangel(x= 1, y= 2, width=1, height=1)
        self.assertGreater(r1, r2)
    
    def test_not_greater_rektangle(self):
        r1 = self.create_rektangle()
        r2 = Rektangel(x= 1, y= 2, width=3, height=2)
        self.assertLess(r1, r2)
    
    def test_greater_equal_rektangle(self):
        r1 = self.create_rektangle()
        r2 = Rektangel(x= 1, y= 2, width=2, height=1)
        self.assertGreaterEqual(r1, r2)
    
    def test_not_greater_equal_rektangle(self):
        r1 = self.create_rektangle()
        r2 = Rektangel(x= 1, y= 2, width=3, height=2)
        self.assertLessEqual(r1, r2)

    #test error 

    def test_empty_rektangle(self):
        with self.assertRaises(TypeError):
            r = Rektangel()

    def test_negativ_width_rektangel(self):
        with self.assertRaises(ValueError):
            r = Rektangel(1, 1, -1, 1)
    
    def test_negativ_height_rektangel(self):
        with self.assertRaises(ValueError):
            r = Rektangel(1, 1, 1, -1)
    
    def test_string_width_rektangel(self):
        with self.assertRaises(TypeError):
            r = Rektangel(1, 1, "1", 1)

    def test_string_height_rektangel(self):
        with self.assertRaises(TypeError):
            r = Rektangel(1, 1, 1, "1")
    
    def test_string_x_rektangel(self):
        with self.assertRaises(TypeError):
            r = Rektangel("1", 1, 1, 1)
    
    def test_string_y_rektangel(self):
        with self.assertRaises(TypeError):
            r = Rektangel(1, "1", 1, 1)

    def test_is_inside_True_rektangel(self):
        x, y = 1, 2
        r1 = self.create_rektangle()
        self.assertTrue(r1.is_inside(x, y)) 
    
    def test_is_inside_True_border_rektangel(self):
        x, y = 1, 3
        r1 = self.create_rektangle()
        self.assertTrue(r1.is_inside(x, y)) 

    def test_is_inside_False_rektangel(self):
        x, y = 5, 5
        r1 = self.create_rektangle()
        self.assertFalse(r1.is_inside(x, y))

if __name__ == "__main__":
    unittest.main()