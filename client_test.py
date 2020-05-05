import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['tob_bid']['price'] + quote['top_ask']['price']) / 2))
        """ ------------ Add the assertion below ------------ """

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['tob_bid']['price'] + quote['top_ask']['price']) / 2))
        """ ------------ Add the assertion below ------------ """

    """ ------------ Add more unit tests ------------ """
    def test_getDataPointPriceBZero(self):
        price_a = 145.2
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b))

    def test_getRatioPriceAZero(self):
        price_a = 0
        price_b = 132.2
        self.assertEqual(getRatio(price_a, price_b), 0)

    def test_getRatioGreaterthan1(self):
        price_a = 143.3
        price_b = 132.1
        self.assertGreater(getRatio(price_a, price_b), 1)

    def test_getRatioLessthan1(self):
        price_a = 123.3
        price_b = 132.2
        self.assertLess(getRatio(price_a, price_b), 1)

    def test_getRatioEqual1(self):
        price_a = 123.2
        price_b = 123.2
        self.assertEqual(getRatio(price_a, price_b), 1)
        

if __name__ == '__main__':
    unittest.main()
