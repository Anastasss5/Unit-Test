import unittest
from circle import circle_long
from math import pi

class TestCircleLong(unittest.TestCase):
    def test_long(self):
        self.assertEqual(circle_long(3), 2*pi*3)
        self.assertEqual(circle_long(1), 2*pi)
        self.assertEqual(circle_long(0), 0)
        self.assertEqual(circle_long(2.5), 2*pi*2.5)

    def test_values(self):  
        self.assertRaises(ValueError, circle_long, -2)
        self.assertRaises(ValueError, circle_long, -1)
    
    def test_types(self):
        self.assertRaises(TypeError, circle_long, 5+2j)
        self.assertRaises(TypeError, circle_long, 'five')
        self.assertRaises(TypeError, circle_long, [16, 22])
        self.assertRaises(TypeError, circle_long, [42])
        self.assertRaises(TypeError, circle_long, True) 

if __name__ == '__main__':
    unittest.main() 