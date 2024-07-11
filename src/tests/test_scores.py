import unittest
from app.schemas import Receipt, Item
from app.scores import (
    score_item_description_length,
    score_price_end_with_00,
    score_price_multiple_of_25,
    score_purchase_between_2pm_and_4pm,
    score_purchase_date_odd,score_receipt_length,
    score_retailer_name,
    total_score
)

class Test(unittest.TestCase):
  def setUp(self):
    self.receipt_data = {
      "retailer": "M&M Corner Market",
      "purchaseDate": "2022-03-20",
      "purchaseTime": "14:33",
      "items": [
        {
          "shortDescription": "Gatorade",
          "price": "2.25"
        },{
          "shortDescription": "Gatorade",
          "price": "2.25"
        },{
          "shortDescription": "Gatorade",
          "price": "2.25"
        },{
          "shortDescription": "Gatorade",
          "price": "2.25"
        }
      ],
      "total": "9.00"
    }
    self.receipt = Receipt(**self.receipt_data)

  def test_item_description(self):
    result = score_retailer_name(self.receipt)
    self.assertEqual(result, 14, "Expected 14 points for retailer name")

  def test_receipt_length(self):
    result = score_receipt_length(self.receipt)
    self.assertEqual(result,10, "Expected 10 points for length of receipt")

  def test_price_ends_with_00(self):
    result = score_price_end_with_00(self.receipt)
    self.assertEqual(result,50, "Expected 50 points for total ending with .00")

  def test_price_multiple_of_25(self):
    result = score_price_multiple_of_25(self.receipt)
    self.assertEqual(result,25, "Expected 25 points for total is a multiple of .25")

  def test_item_description_length(self):
    result = score_item_description_length(self.receipt)
    self.assertEqual(result, 0, "Expected 0 points for items' short description")

  def test_purchase_date_odd(self):
    result = score_purchase_date_odd(self.receipt)
    self.assertEqual(result, 0, "Expected 0 points for purchase date being even")

  def test_purchase_time(self):
    result = score_purchase_between_2pm_and_4pm(self.receipt)
    self.assertEqual(result,10, "Expected 10 points for purchase time between 2pm and 4pm" )

  def test_total_score(self):
    result = total_score(self.receipt)
    self.assertEqual(result,109, "Expected 109 points for receipt")

if __name__ == '__main__':
    unittest.main()