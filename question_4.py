class Restaurant:
    def __init__(self) -> None:
        self.__menu = dict()
    
    def add_item_to_menu(self, menu_item: dict) -> None:
        if self.__menu.get(menu_item.get("id")) != None:
            raise Exception("[ERROR] Item already in menu.")
        else:
            #Removing the id attribute from menu_item and storing item against that key.
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
    

if __name__ == "__main__":
    try:
        rest = Restaurant()
        rest.add_item_to_menu({"id":1, "name":"Coffee", "price":60})
        rest.add_item_to_menu({"id":2, "name":"Lemonade", "price":40})
        print(rest.menu)
    except Exception  as e:
        print(e)