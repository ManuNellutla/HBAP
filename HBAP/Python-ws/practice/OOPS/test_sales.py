from unittest import TestCase
from Shirts import Pant
from sales import SalesPerson
from ppretty import ppretty


class TestSalesPerson(TestCase):
    def test_display_sales(self):
        sp = SalesPerson("Manu", "Nellutla", 1, 150000)
        p1 = Pant('red', 'M', 'Slim', 12.99)
        p2 = Pant('blue', 'L', 'Relaxed', 17.99)
        sp.sell_pants(p1)
        sp.sell_pants(p2)
        sp.calculate_sales()
        print(ppretty(sp))
        print(f"Commission earned by {sp.first_name + ' '+ sp.last_name} is  : ${round(sp.calculate_commission(0.3),2)} ")
        assert True
