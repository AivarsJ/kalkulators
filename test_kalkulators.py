import unittest
from kalkulators import saskaitit

class TestKalkulators(unittest.TestCase):
    
    def test_saskaitit_positive(self):
        self.assertEqual(saskaitit(3, 3), 6)
        
    def test_saskaitit_negative(self):
        self.assertEqual(saskaitit(3, -3), 0)

    def test_saskaitit_zero(self):
        self.assertEqual(saskaitit(0, 3), 3)
        
if __name__ == "__main__":
    unittest.main()