class Inventory:
    def __init__(self) -> None:
        self.items_inventory = dict()

    def add_item(
            self, item_id: int,
            item_name: str, stock_count: int,
            price: float
            ) -> None:
        if self.items_inventory.get(item_id) != None:
            raise Exception("[ERROR] Item all ready exsist.\nOccured while adding item")
        else:
            self.items_inventory[item_id] = {
                "item_name":item_name,
                "stock_count":stock_count,
                "price":price
            }
    
    def update_item(
            self, item_id: int,
            item_name: str, stock_count: int,
            price: float
        ) -> None:
        if self.items_inventory.get(item_id) == None:
            raise Exception("[ERROR] Item not found!\nOccured while updating item")
        else:
            self.items_inventory[item_id] = {
                "item_name":item_name,
                "stock_count":stock_count,
                "price":price
            }

if __name__ == "__main__":
    try:
        invet = Inventory()
        invet.add_item(1, "clock", 32, 100)
        invet.add_item(2, "pen", 100, 15)
        invet.update_item(1, "book", 32, 100)
        print(invet.items_inventory)
    except Exception as e:
        print(e)
