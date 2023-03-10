from datetime import date


class Restaurant:
    def __init__(self) -> None:
        self.__menu = dict()
        self.__reservations = list()
        self.__orders = list()
        self.__GST_RATE = 18

    def add_item_to_menu(self, menu_item: dict) -> None:
        """
        This module add new items to menu. menu_item is a dict
        that must have id, name and price attributes.
        """
        if self.__menu.get(menu_item.get("id")) != None:
            raise Exception("[ERROR] Item already in menu.")
        else:
            # pop() will not only return the id but will also it from menu_item
            self.__menu[menu_item.pop("id")] = menu_item

    @property
    def menu(self) -> str:
        """
        This is a getter function for attribute __menu.
        This function also serves the purpose of display menu function
        that was required in question.
        """
        menu_string = "*-----MENU-----*\n"
        for i in self.__menu:
            menu_string += (
                f"{i}. {self.__menu[i]['name']}" f" ---- {self.__menu[i]['price']}\n"
            )
        return menu_string

    def book_table(self, reservation: dict) -> None:
        """
        reservation must have the following attributes table_id: int, customer_id: int and
        reservation_time: datetime
        """
        # Will raise an exception if same table
        # is booked at the same time slot.
        for i in self.__reservations:
            if i.get("table_id") == reservation.get("table_id") and i.get(
                "reservation_time"
            ) == reservation.get("reservation_time"):
                raise Exception("[ERROR] Table already reserved at this time slot.")
        self.__reservations.append(reservation)

    @property
    def reservations(self) -> str:
        """
        This is a getter for attribute __reservations
        This function also serves the purpose of display reservation function
        that was required in question.
        """
        reservation_string = "*-----RESERVATIONS-----*\nTable\t\tTime\t\tCustomer\n"
        for i in self.__reservations:
            reservation_string += (
                f"{i['table_id']}\t\t"
                f"{i['reservation_time']}\t\t{i['customer_id']}\n"
            )
        return reservation_string

    def customer_order(self, order: dict[int, int]) -> None:
        """
        This module places the order of a customer.
        order dict must have customer_id: int and item_id: int.
        """
        # Will place customers order only if item cutomer
        # ordered is present in menu.
        if not order.get("item_id") in self.__menu:
            raise Exception("[ERROR] Item not in menu")
        else:
            self.__orders.append(order)

    def customer_bill(self, customer_id: int) -> str:
        """
        Calculate and returns the total bill as printable string.
        """
        total_bill = 0.0
        bill_string = f"*-----BILL-----*\n"
        for i in self.__orders:
            if i.get("customer_id") == customer_id:
                bill_string += self.__create_item_string(i.get("item_id"))
                total_bill += self.__menu.get(i.get("item_id")).get("price")
        bill_with_gst = self.__calculate_gst(total_bill)
        bill_string += (
            f"Total bill ---- {total_bill}\n"
            f"GST Rate ---- {self.__GST_RATE}%\n"
            f"TOTAL PAYABLE BILL ---- {bill_with_gst}\n"
        )
        return bill_string

    def __create_item_string(self, item_id: int) -> str:
        """
        This helper function return the item in printable format.
        """
        item = self.__menu.get(item_id)
        item_string = f"{item_id}. {item['name']}" f" ---- {item['price']}\n"
        return item_string

    def __calculate_gst(self, total_bill: float) -> float:
        return total_bill + ((total_bill * self.__GST_RATE) / 100.0)


if __name__ == "__main__":
    try:
        rest = Restaurant()
        rest.add_item_to_menu({"id": 1, "name": "Coffee", "price": 60})
        rest.add_item_to_menu({"id": 2, "name": "Lemonade", "price": 40})
        # will print the menu.
        print(rest.menu)
        # making a reservation.
        rest.book_table(
            {"table_id": 2, "customer_id": 3, "reservation_time": date.today()}
        )
        rest.book_table(
            {"table_id": 1, "customer_id": 3, "reservation_time": date.today()}
        )
        # same customer placing order 2 times.
        rest.customer_order({"customer_id": 1, "item_id": 2})
        rest.customer_order({"customer_id": 1, "item_id": 1})
        print(rest.customer_bill(1))
        # will print the all the reservations.
        print(rest.reservations)
    except Exception as e:
        print(e)
