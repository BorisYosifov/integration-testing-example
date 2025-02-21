import unittest
from discount_module import apply_discount

class TestDiscountModule(unittest.TestCase):
    
    def test_no_discount(self):
        """
        Тест за случай, когато не се прилага отстъпка (цена <= 500).
        """
        total_price = 500
        result = apply_discount(total_price)
        self.assertEqual(result, 500, "Цената не трябва да се променя без отстъпка")
        
        total_price = 300
        result = apply_discount(total_price)
        self.assertEqual(result, 300, "Цената не трябва да се променя без отстъпка")
    
    def test_5_percent_discount(self):
        """
        Тест за случай, когато се прилага 5% отстъпка (500 < цена <= 1000).
        """
        total_price = 800
        expected_price = 800 * 0.95  # 5% отстъпка
        result = apply_discount(total_price)
        self.assertEqual(result, expected_price, f"Цената трябва да бъде {expected_price} след 5% отстъпка")
        
        total_price = 600
        expected_price = 600 * 0.95  # 5% отстъпка
        result = apply_discount(total_price)
        self.assertEqual(result, expected_price, f"Цената трябва да бъде {expected_price} след 5% отстъпка")
    
    def test_10_percent_discount(self):
        """
        Тест за случай, когато се прилага 10% отстъпка (цена > 1000).
        """
        total_price = 1500
        expected_price = 1500 * 0.90  # 10% отстъпка
        result = apply_discount(total_price)
        self.assertEqual(result, expected_price, f"Цената трябва да бъде {expected_price} след 10% отстъпка")
        
        total_price = 1200
        expected_price = 1200 * 0.90  # 10% отстъпка
        result = apply_discount(total_price)
        self.assertEqual(result, expected_price, f"Цената трябва да бъде {expected_price} след 10% отстъпка")

if __name__ == "__main__":
    unittest.main()
