from __future__ import annotations
import sys, os
import unittest
import math

from geometry_shapes import Cirkel
from geometry_shapes import Rektangel


class TestShapes(unittest.TestCase):
    
    def setUp(self):
        self.x, self.y = 1, 2
        self.width, self.height = 2, 1
        self.radius = 1

    def create_rektangle(self):
        return Rektangel(x= self.x, y= self.y, width=self.width, height= self.height)

    def create_cirkel(self):
        return Cirkel(x= self.x, y= self.y, radius= self.radius)

    """
        Testning rektangel

        -----------------------------------
    """
    
    # operator test rektangel.

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
    
    # Is_inside test rektangel

    def test_is_inside_True_rektangel(self):
        x, y = 1, 2
        r1 = self.create_rektangle()
        self.assertTrue(r1.is_inside(x, y)) 
    
    def test_is_inside_True_border_rektangel(self):
        x, y = 2, 2
        r1 = self.create_rektangle()
        self.assertTrue(r1.is_inside(x, y)) 

    def test_is_inside_False_rektangel(self):
        x, y = 5, 5
        r1 = self.create_rektangle()
        self.assertFalse(r1.is_inside(x, y))

    def test_is_inside_string_x_rektangle(self):
        x, y = "a", 1
        r1 = self.create_rektangle()
        with self.assertRaises(TypeError):
            r1.is_inside(x, y)
    
    def test_is_inside_string_x_rektangle(self):
        x, y = 1, "1"
        r1 = self.create_rektangle()
        with self.assertRaises(TypeError):
            r1.is_inside(x, y)
    
    # Translate test Rektangel

    def test_translate_Equal_rektangle(self):
        x, y = 1, 1
        r1 = self.create_rektangle()
        r1.translate(x, y)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
    
    def test_translate_Not_Equal_rektangle(self):
        x, y = 1, 1
        r1 = self.create_rektangle()
        r1.translate(x, y)
        self.assertNotEqual(r1.x, 3)
        self.assertNotEqual(r1.y, 4)

    def test_translate_Equal_negativ_rektangle(self):
        x, y = -1, -1
        r1 = self.create_rektangle()
        r1.translate(x, y)
        self.assertEqual(r1.x, 0)

    def test_translate_string_x_rektangel(self):
        x, y = "1", 1
        r1 = self.create_rektangle()
        with self.assertRaises(TypeError):
            r1.is_inside(x, y)
    
    def test_translate_string_y_rektangel(self):
        x, y = 1, "1"
        r1 = self.create_rektangle()
        with self.assertRaises(TypeError):
            r1.is_inside(x, y)
    
    # kvadrat test rektangel

    def test_kvadrat_True_rektangel(self):
        r1 = Rektangel(0, 0, 1, 1)
        self.assertTrue(r1.square())
    
    def test_kvadrat_False_rektangel(self):
        r1 = Rektangel(0, 0, 1, 2)
        self.assertFalse(r1.square())

    # area test rektangel 

    def test_area_Equal_rektangle(self):
        r1 = self.create_rektangle()
        a = 2 
        self.assertEqual(r1.area, a)
    
    def test_area_not_Equal_rektangle(self):
        r1 = self.create_rektangle()
        a = 4
        self.assertNotEqual(r1.area, a)

    # omkrets test rektangel

    def test_omkrets_Equal_rektangel(self):
        r1 = self.create_rektangle()
        o = 6
        self.assertEqual(r1.omkrets, o)
    
    def test_omkrets_Not_Equal_rektangel(self):
        r1 = self.create_rektangle()
        o = 10
        self.assertNotEqual(r1.omkrets, o)

    """
        Testning cirkel.

        -----------------------------------
    """

    # operator test rektangel.

    def test_equal_cirkel(self):
        c1 = self.create_cirkel()
        c2 = Cirkel(x= 1, y= 2, radius= 1)
        self.assertEqual(c1, c2)
    
    def test_not_equal_cirkel(self):
        c1 = self.create_cirkel()
        c2 = Cirkel(x= 1, y= 2, radius= 3)
        self.assertNotEqual(c1, c2)
    
    def test_greater_cirkel(self):
        c1 = self.create_cirkel()
        c2 = Cirkel(x= 1, y= 2, radius= 0.5)
        self.assertGreater(c1, c2)
    
    def test_not_greater_cirkel(self):
        c1 = self.create_cirkel()
        c2 = Cirkel(x= 1, y= 2, radius= 5)
        self.assertLess(c1, c2)
    
    def test_greater_equal_cirkel(self):
        c1 = self.create_cirkel()
        c2 = Cirkel(x= 1, y= 2, radius=1)
        self.assertGreaterEqual(c1, c2)
    
    def test_not_greater_equal_cirkel(self):
        c1 = self.create_cirkel()
        c2 = Cirkel(x= 1, y= 2, radius= 1)
        self.assertLessEqual(c1, c2)

    #test error 

    def test_empty_cirkel(self):
        with self.assertRaises(TypeError):
            r = Cirkel()

    def test_negativ_radius(self):
        with self.assertRaises(ValueError):
            r = Cirkel(1, 1, -1)
    
    def test_string_radius_cirkel(self):
        with self.assertRaises(TypeError):
            r = Cirkel(1, 1, "1")

    
    def test_string_x_cirkel(self):
        with self.assertRaises(TypeError):
            r = Cirkel("1", 1, 1)
    
    def test_string_y_cirkel(self):
        with self.assertRaises(TypeError):
            r = Cirkel(1, "1", 1)
    
    # Is_inside test cirkel

    def test_is_inside_True_cirkel(self):
        x, y = 1, 2
        c1 = self.create_cirkel()
        self.assertTrue(c1.is_inside(x, y)) 
    
    def test_is_inside_True_border_cirkel(self):
        x, y = 2, 2
        c1 = self.create_cirkel()
        self.assertTrue(c1.is_inside(x, y)) 

    def test_is_inside_False_cirkel(self):
        x, y = 5, 5
        c1 = self.create_cirkel()
        self.assertFalse(c1.is_inside(x, y))

    def test_is_inside_string_x_cirkel(self):
        x, y = "a", 1
        c1 = self.create_cirkel()
        with self.assertRaises(TypeError):
            c1.is_inside(x, y)
    
    def test_is_inside_string_x_cirkel(self):
        x, y = 1, "1"
        c1 = self.create_cirkel()
        with self.assertRaises(TypeError):
            c1.is_inside(x, y)
    
    # Translate test Cirkel

    def test_translate_Equal_cirkel(self):
        x, y = 1, 1
        c1 = self.create_cirkel()
        c1.translate(x, y)
        self.assertEqual(c1.x, 2)
        self.assertEqual(c1.y, 3)
    
    def test_translate_Not_Equal_cirkel(self):
        x, y = 1, 1
        c1 = self.create_cirkel()
        c1.translate(x, y)
        self.assertNotEqual(c1.x, 3)
        self.assertNotEqual(c1.y, 4)

    def test_translate_Equal_negativ_cirkel(self):
        x, y = -1, -1
        c1 = self.create_cirkel()
        c1.translate(x, y)
        self.assertEqual(c1.x, 0)

    def test_translate_string_x_cirkel(self):
        x, y = "1", 1
        c1 = self.create_cirkel()
        with self.assertRaises(TypeError):
            c1.is_inside(x, y)
    
    def test_translate_string_y_cirkel(self):
        x, y = 1, "1"
        c1 = self.create_cirkel()
        with self.assertRaises(TypeError):
            c1.is_inside(x, y)
    
    # enhets_Cirkel test Cirkel

    def test_enhets_Cirkel_True_cirkel(self):
        c1 = Cirkel(0, 0, 1)
        self.assertTrue(c1.enhets_Cirkel())
    
    def test_enhets_Cirkel_False_cirkel(self):
        c1 = Cirkel(0, 0, 2)
        self.assertFalse(c1.enhets_Cirkel())

    # area test Cirkel 

    def test_area_Equal_rektangle(self):
        c1 = self.create_cirkel()
        a = math.pi * 1**2
        self.assertEqual(c1.area, a)
    
    def test_area_not_Equal_cirkel(self):
        c1 = self.create_cirkel()
        a = 4
        self.assertNotEqual(c1.area, a)

    # omkrets test rektangel

    def test_omkrets_Equal_cirkel(self):
        c1 = self.create_cirkel()
        o = 2*math.pi * 1
        self.assertEqual(c1.omkrets, o)
    
    def test_omkrets_Not_Equal_cirkel(self):
        c1 = self.create_cirkel()
        o = 10
        self.assertNotEqual(c1.omkrets, o)
    

if __name__ == "__main__":
    unittest.main()