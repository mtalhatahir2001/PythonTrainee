from datetime import date

class Restaurant:
    def __init__(self) -> None:
        self.__menu = dict()
        self.__reservations = list()
    
    def add_item_to_menu(self, menu_item: dict) -> None:
        if self.__menu.get(menu_item.get("id")) != None:
            raise Exception("[ERROR] Item already in menu.")
        else:
            #pop() will not only return the id but will also it from menu_item
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
            menu_string += f"{i}. {self.__menu[i]['name']}" \
                f" ---- {self.__menu[i]['price']}\n"
        return menu_string
    
    def book_table(self, reservation: dict)->None:
        #Will raise an exception if same table
        #is booked at the same time slot.
        for i in self.__reservations:
            if (i.get("table_id") == reservation.get("table_id")
                    and i.get("reservation_time") == reservation.get("reservation_time")):
                raise Exception("[ERROR] Table already reserved at this time slot.")
        self.__reservations.append(reservation)
    
    @property
    def reservations(self):
        """
        This is a getter for attribute __reservations
        This function also serves the purpose of display reservation function 
        that was required in question.
        """
        reservation_string = "*-----RESERVATIONS-----*\nTable\t\tTime\t\tCustomer\n"
        for i in self.__reservations:
            reservation_string += f"{i['table_id']}\t\t" \
                f"{i['reservation_time']}\t\t{i['customer_id']}\n"
        return reservation_string

if __name__ == "__main__":
    try:
        rest = Restaurant()
        rest.add_item_to_menu({"id":1, "name":"Coffee", "price":60})
        rest.add_item_to_menu({"id":2, "name":"Lemonade", "price":40})
        rest.book_table({"table_id":2, "customer_id":3, "reservation_time":date.today()})
        rest.book_table({"table_id":1, "customer_id":3, "reservation_time":date.today()})
        print(rest.reservations)
    except Exception  as e:
        print(e)