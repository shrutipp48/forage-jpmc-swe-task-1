import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
          {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Call getDataPoint() function and store the returned values
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])

        # Assert that the returned values are of the correct type
        self.assertIsInstance(stock, str)
        self.assertIsInstance(bid_price, float)
        self.assertIsInstance(ask_price, float)
        self.assertIsInstance(price, float)

        # Assert that the returned value is equal to the average of the top bid and top ask prices
        self.assertEqual(price, (121.2 + 120.48) / 2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
          {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        stock, bid_price, ask_price, price = getDataPoint(quotes[0])

        self.assertIsInstance(stock, str)
        self.assertIsInstance(bid_price, float)
        self.assertIsInstance(ask_price, float)
        self.assertIsInstance(price, float)

        self.assertEqual(stock, "ABC")
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 119.2)
        self.assertEqual(price, (120.48 + 119.2) / 2)





