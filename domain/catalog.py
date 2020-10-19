class Catalog:
    def __init__(self, items_limit):
        self.items_limit = items_limit
        self.items = {}


    def add_item(self, item, price):
        if len(item) <= self.items_limit:
            self.items[item] = self.items.get(item, price)
        else:
            raise Exception("Your Catalog has reached its item limit! Create a new one.")
    

    def remove_item(self, item):
        removed_item = self.items.pop(item, None)
        if not removed_item:
            raise Exception("That item doesn't exist in the Catalog.")


    def find(self, item):
        found_item = self.items.get(item, None)
        return found_item
