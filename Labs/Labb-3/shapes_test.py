from __future__ import annotations
import sys, os
from time import sleep
import unittest
import math

from geometry_shapes import Circle
from geometry_shapes import Rectangle
from geometry_shapes import Cube
from geometry_shapes import Sphere


class TestShapes(unittest.TestCase):
    
    def setUp(self):
        self.x, self.y, self.z = 1, 2, 1
        self.width, self.height = 2, 1
        self.radius = 1
        self.depth = 1

    def create_rectangle(self):
        return Rectangle(x= self.x, y= self.y, width=self.width, height= self.height)

    def create_circle(self):
        return Circle(x= self.x, y= self.y, radius= self.radius)

    def create_cube(self):
        return Cube(x= self.x, y= self.y, z= self.z, width= self.width, height= self.height, depth= self.depth)

    def create_sphere(self):
        return Sphere(x= self.x, y= self.y, z= self.z, radius= self.radius)

    """
        Testning rectangle

        -----------------------------------
    """
    
    # operator test rectangle.

    def test_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(x= 1, y= 2, width=2, height=1)
        self.assertEqual(r1, r2)
    
    def test_not_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(x= 1, y= 2, width=3, height=2)
        self.assertNotEqual(r1, r2)
    
    def test_greater_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(x= 1, y= 2, width=1, height=1)
        self.assertGreater(r1, r2)
    
    def test_not_greater_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(x= 1, y= 2, width=3, height=2)
        self.assertLess(r1, r2)
    
    def test_greater_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(x= 1, y= 2, width=2, height=1)
        self.assertGreaterEqual(r1, r2)
    
    def test_not_greater_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(x= 1, y= 2, width=3, height=2)
        self.assertLessEqual(r1, r2)

    #test error 

    def test_empty_rectangle(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_negativ_width_rectangle(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -1, 1)
    
    def test_negativ_height_rectangle(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, 1, -1)
    
    def test_string_width_rectangle(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, "1", 1)

    def test_string_height_rectangle(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, "1")
    
    def test_string_x_rectangle(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 1, 1, 1)
    
    def test_string_y_rectangle(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "1", 1, 1)
    
    # Is_inside test rectangle

    def test_is_inside_True_rectangle(self):
        x, y = 1, 2
        r1 = self.create_rectangle()
        self.assertTrue(r1.is_inside(x, y)) 
    
    def test_is_inside_True_border_rectangle(self):
        x, y = 2, 2
        r1 = self.create_rectangle()
        self.assertTrue(r1.is_inside(x, y)) 

    def test_is_inside_False_rectangle(self):
        x, y = 5, 5
        r1 = self.create_rectangle()
        self.assertFalse(r1.is_inside(x, y))

    def test_is_inside_string_x_rectangle(self):
        x, y = "a", 1
        r1 = self.create_rectangle()
        with self.assertRaises(TypeError):
            r1.is_inside(x, y)
    
    def test_is_inside_string_x_rectangle(self):
        x, y = 1, "1"
        r1 = self.create_rectangle()
        with self.assertRaises(TypeError):
            r1.is_inside(x, y)
    
    # Translate test rectangle

    def test_translate_Equal_rectangle(self):
        x, y = 1, 1
        r1 = self.create_rectangle()
        r1.translate(x, y)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
    
    def test_translate_Not_Equal_rectangle(self):
        x, y = 1, 1
        r1 = self.create_rectangle()
        r1.translate(x, y)
        self.assertNotEqual(r1.x, 3)
        self.assertNotEqual(r1.y, 4)

    def test_translate_Equal_negativ_rectangle(self):
        x, y = -1, -1
        r1 = self.create_rectangle()
        r1.translate(x, y)
        self.assertEqual(r1.x, 0)

    def test_translate_string_x_rectangle(self):
        x, y = "1", 1
        r1 = self.create_rectangle()
        with self.assertRaises(TypeError):
            r1.is_inside(x, y)
    
    def test_translate_string_y_rectangle(self):
        x, y = 1, "1"
        r1 = self.create_rectangle()
        with self.assertRaises(TypeError):
            r1.is_inside(x, y)
    
    # kvadrat test rectangle

    def test_kvadrat_True_rectangle(self):
        r1 = Rectangle(0, 0, 1, 1)
        self.assertTrue(r1.square())
    
    def test_kvadrat_False_rectangle(self):
        r1 = Rectangle(0, 0, 1, 2)
        self.assertFalse(r1.square())

    # area test rectangle 

    def test_area_Equal_rectangle(self):
        r1 = self.create_rectangle()
        a = 2 
        self.assertEqual(r1.area, a)
    
    def test_area_not_Equal_rectangle(self):
        r1 = self.create_rectangle()
        a = 4
        self.assertNotEqual(r1.area, a)

    # omkrets test rectangle

    def test_omkrets_Equal_rectangle(self):
        r1 = self.create_rectangle()
        o = 6
        self.assertEqual(r1.circumference, o)
    
    def test_omkrets_Not_Equal_rectangle(self):
        r1 = self.create_rectangle()
        o = 10
        self.assertNotEqual(r1.circumference, o)

    """
        Testning circle.

        -----------------------------------
    """

    # operator test cirkel.

    def test_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(x= 1, y= 2, radius= 1)
        self.assertEqual(c1, c2)
    
    def test_not_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(x= 1, y= 2, radius= 3)
        self.assertNotEqual(c1, c2)
    
    def test_greater_circle(self):
        c1 = self.create_circle()
        c2 = Circle(x= 1, y= 2, radius= 0.5)
        self.assertGreater(c1, c2)
    
    def test_not_greater_circle(self):
        c1 = self.create_circle()
        c2 = Circle(x= 1, y= 2, radius= 5)
        self.assertLess(c1, c2)
    
    def test_greater_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(x= 1, y= 2, radius=1)
        self.assertGreaterEqual(c1, c2)
    
    def test_not_greater_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(x= 1, y= 2, radius= 1)
        self.assertLessEqual(c1, c2)

    #test error 

    def test_empty_circle(self):
        with self.assertRaises(TypeError):
            r = Circle()

    def test_negativ_radius_circle(self):
        with self.assertRaises(ValueError):
            r = Circle(1, 1, -1)
    
    def test_string_radius_circle(self):
        with self.assertRaises(TypeError):
            r = Circle(1, 1, "1")

    
    def test_string_x_circle(self):
        with self.assertRaises(TypeError):
            r = Circle("1", 1, 1)
    
    def test_string_y_circle(self):
        with self.assertRaises(TypeError):
            r = Circle(1, "1", 1)
    
    # Is_inside test circle

    def test_is_inside_True_circle(self):
        x, y = 1, 2
        c1 = self.create_circle()
        self.assertTrue(c1.is_inside(x, y)) 
    
    def test_is_inside_True_border_circle(self):
        x, y = 2, 2
        c1 = self.create_circle()
        self.assertTrue(c1.is_inside(x, y)) 

    def test_is_inside_False_circle(self):
        x, y = 5, 5
        c1 = self.create_circle()
        self.assertFalse(c1.is_inside(x, y))

    def test_is_inside_string_x_circle(self):
        x, y = "a", 1
        c1 = self.create_circle()
        with self.assertRaises(TypeError):
            c1.is_inside(x, y)
    
    def test_is_inside_string_y_circle(self):
        x, y = 1, "1"
        c1 = self.create_circle()
        with self.assertRaises(TypeError):
            c1.is_inside(x, y)
    
    # Translate test Cirkel

    def test_translate_Equal_circle(self):
        x, y = 1, 1
        c1 = self.create_circle()
        c1.translate(x, y)
        self.assertEqual(c1.x, 2)
        self.assertEqual(c1.y, 3)
    
    def test_translate_Not_Equal_circle(self):
        x, y = 1, 1
        c1 = self.create_circle()
        c1.translate(x, y)
        self.assertNotEqual(c1.x, 3)
        self.assertNotEqual(c1.y, 4)

    def test_translate_Equal_negativ_circle(self):
        x, y = -1, -1
        c1 = self.create_circle()
        c1.translate(x, y)
        self.assertEqual(c1.x, 0)
        self.assertEqual(c1.y, 1)

    def test_translate_string_x_circle(self):
        x, y = "1", 1
        c1 = self.create_circle()
        with self.assertRaises(TypeError):
            c1.is_inside(x, y)
    
    def test_translate_string_y_circle(self):
        x, y = 1, "1"
        c1 = self.create_circle()
        with self.assertRaises(TypeError):
            c1.is_inside(x, y)
    
    # enhets_Cirkel test Cirkel

    def test_enhets_Cirkel_True_circle(self):
        c1 = Circle(0, 0, 1)
        self.assertTrue(c1.unit_Circle())
    
    def test_enhets_Cirkel_False_circle(self):
        c1 = Circle(0, 0, 2)
        self.assertFalse(c1.unit_Circle())

    # area test Circle 

    def test_area_Equal_circle(self):
        c1 = self.create_circle()
        a = math.pi * 1**2
        self.assertEqual(c1.area, a)
    
    def test_area_not_Equal_circle(self):
        c1 = self.create_circle()
        a = 4
        self.assertNotEqual(c1.area, a)

    # circumference test circle

    def test_circumference_Equal_circle(self):
        c1 = self.create_circle()
        o = 2*math.pi * 1
        self.assertEqual(c1.circumference, o)
    
    def test_circumference_Not_Equal_circle(self):
        c1 = self.create_circle()
        o = 10
        self.assertNotEqual(c1.circumference, o)

    
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

    # circumference test cube

    def test_circumference_Equal_cube(self):
        cu1 = self.create_cube()
        o = 16
        self.assertEqual(cu1.circumference, o)
    
    def test_circumference_Not_Equal_cube(self):
        cu1 = self.create_cube()
        o = 10
        self.assertNotEqual(cu1.circumference, o)

    # volume test cube

    def test_volume_Equal_cube(self):
        cu1 = self.create_cube()
        v = 2
        self.assertEqual(cu1.volume, v)
    
    def test_volym_Not_Equal_cube(self):
        cu1 = self.create_cube()
        v = 7
        self.assertNotEqual(cu1.volume, v)

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
        s1 = self.create_circle()
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
        s1 = self.create_circle()
        with self.assertRaises(TypeError):
            s1.is_inside(x, y, z)
    
    def test_is_inside_string_z_sphere(self):
        x, y, z = 1, 1, "1"
        s1 = self.create_circle()
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

    # circumference test sphere

    def test_circumference_Equal_sphere(self):
        s1 = self.create_sphere()
        o = (2 * math.pi * 1)
        self.assertEqual(s1.circumference, o)
    
    def test_circumference_Not_Equal_sphere(self):
        s1 = self.create_sphere()
        o = 10
        self.assertNotEqual(s1.circumference, o)

    # volume testing sphere 

    def test_volume_Equal_sphere(self):
        s1 = self.create_sphere()
        v = ((4 / 3) * math.pi * 1**3)
        self.assertEqual(s1.volume, v)
    
    def test_volume_Not_Equal_sphere(self):
        s1 = self.create_sphere()
        v = 100
        self.assertNotEqual(s1.volume, v)

if __name__ == "__main__":
    unittest.main()