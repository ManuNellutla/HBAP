from unittest import TestCase
from Shirts import Shirt as Sh
from ppretty import ppretty


class TestShirt(TestCase):
    def test_add_discount(self):
        data = 0.2
        a = Sh('blue', 'XL', 'avant', 12.00)
        print(ppretty(a))
        #a.add_discount(0.2)
        #assert a.price == 9.600000000000001
