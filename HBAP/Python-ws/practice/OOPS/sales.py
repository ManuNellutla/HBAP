from Shirts import Pant

class SalesPerson:

    def __init__(self, first_name: str, last_name: str, employee_id: int, salary: float):
        """

        :param first_name:
        :param last_name:
        :param employee_id:
        :param salary:
        """
        self.total_sales = 0
        self.pants_sold = []
        self.salary = salary
        self.employee_id = employee_id
        self.last_name = last_name
        self.first_name = first_name

    def sell_pants(self, pant: Pant):
        """

        :param pant:
        :return:
        """
        self.pants_sold.append(pant)

    def display_sales(self):
        """

        :return:
        """
        for pant in self.pants_sold:
            temp = vars(pant)
            for item in temp:
                print(item, ':', temp[item])

    def calculate_sales(self) -> float:
        """

        :return:
        """
        self.total_sales = sum(p.price for  p in self.pants_sold)
        return self.total_sales

    def calculate_commission(self, comm: float) -> float:
        """

        :param comm:
        :return:
        """
        return comm * self.total_sales
