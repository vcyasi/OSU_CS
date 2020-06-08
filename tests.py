import unittest
import random
from credit_card_validator import credit_card_validator


class TestCardNums(unittest.TestCase):
    # def test9(self):
    #     num = 100000
    #     for i in range(num):
    #         cardnum = random.randint(10000, 99999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(100000, 999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(1000000, 9999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(10000000, 99999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(100000000, 999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(1000000000, 9999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(10000000000, 99999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(100000000000, 999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(1000000000000, 9999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(10000000000000, 99999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(100000000000000, 999999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(1000000000000000, 9999999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(10000000000000000, 99999999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(100000000000000000, 999999999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(1000000000000000000, 9999999999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(10000000000000000000, 99999999999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(100000000000000000000, 999999999999999999999)
    #         credit_card_validator(cardnum)
    #         cardnum = random.randint(1000000000000000000000, 9999999999999999999999)
    #         credit_card_validator(cardnum)

    def test9(self):
        num = 100000
        for i in range(num):
            cardnum = random.randint(4000000000000000, 4999999999999999)
            credit_card_validator(cardnum)
            



if __name__ == '__main__':
    unittest.main()
