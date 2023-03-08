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

    def check_item_details(self, item_id: int) -> str:
        if self.items_inventory.get(item_id) == None:
            raise Exception("[ERROR] Item not found!\nOccured while checking item details")
        else:
            item = self.items_inventory.get(item_id)
            result = f"[ITEM_ID]: {item_id}\n" \
            f"[ITEM_NAME]: {item.get('item_name')}\n" \
            f"[ITEM_STOCK]: {item.get('stock_count')}\n" \
            f"[ITEM_PRICE]: {item.get('price')}\n"
            return result
    
    def increment_stock(self, item_id: int) -> None:
        if self.items_inventory.get(item_id) == None:
            raise Exception("[ERROR] Item not found!\nOccured while incrementing stock")
        else:
            self.items_inventory.get(item_id)["stock_count"] += 1
    
    def decrement_stock(self, item_id: int) -> None:
        if self.items_inventory.get(item_id) == None:
            raise Exception("[ERROR] Item not found!\nOccured while decrementing stock")
        else:
            self.items_inventory.get(item_id)["stock_count"] -= 1

    def delete_stock(self, item_id: int) -> None:
        if self.items_inventory.get(item_id) == None:
            raise Exception("[ERROR] Item not found!\nOccured while deleting stock")
        else:
            del self.items_inventory[item_id]


if __name__ == "__main__":
    try:
        invet = Inventory()
        invet.add_item(1, "clock", 32, 100)
        invet.add_item(2, "pen", 100, 15)
        invet.update_item(1, "book", 32, 100)
        invet.increment_stock(2)
        print(invet.check_item_details(2))
        invet.decrement_stock(2)
        print(invet.check_item_details(2))
        invet.delete_stock(2)
        #Trying to update the deleted item. Should raise an error.
        invet.increment_stock(2)
    except Exception as e:
        print(e)
