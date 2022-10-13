from __future__ import annotations
import sys, os
from time import sleep
import unittest
import math

from geometry_shapes import Cirkel
from geometry_shapes import Rektangel
from geometry_shapes import Cube
from geometry_shapes import Sphere


class TestShapes(unittest.TestCase):
    
    def setUp(self):
        self.x, self.y, self.z = 1, 2, 1
        self.width, self.height = 2, 1
        self.radius = 1
        self.depth = 1

    def create_rektangle(self):
        return Rektangel(x= self.x, y= self.y, width=self.width, height= self.height)

    def create_cirkel(self):
        return Cirkel(x= self.x, y= self.y, radius= self.radius)

    def create_cube(self):
        return Cube(x= self.x, y= self.y, z= self.z, width= self.width, height= self.height, depth= self.depth)

    def create_sphere(self):
        return Sphere(x= self.x, y= self.y, z= self.z, radius= self.radius)

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

    # operator test cirkel.

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
    
    def test_is_inside_string_y_cirkel(self):
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
        self.assertEqual(c1.y, 1)

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

    def test_area_Equal_cirkel(self):
        c1 = self.create_cirkel()
        a = math.pi * 1**2
        self.assertEqual(c1.area, a)
    
    def test_area_not_Equal_cirkel(self):
        c1 = self.create_cirkel()
        a = 4
        self.assertNotEqual(c1.area, a)

    # omkrets test cirkel

    def test_omkrets_Equal_cirkel(self):
        c1 = self.create_cirkel()
        o = 2*math.pi * 1
        self.assertEqual(c1.omkrets, o)
    
    def test_omkrets_Not_Equal_cirkel(self):
        c1 = self.create_cirkel()
        o = 10
        self.assertNotEqual(c1.omkrets, o)

    
    """
        Testning Cube

        -----------------------------------
    """
    
    # operator test Cube.

    def test_equal_Cube(self):
        cu1 = self.create_cube()
        cu2 = Cube(x= 1, y= 2, z= 1, width=2, height=1, depth=1)
        self.assertEqual(cu1, cu2)
    
    def test_not_equal_cube(self):
        cu1 = self.create_cube()
        cu2 = Cube(x= 1, y= 2, z= 1, width=3, height=1, depth=1)
        self.assertNotEqual(cu1, cu2)
    
    def test_greater_cube(self):
        cu1 = self.create_cube()
        cu2 = Cube(x= 1, y= 2, z= 1, width=1, height=1, depth=1)
        self.assertGreater(cu1, cu2)
    
    def test_not_greater_cube(self):
        cu1 = self.create_cube()
        cu2 = Cube(x= 1, y= 2, z= 1, width=5, height=1, depth=1)
        self.assertLess(cu1, cu2)
    
    def test_greater_equal_cube(self):
        cu1 = self.create_cube()
        cu2 = Cube(x= 1, y= 2, z= 1, width=2, height=1, depth=1)
        self.assertGreaterEqual(cu1, cu2)
    
    def test_not_greater_equal_cube(self):
        cu1 = self.create_cube()
        cu2 = Cube(x= 1, y= 2, z= 1, width=2, height=1, depth=1)
        self.assertLessEqual(cu1, cu2)

    #test error 

    def test_empty_cube(self):
        with self.assertRaises(TypeError):
            cu = Cube()

    def test_negativ_width_cube(self):
        with self.assertRaises(ValueError):
            cu = Cube(1, 1, 1, -1, 1, 1)
    
    def test_negativ_height_cube(self):
        with self.assertRaises(ValueError):
            r = Cube(1, 1, 1, 1, -1, 1)
    
    def test_negativ_depth_cube(self):
        with self.assertRaises(ValueError):
            r = Cube(1, 1, 1, 1, 1, -1)
    
    def test_string_width_cube(self):
        with self.assertRaises(TypeError):
            r = Cube(1, 1, 1, "1", 1, 1)

    def test_string_height_cube(self):
        with self.assertRaises(TypeError):
            r = Cube(1, 1, 1, 1, "1", 1)
    
    def test_string_depth_cube(self):
        with self.assertRaises(TypeError):
            r = Cube(1, 1, 1, 1, 1, "1")
    
    def test_string_x_cube(self):
        with self.assertRaises(TypeError):
            r = Cube("1", 1, 1, 1, 1, 1)
    
    def test_string_y_cube(self):
        with self.assertRaises(TypeError):
            r = Cube(1, "1", 1, 1, 1, 1)
    
    def test_string_z_cube(self):
        with self.assertRaises(TypeError):
            r = Cube(1, 1, "1", 1, 1, 1)
    
    # Is_inside test cube

    def test_is_inside_True_cube(self):
        x, y, z = 1, 2, 1
        cu1 = self.create_cube()
        self.assertTrue(cu1.is_inside(x, y, z)) 
    
    def test_is_inside_True_border_cube(self):
        x, y, z = 2, 2, 1
        cu1 = self.create_cube()
        self.assertTrue(cu1.is_inside(x, y, z)) 

    def test_is_inside_False_cube(self):
        x, y, z = 5, 5, 5
        cu1 = self.create_cube()
        self.assertFalse(cu1.is_inside(x, y, z))

    def test_is_inside_string_x_cube(self):
        x, y, z = "a", 1, 1
        cu1 = self.create_cube()
        with self.assertRaises(TypeError):
            cu1.is_inside(x, y, z)
    
    def test_is_inside_string_y_cube(self):
        x, y, z = 1, "1", 1
        cu1 = self.create_cube()
        with self.assertRaises(TypeError):
            cu1.is_inside(x, y, z)
    
    def test_is_inside_string_z_cube(self):
        x, y, z = 1, 1, "1"
        cu1 = self.create_cube()
        with self.assertRaises(TypeError):
            cu1.is_inside(x, y, z)
    
    # Translate test cube

    def test_translate_Equal_cube(self):
        x, y, z = 1, 1, 1
        cu1 = self.create_cube()
        cu1.translate(x, y, z)
        self.assertEqual(cu1.x, 2)
        self.assertEqual(cu1.y, 3)
        self.assertEqual(cu1.z, 2)
    
    def test_translate_Not_Equal_cube(self):
        x, y, z = 1, 1, 1
        cu1 = self.create_cube()
        cu1.translate(x, y, z)
        self.assertNotEqual(cu1.x, 3)
        self.assertNotEqual(cu1.y, 4)
        self.assertNotEqual(cu1.z, 4)

    def test_translate_Equal_negativ_cube(self):
        x, y, z = -1, -1, -1
        cu1 = self.create_cube()
        cu1.translate(x, y, z)
        self.assertEqual(cu1.x, 0)
        self.assertEqual(cu1.y, 1)
        self.assertEqual(cu1.z, 0)

    def test_translate_string_x_cube(self):
        x, y, z = "1", 1, 1
        cu1 = self.create_cube()
        with self.assertRaises(TypeError):
            cu1.is_inside(x, y, z)
    
    def test_translate_string_y_cube(self):
        x, y, z = 1, "1", 1
        cu1 = self.create_cube()
        with self.assertRaises(TypeError):
            cu1.is_inside(x, y, z)
    
    def test_translate_string_z_cube(self):
        x, y, z = 1, "1", 1
        cu1 = self.create_cube()
        with self.assertRaises(TypeError):
            cu1.is_inside(x, y, z)
    
    # is_cube test cube

    def test_cube_True_cube(self):
        cu1 = Cube(0, 0, 0, 1, 1, 1)
        self.assertTrue(cu1.is_cube())
    
    def test_cube_False_cube(self):
        cu1 = Cube(0, 0, 0, 1, 1, 2)
        self.assertFalse(cu1.is_cube())

    # area test cube

    def test_area_Equal_cube(self):
        cu1 = self.create_cube()
        a = 2 
        self.assertEqual(cu1.area, a)
    
    def test_area_not_Equal_cube(self):
        cu1 = self.create_cube()
        a = 16
        self.assertNotEqual(cu1.area, a)

    # omkrets test cube

    def test_omkrets_Equal_cube(self):
        cu1 = self.create_cube()
        o = 16
        self.assertEqual(cu1.omkrets, o)
    
    def test_omkrets_Not_Equal_cube(self):
        cu1 = self.create_cube()
        o = 10
        self.assertNotEqual(cu1.omkrets, o)

    # volym test cube

    def test_volym_Equal_cube(self):
        cu1 = self.create_cube()
        v = 2
        self.assertEqual(cu1.volym, v)
    
    def test_volym_Not_Equal_cube(self):
        cu1 = self.create_cube()
        v = 7
        self.assertNotEqual(cu1.volym, v)

    """
        Testning Sphere.

        -----------------------------------
    """

    # operator test sphere.

    def test_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(x= 1, y= 2, z= 1, radius= 1)
        self.assertEqual(s1, s2)
    
    def test_not_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(x= 1, y= 2, z= 1, radius= 3)
        self.assertNotEqual(s1, s2)
    
    def test_greater_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(x= 1, y= 2, z=1, radius= 0.5)
        self.assertGreater(s1, s2)
    
    def test_not_greater_sphere(self):
        s1 = self.create_cirkel()
        s2 = Sphere(x= 1, y= 2, z= 1, radius= 5)
        self.assertLess(s1, s2)
    
    def test_greater_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(x= 1, y= 2, z= 1, radius=1)
        self.assertGreaterEqual(s1, s2)
    
    def test_not_greater_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(x= 1, y= 2, z= 1, radius= 1)
        self.assertLessEqual(s1, s2)

    #test error 

    def test_empty_sphere(self):
        with self.assertRaises(TypeError):
            r = Sphere()

    def test_negativ_radius_sphere(self):
        with self.assertRaises(ValueError):
            r = Sphere(1, 1, 1, -1)
    
    def test_string_radius_sphere(self):
        with self.assertRaises(TypeError):
            r = Sphere(1, 1, 1, "1")

    
    def test_string_x_sphere(self):
        with self.assertRaises(TypeError):
            r = Sphere("1", 1, 1, 1)
    
    def test_string_y_sphere(self):
        with self.assertRaises(TypeError):
            r = Sphere(1, "1", 1, 1)
    
    def test_string_z_sphere(self):
        with self.assertRaises(TypeError):
            r = Sphere(1, 1, "1", 1)
    
    # Is_inside test sphere

    def test_is_inside_True_sphere(self):
        x, y, z = 1, 2, 1
        s1 = self.create_sphere()
        self.assertTrue(s1.is_inside(x, y, z)) 
    
    def test_is_inside_True_border_sphere(self):
        x, y, z = 2, 2, 1
        s1 = self.create_sphere()
        self.assertTrue(s1.is_inside(x, y, z)) 

    def test_is_inside_False_sphere(self):
        x, y, z = 5, 5, 5
        s1 = self.create_sphere()
        self.assertFalse(s1.is_inside(x, y, z))

    def test_is_inside_string_x_sphere(self):
        x, y, z = "a", 1, 1
        s1 = self.create_sphere()
        with self.assertRaises(TypeError):
            s1.is_inside(x, y, z)
    
    def test_is_inside_string_y_sphere(self):
        x, y, z = 1, "1", 1
        s1 = self.create_cirkel()
        with self.assertRaises(TypeError):
            s1.is_inside(x, y, z)
    
    def test_is_inside_string_z_sphere(self):
        x, y, z = 1, 1, "1"
        s1 = self.create_cirkel()
        with self.assertRaises(TypeError):
            s1.is_inside(x, y, z)
    
    # Translate test sphere

    def test_translate_Equal_sphere(self):
        x, y, z = 1, 1, 1
        s1 = self.create_sphere()
        s1.translate(x, y, z)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.z, 2)
    
    def test_translate_Not_Equal_sphere(self):
        x, y, z = 1, 1, 1
        s1 = self.create_sphere()
        s1.translate(x, y, z)
        self.assertNotEqual(s1.x, 3)
        self.assertNotEqual(s1.y, 4)
        self.assertNotEqual(s1.z, 3)

    def test_translate_Equal_negativ_sphere(self):
        x, y, z = -1, -1, -1
        s1 = self.create_sphere()
        s1.translate(x, y, z)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.z, 0)

    def test_translate_string_x_sphere(self):
        x, y, z = "1", 1, 1
        s1 = self.create_sphere()
        with self.assertRaises(TypeError):
            s1.is_inside(x, y, z)
    
    def test_translate_string_y_sphere(self):
        x, y, z = 1, "1", 1
        s1 = self.create_sphere()
        with self.assertRaises(TypeError):
            s1.is_inside(x, y, z)
    
    def test_translate_string_z_sphere(self):
        x, y, z = 1, 1, "1"
        s1 = self.create_sphere()
        with self.assertRaises(TypeError):
            s1.is_inside(x, y, z)
    
    # unit_sphere test sphere

    def test_unit_sphere_True_sphere(self):
        s1 = Sphere(0, 0, 0, 1)
        self.assertTrue(s1.is_unit_sphere())
    
    def test_unit_sphere_False_sphere(self):
        s1 = Sphere(0, 0, 0, 2)
        self.assertFalse(s1.is_unit_sphere())

    # area test sphere 

    def test_area_Equal_sphere(self):
        s1 = self.create_sphere()
        a = (4 * math.pi * 1**2)
        self.assertEqual(s1.area, a)
    
    def test_area_not_Equal_sphere(self):
        s1 = self.create_sphere()
        a = 10
        self.assertNotEqual(s1.area, a)

    # omkrets test sphere

    def test_omkrets_Equal_sphere(self):
        s1 = self.create_sphere()
        o = (2 * math.pi * 1)
        self.assertEqual(s1.omkrets, o)
    
    def test_omkrets_Not_Equal_sphere(self):
        s1 = self.create_sphere()
        o = 10
        self.assertNotEqual(s1.omkrets, o)

    # volym testing sphere 

    def test_volym_Equal_sphere(self):
        s1 = self.create_sphere()
        v = ((4 / 3) * math.pi * 1**3)
        self.assertEqual(s1.volym, v)
    
    def test_volym_Not_Equal_sphere(self):
        s1 = self.create_sphere()
        v = 100
        self.assertNotEqual(s1.volym, v)

if __name__ == "__main__":
    unittest.main()