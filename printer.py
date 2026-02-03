'''
partitions 
v - 5 to 99
v - 100 to max int

i - int < 5 
i - 0
i - -1 to max negative int 

EC - strings, array, other data types 

3 boundary values - test cases

lower 4 og 5 og 6 
middel 50 
upper 99 og 100 og 101

nul - 0 

minustal er -2

EC er "EK"
'''
import unittest 
import datetime

def discount(antal_print_cart):
    if not isinstance(antal_print_cart, (int)):
        raise TypeError(f"antal printer cartridges skal være en integer, ikke {type(antal_print_cart).__name__}")

    # Minimum 5 prints
    if antal_print_cart < 5:
        raise ValueError("antal_print_cart kan ikke være under 5")
    
    if 5 <= antal_print_cart < 100:
        return 0
    elif antal_print_cart >= 100:
        return 0.2 

class TestDiscount(unittest.TestCase):
    def test_under_5_prints(self):
        with self.assertRaises(ValueError):
            discount(0)
        with self.assertRaises(ValueError):
            discount(1)
        with self.assertRaises(ValueError):
            discount(4)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            discount(-1)

    def test_mellem_5_og_99(self):
        self.assertEqual(discount(5), 0)
        self.assertEqual(discount(50), 0)
        self.assertEqual(discount(99), 0)

    def test_100_og_flere(self):
        self.assertEqual(discount(100), 0.2)
        self.assertEqual(discount(101), 0.2)
        self.assertEqual(discount(150), 0.2)

    def test_wrong_type(self):
        # string
        with self.assertRaises(TypeError):
            discount("EK")

        # lists
        with self.assertRaises(TypeError):
            discount([10,20])
    
    def test_wrong_float_type_is_very_bad(self):
        with self.assertRaises(TypeError):
            discount(22.1)
    
    def test_wrong_date_bad_bad(self):
        with self.assertRaises(TypeError):
            x = datetime.datetime.now()
            discount(x)

if __name__ == '__main__':
    unittest.main()
